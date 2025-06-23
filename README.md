# SuperTX Bulk Sender

A Node.js script for sending native coins or ERC20 tokens to multiple addresses on any EVM-compatible chain. Supports batching, custom gas, and fallback RPCs.

## Features

- Bulk send native coins or ERC20 tokens
- Supports any EVM chain (configured in `chains.json`)
- Batching and nonce management for efficient sending
- Custom gas settings
- Fallback provider for reliable RPC usage
- Interactive CLI prompts

## Prerequisites

- Node.js v18+ recommended
- NPM

## Setup

1. **Clone or Download** this repository.
2. **Install dependencies**:
   ```sh
   npm install
   ```
3. **Configure Chains**:
   - Edit `chains.json` to add or update supported EVM networks and their RPC endpoints.

4. **Prepare Address List**:
   - Create a file named `address.txt` in the same directory.
   - Add one recipient address per line (EVM addresses only).

## Usage

Run the script from the project directory:

```sh
node bot.js
```

You will be prompted to:

- Select a network
- Choose transfer type (Native Coin or ERC20 Token)
- Enter your private key
- (If ERC20) Enter the token contract address
- Enter the amount to send to each address
- Optionally set custom gas parameters

The script will process all addresses in `address.txt` and display transaction results.

## Files

- `bot.js` - Main script
- `chains.json` - List of supported EVM networks and RPCs
- `address.txt` - List of recipient addresses (one per line)

## Notes

- **Never share your private key.** Use a dedicated wallet for bulk sending.
- Make sure you have enough balance for all transactions and gas fees.
- The script will stop if there are critical errors (e.g., insufficient balance, invalid RPCs).

---

<p align="center">
  <img src="https://raw.githubusercontent.com/Jhinkz018/supertx/main/assets/logo.png" alt="supertx logo" width="120"/>
</p>

---

Join our [Discord Community](https://discord.gg/vRHTv6TT) for live discussion and support.
