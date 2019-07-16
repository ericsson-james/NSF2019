from web3 import Web3
ganache_url = "https://ropsten.infura.io/v3/c2c9ec67e10646528586904b7df8f237"
web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())

print(web3.eth.blockNumber)

###account_1 = "0x3A7Ec23F8b04832DC9222411352Dbe2Eb5D53245"
account_2 = "0xbDD48a60cDEfCbaD854b21a137fdb37844867fd3"
##private_key_1 = "43b80999dbfe023d071ae19901399fba872221a9dcc9b46bd584166564d6f4d8"



account_1 = "0x1E41Ec0f883a3F62a42331E243eD8171B2FF16D5"
private_key_1 = "8C08D70497F65A743B9EAFD1B104BEEAEAAA7760E588F5EFC43EB75766088BB1"
# get the nonce
nonce = web3.eth.getTransactionCount(account_1)
# build a transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(.4, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
    }
# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key_1)
# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# get transaction hash
print(web3.toHex(tx_hash))
