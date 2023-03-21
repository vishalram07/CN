import socket

# Initialize socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)

# Data to be sent
data = ['packet1', 'packet2', 'packet3', 'packet4', 'packet5']

# Window size
N = 3

# Sequence number
seq_num = 0

# Send packets
while seq_num < len(data):
    print(f"seq:{seq_num}")
    # Send N packets
    for i in range(seq_num, min(seq_num + N, len(data))):
        message = str(seq_num) + ':' + data[i]
        print(message)
        sock.sendto(message.encode(), server_address)
    # Wait for ACKs
    try:
        sock.settimeout(1)
        while True:
            ack, address = sock.recvfrom(1024)
            ack_seq_num = int(ack.decode())
            print(f"ack: {ack_seq_num}")
            if ack_seq_num >= seq_num:
                seq_num = ack_seq_num + 1
                
    except socket.timeout:
        pass