import json
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

##print(web3.isConnected())

##print(web3.eth.blockNumber)

address = web3.toChecksumAddress("0x893fc12dd13eaddf6913e3af71a143a5f28e9791")
## SensorData is a very long line it's there the idle ide just doesn't like it.
abi = json.loads('[ { "constant": false, "inputs": [ { "name": "id", "type": "uint256" }, { "name": "data", "type": "uint256" } ], "name": "addDataToSensorById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "max", "type": "uint256" }, { "name": "min", "type": "uint256" }, { "name": "description", "type": "string" } ], "name": "addSensor", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "max", "type": "uint256" }, { "name": "min", "type": "uint256" } ], "name": "addSensor", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [], "name": "addSensor", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "uint256" } ], "name": "deleteAllSensorDataById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "uint256" } ], "name": "getAbnormalBehaviorCountById", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "uint256" }, { "name": "description", "type": "string" } ], "name": "updateDescriptionById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "uint256" }, { "name": "max", "type": "uint256" } ], "name": "updateMaxById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "uint256" }, { "name": "min", "type": "uint256" } ], "name": "updateMinById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "constant": true, "inputs": [ { "name": "id", "type": "uint256" } ], "name": "getDescriptionByID", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "uint256" } ], "name": "getMaxById", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "uint256" } ], "name": "getMinByIdfunction", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "uint256" } ], "name": "getSensorDataById", "outputs": [ { "name": "", "type": "uint256[]" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "sensorCount", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "uint256" } ], "name": "sensors", "outputs": [ { "name": "id", "type": "uint256" }, { "name": "max", "type": "uint256" }, { "name": "min", "type": "uint256" }, { "name": "description", "type": "string" }, { "name": "abnormalBehaviors", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" } ]')
## account_1 = "0x3A7Ec23F8b04832DC9222411352Dbe2Eb5D53245"
## account_2 = "0xeb1Fbbada83165E48528830BFd4c44AfEF1A522f"
web3.eth.defaultAccount = web3.eth.accounts[0]
#### In real applications don't hardcode your private key.
#### Take it in as a parameter.
## private_key_1 = "43b80999dbfe023d071ae19901399fba872221a9dcc9b46bd584166564d6f4d8"


contract = web3.eth.contract(address=address, abi=abi)
print(contract.functions.getDescriptionByID(1).call())

tx_hash = contract.functions.updateDescriptionById(1, "test").transact()

web3.eth.waitForTransactionReceipt(tx_hash)
print('Updated Description: {}'.format(
    contract.functions.getDescriptionByID(1).call()
))





### get the nonce
##nonce = web3.eth.getTransactionCount(account_1)
### build a transaction
##tx = {
##    'nonce': nonce,
##    'to': account_2,
##    'value': web3.toWei(.1, 'ether'),
##    'gas': 2000000,
##    'gasPrice': web3.toWei('50', 'gwei')
##    }
### sign transaction
##signed_tx = web3.eth.account.signTransaction(tx, private_key_1)
### send transaction
##tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
### get transaction hash
##print(web3.toHex(tx_hash))
