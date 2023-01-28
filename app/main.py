import socket

"""
    A convenience class to handle strings the way RESP (REdis Serialization Protocol) expects it
"""
class RESPString:
    def __init__(self, s: str) -> None:
        self.s = s
    def as_simple_string(self) -> str:
        return f"+{self.s}\r\n"

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    client, _ = server_socket.accept() # wait for client
    resp = RESPString("PONG")
    client.send(resp.as_simple_string().encode())
    server_socket.close()
    
    

if __name__ == "__main__":
    main()
