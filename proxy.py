import signal
import subprocess

def start_proxy(address, port):

    protocol = "http"
    if ("socks5" in address): protocol = "socks5"
    print("Starting proxy")

    command = [
        "python",
        "-m",
        "pproxy",
        "-l",
        "{}://0.0.0.0:{}".format(protocol, port),
        "-r",
        address
    ]

    process = subprocess.Popen(command)
    print("Proxy started with PID:", process.pid)
    return process

processes = []

try:
    # Russian proxies
    russian_first_port = 8080
    for line in open("ru.txt", "r"):
        processes.append(start_proxy(line, russian_first_port))
        russian_first_port += 1

    # EU proxies
    eu_first_port = 9090
    for line in open("eu.txt", "r"):
        processes.append(start_proxy(line, eu_first_port))
        eu_first_port += 1

    signal.pause()

except:
    for process in processes:
        if process.poll() is None:
            process.terminate()
            process.wait()

    print("Main application exited.")