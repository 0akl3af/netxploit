"""
Author: XolvaID
Tele  : t.me/XolvaID
Github: github.com/XolvaID
Repo  : github.com/XolvaID/netxploit.git
"""






import os,requests,json,re,sys,time,socket
from bs4 import BeautifulSoup as bs
os.system("clear")

grey = '\x1b[90m'
red = '\x1b[91m'
green = '\x1b[92m'
yellow = '\x1b[93m'
blue = '\x1b[94m'
purple = '\x1b[95m'
cyan = '\x1b[96m'
white = '\x1b[37m'
flag = '\x1b[47;30m'
off = '\x1b[m'
bold = '\033[1m'

ses = requests.Session()

print(f"""{bold}{red}o   o      o  o   o      o        o
{red}|\  |      |   \ /       |     o  |
{red}| \ | o-o -o-   O   o-o  | o-o   -o-
{white}|  \| |-'  |   / \  |  | | | | |  |
{white}o   o o-o  o  o   o O-o  o o-o |  o
           [V.10]   | By Xolva{red}ID{off}
{bold}{white}                    o                """)
print("==================================")
# Menu
print(f"{bold}[{cyan}00{off}] Exit Script")
print(f"{bold}[{cyan}01{off}] Whats My IP")
print(f"{bold}[{cyan}02{off}] Convert Host To IP")
print(f"{bold}[{cyan}03{off}] Convert IP To Host")
print(f"{bold}[{cyan}04{off}] Check IP/Host Information")
print(f"{bold}[{cyan}05{off}] Scan Cloudflare Hosts")
print(f"{bold}[{cyan}06{off}] Scan Subdomain")
print(f"{bold}[{cyan}07{off}] Scan Bug")
print(f"{bold}[{cyan}08{off}] Port Checker")
print(f"{bold}[{cyan}69{off}] About Tools")
print(f"{bold}==================================\n")
inp = input(f"Input Menu {bold}{red}>>>{green} ")
print(off)
if inp in ("00","0"):
 exit(f"{bold}[{red}!{off}]Exitting Script.")
elif inp in ("01","1"):
 YourIP = ses.get("http://api.ipify.org").text
 print("Your IP Address Is: "+green+str(YourIP)+off)
elif inp in ("02","2"):
 host = input(f"Input Host {bold}{red}>>>{green} ")
 print(off)
 ipapi = ses.get(f"http://ip-api.com/json/{host}").text
 JsonMenu2 = json.loads(ipapi)
 print("IP Address For "+host+f" Is {bold}{green}"+JsonMenu2["query"])
elif inp in ("03","3"):
 ip = input(f"Input IP {bold}{red}>>>{green} ")
 print(off)
 reverse = ses.get("https://api.hackertarget.com/reverseiplookup/?q="+ip)
 if reverse.text != "error check your search parameter":
  print("Host For "+ip+f" Is {bold}{green}"+reverse.text)
  print(off)
elif inp in ("04","4"):
 WhoisIP = input(f"Input Host/IP {bold}{red}>>>{green} ")
 print(off)
 ipapi = requests.get(f"http://ip-api.com/json/{WhoisIP}").text
 inf = json.loads(ipapi)
 print("==================================")
 print(f"IP           {bold}{green}: "+inf["query"]+f"{off}")
 print(f"COUNTRY      {bold}{green}: "+inf["country"]+f"{off}")
 print(f"COUNTRY CODE {bold}{green}: "+inf["countryCode"]+f"{off}")
 print(f"REGION NAME  {bold}{green}: "+inf["regionName"]+f"{off}")
 print(f"ZIP          {bold}{green}: "+inf["zip"]+f"{off}")
 print(f"CITY         {bold}{green}: "+inf["city"]+f"{off}")
 print(f"ISP          {bold}{green}: "+inf["isp"]+f"{off}")
 print(f"ORG          {bold}{green}: "+inf["org"]+f"{off}")
 print(f"AS           {bold}{green}: "+inf["as"]+f"{off}")
 print(f"{off}==================================")

elif inp in ("05","5"):
 host = input(f"Input Host {bold}{red}>>>{green} ")
 print("")
 r = requests.get(f"https://api.hackertarget.com/hostsearch/?q={host}")
 head = {"Host":"id-public1.sshws.net","Upgrade":"websocket"}
 success = []
 if r == "error invalid host":
  exit(f"[{red}!{off}]Host Atau IP Tidak Valid")
 else:
  pler = re.findall("(.*?),",r.text)
 for kontol in pler:
  try:
   req = requests.get(f"http://{kontol}",headers=head,timeout=0.7)
   if req.status_code == 101:
    print(f"{green}[ SUCCESS ]{off} {kontol}")
    success.append(str(kontol))
   else:
    print(f"{red}[  FAIL   ]{off} {kontol}")
  except:
   pass

 print(f"\nTotal Host/Bug Yang Sukses Didapat: {green}{str(len(success))}{off}")
 if len(success) >= 0:
    print("Berikut hasil yang didapatkan : ")
 print("\n========================")
 for result in success:
    print(f"{green}{result}{off}")
 print("========================\n")

elif inp in ("06","6"):
 ip = input(f"Input Host/Domain {bold}{red}>>>{green} ")
 print(off)
 r = ses.get("https://api.hackertarget.com/hostsearch/?q="+ip)
 if r.text != "error invalid host":
  print(r.text.replace(",","---"))
  with open(ip+".txt","a") as (s):
   s.write(r.text.replace(",","---"))
  print(f"[{green}✓{off}] Saved "+ip+".txt")
 else:
  print(f"[{red}!{off}] Invalid Host")

elif inp in ("07","7"):
 ip = input(f"Input Host/IP {bold}{red}>>>{green} ").replace("http://","").replace("https://","")
 port = input(f"{off}Input Port {bold}{red}>>>{green} ")
 print(off)
 r = ses.get("http://" + ip + ":" +port)
 print("========================")
 try:
  print("Host/IP     : " + green  + ip + off)
  print("Server      : " + green + r.headers["Server"] + off)
  print("Status Code : " + green + str(r.status_code) + off)
  print("Connection  : " + green + r.headers["Connection"] + off)
  print("Content Type: " + green + r.headers["Content-Type"] + off)
  print("Date        : " + green + r.headers["Date"] + off)
  print("========================")
 except:
  pass

elif inp in ("111"):
 udpdomain = input(f"Input Host/IP {bold}{red}>>>{green} ")
 port = input(f"{off}Input Port {bold}{red}>>>{green} ")
 print(off)
 data = {"udpdomain":udpdomain,
         "udpport":port
        }
 post = requests.post("https://openport.net/udp-port-checker/",data=data)
 status = re.search("'>(.*?)</font>",post.text).group(1)
 if status == "Closed":
  status = f"{red}{status}"
 elif status == "Open":
  status = f"{green}{status}"
 print(f"{bold}========================")
 print(f"IP/Host : {green}"+udpdomain)
 print(f"{off}{bold}UDP Port: {green}"+re.search("Port: (.*?)\sS",post.text).group(1))
 print(f"{off}{bold}Status  : {green}"+status)
 print(f"{off}{bold}========================")

elif inp in ("08","8"):
 ip = str(input(f"Input Host/IP {bold}{red}>>>{green} "))
 port = int(input(f"{off}Input Port {bold}{red}>>>{green} "))
 ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 inf = (str(ip), int(port))
 status = ssocket.connect_ex(inf)

 if status == 0:
  status = f"{green}Open"
 else:
  status = f"{red}Closed"
 print(f"\n{off}{bold}========================")
 print(f"Host/IP{green}: "+ip)
 print(f"{off}{bold}Port   {green}: "+str(port))
 print(f"{off}{bold}Status : "+status)
 print(f"{off}{bold}========================")
elif inp in ("69"):
 os.system("clear")
 print("========================")
 print(f"Author  : {bold}{white}Xolva{red}ID{off}")
 print(f"Created : {bold}{white}24 Sept 2021{off}")
 print(f"Feedback: {bold}https://t.me/XolvaID")
 print("========================")
 os.system("xdg-open https://t.me/XolvaID")
 time.sleep(2)
 exit()

a = input(f"\n{bold}[{green}?{off}] Restart Script? [{green}y{off}/{red}n{off}] {red}>>>{green} ")
if a in ("y","Y"):
 os.system("python3 "+sys.argv[0])
else:
 exit()
