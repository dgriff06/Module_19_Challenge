import os
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account, middleware, Web3
import requests
from web3.gas_strategies.time_based import medium_gas_price_strategy

web3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))

def generate_accounts(w3):
    mnemonic = os.getenv("MNEMONIC")
    wallet = Wallet(mnemonic)
    private, public = wallet.derive_account("eth")
    account = Account.privateKeyToAccount(private)
    return account 

def get_balance(web3, address):
    wei_balance = web3.eth.get_balance(address)
    ether = web3.fromWei(wei_balance, "ether")
    return ether

def send_transaction(web3, account, receiver, ether):
    web3.eth.setGasPriceStrategy(medium_gas_price_strategy)
    wei_value = web3.toWei(ether, "ether")
    gas_estimate = web3.eth.estimateGas({"to":receiver, "from":account.address, "value":wei_value})
    
    raw_tx = {
        "to": receiver,
        "from": account.address,
        "value": wei_value,
        "gas": gas_estimate,
        "gasPrice": 0,
        "nonce": web3.eth.getTransactionCount(account.address)
    }
    
    signed_tx = account.signTransaction(raw_tx)
    
    return web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    
    