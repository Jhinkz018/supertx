# EVM Auto Transaction Script

Automate transactions across all major EVM-compatible networks with beautiful logging and multi-network support. This script is perfect for airdrop hunters, network testers, and blockchain developers who want to:

- Send small transactions to random addresses on every EVM chain
- Track transaction status with beautiful, color-coded logs
- Easily add or remove supported networks

## Features
- Supports Ethereum, BSC, Polygon, Avalanche, Arbitrum, Optimism, Fantom, Base, Mode, World, OPBNB, Zora, Linea, Scroll, Lisk, Soneium, Unchain, Ink, and more
- Sends 0.0000001 native token to a random address on each network
- Uses the lowest available gas price (gwei) for each transaction
- Beautiful, informative logs inspired by Helios.js
- Summary of all transactions at the end

## Requirements
- Python 3.8+
- `web3`, `python-dotenv`, `eth-account`, `requests`

## Setup
1. Clone this repo:
   ```bash
   git clone https://github.com/Jhinkz018/supertx.git
   cd supertx
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory:
   ```env
   PRIVATE_KEY=your_private_key_here
   ```
   Replace `your_private_key_here` with your wallet's private key (keep this safe!).
4. (Optional) Edit `scripts/evm_transaction.py` to add/remove networks as needed.

## Usage
Run the script:
```bash
python scripts/evm_transaction.py
```

## Security
- **Never share your private key**
- Test with small amounts first
- Use at your own risk

## Credits
- Built with ❤️ by [Jhinkz018](https://github.com/Jhinkz018)
- Join our community: https://discord.gg/y5YUHrEC
