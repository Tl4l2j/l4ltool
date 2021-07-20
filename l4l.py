import os, sys, requests, re, json, time
from time import sleep
from bs4 import BeautifulSoup as bs
red='\u001b[31;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
yellow='\u001b[33;1m'
reset='\u001b[0m'

def loading(): 
  print (green+"Loading...") 
  for i in range(0, 100): 
    time.sleep(0.02) 
    sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%") 
    sys.stdout.flush()
    print
loading()
os.system('clear')
time.sleep(1)
print(" SUCCESS")
os.system('clear')
time.sleep(1)
ckl4l=input(" Cookie l4l:")
#ckfb=input(" Cookie fb:")
os.system("clear")
hdl4l={
  "Host":"www.like4like.org",
  "x-requested-with":"XMLHttpRequest",
  "user-agent":"Mozilla/5.0 (Linux; Android 10; RMX1971) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36",
  "referer":"https://www.like4like.org/user/earn-facebook-subscribes.php",
  "cookie":ckl4l
}
hdfb={
'Host':'mbasic.facebook.com',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36',
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'cookie':'',
}
#dl=input("Nhập time:")
os.system('clear')
print(yellow+"""

                
 /$$$$$$$$ /$$       /$$           /$$$$$$$              /$$    
|__  $$__/| $$      |__/          | $$__  $$            | $$    
   | $$   | $$$$$$$  /$$  /$$$$$$$| $$  \ $$  /$$$$$$  /$$$$$$  
   | $$   | $$__  $$| $$ /$$_____/| $$  | $$ |____  $$|_  $$_/  
   | $$   | $$  \ $$| $$|  $$$$$$ | $$  | $$  /$$$$$$$  | $$    
   | $$   | $$  | $$| $$ \____  $$| $$  | $$ /$$__  $$  | $$ /$$
   | $$   | $$  | $$| $$ /$$$$$$$/| $$$$$$$/|  $$$$$$$  |  $$$$/
   |__/   |__/  |__/|__/|_______/ |_______/  \_______/   \___/
""")

ten=requests.get("https://www.like4like.org/",headers=hdl4l)
ten1=re.findall('user details.">.*?<',ten.text)[0].replace('user details.">','').replace('<','')
print(blue+"Tài khoản: "+ten1)

a=requests.get("https://www.like4like.org/api/get-user-info.php",headers=hdl4l).json() 
xu1=a['data']['credits'] 
hang=a['data']['weeklyPosition'] 
print(blue+"Tổng xu: "+str(xu1)+"  "+"Hạng: "+str(hang))
print(red+"____________________________________________")
while True:
  while True:
    try:
      getjob=requests.get(url="https://www.like4like.org/api/get-tasks.php?feature=facebooksub",headers=hdl4l).json()
      urll=getjob["data"]["tasks"][0]["url"]
      idlink=getjob["data"]["tasks"][0]["idlink"]
      taskId=getjob["data"]["tasks"][0]["taskId"]
      value=getjob["data"]["tasks"][0]["value"]
      typee=getjob["data"]["tasks"][0]["featureType"]
      code=getjob["data"]["tasks"][0]["code3"]
    except:  
      print(red+"job lỗi",end='\r')
      break
    else:
      sửa=idlink.replace("www","mbasic",1)
      s = requests.get(url=sửa,headers=hdfb)
      s1=s.url
      b = requests.get(s1,headers=hdfb).text
      soup = bs(b,"html.parser")
      link = soup("a",href=True) 
      for i in link: 
        linke=i["href"] 
        if "/a/subscribe.php?" in linke: 
          sub=requests.get("https://mbasic.facebook.com"+linke,headers=hdfb) 
      sleep(1)
      kiem=requests.get(f'https://www.like4like.org/api/start-task.php?idzad={idlink}&vrsta={typee}&idcod={taskId}&feature=facebooksub&_={urll}',headers=hdl4l)
      hdnhan={ 
        "Host":"www.like4like.org",
        "content-length":"194",
        "x-requested-with":"XMLHttpRequest",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; RMX1971) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36",
        "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
        "referer":"https://www.like4like.org/user/earn-facebook-subscribes.php",
        "cookie":ckl4l 
      }
      try:
        urlnhan="https://www.like4like.org/api/validate-task.php"
        datanhan=f'url={urll}&idzad={taskId}&idlinka={idlink}&idclana={code}&cnt=true&vrsta={typee}&feature=facebooksub&addon=false&version=' 
        nhan=requests.post(url=urlnhan,data=datanhan.encode('utf-8'),headers=hdnhan).json()
        sleep(1)
       
        xu=nhan['data']['credits']        
        kq=nhan['success'] 
        
        print(green+"Id Job:"+str(taskId)+" | "+"Xu:"+str(value)+" | "+str(typee)+" | "+"Số dư:"+str(xu)) 
        
      except:
        print("  ",end='\r')
  
