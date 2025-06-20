# 🚀 EVM Auto Transaction Script Guide

Automate transactions across all major EVM-compatible networks with beautiful logging and multi-network support. Perfect for airdrop hunters, network testers, and blockchain developers!

---

## 🌟 Features

- Supports Ethereum, BSC, Polygon, Avalanche, Arbitrum, Optimism, Fantom, Base, Mode, World, OPBNB, Zora, Linea, Scroll, Lisk, Soneium, Unchain, Ink, and more
- Sends 0.0000001 native token to a random address on each network
- Uses the lowest available gas price (gwei) for each transaction
- Beautiful, informative logs
- Summary of all transactions at the end

---

## 🛠️ Requirements

- Python 3.8 or higher
- The following Python packages: `web3`, `python-dotenv`, `eth-account`, `requests`

---

## 📥 Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Jhinkz018/supertx.git
   cd supertx
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up your environment:**
   - Create a `.env` file in the root directory with this content:
     ```
     PRIVATE_KEY=your_private_key_here
     ```
   - Replace `your_private_key_here` with your wallet's private key (keep this safe and never share it!).
4. *(Optional)* Edit `scripts/evm_transaction.py` to add or remove supported networks as you wish.

---

## ▶️ Usage

Run the script with:
```bash
python scripts/evm_transaction.py
```

---

## 🔒 Security Tips

- **Never share your private key**
- Test with small amounts first
- Use at your own risk

---

## 💬 Community

- Built with ❤️ by [Jhinkz018](https://github.com/Jhinkz018)
- Join our community: https://discord.gg/y5YUHrEC

---
