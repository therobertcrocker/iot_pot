import multiprocessing
from coap_server import main as server_main
from coap_client import main as client_main

if __name__ == "__main__":
    server_process = multiprocessing.Process(target=server_main)
    client_process = multiprocessing.Process(target=client_main)

    server_process.start()
    client_process.start()

    server_process.join()
    client_process.join()