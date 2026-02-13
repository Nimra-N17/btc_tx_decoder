# cli.py
# Bitcoin Transaction Decoder CLI

from btc_tx_decoder.decoder import Transaction
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py <raw_transaction_hex>")
        return

    raw_hex = sys.argv[1]

    tx = Transaction(raw_hex)

    print("Version:", tx.version)
    print("Inputs:", tx.inputs)
    print("Outputs:", tx.outputs)
    print("Locktime:", tx.locktime)

if __name__ == "__main__":
    main()
