from web3 import Web3

infura_url = "https://ropsten.infura.io/v3/c2c9ec67e10646528586904b7df8f237"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

print(web3.eth.blockNumber)

balance = web3.eth.getBalance("0x1E41Ec0f883a3F62a42331E243eD8171B2FF16D5")
print(web3.fromWei(balance, 'ether'))
