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
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    response_string = RESPString("Pong").as_simple_string()
    while server_socket.recv(1024):  # While the server receives incoming requests.
        client_socket, _ = server_socket.accept()
        client_socket.send(response_string.encode())
    server_socket.close()


if __name__ == "__main__":
    main()
