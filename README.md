# Bitcoin Fee Estimator

A simple Python CLI tool that estimates Bitcoin transaction fees in satoshis based on mempool congestion.  
This project demonstrates basic Python programming, API usage, and Bitcoin transaction concepts.

## Features

- Fetches live mempool data from [mempool.space](https://mempool.space) API
- Estimates recommended fee based on transaction size (bytes)
- CLI interface with optional argument for transaction size
- Single-file, beginner-friendly Python project

## Usage

### Interactive mode

```bash
python fee_estimator.py
