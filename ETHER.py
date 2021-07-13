from web3 import Web3

node_provider = 'https://mainnet.infura.io/v3/c2bed06ba0424aa995943f39106e49af'

web3_connection = Web3(Web3.HTTPProvider(node_provider))

def are_we_connected():

    print(web3_connection.isConnected())

def latest_block():
    print(web3_connection.eth.block_number)

def balance_of(ETH_address):
    balance = web3_connection.eth.getBalance(ETH_address)
    balance_ETH = web3_connection.fromWei(balance,'ether')
    print(balance_ETH)   