import socket
import threading

"""
    A convenience class to handle strings the way RESP (REdis Serialization Protocol) expects it
"""
class RESPString:
    def __init__(self, s: str) -> None:
        self.s = s
    def as_simple_string(self) -> str:
        return f"+{self.s}\r\n"

RESP_STR = RESPString("PONG").as_simple_string()

def process_connection(client_connection):
    while True:
        try:
            client_connection.recv(1024):  # The server receives data from the client connection.
            client_connection.send(RESP_STR.encode())
        except ConnectionError:
            break



def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        client_connection, _ = server_socket.accept() # main waits for a new client connection.
        threading.Thread(target=process_connection, args=(client_connection,)).start() # new thread is created to process the new connection, and we start it.


if __name__ == "__main__":
    main()
