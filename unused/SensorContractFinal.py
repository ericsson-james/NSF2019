import time
from web3 import Web3, HTTPProvider
import json
import sys
import Adafruit_DHT

infura_url = "https://ropsten.infura.io/v3/c2c9ec67e10646528586904b7df8f237"
w3 = Web3(Web3.HTTPProvider(infura_url))


## If the contract is ever reuploaded then this address will need to be changed.
contract_address = w3.toChecksumAddress("0x3d74538be9f3260e1f61c0601474fa504b54bd9d")
abi = json.loads('[ { "constant": false, "inputs": [ { "name": "id", "type": "int256" }, { "name": "description", "type": "string" } ], "name": "setDescriptionById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "int256" } ], "name": "sensors", "outputs": [ { "name": "id", "type": "int256" }, { "name": "max", "type": "int256" }, { "name": "min", "type": "int256" }, { "name": "description", "type": "string" }, { "name": "abnormalBehaviors", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "int256" }, { "name": "max", "type": "int256" } ], "name": "setMaxById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getSensorDataById", "outputs": [ { "name": "", "type": "int256[]" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [], "name": "addSensor", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "sensorCount", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "int256" } ], "name": "deleteAllSensorDataById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getMinByIdfunction", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "max", "type": "int256" }, { "name": "min", "type": "int256" }, { "name": "description", "type": "string" } ], "name": "addSensor", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "max", "type": "int256" }, { "name": "min", "type": "int256" } ], "name": "addSensor", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getDescriptionById", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "int256" }, { "name": "data", "type": "int256" } ], "name": "setDataToSensorById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getAbnormalBehaviorCountById", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "id", "type": "int256" } ], "name": "getMaxById", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "id", "type": "int256" }, { "name": "min", "type": "int256" } ], "name": "setMinById", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor" } ]')


##  The address and the abi are needed to act as a contract object
contract = w3.eth.contract(address = contract_address, abi = abi)
## While it doesn't matter for the testnet being used for the love of all that is holy
## Don't go putting an actual privatekey for the mainnet up on github or something.
## Probably take it as a parameter and keep it stored elsewhere.
wallet_address = "0x1E41Ec0f883a3F62a42331E243eD8171B2FF16D5"
wallet_private_key = "8C08D70497F65A743B9EAFD1B104BEEAEAAA7760E588F5EFC43EB75766088BB1"



def setDataToSensorById(id, data):
    nonce = w3.eth.getTransactionCount(wallet_address)
    txn_dict = contract.functions.setDataToSensorById(id, data).buildTransaction({
        'chainId': 3,
        'gas': 140000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': nonce
    })

    signed_txn = w3.eth.account.signTransaction(txn_dict, wallet_private_key)
    result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    txn_receipt = w3.eth.getTransactionReceipt(result)
    count = 0

    while txn_receipt is None and (count < 30):
        txn_receipt = w3.eth.getTransactionReceipt(result)
        print("Processing...")
        time.sleep(10)
    if txn_receipt is None:
        return False
    else:
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

        while True:
            humidity, temperature = Adafruit_DHT.read_retry(11, 4)
            humidity = int(humidity)
            if setDataToSensorById(sensorId, humidity):
                print("Data has been succesfully appended to the blockchain.")
            else:
                print("something has gone wrong.")
                exit()
    else:
        print("This program requires 2 inputs from the user and should be executed as such. \n" +
               "Python SensorContractInterface.py Sensor_ID_Number Data")
