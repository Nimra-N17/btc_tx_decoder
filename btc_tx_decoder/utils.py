# btc_tx_decoder/utils.py

def hex_to_bytes(hex_str):
    return bytes.fromhex(hex_str)

def read_varint(b):
    i = b[0]
    if i < 0xfd:
        return i, 1
    elif i == 0xfd:
        return int.from_bytes(b[1:3], "little"), 3
    elif i == 0xfe:
        return int.from_bytes(b[1:5], "little"), 5
    else:
        return int.from_bytes(b[1:9], "little"), 9

def parse_script(b):
    return b.hex()  # Simplified script parsing for now
