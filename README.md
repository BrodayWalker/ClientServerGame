# ClientServerGame
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ClientServerGame is a number guessing game between a server and multiple clients. The server holds a secret, random integer value that the clients must guess. A client connects to the server, sends its guess, receives a response from the server, and adjusts its guess accordingly. The server responds with a -1 for guesses that are too low, a 1 for guesses that are too high, and a 0 for guesses that are correct. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The program was written for and tested on Ubuntu 18.04, but it will run on Windows, thanks to Python's socket and selector modules. These modules use the appropriate system calls for both operating systems.

## Authors
| Name | Email | Github Username |
| ------------------------------------------------ | ------------------------- | --------------- |
| [Broday Walker](https://github.com/BrodayWalker) | brodaywalker@gmail.com | BrodayWalker |
| [Ben Diekhoff](https://github.com/BenDiekhoff) | ben.diekhoff@gmail.com | BenDiekhoff |
| [Ladelle Augustine](https://github.com/Ladelle) | ladelle2016@gmail.com | Ladelle |

Comments are made throughout the code showing who contributed what.

## Instructions
Make sure Client.py and Server.py are executable:

```bash
chmod +x Client.py
chmod +x Server.py
```
To run each file, you need to determine your own ip address. Thanks to Dr. Griffin, a function is provided [here](helpers.py) that tells you what your IP is; you can also run `whatsmyip.py`, which is located in this repo.

Edit [config.py](config.py) and add your own information. Dr. Griffin created this so he wouldn't have to type in the parameters everytime. It is convenient. Use it!

Here is my config file:

```python
host = "127.0.1.1"
host2 =  "192.168.0.11"
port = 6000
debug = False
```

## Starting the Server
Start the server before making any client requests. <br> <br>
**Command if using config**: `./Server.py` <br> <br>
**Command without config**: `./Server.py host=10.0.0.1 port=6000`<br><br>
Keep in mind, the value of host is specific to you and your network.

## Starting the Client
**Command if using config**: `./Client.py`<br><br>
**Command without config**: `./Client.py host=10.0.0.1 port=6000` <br><br>
As with the server, make sure you are using the correct host value.

## Known Issues/Flaws
- The program does not implement a mutex
- Clients must connect, guess, disconnect, repeat

