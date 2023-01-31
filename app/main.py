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
    server_socket.settimeout(1.0)
    timed_out = False
    while not timed_out:
        try:
            client_socket, _ = server_socket.accept() # wait for client
        except socket.timeout:
            print("entered")
            timed_out = True
        else:
            resp = RESPString("PONG")
        client_socket.send(resp.as_simple_string().encode())


if __name__ == "__main__":
    main()
