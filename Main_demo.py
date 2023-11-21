import speedtest
import socket
from colorama import Fore, Style
class color:
    red = Fore.RED
    cyan = Fore.CYAN

st = speedtest.Speedtest()

print("finding server...")
st.get_servers()

print("Choosing best server..")
best = st.get_best_server()

print(f"country name: {best['country']}")
print(f"host name: {socket.gethostname()}")
print("please wait, testing the speed...")
download_speed = st.download()
upload_speed = st.upload()
dwnld_speed = download_speed / 1024 / 1024 / 8
upld_speed = upload_speed/ 1024 / 1024 / 8
print(f"download speed is: {dwnld_speed:.2f} MBps")
print(f"upload speed is: {upld_speed:.2f} MBps")

print(f"{dwnld_speed:.2f} MB/s mean you have currently using {dwnld_speed * 8:.2f} Mbps line from your ISP\n")

print("\nN:B==> if you feel guilty for your connection's speed then\nplease close the program and TEST AGAIN\n2 or 3 times of testing can be more understable about your connection\n")

print(color.cyan+"Codded by MR. Morningstar")
input(" ")
