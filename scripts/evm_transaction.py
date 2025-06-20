from web3 import Web3
from eth_account import Account
import json
from dotenv import load_dotenv
import os
import time
from typing import Dict, Optional
import sys
from datetime import datetime

# Load environment variables
load_dotenv()

# Color codes for beautiful logs
RESET = '\033[0m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
CYAN = '\033[36m'
WHITE = '\033[37m'
BOLD = '\033[1m'

# Helper functions for beautiful logs
def center_text(text):
    terminal_width = 80
    try:
        import shutil
        terminal_width = shutil.get_terminal_size().columns
    except Exception:
        pass
    text_length = len(text.replace('\033[', ''))
    padding = max(0, (terminal_width - len(text)) // 2)
    return ' ' * padding + text

def log_banner():
    print(f"{CYAN}{BOLD}" + center_text("✪ EVM AUTO TRANSACTION ✪") + f"{RESET}")
    print(f"{BLUE}" + center_text("https://discord.gg/y5YUHrEC") + f"{RESET}")
    print(f"{CYAN}" + center_text("Automated Multi-Network Sender") + f"{RESET}\n")

def log_success(msg):
    print(f"{GREEN}{BOLD}✔ {msg}{RESET}")

def log_error(msg):
    print(f"{RED}✖ {msg}{RESET}")

def log_info(msg):
    print(f"{CYAN}{msg}{RESET}")

def log_warn(msg):
    print(f"{YELLOW}! {msg}{RESET}")

class EVMTransactionManager:
    # Network RPC endpoints
    NETWORKS = {
        'ethereum': 'https://rpc.ankr.com/eth',
        'bsc': 'https://bsc-dataseed.binance.org/',
        'polygon': 'https://polygon-rpc.com',
        'avalanche': 'https://api.avax.network/ext/bc/C/rpc',
        'arbitrum': 'https://arb1.arbitrum.io/rpc',
        'optimism': 'https://mainnet.optimism.io',
        'fantom': 'https://rpc.ftm.tools/',
        'base': 'https://mainnet.base.org',
        'mode': 'https://mainnet.mode.network',
        'world': 'https://rpc.worldchain.foundation/http',
        'opbnb': 'https://opbnb-mainnet-rpc.bnbchain.org',
        'zora': 'https://rpc.zora.energy',
        'linea': 'https://rpc.linea.build',
        'scroll': 'https://rpc.scroll.io',
        'lisk': 'https://rpc.lisk.com',
        'soneium': 'https://rpc.soneium.io',
        'unchain': 'https://rpc.unchain.io',
        'ink': 'https://rpc.ink.network',
        # Add more as needed
    }

    def __init__(self, private_key: str):
        """Initialize with a private key"""
        self.account = Account.from_key(private_key)
        self.web3_connections: Dict[str, Web3] = {}
        self._setup_connections()

    def _setup_connections(self):
        """Set up Web3 connections for all networks"""
        for network, rpc_url in self.NETWORKS.items():
            try:
                web3 = Web3(Web3.HTTPProvider(rpc_url))
                if web3.is_connected():
                    self.web3_connections[network] = web3
                    log_success(f"Successfully connected to {network}")
                else:
                    log_error(f"Failed to connect to {network}")
            except Exception as e:
                log_error(f"Error connecting to {network}: {str(e)}")

    def get_gas_price(self, network: str) -> int:
        """Get current gas price for the specified network"""
        if network not in self.web3_connections:
            raise ValueError(f"Network {network} not supported")
        
        web3 = self.web3_connections[network]
        return web3.eth.gas_price

    def get_nonce(self, network: str) -> int:
        """Get the next nonce for the account on specified network"""
        if network not in self.web3_connections:
            raise ValueError(f"Network {network} not supported")
        
        web3 = self.web3_connections[network]
        return web3.eth.get_transaction_count(self.account.address)

    def send_transaction(
        self,
        network: str,
        to_address: str,
        value: int,
        data: str = "",
        gas_limit: Optional[int] = None,
        gas_price_multiplier: float = 1.1
    ):
        """
        Send a transaction on the specified network
        
        Args:
            network: Name of the network
            to_address: Recipient address
            value: Amount in wei
            data: Transaction data (for contract interactions)
            gas_limit: Optional gas limit (will be estimated if not provided)
            gas_price_multiplier: Multiplier for gas price (default 1.1 = 10% higher)
        """
        if network not in self.web3_connections:
            raise ValueError(f"Network {network} not supported")

        web3 = self.web3_connections[network]
        
        # Prepare transaction
        transaction = {
            'nonce': self.get_nonce(network),
            'to': to_address,
            'value': value,
            'data': web3.to_hex(text=data) if data else "0x",
            'chainId': web3.eth.chain_id,
        }

        # Get gas price and apply multiplier
        gas_price = int(self.get_gas_price(network) * gas_price_multiplier)
        transaction['gasPrice'] = gas_price

        # Estimate gas if not provided
        if not gas_limit:
            gas_limit = web3.eth.estimate_gas(transaction)
        transaction['gas'] = gas_limit

        try:
            # Sign transaction
            signed_txn = web3.eth.account.sign_transaction(
                transaction, self.account.key
            )

            # Send transaction
            tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            log_success(f"Transaction sent on {network}. Hash: {tx_hash.hex()}")

            # Wait for transaction receipt
            receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
            return receipt

        except Exception as e:
            log_error(f"Error sending transaction on {network}: {str(e)}")
            return None

    @staticmethod
    def random_address():
        """Generate a random EVM address"""
        import random
        return '0x' + ''.join(random.choices('0123456789abcdef', k=40))

def main():
    # Load private key from environment variable
    private_key = os.getenv('PRIVATE_KEY')
    if not private_key:
        raise ValueError("Please set PRIVATE_KEY in your .env file")

    # Initialize transaction manager
    manager = EVMTransactionManager(private_key)

    # Amount to send: 0.0000001 native token (in wei)
    amount = Web3.to_wei(0.0000001, 'ether')
    log_info(f"Sending {amount} wei (0.0000001 native token) to a random address on each network.\n")
    success_count = 0
    fail_count = 0
    start_time = datetime.now()
    for network in manager.NETWORKS:
        try:
            to_address = EVMTransactionManager.random_address()
            log_info(f"[{network.upper()}] Sending to {to_address} ...")
            receipt = manager.send_transaction(
                network=network,
                to_address=to_address,
                value=amount,
                gas_price_multiplier=1.0
            )
            if receipt:
                log_success(f"[{network.upper()}] Success! Block: {receipt['blockNumber']} | Hash: {receipt['transactionHash'].hex()} | To: {to_address}")
                success_count += 1
            else:
                log_error(f"[{network.upper()}] Transaction failed!")
                fail_count += 1
        except Exception as e:
            log_error(f"[{network.upper()}] Error: {e}")
            fail_count += 1
    elapsed = (datetime.now() - start_time).total_seconds()
    print(f"\n{BOLD}{WHITE}Summary:{RESET}")
    print(f"{GREEN}Success: {success_count}{RESET} | {RED}Failed: {fail_count}{RESET} | {CYAN}Elapsed: {elapsed:.1f}s{RESET}\n")
    print(center_text(f"{BOLD}{CYAN}All done!{RESET}"))

if __name__ == "__main__":
    log_banner()
    main()
