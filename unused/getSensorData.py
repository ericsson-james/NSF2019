import time
from web3 import Web3, HTTPProvider
import json
import sys

infura_url = "https://ropsten.infura.io/v3/c2c9ec67e10646528586904b7df8f237"
w3 = Web3(Web3.HTTPProvider(infura_url))


## If the contract is ever reuploaded then this address will need to be changed.
contract_address = w3.toChecksumAddress("0x3d74538be9f3260e1f61c0601474fa504b54bd9d")
abi = json.loads('[ { "constant": false, "inputs": [ { "name": "id", "type": "int256" }, { "name": "description", "type": "string" } ], "name": "setDescriptionById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "int256" } ], "name": "sensors", "outputs": [ { "name": "id", "type": "int256" }, { "name": "max", "type": "int256" }, { "name": "min", "type": "int256" }, { "name": "description", "type": "string" }, { "name": "abnormalBehaviors", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "int256" }, { "name": "max", "type": "int256" } ], "name": "setMaxById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getSensorDataById", "outputs": [ { "name": "", "type": "int256[]" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [], "name": "addSensor", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "sensorCount", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "int256" } ], "name": "deleteAllSensorDataById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getMinByIdfunction", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "max", "type": "int256" }, { "name": "min", "type": "int256" }, { "name": "description", "type": "string" } ], "name": "addSensor", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "max", "type": "int256" }, { "name": "min", "type": "int256" } ], "name": "addSensor", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getDescriptionById", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "int256" }, { "name": "data", "type": "int256" } ], "name": "setDataToSensorById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getAbnormalBehaviorCountById", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getMaxById", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "int256" }, { "name": "min", "type": "int256" } ], "name": "setMinById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor" } ]')

##  The address and the abi are needed to act as a contract object
contract = w3.eth.contract(address = contract_address, abi = abi)

print(contract.functions.getSensorDataById(0).call())