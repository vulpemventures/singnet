# SingularityNET

To allow multiple computers to work as a whole to provide various services in a distributed and decentralized way.

## Architectural Overview ##
There are seven major interacting components in the SingularityNET architecture:

* **Network** - the block-chain and smart-contract network used for agent 
  negotiation and discovery
  
* **Agent** - the agent which provides services and responds to service
 requests by other agents in the SingularityNET

* **Ontology** - contains definitions of services available in SingularityNET. 
 Ontologies are versioned and define the semantics of network operations.

* **ServiceDescriptor** - a signed immutable post-negotiation description of a
 service which can be performed by an Agent
 
* **JobDescriptor** - a list of jobs which tie a particular ServiceDescriptor with 
 job-specific data like input and output data types, URLs, specific communication
 protocols etc.

* **ServiceAdapter** - a wrapper for AI and other services which an Agent can
 invoke to perform the actual services required to perform a job according to
 the negotiated ServiceDescriptor.

* **ExternalServiceProvider** - a wrapper for interacting with external service
 agents in the SingularityNET universe.

## Example Scenario ##
A SingularityNET Agent provides document smmarization services for corporate work
groups. As inputs for this service, it might require:

* **Glossary** - a glossary of terms and entities relevant a the corporation

* **People Images** - a set of images representing people to be recognized

* **Object Images** - a set of images representing things to be identified
  
* **Documents** - a set of documents to summarize in accepted formats

The task of performing document summarization requires summarizing text, identifying
relevant objects and people in images, ranking relevance, processing video to
extract objects and people and to provide a textual description, and generating
a ranked summary of the document.

### Internal Services ###
The SingularityNET Agent might perform the following services internally:

* **Final Document Summary** - assembling the parts and generating the final product

* **Text Summary** - processing the text to build a summary of text-only portions


### External Services ###
The Agent might use ExternalServiceProvider agents to perform the following services:

* **Word Sense Disambiguation** - a sub-service used by the Agent's Text Summary
 service to disambiguate words and meanings from text and context when more than
 one sense is possible and grammatically correct. 

* **Entity Extraction** - a sub-service which extracts object identities from
 images and text which match the Glossary and Images entries.

* **Video Summary** - a sub-service which extracts object identities from
 images and text which match the Glossary and both Images inputs.

* **Face Recognizer** - a sub-service which identifies people from the People
Images inputs

The architecture supports scenarios like the above where individual agents may 
provide subsets or all of the services required to deliver any Service in the
ontology.

## SingularityNET API

### NetworkABC ###
The base class for block-chain netwoks. NetworkABC defines the protocol for
managing the interactions of Agents, Ontology, ServiceDescriptors, as well as 
Agent discovery, and negotion. Each block-chain implementation will require a
separate NetworkABC subclass which implements the smart-contracts and communication
protocols required to implement the Network ABC API.

NetworkABC subclasses must implement:
* **`join_network`** - creates a new agent on the block chain
* **`leave_network`** - removes agent from the block chain
* **`logon_network`** - opens a connection for an agent
* **`logoff_network`** - closes the connection for an agent
* **`get_network_status`** - get the agents status on the network
* **`update_ontology`** - queries the block-chain and updates the ontology to current version
* **`advertise_service`** - registers an agent's service offerings on the blockchain
* **`remove_service_advertisement`** - removes an agents service offerings from the blockchain
* **`find_service_providers`** - returns a list of external service provider agents


### ServiceAdapterABC ###
This is the base class for all Service Adapters. Services can be AI services or
other services of use by the network like file storage, backup, etc.

ServiceAdapterABC subclasses must implement:
* **`perform`** - perform the service defined by the JobDescriptor

Additionally, ServiceAdapterABC subclasses may also implement:
* **`init`** - perform service one-time initialization
* **`start`** - connect with external network providers required to perform service
* **`stop`** - disconnect in preparation for taking service offline
* **`can_perform`** - override to implment service specific logic
* **`all_required_agents_can_perform`** - check if dependent agents can perform subservices



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
