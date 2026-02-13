# Bitcoin Transaction Decoder

A Python CLI tool that parses raw Bitcoin transaction hex and displays basic transaction fields. This project demonstrates understanding of Bitcoin transaction structure, Python programming, and CLI tools.

## Features

- Parses transaction version and input count
- Displays raw transaction size in bytes
- Simple CLI interface for easy testing
- Modular design for future extension

## Usage

Run the script with a raw transaction hex:

python main.py <raw_transaction_hex>

## Installation

1. Make sure Python 3 is installed
2. (Optional) Create a virtual environment
3. Run the script using Python as shown above

## Why I Built This

This project helps beginners understand Bitcoin transaction structure at the byte level. It demonstrates reading and parsing raw transaction data, modular Python code, and CLI usage.

## Future Improvements

- Fully parse inputs and outputs
- Detect common script types (P2PKH, P2SH, P2WPKH, P2WSH)
- Add unit tests for all parsing functions
