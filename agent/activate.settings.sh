#!/usr/bin/env bash
# App settings go here, they're validated in app.settings - an attempt to coerce to the internal type is made at run time

# Boolean values can be any of: '1', 'TRUE', 'YES', 'ON' - case insensitive

# the AIO_ env variables are used by `adev runserver` when serving your app for development
#export AIO_APP_PATH="app/"
export AIO_STATIC_PATH="${AGENT_SRC_DIR}/sn_agent/static/"
export AIO_LIVERELOAD="true"
export AIO_DEBUG_TOOLBAR="true"
export AIO_PRECHECK="true"
export AIO_PORT=8080
export AIO_AUX_PORT=8081


export SN_DB_URL="sqlite://"
export SN_AGENT_ETH_CLIENT="http://localhost:8545"

# this is the key used to encrypt cookies. Keep it safe!
# you can generate a new key with `./tools.sh cookie`
export SN_AGENT_COOKIE_SECRET="M0a6HuukMqXf9VMmMMf9RiZFKKPc5etebG4-R8IPTQc="

# this should be changed for every agent - we need a way to create these and store the data persistently - perhaps a file?
export SN_NETWORK_AGENT_ID='b545478a-971a-48ec-bc56-4b9b7176799c'

export SN_WORKER_WORKER_CONFIG_FILE="${AGENT_DIR}/worker_config_testing.yml"
