var fs = require('fs')

var Agent = artifacts.require('agent/Agent.sol')
var AgentFactory = artifacts.require('agent/AgentFactory.sol')
var AgentRegistry = artifacts.require('registries/AgentRegistry.sol')
var FixedSupplyToken = artifacts.require('tokens/FixedSupplyToken.sol')
var Escrow = artifacts.require('Escrow.sol')
var ownable = artifacts.require('ownership/ownable.sol')
var OrganizationFactory = artifacts.require('organization/OrganizationFactory.sol')
var Organization = artifacts.require('organization/Organization.sol')

module.exports = function(deployer) {
  deployer.deploy([
    Agent,
    AgentFactory,
    AgentRegistry,
    FixedSupplyToken,
    Escrow,
    ownable,
    Organization,
    OrganizationFactory
  ]).then(() => {
    const fileName = "addresses.json"
    const content = {
      Agent: Agent.address,
      AgentFactory: AgentFactory.address,
      AgentRegistry: AgentRegistry.address,
      FixedSupplyToken: FixedSupplyToken.address,
      Escrow: Escrow.address,
      ownable: ownable.address,
      Organization: Organization.address,
      OrganizationFactory: OrganizationFactory.address
    }

    fs.writeFile(fileName, JSON.stringify(content), 'utf-8', (err) => {
      if (err) { throw err }
      console.log("Contracts' addresses saved in ./" + fileName)
    })
  })
};
