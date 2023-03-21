import math

# Define the original IP datagram
orig_datagram = {
    'seq_num': 0,
    'ident': 345,
    'total_len': 5140,
    'df': 0,
    'mf': 1,
    'frag_offset': 0,
}

# Define the MTU sizes of the networks
mtu1 = 1500
mtu2 = 620

# Calculate the number of fragments required for each MTU size
payload_size = orig_datagram['total_len'] - 20 # Subtract the header size
num_frags_mtu1 = math.ceil(payload_size / (mtu1 - 20))
num_frags_mtu2 = math.ceil(payload_size / (mtu2 - 20))

# Fragment the original datagram for MTU size 1
frags_mtu1 = []
offset = 0
print("\nNUMBER OF FRAGMENTS AT ROUTER R1 : ",num_frags_mtu1)
for i in range(num_frags_mtu1):
    frag = {
        'seq_num': orig_datagram['seq_num'],
        'ident': orig_datagram['ident'],
        'total_len': mtu1,
        'df': orig_datagram['df'],
        'mf': 1 if i < num_frags_mtu1-1 else 0, # Set MF flag only for non-last fragments
        'frag_offset': offset,
    }
    frags_mtu1.append(frag)
    offset += mtu1-20

# Fragment the original datagram for MTU size 2
frags_mtu2 = []
print("\nNUMBER OF FRAGMENTS AT ROUTER R2 or R3 : ",num_frags_mtu2)
offset = 0
for i in range(num_frags_mtu2):
    frag = {
        'seq_num': orig_datagram['seq_num'],
        'ident': orig_datagram['ident'],
        'total_len': mtu2,
        'df': orig_datagram['df'],
        'mf': 1 if i < num_frags_mtu2-1 else 0, # Set MF flag only for non-last fragments
        'frag_offset': offset,
    }
    frags_mtu2.append(frag)
    offset += mtu2-20

# Display the IP fragments at router R1
print("IP fragments at router R1:")
for frag in frags_mtu1:
    print(frag)

# Display the IP fragments at router R2 or R3
print("IP fragments at router R2 or R3:")
for frag in frags_mtu2:
    print(frag)

# Reassemble the packets and display the whole IP packet at the destination B
reassembled_payload = ''
reassembled_datagram = {
    'seq_num': orig_datagram['seq_num'],
    'ident': orig_datagram['ident'],
    'total_len': orig_datagram['total_len'],
    'df': orig_datagram['df'],
    'mf': 0,
    'frag_offset': 0,
}
print("Reassembled IP datagram at destination B:")
print(reassembled_datagram)