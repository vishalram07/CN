import socket

# Initialize socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
sock.bind(server_address)

# Expected sequence number
expected_seq_num = 0

# Window size
N = 3

while True:
    # Receive packet
    packet, address = sock.recvfrom(1024)
    packet_data = packet.decode().split(':')
    seq_num = int(packet_data[0])
    message = packet_data[1]
    
    print("OUTER")
    # Check sequence number
    if seq_num == expected_seq_num:
        print(message)

        # Send ACK
        ack = str(seq_num)
        sock.sendto(ack.encode(), address)

        # Move window
        expected_seq_num += 1
        print("exp_seq :", expected_seq_num)

        # Handle out-of-order packets
        while True:
            print("INNER")
            try:
                packet, address = sock.recvfrom(1024)
                packet_data = packet.decode().split(':')
                seq_num = int(packet_data[0])
                message = packet_data[1]

                if seq_num == expected_seq_num:
                    print(message)

                    # Send ACK
                    ack = str(seq_num)
                    sock.sendto(ack.encode(), address)

                    # Move window
                    expected_seq_num += 1
                else:
                    break
            except socket.timeout:
                break
    else:
        # Discard packet
        pass