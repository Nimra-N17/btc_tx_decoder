# demo.py
# Bitcoin Transaction Decoder demo

import sys
import os

# Add the inner btc_tx_decoder folder to Python's module search path
inner_path = os.path.join(os.path.dirname(__file__), "btc_tx_decoder")
sys.path.insert(0, inner_path)  # insert at beginning

# Now import decoder from the inner folder
import decoder

# Example raw transaction (replace this with a real one)
raw_hex = "0100000001b1a2..."  

# Create Transaction object
tx = decoder.Transaction(raw_hex)

# Print transaction details
print("Version:", tx.version)
print("Inputs:", tx.inputs)
print("Outputs:", tx.outputs)
print("Locktime:", tx.locktime)
