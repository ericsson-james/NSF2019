import time
from web3 import Web3, HTTPProvider
import json
import sys
##import Adafruit_DHT

infura_url = "https://ropsten.infura.io/v3/c2c9ec67e10646528586904b7df8f237"
w3 = Web3(Web3.HTTPProvider(infura_url))



## If the contract is ever reuploaded then this address will need to be changed.
contract_address1 = w3.toChecksumAddress("0xf8e8fAD7AbB87eb3aCEAD25bC7Dad959bF243236")
abi1 = json.loads('[ { "constant": false, "inputs": [ { "name": "max", "type": "int256" }, { "name": "min", "type": "int256" }, { "name": "description", "type": "string" } ], "name": "addSensor", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "int256" }, { "name": "data", "type": "int256" } ], "name": "setDataToSensorById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getAbnormalBehaviorCountById", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getDescriptionById", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getSensorDataById", "outputs": [ { "name": "", "type": "int256[]" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "sensorCount", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "int256" } ], "name": "sensors", "outputs": [ { "name": "id", "type": "int256" }, { "name": "max", "type": "int256" }, { "name": "min", "type": "int256" }, { "name": "description", "type": "string" }, { "name": "abnormalBehaviors", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" } ]')

## This is the original contract with n = 20 that ended up excedding gas limits
# contract_address2 = w3.toChecksumAddress("0x426cbcd22194c3423fc282f7ba1c1b8a615025d1")
# abi2 = json.loads('[ { "constant": false, "inputs": [ { "name": "max", "type": "int256" }, { "name": "min", "type": "int256" }, { "name": "description", "type": "string" } ], "name": "addSensor", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "int256" }, { "name": "data", "type": "int256" } ], "name": "setDataToSensorById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getAbnormalBehaviorCountById", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getDescriptionById", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getSensorDataById", "outputs": [ { "name": "", "type": "int256[]" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "MaxArrayLength", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "sensorCount", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "int256" } ], "name": "sensors", "outputs": [ { "name": "id", "type": "int256" }, { "name": "max", "type": "int256" }, { "name": "min", "type": "int256" }, { "name": "description", "type": "string" }, { "name": "abnormalBehaviors", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" } ]')


##This is the same contract as 3 except for only having n = 2000
contract_address2 = w3.toChecksumAddress("0x43730bab1269d0eada35e1681f5ddc0c087dfc19")
abi2 = json.loads('[ { "constant": false, "inputs": [ { "name": "max", "type": "int256" }, { "name": "min", "type": "int256" }, { "name": "description", "type": "string" } ], "name": "addSensor", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "int256" }, { "name": "data", "type": "int256" } ], "name": "setDataToSensorById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getAbnormalBehaviorCountById", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getDescriptionById", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getSensorDataById", "outputs": [ { "name": "", "type": "int256[]" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getTotalAdditions", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "MaxArraySize", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "sensorCount", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "int256" } ], "name": "sensors", "outputs": [ { "name": "id", "type": "int256" }, { "name": "max", "type": "int256" }, { "name": "min", "type": "int256" }, { "name": "description", "type": "string" }, { "name": "abnormalBehaviors", "type": "int256" }, { "name": "totalAdditions", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" } ]')



## This Contract is the substition option n=2000 Values
contract_address3 = w3.toChecksumAddress("0x0f0f612205d2d2f51ba94d74ce7f2560635c49fc")
abi3 = json.loads('[ { "constant": false, "inputs": [ { "name": "max", "type": "int256" }, { "name": "min", "type": "int256" }, { "name": "description", "type": "string" } ], "name": "addSensor", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "int256" }, { "name": "data", "type": "int256" } ], "name": "setDataToSensorById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getAbnormalBehaviorCountById", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getDescriptionById", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getSensorDataById", "outputs": [ { "name": "", "type": "int256[]" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getTotalAdditions", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "MaxArraySize", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "sensorCount", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "int256" } ], "name": "sensors", "outputs": [ { "name": "id", "type": "int256" }, { "name": "max", "type": "int256" }, { "name": "min", "type": "int256" }, { "name": "description", "type": "string" }, { "name": "abnormalBehaviors", "type": "int256" }, { "name": "totalAdditions", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" } ]')


##  The address and the abi are needed to act as a contract object
contract1 = w3.eth.contract(address = contract_address1, abi = abi1)
contract2 = w3.eth.contract(address = contract_address2, abi = abi2)
contract3 = w3.eth.contract(address = contract_address3, abi = abi3)
## While it doesn't matter for the testnet being used for the love of all that is holy
## Don't go putting an actual privatekey for the mainnet up on github or something.
## Probably take it as a parameter and keep it stored elsewhere.
wallet_address = "0xbDD48a60cDEfCbaD854b21a137fdb37844867fd3"
wallet_private_key = "52F9DBC5C2B40683745994DD8514D60FA015C432AE0A922ACF941B4E78EA3463"



def setDataToSensorById(id, data):
    nonce = w3.eth.getTransactionCount(wallet_address)
    txn_dict1 = contract1.functions.setDataToSensorById(id, data).buildTransaction({
        'chainId': 3,
        'gas': 140000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': nonce
    })
    txn_dict2 = contract2.functions.setDataToSensorById(id, data).buildTransaction({
        'chainId': 3,
        'gas': 140000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': nonce + 1
    })
    txn_dict3 = contract3.functions.setDataToSensorById(id, data).buildTransaction({
        'chainId': 3,
        'gas': 140000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': nonce + 2
    })

    signed_txn1 = w3.eth.account.signTransaction(txn_dict1, wallet_private_key)
    signed_txn2 = w3.eth.account.signTransaction(txn_dict2, wallet_private_key)
    signed_txn3 = w3.eth.account.signTransaction(txn_dict3, wallet_private_key)
    result1 = w3.eth.sendRawTransaction(signed_txn1.rawTransaction)
    result2 = w3.eth.sendRawTransaction(signed_txn2.rawTransaction)
    result3 = w3.eth.sendRawTransaction(signed_txn3.rawTransaction)
    txn_receipt1 = w3.eth.getTransactionReceipt(result1)
    txn_receipt2 = w3.eth.getTransactionReceipt(result2)
    txn_receipt3 = w3.eth.getTransactionReceipt(result3)
    count = 0

    while txn_receipt3 is None or txn_receipt2 is None or txn_receipt1 is None:
        txn_receipt1 = w3.eth.getTransactionReceipt(result1)
        txn_receipt2 = w3.eth.getTransactionReceipt(result2)
        txn_receipt3 = w3.eth.getTransactionReceipt(result3)
        print("Processing...")
        time.sleep(10)
    if txn_receipt1 is None or txn_receipt2 is None:
        return False
    else:
        print(txn_receipt1.gasUsed)
        print(txn_receipt2.gasUsed)
        print(txn_receipt3.gasUsed)
        f = open("DataFile200.txt", "a")
        f.write(str(data) + "," + str(txn_receipt1.gasUsed) + ',' + str(txn_receipt2.gasUsed) + "\n")
        f.close()
        d = open("DataFile2000.txt", "a")
        d.write(str(data) + "," + str(txn_receipt1.gasUsed) + ',' + str(txn_receipt3.gasUsed) + "\n")
        d.close()
        return True



if __name__ == "__main__":
    sensor_Id = 0;
    if len(sys.argv) == 2:
        print("Correct number of parameters.")
        try:
            sensorId = int(sys.argv[1])
        except ValueError:
            print("There should be one number entered in as a parameter.")
            exit()

        humidity = 274877906944
        backwardsHumidity = 2000
        while True:
            time.sleep(5)
            if setDataToSensorById(sensorId, humidity):
                print("Data has been succesfully appended to the blockchain.")
                humidity = humidity * 2
            else:
                print("something has gone wrong.")
                exit()
    else:
        print("This program requires 1 input from the user and should be executed as such. \n" +
               "Python SensorContractInterface.py Sensor_ID_Number")
