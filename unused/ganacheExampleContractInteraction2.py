import json
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

##print(web3.isConnected())

##print(web3.eth.blockNumber)

## address = web3.toChecksumAddress("0x893fc12dd13eaddf6913e3af71a143a5f28e9791")
## abi and bytecode is a very long line it's there the idle ide just doesn't like it.
abi = json.loads('[ { "constant": false, "inputs": [ { "name": "id", "type": "uint256" }, { "name": "data", "type": "uint256" } ], "name": "addDataToSensorById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "max", "type": "uint256" }, { "name": "min", "type": "uint256" }, { "name": "description", "type": "string" } ], "name": "addSensor", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "max", "type": "uint256" }, { "name": "min", "type": "uint256" } ], "name": "addSensor", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [], "name": "addSensor", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "uint256" } ], "name": "deleteAllSensorDataById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "uint256" } ], "name": "getAbnormalBehaviorCountById", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "uint256" }, { "name": "description", "type": "string" } ], "name": "updateDescriptionById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "uint256" }, { "name": "max", "type": "uint256" } ], "name": "updateMaxById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "uint256" }, { "name": "min", "type": "uint256" } ], "name": "updateMinById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "constant": true, "inputs": [ { "name": "id", "type": "uint256" } ], "name": "getDescriptionByID", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "uint256" } ], "name": "getMaxById", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "uint256" } ], "name": "getMinByIdfunction", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "uint256" } ], "name": "getSensorDataById", "outputs": [ { "name": "", "type": "uint256[]" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "sensorCount", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "uint256" } ], "name": "sensors", "outputs": [ { "name": "id", "type": "uint256" }, { "name": "max", "type": "uint256" }, { "name": "min", "type": "uint256" }, { "name": "description", "type": "string" }, { "name": "abnormalBehaviors", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" } ]')
bytecode = "608060405234801561001057600080fd5b50610062606f60206040805190810160405280601381526020017f4572696373736f6e20697320417765736f6d6500000000000000000000000000815250610068640100000000026401000000009004565b506101cb565b600080600081548092919060010191905055506000546001600080548152602001908152602001600020600001819055506000546001600080548152602001908152602001600020600001819055508360016000805481526020019081526020016000206001018190555082600160008054815260200190815260200160002060020181905550816001600080548152602001908152602001600020600301908051906020019061011a929190610126565b50600190509392505050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061016757805160ff1916838001178555610195565b82800160010185558215610195579182015b82811115610194578251825591602001919060010190610179565b5b5090506101a291906101a6565b5090565b6101c891905b808211156101c45760008160009055506001016101ac565b5090565b90565b610d73806101da6000396000f3fe6080604052600436106100d5576000357c01000000000000000000000000000000000000000000000000000000009004806312a7ab9a146100da5780631b30752e146101ce5780631be141e014610282578063272cab21146102c7578063293dee981461031a57806332e081b8146103315780633b8210fd14610380578063412f2e82146103cf5780634d33dfe51461049f578063642cd7871461058957806375456c82146105b4578063a718751614610611578063c08646ac14610660578063e74dcdf1146106bd578063f547e7b21461071a575b600080fd5b3480156100e657600080fd5b506101b4600480360360608110156100fd57600080fd5b8101908080359060200190929190803590602001909291908035906020019064010000000081111561012e57600080fd5b82018360208201111561014057600080fd5b8035906020019184600183028401116401000000008311171561016257600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f8201169050808301925050505050505091929192905050506107aa565b604051808215151515815260200191505060405180910390f35b3480156101da57600080fd5b50610207600480360360208110156101f157600080fd5b8101908080359060200190929190505050610868565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561024757808201518184015260208101905061022c565b50505050905090810190601f1680156102745780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b34801561028e57600080fd5b506102c5600480360360408110156102a557600080fd5b810190808035906020019092919080359060200190929190505050610920565b005b3480156102d357600080fd5b50610300600480360360208110156102ea57600080fd5b8101908080359060200190929190505050610965565b604051808215151515815260200191505060405180910390f35b34801561032657600080fd5b5061032f610992565b005b34801561033d57600080fd5b5061036a6004803603602081101561035457600080fd5b81019080803590602001909291905050506109a0565b6040518082815260200191505060405180910390f35b34801561038c57600080fd5b506103b9600480360360208110156103a357600080fd5b81019080803590602001909291905050506109c0565b6040518082815260200191505060405180910390f35b3480156103db57600080fd5b50610408600480360360208110156103f257600080fd5b81019080803590602001909291905050506109e0565b6040518086815260200185815260200184815260200180602001838152602001828103825284818151815260200191508051906020019080838360005b83811015610460578082015181840152602081019050610445565b50505050905090810190601f16801561048d5780820380516001836020036101000a031916815260200191505b50965050505050505060405180910390f35b3480156104ab57600080fd5b5061056f600480360360408110156104c257600080fd5b8101908080359060200190929190803590602001906401000000008111156104e957600080fd5b8201836020820111156104fb57600080fd5b8035906020019184600183028401116401000000008311171561051d57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290505050610aae565b604051808215151515815260200191505060405180910390f35b34801561059557600080fd5b5061059e610ae5565b6040518082815260200191505060405180910390f35b3480156105c057600080fd5b506105f7600480360360408110156105d757600080fd5b810190808035906020019092919080359060200190929190505050610aeb565b604051808215151515815260200191505060405180910390f35b34801561061d57600080fd5b5061064a6004803603602081101561063457600080fd5b8101908080359060200190929190505050610b12565b6040518082815260200191505060405180910390f35b34801561066c57600080fd5b506106a36004803603604081101561068357600080fd5b810190808035906020019092919080359060200190929190505050610b32565b604051808215151515815260200191505060405180910390f35b3480156106c957600080fd5b50610700600480360360408110156106e057600080fd5b810190808035906020019092919080359060200190929190505050610bec565b604051808215151515815260200191505060405180910390f35b34801561072657600080fd5b506107536004803603602081101561073d57600080fd5b8101908080359060200190929190505050610c13565b6040518080602001828103825283818151815260200191508051906020019060200280838360005b8381101561079657808201518184015260208101905061077b565b505050509050019250505060405180910390f35b600080600081548092919060010191905055506000546001600080548152602001908152602001600020600001819055506000546001600080548152602001908152602001600020600001819055508360016000805481526020019081526020016000206001018190555082600160008054815260200190815260200160002060020181905550816001600080548152602001908152602001600020600301908051906020019061085c929190610c81565b50600190509392505050565b6060600160008381526020019081526020016000206003018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156109145780601f106108e957610100808354040283529160200191610914565b820191906000526020600020905b8154815290600101906020018083116108f757829003601f168201915b50505050509050919050565b61096082826040805190810160405280600f81526020017f4e6f204465736372697074696f6e2e00000000000000000000000000000000008152506107aa565b505050565b60006001600083815260200190815260200160002060050160006109899190610d01565b60019050919050565b61099e60646000610920565b565b600060016000838152602001908152602001600020600101549050919050565b600060016000838152602001908152602001600020600201549050919050565b6001602052806000526040600020600091509050806000015490806001015490806002015490806003018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610a9e5780601f10610a7357610100808354040283529160200191610a9e565b820191906000526020600020905b815481529060010190602001808311610a8157829003601f168201915b5050505050908060040154905085565b600081600160008581526020019081526020016000206003019080519060200190610ada929190610c81565b506001905092915050565b60005481565b60008160016000858152602001908152602001600020600201819055506001905092915050565b600060016000838152602001908152602001600020600401549050919050565b600080600160008581526020019081526020016000209050806001015483101580610b61575080600201548311155b15610bb2578060040160008154809291906001019190505550806005018390806001815401808255809150509060018203906000526020600020016000909192909190915055506001915050610be6565b8060050183908060018154018082558091505090600182039060005260206000200160009091929091909150555060009150505b92915050565b60008160016000858152602001908152602001600020600101819055506001905092915050565b606060016000838152602001908152602001600020600501805480602002602001604051908101604052809291908181526020018280548015610c7557602002820191906000526020600020905b815481526020019060010190808311610c61575b50505050509050919050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f10610cc257805160ff1916838001178555610cf0565b82800160010185558215610cf0579182015b82811115610cef578251825591602001919060010190610cd4565b5b509050610cfd9190610d22565b5090565b5080546000825590600052602060002090810190610d1f9190610d22565b50565b610d4491905b80821115610d40576000816000905550600101610d28565b5090565b9056fea165627a7a72305820ef80f38bf623236ca123f51aad06a815751f324f158b61d907686f8366eb35540029"
## account_1 = "0x3A7Ec23F8b04832DC9222411352Dbe2Eb5D53245"
## account_2 = "0xeb1Fbbada83165E48528830BFd4c44AfEF1A522f"
web3.eth.defaultAccount = web3.eth.accounts[1]
#### In real applications don't hardcode your private key.
#### Take it in as a parameter.
## private_key_1 = "43b80999dbfe023d071ae19901399fba872221a9dcc9b46bd584166564d6f4d8"
SensorData = web3.eth.contract(abi=abi, bytecode=bytecode)


tx_hash = SensorData.constructor().transact()
##print(tx_hash)
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

contract = web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

print(contract.functions.getDescriptionByID(1).call())

tx_hash = contract.functions.updateDescriptionById(1, "new description").transact()

tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

print(contract.functions.getDescriptionByID(1).call())














## contract = web3.eth.contract(address=address, abi=abi)
## print(contract.functions.getDescriptionByID(1).call())

## tx_hash = contract.functions.updateDescriptionById(1, "test").transact()

## web3.eth.waitForTransactionReceipt(tx_hash)
##
##print('Updated Description: {}'.format(
##    contract.functions.getDescriptionByID(1).call()
##))





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