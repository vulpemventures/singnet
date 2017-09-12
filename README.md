# SingularityNET

To allow multiple computers to work as a whole providing various services in a distributed and decentralized way.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

The agent is service responsible for communicating with the workers and the rest of the network. You can run an agent connected to the network as a client or as a client with underlying workers.

### Prerequisites

At this time, the only OS that this has been tested on is Ubunut 16.04 LTS. This may change in the future but for now, you must start there. There are only a few system level requirement.
The installer script will download, compile several packages but they are all installed locally. To support the compilation, the operating system needs to have the following run:

```
sudo ./tools.sh system-prep
```

If you are installing the agent to provide work and have an NVIDIA GPU, please start by running:

```
sudo ./tools.sh system-gpu-prep
```

### Installing

The install process can take a bit of time. If you run into any issue, please do not hesitate to file a but report. Be sure to include the last few lines of the console output to help us determine where it failed.

You will not need sudo for the install as long as the items in the prerequisites section have been installed properly.

```
./tools.sh prep
```
You can re-run prep over and over again as it, in most cases, will not re-install because it does checks to make sure the component exists or not, if it exists it does not run again.

## Running the tests

Tests are handled by PyTest via Tox

```
./tools.sh test
```

### Generating docs

Docs are not currently included in the source as they are changing rapidly. We do suggest you create the docs and look them over. Once this settles, we will likely have a online reference to these.

```
./tools.sh docs
```

## Deployment

We will update this section once things settle out, likely this will be a docker image or some other stateful package.

## Built With

* [AIOHttp](https://aiohttp.readthedocs.io/en/stable/) - The async web framework used
* [SQLAlchemy](https://www.sqlalchemy.org/) - Internal data storage

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/opencog/singnet/tags). 

See also the list of [contributors](https://github.com/opencog/singnet/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
