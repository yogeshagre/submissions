from eth_account import account
from web3 import Web3
import web3
from web3.types import Nonce

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = "0x9c2c6E90B6F88d6389BdCe687dA8de3F3506D5e5"
account_2 = "0x35679e367992aa3A5B19998a147921B937278288"

private_key = "07c551adb423b1339d6786980b2b6e9f133812f43bff61a897b492dd2697491f"

nonce  = web3.eth.getTransactionCount(account_1)

tx ={
   'nonce': nonce,
   'to': account_2,
   'value': web3.toWei(1,'ether'),
   'gas': 200000,
   'gasPrice': web3.toWei('50','gwei') 
}

signed_tx = web3.eth.account.signTransaction(tx,private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))









