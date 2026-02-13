# tests/test_decoder.py
import unittest
from btc_tx_decoder.decoder import Transaction

class TestTransactionParsing(unittest.TestCase):
    def test_simple_tx(self):
        # Replace this with a real transaction hex later
        raw_hex = "0100000001b1a2..."  
        tx = Transaction(raw_hex)
        self.assertTrue(tx.version > 0)
        self.assertTrue(len(tx.inputs) > 0)
        self.assertTrue(len(tx.outputs) > 0)

if __name__ == "__main__":
    unittest.main()
