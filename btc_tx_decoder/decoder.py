# btc_tx_decoder/decoder.py
import struct
from .utils import hex_to_bytes, read_varint, parse_script

class TxInput:
    def __init__(self, txid, vout, script_sig, sequence):
        self.txid = txid
        self.vout = vout
        self.script_sig = script_sig
        self.sequence = sequence

    def __repr__(self):
        return f"TxInput(txid={self.txid}, vout={self.vout}, script_sig={self.script_sig}, sequence={self.sequence})"

class TxOutput:
    def __init__(self, value, script_pubkey):
        self.value = value
        self.script_pubkey = script_pubkey

    def __repr__(self):
        return f"TxOutput(value={self.value}, script_pubkey={self.script_pubkey})"

class Transaction:
    def __init__(self, raw_hex):
        self.raw_bytes = hex_to_bytes(raw_hex)
        self.inputs = []
        self.outputs = []
        self.version = 0
        self.locktime = 0
        self.parse()

    def parse(self):
        b = self.raw_bytes
        offset = 0

        # Version
        self.version, = struct.unpack_from("<I", b, offset)
        offset += 4

        # Input count
        in_count, in_size = read_varint(b[offset:])
        offset += in_size

        # Inputs
        for _ in range(in_count):
            txid = b[offset:offset+32][::-1].hex()
            offset += 32
            vout, = struct.unpack_from("<I", b, offset)
            offset += 4

            script_len, size_len = read_varint(b[offset:])
            offset += size_len
            script_sig = b[offset:offset+script_len].hex()
            offset += script_len

            sequence, = struct.unpack_from("<I", b, offset)
            offset += 4

            self.inputs.append(TxInput(txid, vout, script_sig, sequence))

        # Output count
        out_count, out_size = read_varint(b[offset:])
        offset += out_size

        # Outputs
        for _ in range(out_count):
            value, = struct.unpack_from("<Q", b, offset)
            offset += 8

            script_len, size_len = read_varint(b[offset:])
            offset += size_len
            script_pubkey = parse_script(b[offset:offset+script_len])
            offset += script_len

            self.outputs.append(TxOutput(value, script_pubkey))

        # Locktime
        self.locktime, = struct.unpack_from("<I", b, offset)
