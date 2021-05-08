var SaiToken = artifacts.require("SaiToken.sol");

contract('SaiToken', function(accounts) {

  it('sets totalSupply upon deployment', function() {
    return SaiToken.deployed().then(function(instance) {
      tokenInstance = instance;
      return tokenInstance.totalSupply();
    }).then(function(totalSupply) {
      assert.equal(totalSupply.toNumber(), 1000000, 'set the total supply to 1000000');
    })
    });
})