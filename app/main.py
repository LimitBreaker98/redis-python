import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    host_address, port = server_socket.accept() # wait for client
    print(host_address, port)
    

if __name__ == "__main__":
    main()
