from bitcoinlib.wallets import Wallet
import random
import string


def gen_address(user_wallet):
    w = Wallet.create(user_wallet)
    wallet = w.get_key()
    address = wallet.address
    return address

# def get_transactions(wallet_id):
#     w = Wallet(wallet_id)
#     trans = w.transactions
#     return trans
