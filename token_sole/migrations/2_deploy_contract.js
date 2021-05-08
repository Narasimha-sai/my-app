const SaiToken = artifacts.require("SaiToken");

module.exports = function (deployer) {
  deployer.deploy(SaiToken);
};
