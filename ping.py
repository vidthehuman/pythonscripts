import os
def check_server(host):
  response = os.system("ping -c 3 " + host)
  if response == 0:
    print(host + " is up!")
  else:
    print(host + " is down!")