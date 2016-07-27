import socket
from time import time
from re import search

def start_server():
    try:
        print("\nWARNING: May not work on some machines and will be slow on mobile devices\n")
        remote_server = input("Enter host to scan: ")
        # Validation
        if type(search("\d.\d.\d.\d", remote_server)) != None: # Is ip
            remote_server_name = socket.gethostbyaddr(remote_server)[0]
            remote_server_ip = remote_server
        else: # Isn't ip
            remote_server_ip = socket.gethostbyname(remote_server)
            remote_server_name = remote_server
        # Ui messages
        print("----- SCANING -----")
        print("  Server: " + remote_server_name)
        print("  IP: " + remote_server_ip)
        print()
        return remote_server_ip
    except:
        print("ERROR: Host not found")

def scan(ip):
    try:
        for port in range(1, 50000):
            print("Trying port " + str(port), end = "\r")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(" " * 100, end = "\r") # Clear line
                print("  PORT: " + str(port))
            sock.close()
    except:
        print("Error when scanning. Aborting")
    print()

def main():
    start_time = time()
    sock = start_server()
    scan(sock)
    print("Time taken: %s seconds" % str(time() - start_time))

if __name__ == "__main__":
    main()
