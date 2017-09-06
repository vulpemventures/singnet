#!/usr/bin/env bash

set -o errexit
set -o verbose
set -o xtrace
set -o nounset

# download, compile and install python: https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz
# download, decompress node:

# sudo apt install build-essential cmake libboost-all-dev libz3-dev libcupti-dev

BASE_DIR=${PWD}
AGENT_DIR=${BASE_DIR}/agent
AGENT_SRC_DIR=${AGENT_DIR}/src
INSTALL_DIR=${BASE_DIR}/local
PYTHON2_DIR=${INSTALL_DIR}/python2
PYTHON2_BIN_DIR=${INSTALL_DIR}/python2/bin
PYTHON2=${PYTHON2_DIR}/bin/python2

PYTHON3_DIR=${INSTALL_DIR}/python3
PYTHON3=${PYTHON3_DIR}/bin/python3
PIP3=${PYTHON3_DIR}/bin/pip3
VENV=${INSTALL_DIR}/venv
VENV_BIN_DIR=${VENV}/bin
VPYTHON3=${VENV}/bin/python3

NODE_DIR=${INSTALL_DIR}/node
NODE=${NODE_DIR}/bin/node
NPM=${NODE_DIR}/bin/npm
NODE_MODULES=${AGENT_DIR}/node_modules
VENDOR=${AGENT_SRC_DIR}/sn_agent/static/vendor

RUBY_DIR=${INSTALL_DIR}/ruby
RUBY=${RUBY_DIR}/bin/ruby
GEM=${RUBY_DIR}/bin/gem
SCSS=${RUBY_DIR}/bin/scss

REDIS_DIR=${INSTALL_DIR}/redis
REDIS=${REDIS_DIR}/bin/redis-server

GETH=${INSTALL_DIR}/geth/geth
SOLC=${INSTALL_DIR}/solidity-src/build/solc/solc

function ensure_install_dir {
    mkdir -p ${INSTALL_DIR}
}

function install_python2 {

    ensure_install_dir
    cd ${INSTALL_DIR}

    src=python2-src.tgz


    if [ ! -f ${src} ]; then
        curl -o ${src} "https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz"
    fi

    out_dir=python2-src
    if [ ! -d ${out_dir} ]; then
        mkdir ${out_dir}
        tar xfzv ${src} --directory ${out_dir} --strip-components=1
    fi

    if [ ! -f ${PYTHON2} ]; then
        cd ${out_dir}
        ./configure --prefix=${PYTHON2_DIR}
        make
#        make test
        make install
        cd ..
    fi

    cd ..
}

function install_python3 {
    ensure_install_dir
    cd ${INSTALL_DIR}

    src=python3-src.tgz


    if [ ! -f ${src} ]; then
        curl -o ${src} "https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz"
    fi

    out_dir=python3-src
    if [ ! -d ${out_dir} ]; then
        mkdir ${out_dir}
        tar xfzv ${src} --directory ${out_dir} --strip-components=1
    fi

    if [ ! -f ${PYTHON3} ]; then
        cd ${out_dir}
        ./configure --prefix=${PYTHON3_DIR}
        make
        make test
        make install
        cd ..
    fi

    cd ..
}

function install_node {
    ensure_install_dir
    cd ${INSTALL_DIR}

    src=node-src.tgz

    if [ ! -f ${src} ]; then
        curl -o ${src} "https://nodejs.org/dist/v6.11.2/node-v6.11.2.tar.gz"
    fi

    out_dir=node-src
    if [ ! -d ${out_dir} ]; then
        mkdir ${out_dir}
        tar xfzv ${src} --directory ${out_dir} --strip-components=1
    fi

    if [ ! -f ${NODE} ]; then
        cd ${out_dir}
        export PATH=${PYTHON2_BIN_DIR}:$PATH
        ${PYTHON2} configure --prefix=${NODE_DIR}
        make -j4
        make install
        cd ..
    fi

    cd ..
}

function install_solidity {
    ensure_install_dir
    cd ${INSTALL_DIR}

    src=solidity-src.tgz

    if [ ! -f ${src} ]; then
        curl -L -o ${src} "https://github.com/ethereum/solidity/releases/download/v0.4.16/solidity_0.4.16.tar.gz"
    fi

    out_dir=solidity-src
    if [ ! -d ${out_dir} ]; then
        mkdir ${out_dir}
        tar xfzv ${src} --directory ${out_dir} --strip-components=1
    fi

    if [ ! -f ${SOLC} ]; then
        cd ${out_dir}

        mkdir -p build
        cd build
        cmake ..
        make

        cd ..
    fi

    cd ..
}

function install_ruby {
    ensure_install_dir
    cd ${INSTALL_DIR}

    src=ruby-src.tgz

    if [ ! -f ${src} ]; then
        curl -o ${src} "https://cache.ruby-lang.org/pub/ruby/2.4/ruby-2.4.1.tar.gz"
    fi

    out_dir=ruby-src
    if [ ! -d ${out_dir} ]; then
        mkdir ${out_dir}
        tar xfzv ${src} --directory ${out_dir} --strip-components=1
    fi

    if [ ! -f ${RUBY} ]; then
        cd ${out_dir}
        ./configure --prefix=${RUBY_DIR}
        make
        make install
        cd ..
    fi

    cd ..
}

function install_redis {
    ensure_install_dir
    cd ${INSTALL_DIR}

    src=redis-src.tgz

    if [ ! -f ${src} ]; then
        curl -o ${src} "http://download.redis.io/releases/redis-4.0.1.tar.gz"
    fi

    out_dir=redis-src
    if [ ! -d ${out_dir} ]; then
        mkdir ${out_dir}
        tar xfzv ${src} --directory ${out_dir} --strip-components=1
    fi

    if [ ! -f ${REDIS} ]; then
        cd ${out_dir}
        make
        make test
        make PREFIX=${REDIS_DIR} install
        cd ..
    fi

    cd ..
}

function install_geth {
    ensure_install_dir
    cd ${INSTALL_DIR}

    src=geth.tgz

    if [ ! -f ${src} ]; then
        curl -o ${src} "https://gethstore.blob.core.windows.net/builds/geth-alltools-linux-amd64-1.6.7-ab5646c5.tar.gz"
    fi

    out_dir=geth
    if [ ! -d ${out_dir} ]; then
        mkdir ${out_dir}
        tar xfzv ${src} --directory ${out_dir} --strip-components=1
    fi

    cd ..
}

function install_gems {
    if [ ! -f ${SCSS} ]; then
        ${GEM} install sass
    fi
}

function install_pip {
    ${PYTHON3} -m venv ${VENV}
    echo $PWD
    ${VENV}/bin/pip3 install -r ${AGENT_DIR}/requirements.txt
}

function remove_install_dir {
    rm -Rf ${INSTALL_DIR}
}

function npm_run {
    cd ${AGENT_SRC_DIR}
    ${NPM} install
    cd ..
}

function copy_vendor {
    # Seems weird that we have to do this, I would prefer to use them in-place and have some sort of collector put them where they need to be after a compression - Webpack?

    rm -Rf ${VENDOR}
    mkdir ${VENDOR}

    cp -R ${NODE_MODULES}/bootstrap/dist ${VENDOR}/bootstrap
    cp -R ${NODE_MODULES}/jquery/dist ${VENDOR}/jquery
    cp -R ${NODE_MODULES}/vue/dist ${VENDOR}/vue
    cp -R ${NODE_MODULES}/metismenu/dist ${VENDOR}/metismenu
    cp -R ${NODE_MODULES}/font-awesome ${VENDOR}/font-awesome
    cp -R ${NODE_MODULES}/highcharts ${VENDOR}/highcharts

}

function create_docs {
    ${VENV_BIN_DIR}/sphinx-build -b dirhtml "${AGENT_DIR}/docs/" "${AGENT_DIR}/docs/_build"
#    make html
#    make coverage
    cd ..
}

function run_tests {
    cd ${AGENT_DIR}
    ${VENV}/bin/tox
}

case "$1" in

clean)
    remove_install_dir
    ;;

prep)
    install_python2
    install_python3
    install_node
    install_ruby
    install_redis
    install_geth
    install_gems
    install_pip
    install_solidity

    npm_run
    copy_vendor
    ;;

run)
    source ${AGENT_DIR}/activate.settings.sh
    PYTHONPATH=${AGENT_SRC_DIR} ${VENV_BIN_DIR}/adev runserver --verbose ${AGENT_SRC_DIR}/sn_agent
    ;;

run-geth)
    source ${AGENT_DIR}/activate.settings.sh
    ${GETH} --rpcapi admin,debug,personal,txpool,eth,web3,shh --rpc --shh --datadir "/mnt/singnet-data/geth-data" --syncmode "full"
    ;;
run-redis)
    source ${AGENT_DIR}/activate.settings.sh
    ${REDIS}
    ;;

reset)
	source ${AGENT_DIR}/activate.settings.sh
    PYTHONPATH=${AGENT_SRC_DIR} ${VPYTHON3} sn_agent/utils.py
    ;;

cookie)
    cd ${AGENT_SRC_DIR}
    PYTHONPATH=${AGENT_SRC_DIR} ${VPYTHON3} sn_agent/session.py
    ;;

docs)
    create_docs
    ;;

test)
    run_tests
    ;;

*) echo 'No operation specified'
    exit 0;
    ;;

esac
