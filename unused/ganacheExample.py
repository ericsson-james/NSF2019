from web3 import Web3
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())

print(web3.eth.blockNumber)

account_1 = "0x3A7Ec23F8b04832DC9222411352Dbe2Eb5D53245"
account_2 = "0xeb1Fbbada83165E48528830BFd4c44AfEF1A522f"
private_key_1 = "43b80999dbfe023d071ae19901399fba872221a9dcc9b46bd584166564d6f4d8"

# get the nonce
nonce = web3.eth.getTransactionCount(account_1)
# build a transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(.1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
    }
# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key_1)
# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# get transaction hash
print(web3.toHex(tx_hash))
