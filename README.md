# Asynchronous-Chat-Room

A demo application built as part of my college BTP. 

The server is coded in Rust using [tokio](https://tokio.rs/). The client is built using python.

# Demo
![demo](https://user-images.githubusercontent.com/10794178/163797115-0901294d-5037-4328-abc6-4a543efa7d4e.gif)


# How to run

To start the TCP server, do

```
cd Server
cargo run
```

For starting the python client, do

```
cd Client
poetry install --no-dev
poetry shell
python client.py
```
