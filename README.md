# Asynchronous-Chat-Room

A demo application built as part of my college BTP. 

The server is coded in Rust using [tokio](https://tokio.rs/). The client is built using python.

# Demo
![gif](https://user-images.githubusercontent.com/10794178/163668433-1a366bb0-f066-495a-977f-4dd864a4b98e.gif)

# How to run

First, install the rust dependencies

```
cd Server
cargo install
```

Now, to start the TCP server, do

```
cargo run
```
For starting the python client, do

```
cd Client
python client.py
```
