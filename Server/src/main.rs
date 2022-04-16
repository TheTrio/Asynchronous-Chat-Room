use tokio::{
    io::{AsyncBufReadExt, AsyncWriteExt, BufReader},
    net::TcpListener,
    sync::broadcast,
};

#[tokio::main]
async fn main() {
    let listener = TcpListener::bind("127.0.0.1:8080").await.unwrap();
    let (tx, _rx) = broadcast::channel(10);
    loop {
        let tx = tx.clone();
        let mut rx = tx.subscribe();
        let (mut socket, addr) = listener.accept().await.unwrap();
        let ip = socket.peer_addr().unwrap();
        println!("Connected with {}", addr);
        tokio::spawn(async move {
            let (read, mut writer) = socket.split();
            let mut reader = BufReader::new(read);
            let mut line = String::new();

            loop {
                tokio::select! {
                    result = reader.read_line(&mut line) => {
                        if result.unwrap()==0 || line.replace("\n", "") == "quit"{
                            // client has disconnected
                            break;
                        }

                        println!("{} sent {}", ip, line.replace("\n", ""));
                        tx.send((line.clone(), ip)).unwrap();
                        line.clear();
                    }
                    result = rx.recv() => {
                        let (msg, address) = result.unwrap();
                        if address!=addr{
                            writer.write_all(msg.as_bytes()).await.unwrap();
                        }
                    }
                }
            }
        });
    }
}
