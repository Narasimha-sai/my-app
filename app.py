# from tatumpython.tatum.ledger import account
# from tatumpython.tatum.blockchain import ethereum
#from dotenv import load_dotenv
#import os
# body_params = {"currency": "BTC", "accountCode":"04_ACC_03", 'customer':{'externalId': '3dss4'}}
# print(account.create_new_account(body_params))

# body_params ={
#     "to": "0xCa64518Fe2fA22CdE41792668a9481dcd3bD1791",
#     "amount": "100",
#     "contractAddress": "0xc1f24Ab5707d2BB8Bc0B7ac5864b27E6DA6DFD1f",
#     "digits": 18,
#     "fromPrivateKey": "0x05e150c73f1920ec14caa1e0b6aa09940899678051a78542840c2668ce5080c2",
# }
# print(ethereum.transfer_ethereum_erc20(body_params))
#query_params = {'mnemonic': "maze truly suit grape buzz vessel coil broken photo rain material bind struggle hybrid cargo bench trash want ecology black enroll kid birth hurt"}
#print(ethereum.generate_ethereum_wallet(query_params))

#print(ethereum.generate_ethereum_wallet({'mnemonic': "maze truly suit grape buzz vessel coil broken photo rain material bind struggle hybrid cargo bench trash want ecology black enroll kid birth hurt"}))
from web3 import Web3
import json

# ganache_url = "https://mainnet.infura.io/v3/5ff8e077421744bca6c544a5e56756df"
ganache_url = "HTTP://127.0.0.1:8545"
# ganache_url = "https://ropsten.infura.io/v3/5ff8e077421744bca6c544a5e56756df"
web3 = Web3(Web3.HTTPProvider(ganache_url))


# video1

# print(web3.isConnected())
# print(web3.eth.getBalance('0x024a07b814B4908e2D9de255e338309eB223A560'))
# print(web3.fromWei(web3.eth.getBalance('0x024a07b814B4908e2D9de255e338309eB223A560'),'ether'))

#video 2


# abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"withdrawEther","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_value","type":"uint256"}],"name":"burn","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_value","type":"uint256"}],"name":"unfreeze","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"freezeOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_value","type":"uint256"}],"name":"freeze","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[{"name":"initialSupply","type":"uint256"},{"name":"tokenName","type":"string"},{"name":"decimalUnits","type":"uint8"},{"name":"tokenSymbol","type":"string"}],"payable":false,"type":"constructor"},{"payable":true,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Freeze","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Unfreeze","type":"event"}]')
# address = '0xB8c77482e45F1F44dE1745F52C74426C631bDD52'
# contract = web3.eth.contract(address=address,abi=abi)
# print(contract)
# print(contract.functions.name().call())
# print(contract.functions.totalSupply().call())
# s=contract.functions.totalSupply().call()
# print(web3.fromWei(s,'ether'))
# print(contract.functions.decimals().call())
# print(contract.functions.symbol().call())
# print(contract.functions.owner().call())
# print(contract.functions.balanceOf('0xB8c77482e45F1F44dE1745F52C74426C631bDD52').call())
# b=contract.functions.balanceOf('0xB8c77482e45F1F44dE1745F52C74426C631bDD52').call()
# print(web3.fromWei(b,'ether'))

# video 3

# account_1= '0xaE0835EC16922Bd9993EEF5cDa04606D53075c9c'
# account_2 = '0xe8a89c132f5Ffe4ddB31188f5D015a73f4dA1c8f'

# privateKey = '8c99665b1dc6a63e3583097f55478c2302ebcdeaf1311362d46f0cfa4ae1ac6d'

# get the nonce
# nonce = web3.eth.getTransactionCount(account_1)
# build a Transaction

# tx ={
#     'nonce' : nonce,
#     'to' : '0x1458Cc2CcC9Dd98AbDF50bBA9eea410EBF8DD325',
#     'value' : web3.toWei(1,'ether'),
#     'gas':2000000,
#     'gasPrice' : web3.toWei('101','gwei')
# }
# sign Transaction 
# sign_tx = web3.eth.account.signTransaction(tx,privateKey)

# send Transaction

# txn_hash = web3.eth.sendRawTransaction(sign_tx.rawTransaction)
# print(txn_hash)
# print hash
# print(txn_hash)
# Transaction Cost
# gas_price = web3.eth.getTransaction(txn_hash).gasPrice
# gas_used = web3.eth.getTransactionReceipt(txn_hash).gasUsed

# transaction_cost = gas_price* gas_used
# print(web3.toWei(gas_used,'ether'))
# print(gas_used)
# print(web3.toWei(gas_price,'ether'))
# print(gas_price)
# print(web3.toHex(txn_hash))

# video 4
# ------------------  code for remix ------------------------
# '''
# pragma solidity ^0.4.21;

# contract Greeter {

#     string public greeting;

#     function Greeter() public {
#     greeting = "Hello";
#     }
    
#     function setGreeting(string _greeting) public { 
#         greeting = _greeting;
#     }
    
#     function greet() view public returns (string) {
#         return greeting;
#     }
# }
# '''

# web3.eth.defaultAccount = web3.eth.accounts[0]
# abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
# address = web3.toChecksumAddress('0xc1e6239a505D4eFd0abAdaEE0dbF48918E57C694')
# contract = web3.eth.contract(address=address,abi=abi)
# print(contract.functions.greet().call())
'''-----------------------------------------------'''
# abi = json.loads('[{"constant": false,"inputs": [{"name": "spender","type": "address"},{"name": "value","type": "uint256"}],"name": "approve","outputs": [{"name": "","type": "bool"}],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": false,"inputs": [{"name": "spender","type": "address"},{"name": "subtractedValue","type": "uint256"}],"name": "decreaseAllowance","outputs": [{"name": "","type": "bool"}],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": false,"inputs": [{"name": "spender","type": "address"},{"name": "addedValue","type": "uint256"}],"name": "increaseAllowance","outputs": [{"name": "","type": "bool"}],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": false,"inputs": [{"name": "recipient","type": "address"},{"name": "amount","type": "uint256"}],"name": "transfer","outputs": [{"name": "","type": "bool"}],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": false,"inputs": [{"name": "sender","type": "address"},{"name": "recipient","type": "address"},{"name": "amount","type": "uint256"}],"name": "transferFrom","outputs": [{"name": "","type": "bool"}],"payable": false,"stateMutability": "nonpayable","type": "function"},{"inputs": [],"payable": false,"stateMutability": "nonpayable","type": "constructor"},{"anonymous": false,"inputs": [{"indexed": true,"name": "from","type": "address"},{"indexed": true,"name": "to","type": "address"},{"indexed": false,"name": "value","type": "uint256"}],"name": "Transfer","type": "event"},{"anonymous": false,"inputs": [{"indexed": true,"name": "owner","type": "address"},{"indexed": true,"name": "spender","type": "address"},{"indexed": false,"name": "value","type": "uint256"}],"name": "Approval","type": "event"},{"constant": true,"inputs": [{"name": "owner","type": "address"},{"name": "spender","type": "address"}],"name": "allowance","outputs": [{"name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [{"name": "account","type": "address"}],"name": "balanceOf","outputs": [{"name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "decimals","outputs": [{"name": "","type": "uint8"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "name","outputs": [{"name": "","type": "string"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "symbol","outputs": [{"name": "","type": "string"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "totalSupply","outputs": [{"name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"}]')
# address = web3.toChecksumAddress('')
# contract = web3.eth.contract(address=address,abi=abi)
# print(contract.functions.totalSupply().call())
'''----------------'''
# https://rinkeby.etherscan.io/tx/0x665e83f20234c230a530dec7934cd3c04048e3eb6d765343f558582b4a730e9f
# https://rinkeby.etherscan.io/tx/0x1195427803f94f14c53e956eadee3f4482fc4c8b473ced029e9f0673ba99a8de
# https://ropsten.etherscan.io/address/0x7845ea6fd886bef06e99cf7392d504f4e20cf9aa #faucet

# print(contract.functions.greet().call())
# print(web3.toHex(contract.functions.setGreeting('Hellooooooooooooo bro!').transact()))
# tx_hash = contract.functions.setGreeting('Hello bro!').transact()
# web3.eth.waitForTransactionReceipt(tx_hash)
# print("New Greeting : {}".format(contract.functions.greet().call()))

# abi = json.loads('[{"inputs":[],"name":"retrieve","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"num","type":"uint256"}],"name":"store","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
# address = web3.toChecksumAddress('0xf8e81D47203A594245E36C48e151709F0C19fBe8')
# contract = web3.eth.contract(address=address,abi=abi)
# print(contract.functions.store(10).transact())

# Video 5

# deploying the smart contract to blockchain (ganache)

# web3.eth.defaultAccount = web3.eth.accounts[0]
# abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
# bytecode = '6060604052341561000f57600080fd5b6040805190810160405280600581526020017f48656c6c6f0000000000000000000000000000000000000000000000000000008152506000908051906020019061005a929190610060565b50610105565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106100a157805160ff19168380011785556100cf565b828001600101855582156100cf579182015b828111156100ce5782518255916020019190600101906100b3565b5b5090506100dc91906100e0565b5090565b61010291905b808211156100fe5760008160009055506001016100e6565b5090565b90565b61041a806101146000396000f300606060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063a41368621461005c578063cfae3217146100b9578063ef690cc014610147575b600080fd5b341561006757600080fd5b6100b7600480803590602001908201803590602001908080601f016020809104026020016040519081016040528093929190818152602001838380828437820191505050505050919050506101d5565b005b34156100c457600080fd5b6100cc6101ef565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561010c5780820151818401526020810190506100f1565b50505050905090810190601f1680156101395780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b341561015257600080fd5b61015a610297565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561019a57808201518184015260208101905061017f565b50505050905090810190601f1680156101c75780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b80600090805190602001906101eb929190610335565b5050565b6101f76103b5565b60008054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561028d5780601f106102625761010080835404028352916020019161028d565b820191906000526020600020905b81548152906001019060200180831161027057829003601f168201915b5050505050905090565b60008054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561032d5780601f106103025761010080835404028352916020019161032d565b820191906000526020600020905b81548152906001019060200180831161031057829003601f168201915b505050505081565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061037657805160ff19168380011785556103a4565b828001600101855582156103a4579182015b828111156103a3578251825591602001919060010190610388565b5b5090506103b191906103c9565b5090565b602060405190810160405280600081525090565b6103eb91905b808211156103e75760008160009055506001016103cf565b5090565b905600a165627a7a723058205a7345ea6a4626ca9b62b37985fab4626ecbf890efe7b10370e5b432ae80820f0029'

# Greeter = web3.eth.contract(abi=abi,bytecode=bytecode)
# tx_hash = Greeter.constructor().transact()
# tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
# print(tx_receipt)

# contract = web3.eth.contract(address=tx_receipt.contractAddress,abi=abi)
# print(contract.functions.greet().call())
# print(contract.functions.setGreeting("Hello Narsi").transact())
# print(contract.functions.greet().call())

# video 6

# latest = web3.eth.blockNumber 
# print(latest)

# print(web3.eth.getBlock(latest)) # all details of block

# for i in range(0,10):
#     print(web3.eth.getBlock(latest-i))
#     print()




# hash = "0x3b9e1085e03cc5b2f09486154c5b760499949dd6f9e4a02a17739cf39d79244a"
# print(web3.eth.getTransactionByBlock(hash,2)) # here 2 means secound transaction

# --------------------------------------------------------------------------------------
# import mnemonic
# import bip32utils,base58,binascii
# mobj = mnemonic.Mnemonic("english")
# seed = mobj.to_seed("sketch gown boss rival bread era hood awake cover wreck price price")

# bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
# bip32_child_key_obj = bip32_root_key_obj.ChildKey(44 + bip32utils.BIP32_HARDEN).ChildKey(60 + bip32utils.BIP32_HARDEN).ChildKey(0 + bip32utils.BIP32_HARDEN).ChildKey(0).ChildKey(2)

# wif = bip32_child_key_obj.WalletImportFormat()

# first_encode = base58.b58decode(wif)
# private_key_full = binascii.hexlify(first_encode)
# private_key = '0x' + private_key_full[2:-10].decode("utf-8")
# print(private_key)

# txn = web3.eth.contract(address, abi=standard_token_abi).sendTransaction({
#     'from': from_address
# }).transfer(to_address, amount)
# print(txn)
# '''
# pragma solidity ^0.4.21;

# contract SoapBox {
#     // Our 'dict' of addresses that are approved to share opinions
#     mapping (address => bool) approvedSoapboxer;
#     string opinion;
     
#     // Our event to announce an opinion on the blockchain
#     event OpinionBroadcast(address _soapboxer, string _opinion);
#     // This is a constructor function, so its name has to match the contract
#     function SoapBox() public {
#     }
    
#     // Because this function is 'payable' it will be called when ether is sent to the contract address.
#     function() public payable{
#         // msg is a special variable that contains information about the transaction
#         if (msg.value > 20000000000000000) {  
#             //if the value sent greater than 0.02 ether (in Wei)
#             // then add the sender's address to approvedSoapboxer 
#             approvedSoapboxer[msg.sender] =  true;
#         }
#     }
    
    
#     // Our read-only function that checks whether the specified address is approved to post opinions.
    
#     function isApproved(address _soapboxer) public view returns (bool approved) {
#         return approvedSoapboxer[_soapboxer];    
        
#     } 
    
#     // Read-only function that returns the current opinion
#     function getCurrentOpinion() public view returns(string) {
#         return opinion;}
#     //Our function that modifies the state on the blockchain
#     function broadcastOpinion(string _opinion) public returns (bool success) {
#         // Looking up the address of the sender will return false if the sender isn't approved
#         if (approvedSoapboxer[msg.sender]) {
            
#             opinion = _opinion;
#             emit OpinionBroadcast(msg.sender, opinion);
#             return true;
            
#         } else {
#             return false;
#         }
        
#     }
# }'''
# [{constant: true,inputs: [],name: 'name',outputs: [{name: '',type: 'string',},],payable: false,stateMutability: 'view',type: 'function',},{constant: false,inputs: [{name: 'spender',type: 'address',},{name: 'value',type: 'uint256',},],name: 'approve',outputs: [{name: '',type: 'bool',},],payable: false,stateMutability: 'nonpayable',type: 'function',},{constant: true,inputs: [],name: 'totalSupply',outputs: [{name: '',type: 'uint256',},],payable: false,stateMutability: 'view',type: 'function',},{constant: false,inputs: [{name: 'from',type: 'address',},{name: 'to',type: 'address',},{name: 'value',type: 'uint256',},],name: 'transferFrom',outputs: [{name: '',type: 'bool',},],payable: false,stateMutability: 'nonpayable',type: 'function',},{constant: true,inputs: [],name: 'decimals',outputs: [{name: '',type: 'uint8',},],payable: false,stateMutability: 'view',type: 'function',},{constant: true,inputs: [],name: 'cap',outputs: [{name: '',type: 'uint256',},],payable: false,stateMutability: 'view',type: 'function',},{constant: false,inputs: [{name: 'spender',type: 'address',},{name: 'addedValue',type: 'uint256',},],name: 'increaseAllowance',outputs: [{name: '',type: 'bool',},],payable: false,stateMutability: 'nonpayable',type: 'function',},{constant: false,inputs: [{name: 'to',type: 'address',},{name: 'value',type: 'uint256',},],name: 'mint',outputs: [{name: '',type: 'bool',},],payable: false,stateMutability: 'nonpayable',type: 'function',},{constant: false,inputs: [{name: 'value',type: 'uint256',},],name: 'burn',outputs: [],payable: false,stateMutability: 'nonpayable',type: 'function',},{constant: true,inputs: [{name: 'owner',type: 'address',},],name: 'balanceOf',outputs: [{name: '',type: 'uint256',},],payable: false,stateMutability: 'view',type: 'function',},{constant: false,inputs: [{name: 'from',type: 'address',},{name: 'value',type: 'uint256',},],name: 'burnFrom',outputs: [],payable: false,stateMutability: 'nonpayable',type: 'function',},{constant: true,inputs: [],name: 'symbol',outputs: [{name: '',type: 'string',},],payable: false,stateMutability: 'view',type: 'function',},{constant: false,inputs: [{name: 'account',type: 'address',},],name: 'addMinter',outputs: [],payable: false,stateMutability: 'nonpayable',type: 'function',},{constant: false,inputs: [],name: 'renounceMinter',outputs: [],payable: false,stateMutability: 'nonpayable',type: 'function',},{constant: false,inputs: [{name: 'spender',type: 'address',},{name: 'subtractedValue',type: 'uint256',},],name: 'decreaseAllowance',outputs: [{name: '',type: 'bool',},],payable: false,stateMutability: 'nonpayable',type: 'function',},{constant: false,inputs: [{name: 'to',type: 'address',},{name: 'value',type: 'uint256',},],name: 'transfer',outputs: [{name: '',type: 'bool',},],payable: false,stateMutability: 'nonpayable',type: 'function',},{constant: true,inputs: [{name: 'account',type: 'address',},],name: 'isMinter',outputs: [{name: '',type: 'bool',},],payable: false,stateMutability: 'view',type: 'function',},{constant: true,inputs: [],name: 'builtOn',outputs: [{name: '',type: 'string',},],payable: false,stateMutability: 'view',type: 'function',},{constant: true,inputs: [{name: 'owner',type: 'address',},{name: 'spender',type: 'address',},],name: 'allowance',outputs: [{name: '',type: 'uint256',},],payable: false,stateMutability: 'view',type: 'function',},{inputs: [{name: 'name',type: 'string',},{name: 'symbol',type: 'string',},{name: 'receiver',type: 'address',},{name: 'decimals',type: 'uint8',},{name: 'cap',type: 'uint256',},{name: 'initialBalance',type: 'uint256',},],payable: false,stateMutability: 'nonpayable',type: 'constructor',},{anonymous: false,inputs: [{indexed: true,name: 'account',type: 'address',},],name: 'MinterAdded',type: 'event',},{anonymous: false,inputs: [{indexed: true,name: 'account',type: 'address',},],name: 'MinterRemoved',type: 'event',},{anonymous: false,inputs: [{indexed: true,name: 'from',type: 'address',},{indexed: true,name: 'to',type: 'address',},{indexed: false,name: 'value',type: 'uint256',},],name: 'Transfer',type: 'event',},{anonymous: false,inputs: [{indexed: true,name: 'owner',type: 'address',},{indexed: true,name: 'spender',type: 'address',},{indexed: false,name: 'value',type: 'uint256',},],name: 'Approval',type: 'event',},]
# abi = json.loads("[{'constant': true,'inputs': [],'name': 'name','outputs': [{'name': '','type': 'string',},],'payable': false,'stateMutability': 'view','type': 'function',},{'constant': false,'inputs': [{'name': 'spender','type': 'address',},{'name': 'value','type': 'uint256',},],'name': 'approve','outputs': [{'name': '','type': 'bool',},],'payable': false,'stateMutability': 'nonpayable','type': 'function',},{'constant': true,'inputs': [],'name': 'totalSupply','outputs': [{'name': '','type': 'uint256',},],'payable': false,'stateMutability': 'view','type': 'function',},{'constant': false,'inputs': [{'name': 'from','type': 'address',},{'name': 'to','type': 'address',},{'name': 'value','type': 'uint256',},],'name': 'transferFrom','outputs': [{'name': '','type': 'bool',},],'payable': false,'stateMutability': 'nonpayable','type': 'function',},{'constant': true,'inputs': [],'name': 'decimals','outputs': [{'name': '','type': 'uint8',},],'payable': false,'stateMutability': 'view','type': 'function',},{'constant': true,'inputs': [],'name': 'cap','outputs': [{'name': '','type': 'uint256',},],'payable': false,'stateMutability': 'view','type': 'function',},{'constant': false,'inputs': [{'name': 'spender','type': 'address',},{'name': 'addedValue','type': 'uint256',},],'name': 'increaseAllowance','outputs': [{'name': '','type': 'bool',},],'payable': false,'stateMutability': 'nonpayable','type': 'function',},{'constant': false,'inputs': [{'name': 'to','type': 'address',},{'name': 'value','type': 'uint256',},],'name': 'mint','outputs': [{'name': '','type': 'bool',},],'payable': false,'stateMutability': 'nonpayable','type': 'function',},{'constant': false,'inputs': [{'name': 'value','type': 'uint256',},],'name': 'burn','outputs': [],'payable': false,'stateMutability': 'nonpayable','type': 'function',},{'constant': true,'inputs': [{'name': 'owner','type': 'address',},],'name': 'balanceOf','outputs': [{'name': '','type': 'uint256',},],'payable': false,'stateMutability': 'view','type': 'function',},{'constant': false,'inputs': [{'name': 'from','type': 'address',},{'name': 'value','type': 'uint256',},],'name': 'burnFrom','outputs': [],'payable': false,'stateMutability': 'nonpayable','type': 'function',},{'constant': true,'inputs': [],'name': 'symbol','outputs': [{'name': '','type': 'string',},],'payable': false,'stateMutability': 'view','type': 'function',},{'constant': false,'inputs': [{'name': 'account','type': 'address',},],'name': 'addMinter','outputs': [],'payable': false,'stateMutability': 'nonpayable','type': 'function',},{'constant': false,'inputs': [],'name': 'renounceMinter','outputs': [],'payable': false,'stateMutability': 'nonpayable','type': 'function',},{'constant': false,'inputs': [{'name': 'spender','type': 'address',},{'name': 'subtractedValue','type': 'uint256',},],'name': 'decreaseAllowance','outputs': [{'name': '','type': 'bool',},],'payable': false,'stateMutability': 'nonpayable','type': 'function',},{'constant': false,'inputs': [{'name': 'to','type': 'address',},{'name': 'value','type': 'uint256',},],'name': 'transfer','outputs': [{'name': '','type': 'bool',},],'payable': false,'stateMutability': 'nonpayable','type': 'function',},{'constant': true,'inputs': [{'name': 'account','type': 'address',},],'name': 'isMinter','outputs': [{'name': '','type': 'bool',},],'payable': false,'stateMutability': 'view','type': 'function',},{'constant': true,'inputs': [],'name': 'builtOn','outputs': [{'name': '','type': 'string',},],'payable': false,'stateMutability': 'view','type': 'function',},{'constant': true,'inputs': [{'name': 'owner','type': 'address',},{'name': 'spender','type': 'address',},],'name': 'allowance','outputs': [{'name': '','type': 'uint256',},],'payable': false,'stateMutability': 'view','type': 'function',},{'inputs': [{'name': 'name','type': 'string',},{'name': 'symbol','type': 'string',},{'name': 'receiver','type': 'address',},{'name': 'decimals','type': 'uint8',},{'name': 'cap','type': 'uint256',},{'name': 'initialBalance','type': 'uint256',},],'payable': false,'stateMutability': 'nonpayable','type': 'constructor',},{'anonymous': false,'inputs': [{'indexed': true,'name': 'account','type': 'address',},],'name': 'MinterAdded','type': 'event',},{'anonymous': false,'inputs': [{'indexed': true,'name': 'account','type': 'address',},],'name': 'MinterRemoved','type': 'event',},{'anonymous': false,'inputs': [{'indexed': true,'name': 'from','type': 'address',},{'indexed': true,'name': 'to','type': 'address',},{'indexed': false,'name': 'value','type': 'uint256',},],'name': 'Transfer','type': 'event',},{'anonymous': false,'inputs': [{'indexed': true,'name': 'owner','type': 'address',},{'indexed': true,'name': 'spender','type': 'address',},{'indexed': false,'name': 'value','type': 'uint256',},],'name': 'Approval','type': 'event',},]")
# address = address = web3.toChecksumAddress('0x0C0db1Eeb7c420eBebf34C50c80da0C6361688d7')
# print(web3.eth.contract(address=address,abi=abi))
# bytecode = "0x60806040526040805190810160405280601081526020017f68747470733a2f2f746174756d2e696f000000000000000000000000000000008152506008908051906020019062000051929190620005e5565b503480156200005f57600080fd5b5060405162001db138038062001db1833981018060405260c08110156200008557600080fd5b8101908080516401000000008111156200009e57600080fd5b82810190506020810184811115620000b557600080fd5b8151856001820283011164010000000082111715620000d357600080fd5b50509291906020018051640100000000811115620000f057600080fd5b828101905060208101848111156200010757600080fd5b81518560018202830111640100000000821117156200012557600080fd5b50509291906020018051906020019092919080519060200190929190805190602001909291908051906020019092919050505081868685826000908051906020019062000174929190620005e5565b5081600190805190602001906200018d929190620005e5565b5080600260006101000a81548160ff021916908360ff160217905550505050620001c63362000210640100000000026401000000009004565b600081111515620001d657600080fd5b8060078190555050600081111562000204576200020384826200027a640100000000026401000000009004565b5b50505050505062000694565b62000234816006620002ea6401000000000262001582179091906401000000009004565b8073ffffffffffffffffffffffffffffffffffffffff167f6ae172837ea30b801fbfcdd4108aa1d5bf8ff775444fd70256b44e6bf3dfc3f660405160405180910390a250565b600754620002b8826200029b620003ad640100000000026401000000009004565b620003b7640100000000026200108e179091906401000000009004565b11151515620002c657600080fd5b620002e68282620003d9640100000000026200142c176401000000009004565b5050565b600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff16141515156200032757600080fd5b62000342828262000550640100000000026401000000009004565b1515156200034f57600080fd5b60018260000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055505050565b6000600554905090565b6000808284019050838110151515620003cf57600080fd5b8091505092915050565b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff16141515156200041657600080fd5b6200043b81600554620003b7640100000000026200108e179091906401000000009004565b600581905550620004a381600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054620003b7640100000000026200108e179091906401000000009004565b600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508173ffffffffffffffffffffffffffffffffffffffff16600073ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef836040518082815260200191505060405180910390a35050565b60008073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff16141515156200058e57600080fd5b8260000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905092915050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106200062857805160ff191683800117855562000659565b8280016001018555821562000659579182015b82811115620006585782518255916020019190600101906200063b565b5b5090506200066891906200066c565b5090565b6200069191905b808211156200068d57600081600090555060010162000673565b5090565b90565b61170d80620006a46000396000f3fe608060405234801561001057600080fd5b506004361061013e576000357c01000000000000000000000000000000000000000000000000000000009004806370a08231116100ca578063a457c2d71161008e578063a457c2d714610583578063a9059cbb146105e9578063aa271e1a1461064f578063b60b7084146106ab578063dd62ed3e1461072e5761013e565b806370a082311461040c57806379cc67901461046457806395d89b41146104b2578063983b2d561461053557806398650275146105795761013e565b8063313ce56711610111578063313ce567146102d0578063355274ea146102f4578063395093511461031257806340c10f191461037857806342966c68146103de5761013e565b806306fdde0314610143578063095ea7b3146101c657806318160ddd1461022c57806323b872dd1461024a575b600080fd5b61014b6107a6565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561018b578082015181840152602081019050610170565b50505050905090810190601f1680156101b85780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b610212600480360360408110156101dc57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050610848565b604051808215151515815260200191505060405180910390f35b61023461085f565b6040518082815260200191505060405180910390f35b6102b66004803603606081101561026057600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050610869565b604051808215151515815260200191505060405180910390f35b6102d861091a565b604051808260ff1660ff16815260200191505060405180910390f35b6102fc610931565b6040518082815260200191505060405180910390f35b61035e6004803603604081101561032857600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291908035906020019092919050505061093b565b604051808215151515815260200191505060405180910390f35b6103c46004803603604081101561038e57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803590602001909291905050506109e0565b604051808215151515815260200191505060405180910390f35b61040a600480360360208110156103f457600080fd5b8101908080359060200190929190505050610a0a565b005b61044e6004803603602081101561042257600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610a17565b6040518082815260200191505060405180910390f35b6104b06004803603604081101561047a57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050610a60565b005b6104ba610a6e565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156104fa5780820151818401526020810190506104df565b50505050905090810190601f1680156105275780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b6105776004803603602081101561054b57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610b10565b005b610581610b30565b005b6105cf6004803603604081101561059957600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050610b3b565b604051808215151515815260200191505060405180910390f35b610635600480360360408110156105ff57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050610be0565b604051808215151515815260200191505060405180910390f35b6106916004803603602081101561066557600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610bf7565b604051808215151515815260200191505060405180910390f35b6106b3610c14565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156106f35780820151818401526020810190506106d8565b50505050905090810190601f1680156107205780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b6107906004803603604081101561074457600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610cb2565b6040518082815260200191505060405180910390f35b606060008054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561083e5780601f106108135761010080835404028352916020019161083e565b820191906000526020600020905b81548152906001019060200180831161082157829003601f168201915b5050505050905090565b6000610855338484610d39565b6001905092915050565b6000600554905090565b6000610876848484610e9c565b61090f843361090a85600460008a73ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461106c90919063ffffffff16565b610d39565b600190509392505050565b6000600260009054906101000a900460ff16905090565b6000600754905090565b60006109d633846109d185600460003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008973ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461108e90919063ffffffff16565b610d39565b6001905092915050565b60006109eb33610bf7565b15156109f657600080fd5b610a0083836110af565b6001905092915050565b610a1433826110e7565b50565b6000600360008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b610a6a828261123d565b5050565b606060018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610b065780601f10610adb57610100808354040283529160200191610b06565b820191906000526020600020905b815481529060010190602001808311610ae957829003601f168201915b5050505050905090565b610b1933610bf7565b1515610b2457600080fd5b610b2d816112e4565b50565b610b393361133e565b565b6000610bd63384610bd185600460003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008973ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461106c90919063ffffffff16565b610d39565b6001905092915050565b6000610bed338484610e9c565b6001905092915050565b6000610c0d82600661139890919063ffffffff16565b9050919050565b60088054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610caa5780601f10610c7f57610100808354040283529160200191610caa565b820191906000526020600020905b815481529060010190602001808311610c8d57829003601f168201915b505050505081565b6000600460008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054905092915050565b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff1614151515610d7557600080fd5b600073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff1614151515610db157600080fd5b80600460008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925836040518082815260200191505060405180910390a3505050565b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff1614151515610ed857600080fd5b610f2a81600360008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461106c90919063ffffffff16565b600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550610fbf81600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461108e90919063ffffffff16565b600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef836040518082815260200191505060405180910390a3505050565b600082821115151561107d57600080fd5b600082840390508091505092915050565b60008082840190508381101515156110a557600080fd5b8091505092915050565b6007546110cc826110be61085f565b61108e90919063ffffffff16565b111515156110d957600080fd5b6110e3828261142c565b5050565b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415151561112357600080fd5b6111388160055461106c90919063ffffffff16565b60058190555061119081600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461106c90919063ffffffff16565b600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef836040518082815260200191505060405180910390a35050565b61124782826110e7565b6112e082336112db84600460008873ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461106c90919063ffffffff16565b610d39565b5050565b6112f881600661158290919063ffffffff16565b8073ffffffffffffffffffffffffffffffffffffffff167f6ae172837ea30b801fbfcdd4108aa1d5bf8ff775444fd70256b44e6bf3dfc3f660405160405180910390a250565b61135281600661163290919063ffffffff16565b8073ffffffffffffffffffffffffffffffffffffffff167fe94479a9f7e1952cc78f2d6baab678adc1b772d936c6583def489e524cb6669260405160405180910390a250565b60008073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff16141515156113d557600080fd5b8260000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905092915050565b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415151561146857600080fd5b61147d8160055461108e90919063ffffffff16565b6005819055506114d581600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461108e90919063ffffffff16565b600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508173ffffffffffffffffffffffffffffffffffffffff16600073ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef836040518082815260200191505060405180910390a35050565b600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff16141515156115be57600080fd5b6115c88282611398565b1515156115d457600080fd5b60018260000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055505050565b600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff161415151561166e57600080fd5b6116788282611398565b151561168357600080fd5b60008260000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff021916908315150217905550505056fea165627a7a72305820bd0d80acdad0a158a00477c7002345806238849601fbc1885354626cddf54c990029"

# Greeter = web3.eth.contract(abi=abi,bytecode=bytecode)
# print(Greeter)
# ==============================================================================================================================

import cerberus
import re
from termcolor import colored
v = cerberus.Validator()


def erros_print(v):
    if v.errors != {}:
        print(colored(v.errors, 'red')) 
        return False
    else:
        return True

def check_allowed_chars(allowed_chars, variableName, variableValue):
    match = re.search(allowed_chars, variableValue)
    if match is None:
        print(colored("'{}': contains not allowed characters".format(variableName), 'red'))
        return False
    else:
        return True

def invoke_smart_contract_method(body_params):
    result = True
    body_schema = {
            "contractAddress": {"required": True, "type" : "string", "minlength": 42, "maxlength": 42},
            "methodName": {"required": True, "type" : "string", "minlength": 1, "maxlength": 500},
            "methodABI": {"required": True, "type" : "list", 'schema' : {'type':'dict'}},
            "params": {"required": True, "type" : "dict"},
            "fromPrivateKey": {"type" : "string", "minlength": 66, "maxlength": 66},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
            "nonce": {"type" : "string",  "minlength": 0},
            "fee": {"type" : "dict", 'schema': {'gasLimit': {"required": True, "type" : "string"}, 'gasPrice': {"required": True, "type" : "string"}}}
        }
    v.validate(body_params, body_schema)
    result = result & erros_print(v)
    if result:
        if 'fee' in body_params.keys():
            result = result & check_allowed_chars('^[+]?\d+$', 'gasLimit', body_params['fee']['gasLimit'])
            result = result & check_allowed_chars('^[+]?\d+$', 'gasPrice', body_params['fee']['gasPrice'])
        return result

body_params = {
    'contractAddress':'0x06DAed049dB2dE3ACac8EC935dD2Fb82816F2594',
    'methodName':'name',
    'params':{}, #'address':'0xaE0835EC16922Bd9993EEF5cDa04606D53075c9c'},
    'methodABI':[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint256","name":"_decimals","type":"uint256"},{"internalType":"uint256","name":"_totalSupply","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":'false',"inputs":[{"indexed":'false',"internalType":"address","name":"owner","type":"address"},{"indexed":'false',"internalType":"address","name":"spender","type":"address"},{"indexed":'false',"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":'false',"inputs":[{"indexed":'false',"internalType":"address","name":"from","type":"address"},{"indexed":'false',"internalType":"address","name":"to","type":"address"},{"indexed":'false',"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"_spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_spender","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]
}

def invoke_func(body_params):
    if(invoke_smart_contract_method(body_params)):
        # abi = json.loads('[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint256","name":"_decimals","type":"uint256"},{"internalType":"uint256","name":"_totalSupply","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"_spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_spender","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]')
        # address = web3.toChecksumAddress('0x06DAed049dB2dE3ACac8EC935dD2Fb82816F2594')
        contract = web3.eth.contract(abi=body_params['methodABI'],address=body_params['contractAddress'])
        # return(len(body_params['params']))
        if(len(body_params['params'])==0):
          if('name'== body_params['methodName']):
            return({'data': contract.functions.name().call()})
          if('symbol' == body_params['methodName']):
            return({'data':contract.functions.symbol().call()})
          if('decimals' == body_params['methodName']):
            return({'data':contract.functions.decimals().call()})
          if('totalSupply' == body_params['methodName']):
            return({'data':contract.functions.totalSupply().call()})
        else:
          if('balanceOf' == body_params['methodName']):
            return({'data':contract.functions.balanceOf(body_params['params']['address']).call()})

print(invoke_func(body_params))


ab = [{"inputs": [
        {
          "internalType": "string",
          "name": "name_",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "symbol_",
          "type": "string"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": 'false',
      "inputs": [
        {
          "indexed": 'true',
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": 'true',
          "internalType": "address",
          "name": "approved",
          "type": "address"
        },
        {
          "indexed": 'true',
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        }
      ],
      "name": "Approval",
      "type": "event"
    },
    {
      "anonymous": 'false',
      "inputs": [
        {
          "indexed": 'true',
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": 'true',
          "internalType": "address",
          "name": "operator",
          "type": "address"
        },
        {
          "indexed": 'false',
          "internalType": "bool",
          "name": "approved",
          "type": "bool"
        }
      ],
      "name": "ApprovalForAll",
      "type": "event"
    },
    {
      "anonymous": 'false',
      "inputs": [
        {
          "indexed": 'true',
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "indexed": 'true',
          "internalType": "bytes32",
          "name": "previousAdminRole",
          "type": "bytes32"
        },
        {
          "indexed": 'true',
          "internalType": "bytes32",
          "name": "newAdminRole",
          "type": "bytes32"
        }
      ],
      "name": "RoleAdminChanged",
      "type": "event"
    },
    {
      "anonymous": 'false',
      "inputs": [
        {
          "indexed": 'true',
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "indexed": 'true',
          "internalType": "address",
          "name": "account",
          "type": "address"
        },
        {
          "indexed": 'true',
          "internalType": "address",
          "name": "sender",
          "type": "address"
        }
      ],
      "name": "RoleGranted",
      "type": "event"
    },
    {
      "anonymous": 'false',
      "inputs": [
        {
          "indexed": 'true',
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "indexed": 'true',
          "internalType": "address",
          "name": "account",
          "type": "address"
        },
        {
          "indexed": 'true',
          "internalType": "address",
          "name": "sender",
          "type": "address"
        }
      ],
      "name": "RoleRevoked",
      "type": "event"
    },
    {
      "anonymous": 'false',
      "inputs": [
        {
          "indexed": 'true',
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "indexed": 'true',
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "indexed": 'true',
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        }
      ],
      "name": "Transfer",
      "type": "event"
    },
    {
      "inputs": [],
      "name": "DEFAULT_ADMIN_ROLE",
      "outputs": [
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "MINTER_ROLE",
      "outputs": [
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        }
      ],
      "name": "approve",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "owner",
          "type": "address"
        }
      ],
      "name": "balanceOf",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        }
      ],
      "name": "burn",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        }
      ],
      "name": "getApproved",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        }
      ],
      "name": "getRoleAdmin",
      "outputs": [
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "internalType": "uint256",
          "name": "index",
          "type": "uint256"
        }
      ],
      "name": "getRoleMember",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        }
      ],
      "name": "getRoleMemberCount",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "grantRole",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "hasRole",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "operator",
          "type": "address"
        }
      ],
      "name": "isApprovedForAll",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address[]",
          "name": "to",
          "type": "address[]"
        },
        {
          "internalType": "uint256[]",
          "name": "tokenId",
          "type": "uint256[]"
        },
        {
          "internalType": "string[]",
          "name": "tokenURI",
          "type": "string[]"
        }
      ],
      "name": "mintMultiple",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        },
        {
          "internalType": "string",
          "name": "tokenURI",
          "type": "string"
        }
      ],
      "name": "mintWithTokenURI",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "name",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        }
      ],
      "name": "ownerOf",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "renounceRole",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "revokeRole",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "internalType": "uint256","name": "tokenId","type": "uint256"}],"name": "safeTransfer","outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [{"internalType": "address","name": "from","type": "address"},{"internalType": "address","name": "to","type": "address"},{"internalType": "uint256","name": "tokenId","type": "uint256"}],"name": "safeTransferFrom","outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [{"internalType": "address","name": "from","type": "address"},{"internalType": "address","name": "to","type": "address"},{"internalType": "uint256","name": "tokenId","type": "uint256"},{"internalType": "bytes","name": "_data","type": "bytes"}],"name": "safeTransferFrom","outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [{"internalType": "address","name": "operator","type": "address"},{"internalType": "bool","name": "approved","type": "bool"}],"name": "setApprovalForAll","outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [{"internalType": "bytes4","name": "interfaceId","type": "bytes4"}],"name": "supportsInterface","outputs": [{"internalType": "bool","name": "","type": "bool"}],"stateMutability": "view","type": "function"},{"inputs": [],"name": "symbol","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"},{"inputs": [{"internalType": "uint256","name": "index","type": "uint256"}],"name": "tokenByIndex","outputs": [{"internalType": "uint256","name": "","type": "uint256"}],"stateMutability": "view","type": "function"},{"inputs": [{"internalType": "address","name": "owner","type": "address"},{"internalType": "uint256","name": "index","type": "uint256"}],"name": "tokenOfOwnerByIndex","outputs": [{"internalType": "uint256","name": "","type": "uint256"}],"stateMutability": "view","type": "function"},{"inputs": [{"internalType": "uint256","name": "tokenId","type": "uint256"}],"name": "tokenURI","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"},{"inputs": [{"internalType": "address","name": "owner","type": "address"}],"name": "tokensOfOwner","outputs": [{"internalType": "uint256[]","name": "","type": "uint256[]"}],"stateMutability": "view","type": "function"},{"inputs": [],"name": "totalSupply","outputs": [{"internalType": "uint256","name": "","type": "uint256"}],"stateMutability": "view","type": "function"},{"inputs": [{"internalType": "address","name": "from","type": "address"},{"internalType": "address","name": "to","type": "address"},{"internalType": "uint256","name": "tokenId","type": "uint256"}],"name": "transferFrom","outputs": [],"stateMutability": "nonpayable","type": "function"}]

# bytecode = '0x60806040523480156200001157600080fd5b50604051620051cf380380620051cf833981810160405281019062000037919062000494565b818181600090805190602001906200005192919062000372565b5080600190805190602001906200006a92919062000372565b505050620000916000801b62000085620000da60201b60201c565b620000e260201b60201c565b620000d27f9f2df0fed2c77648de5860a4cc508cd0818c85b8b8a1ab4ceeef8d981c8956a6620000c6620000da60201b60201c565b620000e260201b60201c565b505062000638565b600033905090565b620000f982826200012a60201b620014e71760201c565b6200012581600c60008581526020019081526020016000206200014060201b620014f51790919060201c565b505050565b6200013c82826200017860201b60201c565b5050565b600062000170836000018373ffffffffffffffffffffffffffffffffffffffff1660001b6200026a60201b60201c565b905092915050565b6200018a8282620002e460201b60201c565b62000266576001600b600084815260200190815260200160002060000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055506200020b620000da60201b60201c565b73ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff16837f2f8788117e7eff1d82e926ec794901d17c78024a50270940304540a733656f0d60405160405180910390a45b5050565b60006200027e83836200034f60201b60201c565b620002d9578260000182908060018154018082558091505060019003906000526020600020016000909190919091505582600001805490508360010160008481526020019081526020016000208190555060019050620002de565b600090505b92915050565b6000600b600084815260200190815260200160002060000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905092915050565b600080836001016000848152602001908152602001600020541415905092915050565b8280546200038090620005a4565b90600052602060002090601f016020900481019282620003a45760008555620003f0565b82601f10620003bf57805160ff1916838001178555620003f0565b82800160010185558215620003f0579182015b82811115620003ef578251825591602001919060010190620003d2565b5b509050620003ff919062000403565b5090565b5b808211156200041e57600081600090555060010162000404565b5090565b60006200043962000433846200053b565b62000507565b9050828152602081018484840111156200045257600080fd5b6200045f8482856200056e565b509392505050565b600082601f8301126200047957600080fd5b81516200048b84826020860162000422565b91505092915050565b60008060408385031215620004a857600080fd5b600083015167ffffffffffffffff811115620004c357600080fd5b620004d18582860162000467565b925050602083015167ffffffffffffffff811115620004ef57600080fd5b620004fd8582860162000467565b9150509250929050565b6000604051905081810181811067ffffffffffffffff8211171562000531576200053062000609565b5b8060405250919050565b600067ffffffffffffffff82111562000559576200055862000609565b5b601f19601f8301169050602081019050919050565b60005b838110156200058e57808201518184015260208101905062000571565b838111156200059e576000848401525b50505050565b60006002820490506001821680620005bd57607f821691505b60208210811415620005d457620005d3620005da565b5b50919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b614b8780620006486000396000f3fe608060405234801561001057600080fd5b50600436106101da5760003560e01c80635a9c9eb811610104578063a217fddf116100a2578063ca15c87311610071578063ca15c873146105c3578063d5391393146105f3578063d547741f14610611578063e985e9c51461062d576101da565b8063a217fddf1461053d578063a22cb4651461055b578063b88d4fde14610577578063c87b56dd14610593576101da565b80638462151c116100de5780638462151c1461048f5780639010d07c146104bf57806391d14854146104ef57806395d89b411461051f576101da565b80635a9c9eb8146103ff5780636352211e1461042f57806370a082311461045f576101da565b80632f2ff15d1161017c57806342842e0e1161014b57806342842e0e1461036757806342966c68146103835780634f6ccce71461039f57806350bb4e7f146103cf576101da565b80632f2ff15d146102e35780632f745c59146102ff57806336568abe1461032f578063423f6cef1461034b576101da565b8063095ea7b3116101b8578063095ea7b31461025d57806318160ddd1461027957806323b872dd14610297578063248a9ca3146102b3576101da565b806301ffc9a7146101df57806306fdde031461020f578063081812fc1461022d575b600080fd5b6101f960048036038101906101f4919061373c565b61065d565b60405161020691906142e6565b60405180910390f35b61021761066f565b604051610224919061431c565b60405180910390f35b6102476004803603810190610242919061378e565b610701565b604051610254919061425d565b60405180910390f35b61027760048036038101906102729190613561565b610786565b005b61028161089e565b60405161028e919061463e565b60405180910390f35b6102b160048036038101906102ac919061345b565b6108ab565b005b6102cd60048036038101906102c8919061369b565b61090b565b6040516102da9190614301565b60405180910390f35b6102fd60048036038101906102f891906136c4565b61092b565b005b61031960048036038101906103149190613561565b61095f565b604051610326919061463e565b60405180910390f35b610349600480360381019061034491906136c4565b610a04565b005b61036560048036038101906103609190613561565b610a87565b005b610381600480360381019061037c919061345b565b610aad565b005b61039d6004803603810190610398919061378e565b610acd565b005b6103b960048036038101906103b4919061378e565b610b29565b6040516103c6919061463e565b60405180910390f35b6103e960048036038101906103e4919061359d565b610bc0565b6040516103f691906142e6565b60405180910390f35b61041960048036038101906104149190613604565b610c51565b60405161042691906142e6565b60405180910390f35b6104496004803603810190610444919061378e565b610e02565b604051610456919061425d565b60405180910390f35b610479600480360381019061047491906133f6565b610eb4565b604051610486919061463e565b60405180910390f35b6104a960048036038101906104a491906133f6565b610f6c565b6040516104b691906142c4565b60405180910390f35b6104d960048036038101906104d49190613700565b6110af565b6040516104e6919061425d565b60405180910390f35b610509600480360381019061050491906136c4565b6110de565b60405161051691906142e6565b60405180910390f35b610527611149565b604051610534919061431c565b60405180910390f35b6105456111db565b6040516105529190614301565b60405180910390f35b61057560048036038101906105709190613525565b6111e2565b005b610591600480360381019061058c91906134aa565b611363565b005b6105ad60048036038101906105a8919061378e565b6113c5565b6040516105ba919061431c565b60405180910390f35b6105dd60048036038101906105d8919061369b565b6113d7565b6040516105ea919061463e565b60405180910390f35b6105fb6113fb565b6040516106089190614301565b60405180910390f35b61062b600480360381019061062691906136c4565b61141f565b005b6106476004803603810190610642919061341f565b611453565b60405161065491906142e6565b60405180910390f35b600061066882611525565b9050919050565b60606000805461067e90614965565b80601f01602080910402602001604051908101604052809291908181526020018280546106aa90614965565b80156106f75780601f106106cc576101008083540402835291602001916106f7565b820191906000526020600020905b8154815290600101906020018083116106da57829003601f168201915b5050505050905090565b600061070c8261159f565b61074b576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016107429061451e565b60405180910390fd5b6004600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050919050565b600061079182610e02565b90508073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff161415610802576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016107f99061457e565b60405180910390fd5b8073ffffffffffffffffffffffffffffffffffffffff1661082161160b565b73ffffffffffffffffffffffffffffffffffffffff161480610850575061084f8161084a61160b565b611453565b5b61088f576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016108869061445e565b60405180910390fd5b6108998383611613565b505050565b6000600880549050905090565b6108bc6108b661160b565b826116cc565b6108fb576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016108f29061459e565b60405180910390fd5b6109068383836117aa565b505050565b6000600b6000838152602001908152602001600020600101549050919050565b6109358282611a06565b61095a81600c60008581526020019081526020016000206114f590919063ffffffff16565b505050565b600061096a83610eb4565b82106109ab576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016109a29061437e565b60405180910390fd5b600660008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600083815260200190815260200160002054905092915050565b610a0c61160b565b73ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff1614610a79576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610a709061461e565b60405180910390fd5b610a838282611a6c565b5050565b610aa9610a9261160b565b838360405180602001604052806000815250611363565b5050565b610ac883838360405180602001604052806000815250611363565b505050565b610ade610ad861160b565b826116cc565b610b1d576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610b14906145fe565b60405180910390fd5b610b2681611b4e565b50565b6000610b3361089e565b8210610b74576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610b6b906145be565b60405180910390fd5b60088281548110610bae577f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b90600052602060002001549050919050565b6000610bf37f9f2df0fed2c77648de5860a4cc508cd0818c85b8b8a1ab4ceeef8d981c8956a6610bee61160b565b6110de565b610c32576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610c29906145de565b60405180910390fd5b610c3c8484611b5a565b610c468383611d28565b600190509392505050565b6000610c847f9f2df0fed2c77648de5860a4cc508cd0818c85b8b8a1ab4ceeef8d981c8956a6610c7f61160b565b6110de565b610cc3576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610cba906145de565b60405180910390fd5b60005b8451811015610df657610d59858281518110610d0b577f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b6020026020010151858381518110610d4c577f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b6020026020010151611b5a565b610de3848281518110610d95577f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b6020026020010151848381518110610dd6577f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b6020026020010151611d28565b8080610dee90614997565b915050610cc6565b50600190509392505050565b6000806002600084815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff161415610eab576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610ea29061449e565b60405180910390fd5b80915050919050565b60008073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415610f25576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610f1c9061447e565b60405180910390fd5b600360008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b60606000610f7983610eb4565b67ffffffffffffffff811115610fb8577f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b604051908082528060200260200182016040528015610fe65781602001602082028036833780820191505090505b50905060005b610ff584610eb4565b8110156110a557600660008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082815260200190815260200160002054828281518110611086577f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b602002602001018181525050808061109d90614997565b915050610fec565b5080915050919050565b60006110d682600c6000868152602001908152602001600020611d9c90919063ffffffff16565b905092915050565b6000600b600084815260200190815260200160002060000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905092915050565b60606001805461115890614965565b80601f016020809104026020016040519081016040528092919081815260200182805461118490614965565b80156111d15780601f106111a6576101008083540402835291602001916111d1565b820191906000526020600020905b8154815290600101906020018083116111b457829003601f168201915b5050505050905090565b6000801b81565b6111ea61160b565b73ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415611258576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161124f906143fe565b60405180910390fd5b806005600061126561160b565b73ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055508173ffffffffffffffffffffffffffffffffffffffff1661131261160b565b73ffffffffffffffffffffffffffffffffffffffff167f17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c318360405161135791906142e6565b60405180910390a35050565b61137461136e61160b565b836116cc565b6113b3576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016113aa9061459e565b60405180910390fd5b6113bf84848484611db6565b50505050565b60606113d082611e12565b9050919050565b60006113f4600c6000848152602001908152602001600020611f64565b9050919050565b7f9f2df0fed2c77648de5860a4cc508cd0818c85b8b8a1ab4ceeef8d981c8956a681565b6114298282611f79565b61144e81600c6000858152602001908152602001600020611fdf90919063ffffffff16565b505050565b6000600560008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905092915050565b6114f1828261200f565b5050565b600061151d836000018373ffffffffffffffffffffffffffffffffffffffff1660001b6120f0565b905092915050565b60007f5a05180f000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff19161480611598575061159782612160565b5b9050919050565b60008073ffffffffffffffffffffffffffffffffffffffff166002600084815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614159050919050565b600033905090565b816004600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff1661168683610e02565b73ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b92560405160405180910390a45050565b60006116d78261159f565b611716576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161170d9061441e565b60405180910390fd5b600061172183610e02565b90508073ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff16148061179057508373ffffffffffffffffffffffffffffffffffffffff1661177884610701565b73ffffffffffffffffffffffffffffffffffffffff16145b806117a157506117a08185611453565b5b91505092915050565b8273ffffffffffffffffffffffffffffffffffffffff166117ca82610e02565b73ffffffffffffffffffffffffffffffffffffffff1614611820576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016118179061453e565b60405180910390fd5b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415611890576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611887906143de565b60405180910390fd5b61189b8383836121da565b6118a6600082611613565b6001600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282546118f69190614871565b925050819055506001600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825461194d91906147ea565b92505081905550816002600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60405160405180910390a4505050565b611a1f611a128361090b565b611a1a61160b565b6110de565b611a5e576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611a559061435e565b60405180910390fd5b611a68828261200f565b5050565b611a7682826110de565b15611b4a576000600b600084815260200190815260200160002060000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff021916908315150217905550611aef61160b565b73ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff16837ff6391f5c32d9c69d2a47ea670b442974b53935d1edc7fd64eb21e047a839171b60405160405180910390a45b5050565b611b57816121ea565b50565b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415611bca576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611bc1906144de565b60405180910390fd5b611bd38161159f565b15611c13576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611c0a906143be565b60405180910390fd5b611c1f600083836121da565b6001600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254611c6f91906147ea565b92505081905550816002600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff16600073ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60405160405180910390a45050565b611d318261159f565b611d70576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611d67906144be565b60405180910390fd5b80600a60008481526020019081526020016000209080519060200190611d97929190613012565b505050565b6000611dab836000018361223d565b60001c905092915050565b611dc18484846117aa565b611dcd848484846122d7565b611e0c576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611e039061439e565b60405180910390fd5b50505050565b6060611e1d8261159f565b611e5c576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611e53906144fe565b60405180910390fd5b6000600a60008481526020019081526020016000208054611e7c90614965565b80601f0160208091040260200160405190810160405280929190818152602001828054611ea890614965565b8015611ef55780601f10611eca57610100808354040283529160200191611ef5565b820191906000526020600020905b815481529060010190602001808311611ed857829003601f168201915b505050505090506000611f0661246e565b9050600081511415611f1c578192505050611f5f565b600082511115611f51578082604051602001611f39929190614239565b60405160208183030381529060405292505050611f5f565b611f5a84612485565b925050505b919050565b6000611f728260000161252c565b9050919050565b611f92611f858361090b565b611f8d61160b565b6110de565b611fd1576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611fc89061443e565b60405180910390fd5b611fdb8282611a6c565b5050565b6000612007836000018373ffffffffffffffffffffffffffffffffffffffff1660001b61253d565b905092915050565b61201982826110de565b6120ec576001600b600084815260200190815260200160002060000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff02191690831515021790555061209161160b565b73ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff16837f2f8788117e7eff1d82e926ec794901d17c78024a50270940304540a733656f0d60405160405180910390a45b5050565b60006120fc83836126c7565b61215557826000018290806001815401808255809150506001900390600052602060002001600090919091909150558260000180549050836001016000848152602001908152602001600020819055506001905061215a565b600090505b92915050565b60007f7965db0b000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff191614806121d357506121d2826126ea565b5b9050919050565b6121e5838383612764565b505050565b6121f381612878565b6000600a6000838152602001908152602001600020805461221390614965565b90501461223a57600a600082815260200190815260200160002060006122399190613098565b5b50565b600081836000018054905011612288576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161227f9061433e565b60405180910390fd5b8260000182815481106122c4577f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b9060005260206000200154905092915050565b60006122f88473ffffffffffffffffffffffffffffffffffffffff16612989565b15612461578373ffffffffffffffffffffffffffffffffffffffff1663150b7a0261232161160b565b8786866040518563ffffffff1660e01b81526004016123439493929190614278565b602060405180830381600087803b15801561235d57600080fd5b505af192505050801561238e57506040513d601f19601f8201168201806040525081019061238b9190613765565b60015b612411573d80600081146123be576040519150601f19603f3d011682016040523d82523d6000602084013e6123c3565b606091505b50600081511415612409576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016124009061439e565b60405180910390fd5b805181602001fd5b63150b7a0260e01b7bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916817bffffffffffffffffffffffffffffffffffffffffffffffffffffffff191614915050612466565b600190505b949350505050565b606060405180602001604052806000815250905090565b60606124908261159f565b6124cf576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016124c69061455e565b60405180910390fd5b60006124d961246e565b905060008151116124f95760405180602001604052806000815250612524565b806125038461299c565b604051602001612514929190614239565b6040516020818303038152906040525b915050919050565b600081600001805490509050919050565b600080836001016000848152602001908152602001600020549050600081146126bb57600060018261256f9190614871565b90506000600186600001805490506125879190614871565b905060008660000182815481106125c7577f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b9060005260206000200154905080876000018481548110612611577f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b906000526020600020018190555060018361262c91906147ea565b876001016000838152602001908152602001600020819055508660000180548061267f577f4e487b7100000000000000000000000000000000000000000000000000000000600052603160045260246000fd5b600190038181906000526020600020016000905590558660010160008781526020019081526020016000206000905560019450505050506126c1565b60009150505b92915050565b600080836001016000848152602001908152602001600020541415905092915050565b60007f780e9d63000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916148061275d575061275c82612b49565b5b9050919050565b61276f838383612c2b565b600073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff1614156127b2576127ad81612c30565b6127f1565b8173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff16146127f0576127ef8382612c79565b5b5b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff1614156128345761282f81612de6565b612873565b8273ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff1614612872576128718282612f29565b5b5b505050565b600061288382610e02565b9050612891816000846121da565b61289c600083611613565b6001600360008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282546128ec9190614871565b925050819055506002600083815260200190815260200160002060006101000a81549073ffffffffffffffffffffffffffffffffffffffff021916905581600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60405160405180910390a45050565b600080823b905060008111915050919050565b606060008214156129e4576040518060400160405280600181526020017f30000000000000000000000000000000000000000000000000000000000000008152509050612b44565b600082905060005b60008214612a165780806129ff90614997565b915050600a82612a0f9190614840565b91506129ec565b60008167ffffffffffffffff811115612a58577f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b6040519080825280601f01601f191660200182016040528015612a8a5781602001600182028036833780820191505090505b5090505b60008514612b3d57600182612aa39190614871565b9150600a85612ab291906149e0565b6030612abe91906147ea565b60f81b818381518110612afa577f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916908160001a905350600a85612b369190614840565b9450612a8e565b8093505050505b919050565b60007f80ac58cd000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff19161480612c1457507f5b5e139f000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916145b80612c245750612c2382612fa8565b5b9050919050565b505050565b6008805490506009600083815260200190815260200160002081905550600881908060018154018082558091505060019003906000526020600020016000909190919091505550565b60006001612c8684610eb4565b612c909190614871565b9050600060076000848152602001908152602001600020549050818114612d75576000600660008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600084815260200190815260200160002054905080600660008773ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600084815260200190815260200160002081905550816007600083815260200190815260200160002081905550505b6007600084815260200190815260200160002060009055600660008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008381526020019081526020016000206000905550505050565b60006001600880549050612dfa9190614871565b9050600060096000848152602001908152602001600020549050600060088381548110612e50577f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b906000526020600020015490508060088381548110612e98577f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b906000526020600020018190555081600960008381526020019081526020016000208190555060096000858152602001908152602001600020600090556008805480612f0d577f4e487b7100000000000000000000000000000000000000000000000000000000600052603160045260246000fd5b6001900381819060005260206000200160009055905550505050565b6000612f3483610eb4565b905081600660008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600083815260200190815260200160002081905550806007600084815260200190815260200160002081905550505050565b60007f01ffc9a7000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916149050919050565b82805461301e90614965565b90600052602060002090601f0160209004810192826130405760008555613087565b82601f1061305957805160ff1916838001178555613087565b82800160010185558215613087579182015b8281111561308657825182559160200191906001019061306b565b5b50905061309491906130d8565b5090565b5080546130a490614965565b6000825580601f106130b657506130d5565b601f0160209004906000526020600020908101906130d491906130d8565b5b50565b5b808211156130f15760008160009055506001016130d9565b5090565b60006131086131038461468a565b614659565b9050808382526020820190508285602086028201111561312757600080fd5b60005b85811015613157578161313d88826132a6565b84526020840193506020830192505060018101905061312a565b5050509392505050565b600061317461316f846146b6565b614659565b9050808382526020820190508260005b858110156131b4578135850161319a88826133b7565b845260208401935060208301925050600181019050613184565b5050509392505050565b60006131d16131cc846146e2565b614659565b905080838252602082019050828560208602820111156131f057600080fd5b60005b85811015613220578161320688826133e1565b8452602084019350602083019250506001810190506131f3565b5050509392505050565b600061323d6132388461470e565b614659565b90508281526020810184848401111561325557600080fd5b613260848285614923565b509392505050565b600061327b6132768461473e565b614659565b90508281526020810184848401111561329357600080fd5b61329e848285614923565b509392505050565b6000813590506132b581614ade565b92915050565b600082601f8301126132cc57600080fd5b81356132dc8482602086016130f5565b91505092915050565b600082601f8301126132f657600080fd5b8135613306848260208601613161565b91505092915050565b600082601f83011261332057600080fd5b81356133308482602086016131be565b91505092915050565b60008135905061334881614af5565b92915050565b60008135905061335d81614b0c565b92915050565b60008135905061337281614b23565b92915050565b60008151905061338781614b23565b92915050565b600082601f83011261339e57600080fd5b81356133ae84826020860161322a565b91505092915050565b600082601f8301126133c857600080fd5b81356133d8848260208601613268565b91505092915050565b6000813590506133f081614b3a565b92915050565b60006020828403121561340857600080fd5b6000613416848285016132a6565b91505092915050565b6000806040838503121561343257600080fd5b6000613440858286016132a6565b9250506020613451858286016132a6565b9150509250929050565b60008060006060848603121561347057600080fd5b600061347e868287016132a6565b935050602061348f868287016132a6565b92505060406134a0868287016133e1565b9150509250925092565b600080600080608085870312156134c057600080fd5b60006134ce878288016132a6565b94505060206134df878288016132a6565b93505060406134f0878288016133e1565b925050606085013567ffffffffffffffff81111561350d57600080fd5b6135198782880161338d565b91505092959194509250565b6000806040838503121561353857600080fd5b6000613546858286016132a6565b925050602061355785828601613339565b9150509250929050565b6000806040838503121561357457600080fd5b6000613582858286016132a6565b9250506020613593858286016133e1565b9150509250929050565b6000806000606084860312156135b257600080fd5b60006135c0868287016132a6565b93505060206135d1868287016133e1565b925050604084013567ffffffffffffffff8111156135ee57600080fd5b6135fa868287016133b7565b9150509250925092565b60008060006060848603121561361957600080fd5b600084013567ffffffffffffffff81111561363357600080fd5b61363f868287016132bb565b935050602084013567ffffffffffffffff81111561365c57600080fd5b6136688682870161330f565b925050604084013567ffffffffffffffff81111561368557600080fd5b613691868287016132e5565b9150509250925092565b6000602082840312156136ad57600080fd5b60006136bb8482850161334e565b91505092915050565b600080604083850312156136d757600080fd5b60006136e58582860161334e565b92505060206136f6858286016132a6565b9150509250929050565b6000806040838503121561371357600080fd5b60006137218582860161334e565b9250506020613732858286016133e1565b9150509250929050565b60006020828403121561374e57600080fd5b600061375c84828501613363565b91505092915050565b60006020828403121561377757600080fd5b600061378584828501613378565b91505092915050565b6000602082840312156137a057600080fd5b60006137ae848285016133e1565b91505092915050565b60006137c3838361421b565b60208301905092915050565b6137d8816148a5565b82525050565b60006137e98261477e565b6137f381856147ac565b93506137fe8361476e565b8060005b8381101561382f57815161381688826137b7565b97506138218361479f565b925050600181019050613802565b5085935050505092915050565b613845816148b7565b82525050565b613854816148c3565b82525050565b600061386582614789565b61386f81856147bd565b935061387f818560208601614932565b61388881614acd565b840191505092915050565b600061389e82614794565b6138a881856147ce565b93506138b8818560208601614932565b6138c181614acd565b840191505092915050565b60006138d782614794565b6138e181856147df565b93506138f1818560208601614932565b80840191505092915050565b600061390a6022836147ce565b91507f456e756d657261626c655365743a20696e646578206f7574206f6620626f756e60008301527f64730000000000000000000000000000000000000000000000000000000000006020830152604082019050919050565b6000613970602f836147ce565b91507f416363657373436f6e74726f6c3a2073656e646572206d75737420626520616e60008301527f2061646d696e20746f206772616e7400000000000000000000000000000000006020830152604082019050919050565b60006139d6602b836147ce565b91507f455243373231456e756d657261626c653a206f776e657220696e646578206f7560008301527f74206f6620626f756e64730000000000000000000000000000000000000000006020830152604082019050919050565b6000613a3c6032836147ce565b91507f4552433732313a207472616e7366657220746f206e6f6e20455243373231526560008301527f63656976657220696d706c656d656e74657200000000000000000000000000006020830152604082019050919050565b6000613aa2601c836147ce565b91507f4552433732313a20746f6b656e20616c7265616479206d696e746564000000006000830152602082019050919050565b6000613ae26024836147ce565b91507f4552433732313a207472616e7366657220746f20746865207a65726f2061646460008301527f72657373000000000000000000000000000000000000000000000000000000006020830152604082019050919050565b6000613b486019836147ce565b91507f4552433732313a20617070726f766520746f2063616c6c6572000000000000006000830152602082019050919050565b6000613b88602c836147ce565b91507f4552433732313a206f70657261746f7220717565727920666f72206e6f6e657860008301527f697374656e7420746f6b656e00000000000000000000000000000000000000006020830152604082019050919050565b6000613bee6030836147ce565b91507f416363657373436f6e74726f6c3a2073656e646572206d75737420626520616e60008301527f2061646d696e20746f207265766f6b65000000000000000000000000000000006020830152604082019050919050565b6000613c546038836147ce565b91507f4552433732313a20617070726f76652063616c6c6572206973206e6f74206f7760008301527f6e6572206e6f7220617070726f76656420666f7220616c6c00000000000000006020830152604082019050919050565b6000613cba602a836147ce565b91507f4552433732313a2062616c616e636520717565727920666f7220746865207a6560008301527f726f2061646472657373000000000000000000000000000000000000000000006020830152604082019050919050565b6000613d206029836147ce565b91507f4552433732313a206f776e657220717565727920666f72206e6f6e657869737460008301527f656e7420746f6b656e00000000000000000000000000000000000000000000006020830152604082019050919050565b6000613d86602e836147ce565b91507f45524337323155524953746f726167653a2055524920736574206f66206e6f6e60008301527f6578697374656e7420746f6b656e0000000000000000000000000000000000006020830152604082019050919050565b6000613dec6020836147ce565b91507f4552433732313a206d696e7420746f20746865207a65726f20616464726573736000830152602082019050919050565b6000613e2c6031836147ce565b91507f45524337323155524953746f726167653a2055524920717565727920666f722060008301527f6e6f6e6578697374656e7420746f6b656e0000000000000000000000000000006020830152604082019050919050565b6000613e92602c836147ce565b91507f4552433732313a20617070726f76656420717565727920666f72206e6f6e657860008301527f697374656e7420746f6b656e00000000000000000000000000000000000000006020830152604082019050919050565b6000613ef86029836147ce565b91507f4552433732313a207472616e73666572206f6620746f6b656e2074686174206960008301527f73206e6f74206f776e00000000000000000000000000000000000000000000006020830152604082019050919050565b6000613f5e602f836147ce565b91507f4552433732314d657461646174613a2055524920717565727920666f72206e6f60008301527f6e6578697374656e7420746f6b656e00000000000000000000000000000000006020830152604082019050919050565b6000613fc46021836147ce565b91507f4552433732313a20617070726f76616c20746f2063757272656e74206f776e6560008301527f72000000000000000000000000000000000000000000000000000000000000006020830152604082019050919050565b600061402a6031836147ce565b91507f4552433732313a207472616e736665722063616c6c6572206973206e6f74206f60008301527f776e6572206e6f7220617070726f7665640000000000000000000000000000006020830152604082019050919050565b6000614090602c836147ce565b91507f455243373231456e756d657261626c653a20676c6f62616c20696e646578206f60008301527f7574206f6620626f756e647300000000000000000000000000000000000000006020830152604082019050919050565b60006140f6603d836147ce565b91507f4552433732315072657365744d696e7465725061757365724175746f49643a2060008301527f6d7573742068617665206d696e74657220726f6c6520746f206d696e740000006020830152604082019050919050565b600061415c6030836147ce565b91507f4552433732314275726e61626c653a2063616c6c6572206973206e6f74206f7760008301527f6e6572206e6f7220617070726f766564000000000000000000000000000000006020830152604082019050919050565b60006141c2602f836147ce565b91507f416363657373436f6e74726f6c3a2063616e206f6e6c792072656e6f756e636560008301527f20726f6c657320666f722073656c6600000000000000000000000000000000006020830152604082019050919050565b61422481614919565b82525050565b61423381614919565b82525050565b600061424582856138cc565b915061425182846138cc565b91508190509392505050565b600060208201905061427260008301846137cf565b92915050565b600060808201905061428d60008301876137cf565b61429a60208301866137cf565b6142a7604083018561422a565b81810360608301526142b9818461385a565b905095945050505050565b600060208201905081810360008301526142de81846137de565b905092915050565b60006020820190506142fb600083018461383c565b92915050565b6000602082019050614316600083018461384b565b92915050565b600060208201905081810360008301526143368184613893565b905092915050565b60006020820190508181036000830152614357816138fd565b9050919050565b6000602082019050818103600083015261437781613963565b9050919050565b60006020820190508181036000830152614397816139c9565b9050919050565b600060208201905081810360008301526143b781613a2f565b9050919050565b600060208201905081810360008301526143d781613a95565b9050919050565b600060208201905081810360008301526143f781613ad5565b9050919050565b6000602082019050818103600083015261441781613b3b565b9050919050565b6000602082019050818103600083015261443781613b7b565b9050919050565b6000602082019050818103600083015261445781613be1565b9050919050565b6000602082019050818103600083015261447781613c47565b9050919050565b6000602082019050818103600083015261449781613cad565b9050919050565b600060208201905081810360008301526144b781613d13565b9050919050565b600060208201905081810360008301526144d781613d79565b9050919050565b600060208201905081810360008301526144f781613ddf565b9050919050565b6000602082019050818103600083015261451781613e1f565b9050919050565b6000602082019050818103600083015261453781613e85565b9050919050565b6000602082019050818103600083015261455781613eeb565b9050919050565b6000602082019050818103600083015261457781613f51565b9050919050565b6000602082019050818103600083015261459781613fb7565b9050919050565b600060208201905081810360008301526145b78161401d565b9050919050565b600060208201905081810360008301526145d781614083565b9050919050565b600060208201905081810360008301526145f7816140e9565b9050919050565b600060208201905081810360008301526146178161414f565b9050919050565b60006020820190508181036000830152614637816141b5565b9050919050565b6000602082019050614653600083018461422a565b92915050565b6000604051905081810181811067ffffffffffffffff821117156146805761467f614a9e565b5b8060405250919050565b600067ffffffffffffffff8211156146a5576146a4614a9e565b5b602082029050602081019050919050565b600067ffffffffffffffff8211156146d1576146d0614a9e565b5b602082029050602081019050919050565b600067ffffffffffffffff8211156146fd576146fc614a9e565b5b602082029050602081019050919050565b600067ffffffffffffffff82111561472957614728614a9e565b5b601f19601f8301169050602081019050919050565b600067ffffffffffffffff82111561475957614758614a9e565b5b601f19601f8301169050602081019050919050565b6000819050602082019050919050565b600081519050919050565b600081519050919050565b600081519050919050565b6000602082019050919050565b600082825260208201905092915050565b600082825260208201905092915050565b600082825260208201905092915050565b600081905092915050565b60006147f582614919565b915061480083614919565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0382111561483557614834614a11565b5b828201905092915050565b600061484b82614919565b915061485683614919565b92508261486657614865614a40565b5b828204905092915050565b600061487c82614919565b915061488783614919565b92508282101561489a57614899614a11565b5b828203905092915050565b60006148b0826148f9565b9050919050565b60008115159050919050565b6000819050919050565b60007fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b82818337600083830152505050565b60005b83811015614950578082015181840152602081019050614935565b8381111561495f576000848401525b50505050565b6000600282049050600182168061497d57607f821691505b6020821081141561499157614990614a6f565b5b50919050565b60006149a282614919565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8214156149d5576149d4614a11565b5b600182019050919050565b60006149eb82614919565b91506149f683614919565b925082614a0657614a05614a40565b5b828206905092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b6000601f19601f8301169050919050565b614ae7816148a5565b8114614af257600080fd5b50565b614afe816148b7565b8114614b0957600080fd5b50565b614b15816148c3565b8114614b2057600080fd5b50565b614b2c816148cd565b8114614b3757600080fd5b50565b614b4381614919565b8114614b4e57600080fd5b5056fea26469706673582212201b45701b4b4e7d4c9617883606f68222fa116033ffcfefe7d3c9a23f48d56ac764736f6c63430008000033'
# address = web3.toChecksumAddress('0xB33F5f76C4cc11b5e4Be32C0363927d84BDf84D6')
# contract = web3.eth.contract(abi = abi,address = address)
# print(contract)

# tx = contract.constructor('Color','CLR').transact({'from':'0xaE0835EC16922Bd9993EEF5cDa04606D53075c9c'})
# print(tx)
# print(contract.functions.name().call())

# address = '0xd7b1dA90D56A59c39CaCbdf3F7396dA8C0e35225'
# contract = web3.eth.contract(abi=abi, bytecode=bytecode)
# tx = contract.constructor('Color','COLOR').transact({'from':'0xaE0835EC16922Bd9993EEF5cDa04606D53075c9c'})
# print(contract.functions.mintWithTokenURI('0xaE0835EC16922Bd9993EEF5cDa04606D53075c9c','1','http://my_token_data.com/1').transact({'from':'0xaE0835EC16922Bd9993EEF5cDa04606D53075c9c'}))
# print(contract.functions.tokenURI.call())
# print(contract)


# tatum erc20
# abi = json.loads('[{"constant": true,"inputs": [],"name": "name","outputs": [{"name": "","type": "string"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": false,"inputs": [{"name": "spender","type": "address"},{"name": "value","type": "uint256"}],"name": "approve","outputs": [{"name": "","type": "bool"}],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": true,"inputs": [],"name": "totalSupply","outputs": [{"name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": false,"inputs": [{"name": "from","type": "address"},{"name": "to","type": "address"},{"name": "value","type": "uint256"}],"name": "transferFrom","outputs": [{"name": "","type": "bool"}],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": true,"inputs": [],"name": "decimals","outputs": [{"name": "","type": "uint8"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "cap","outputs": [{"name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": false,"inputs": [{"name": "spender","type": "address"},{"name": "addedValue","type": "uint256"}],"name": "increaseAllowance","outputs": [{"name": "","type": "bool"}],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": false,"inputs": [{"name": "to","type": "address"},{"name": "value","type": "uint256"}],"name": "mint","outputs": [{"name": "","type": "bool"}],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": false,"inputs": [{"name": "value","type": "uint256"}],"name": "burn","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": true,"inputs": [{"name": "owner","type": "address"}],"name": "balanceOf","outputs": [{"name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": false,"inputs": [{"name": "from","type": "address"},{"name": "value","type": "uint256"}],"name": "burnFrom","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": true,"inputs": [],"name": "symbol","outputs": [{"name": "","type": "string"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": false,"inputs": [{"name": "account","type": "address"}],"name": "addMinter","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": false,"inputs": [],"name": "renounceMinter","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": false,"inputs": [{"name": "spender","type": "address"},{"name": "subtractedValue","type": "uint256"}],"name": "decreaseAllowance","outputs": [{"name": "","type": "bool"}],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": false,"inputs": [{"name": "to","type": "address"},{"name": "value","type": "uint256"}],"name": "transfer","outputs": [{"name": "","type": "bool"}],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": true,"inputs": [{"name": "account","type": "address"}],"name": "isMinter","outputs": [{"name": "","type": "bool"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "builtOn","outputs": [{"name": "","type": "string"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [{"name": "owner","type": "address"},{"name": "spender","type": "address"}],"name": "allowance","outputs": [{"name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"inputs": [{"name": "name","type": "string"},{"name": "symbol","type": "string"},{"name": "receiver","type": "address"},{"name": "decimals","type": "uint8"},{"name": "cap","type": "uint256"},{"name": "initialBalance","type": "uint256"}],"payable": false,"stateMutability": "nonpayable","type": "constructor"},{"anonymous": false,"inputs": [{"indexed": true,"name": "account","type": "address"}],"name": "MinterAdded","type": "event"},{"anonymous": false,"inputs": [{"indexed": true,"name": "account","type": "address"}],"name": "MinterRemoved","type": "event"},{"anonymous": false,"inputs": [{"indexed": true,"name": "from","type": "address"},{"indexed": true,"name": "to","type": "address"},{"indexed": false,"name": "value","type": "uint256"}],"name": "Transfer","type": "event"},{"anonymous": false,"inputs": [{"indexed": true,"name": "owner","type": "address"},{"indexed": true,"name": "spender","type": "address"},{"indexed": false,"name": "value","type": "uint256"}],"name": "Approval","type": "event"}]')
# bytecode = '0x60806040526040805190810160405280601081526020017f68747470733a2f2f746174756d2e696f000000000000000000000000000000008152506008908051906020019062000051929190620005e5565b503480156200005f57600080fd5b5060405162001db138038062001db1833981018060405260c08110156200008557600080fd5b8101908080516401000000008111156200009e57600080fd5b82810190506020810184811115620000b557600080fd5b8151856001820283011164010000000082111715620000d357600080fd5b50509291906020018051640100000000811115620000f057600080fd5b828101905060208101848111156200010757600080fd5b81518560018202830111640100000000821117156200012557600080fd5b50509291906020018051906020019092919080519060200190929190805190602001909291908051906020019092919050505081868685826000908051906020019062000174929190620005e5565b5081600190805190602001906200018d929190620005e5565b5080600260006101000a81548160ff021916908360ff160217905550505050620001c63362000210640100000000026401000000009004565b600081111515620001d657600080fd5b8060078190555050600081111562000204576200020384826200027a640100000000026401000000009004565b5b50505050505062000694565b62000234816006620002ea6401000000000262001582179091906401000000009004565b8073ffffffffffffffffffffffffffffffffffffffff167f6ae172837ea30b801fbfcdd4108aa1d5bf8ff775444fd70256b44e6bf3dfc3f660405160405180910390a250565b600754620002b8826200029b620003ad640100000000026401000000009004565b620003b7640100000000026200108e179091906401000000009004565b11151515620002c657600080fd5b620002e68282620003d9640100000000026200142c176401000000009004565b5050565b600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff16141515156200032757600080fd5b62000342828262000550640100000000026401000000009004565b1515156200034f57600080fd5b60018260000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055505050565b6000600554905090565b6000808284019050838110151515620003cf57600080fd5b8091505092915050565b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff16141515156200041657600080fd5b6200043b81600554620003b7640100000000026200108e179091906401000000009004565b600581905550620004a381600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054620003b7640100000000026200108e179091906401000000009004565b600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508173ffffffffffffffffffffffffffffffffffffffff16600073ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef836040518082815260200191505060405180910390a35050565b60008073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff16141515156200058e57600080fd5b8260000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905092915050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106200062857805160ff191683800117855562000659565b8280016001018555821562000659579182015b82811115620006585782518255916020019190600101906200063b565b5b5090506200066891906200066c565b5090565b6200069191905b808211156200068d57600081600090555060010162000673565b5090565b90565b61170d80620006a46000396000f3fe608060405234801561001057600080fd5b506004361061013e576000357c01000000000000000000000000000000000000000000000000000000009004806370a08231116100ca578063a457c2d71161008e578063a457c2d714610583578063a9059cbb146105e9578063aa271e1a1461064f578063b60b7084146106ab578063dd62ed3e1461072e5761013e565b806370a082311461040c57806379cc67901461046457806395d89b41146104b2578063983b2d561461053557806398650275146105795761013e565b8063313ce56711610111578063313ce567146102d0578063355274ea146102f4578063395093511461031257806340c10f191461037857806342966c68146103de5761013e565b806306fdde0314610143578063095ea7b3146101c657806318160ddd1461022c57806323b872dd1461024a575b600080fd5b61014b6107a6565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561018b578082015181840152602081019050610170565b50505050905090810190601f1680156101b85780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b610212600480360360408110156101dc57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050610848565b604051808215151515815260200191505060405180910390f35b61023461085f565b6040518082815260200191505060405180910390f35b6102b66004803603606081101561026057600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050610869565b604051808215151515815260200191505060405180910390f35b6102d861091a565b604051808260ff1660ff16815260200191505060405180910390f35b6102fc610931565b6040518082815260200191505060405180910390f35b61035e6004803603604081101561032857600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291908035906020019092919050505061093b565b604051808215151515815260200191505060405180910390f35b6103c46004803603604081101561038e57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803590602001909291905050506109e0565b604051808215151515815260200191505060405180910390f35b61040a600480360360208110156103f457600080fd5b8101908080359060200190929190505050610a0a565b005b61044e6004803603602081101561042257600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610a17565b6040518082815260200191505060405180910390f35b6104b06004803603604081101561047a57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050610a60565b005b6104ba610a6e565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156104fa5780820151818401526020810190506104df565b50505050905090810190601f1680156105275780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b6105776004803603602081101561054b57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610b10565b005b610581610b30565b005b6105cf6004803603604081101561059957600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050610b3b565b604051808215151515815260200191505060405180910390f35b610635600480360360408110156105ff57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050610be0565b604051808215151515815260200191505060405180910390f35b6106916004803603602081101561066557600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610bf7565b604051808215151515815260200191505060405180910390f35b6106b3610c14565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156106f35780820151818401526020810190506106d8565b50505050905090810190601f1680156107205780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b6107906004803603604081101561074457600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610cb2565b6040518082815260200191505060405180910390f35b606060008054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561083e5780601f106108135761010080835404028352916020019161083e565b820191906000526020600020905b81548152906001019060200180831161082157829003601f168201915b5050505050905090565b6000610855338484610d39565b6001905092915050565b6000600554905090565b6000610876848484610e9c565b61090f843361090a85600460008a73ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461106c90919063ffffffff16565b610d39565b600190509392505050565b6000600260009054906101000a900460ff16905090565b6000600754905090565b60006109d633846109d185600460003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008973ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461108e90919063ffffffff16565b610d39565b6001905092915050565b60006109eb33610bf7565b15156109f657600080fd5b610a0083836110af565b6001905092915050565b610a1433826110e7565b50565b6000600360008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b610a6a828261123d565b5050565b606060018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610b065780601f10610adb57610100808354040283529160200191610b06565b820191906000526020600020905b815481529060010190602001808311610ae957829003601f168201915b5050505050905090565b610b1933610bf7565b1515610b2457600080fd5b610b2d816112e4565b50565b610b393361133e565b565b6000610bd63384610bd185600460003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008973ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461106c90919063ffffffff16565b610d39565b6001905092915050565b6000610bed338484610e9c565b6001905092915050565b6000610c0d82600661139890919063ffffffff16565b9050919050565b60088054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610caa5780601f10610c7f57610100808354040283529160200191610caa565b820191906000526020600020905b815481529060010190602001808311610c8d57829003601f168201915b505050505081565b6000600460008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054905092915050565b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff1614151515610d7557600080fd5b600073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff1614151515610db157600080fd5b80600460008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925836040518082815260200191505060405180910390a3505050565b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff1614151515610ed857600080fd5b610f2a81600360008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461106c90919063ffffffff16565b600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550610fbf81600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461108e90919063ffffffff16565b600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef836040518082815260200191505060405180910390a3505050565b600082821115151561107d57600080fd5b600082840390508091505092915050565b60008082840190508381101515156110a557600080fd5b8091505092915050565b6007546110cc826110be61085f565b61108e90919063ffffffff16565b111515156110d957600080fd5b6110e3828261142c565b5050565b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415151561112357600080fd5b6111388160055461106c90919063ffffffff16565b60058190555061119081600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461106c90919063ffffffff16565b600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef836040518082815260200191505060405180910390a35050565b61124782826110e7565b6112e082336112db84600460008873ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461106c90919063ffffffff16565b610d39565b5050565b6112f881600661158290919063ffffffff16565b8073ffffffffffffffffffffffffffffffffffffffff167f6ae172837ea30b801fbfcdd4108aa1d5bf8ff775444fd70256b44e6bf3dfc3f660405160405180910390a250565b61135281600661163290919063ffffffff16565b8073ffffffffffffffffffffffffffffffffffffffff167fe94479a9f7e1952cc78f2d6baab678adc1b772d936c6583def489e524cb6669260405160405180910390a250565b60008073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff16141515156113d557600080fd5b8260000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905092915050565b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415151561146857600080fd5b61147d8160055461108e90919063ffffffff16565b6005819055506114d581600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461108e90919063ffffffff16565b600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508173ffffffffffffffffffffffffffffffffffffffff16600073ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef836040518082815260200191505060405180910390a35050565b600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff16141515156115be57600080fd5b6115c88282611398565b1515156115d457600080fd5b60018260000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055505050565b600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff161415151561166e57600080fd5b6116788282611398565b151561168357600080fd5b60008260000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff021916908315150217905550505056fea165627a7a72305820bd0d80acdad0a158a00477c7002345806238849601fbc1885354626cddf54c990029'
# contract = web3.eth.contract(abi = abi,bytecode = bytecode)
# print(contract.constructor('Narsi','NSI','0xaE0835EC16922Bd9993EEF5cDa04606D53075c9c',2,100000,1000000000))





            
