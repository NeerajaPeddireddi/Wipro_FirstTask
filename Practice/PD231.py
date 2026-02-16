import time
from idlelib.iomenu import encoding

import requests,threading

urls=[
    "https://www.google.com",
    "https://www.yahoo.com",
    "https://www.rediff.com",
    "https://www.amazon.in"
]
def download_urls(url):
    response=requests.get(url)
    filename=url.split("/")[-1]+".txt"

    with open(filename,"w",encoding="utf-8") as file:
        file.write(response.text)
start_time=time.time()
for url in urls:
    download_urls(url)
end_time=time.time()
print(end_time-start_time)

thread_start_time=time.time()
threads=[]
for url in urls:
    thread=threading.Thread(target=download_urls,args=(url,))
    threads.append(thread)
    thread.start()
thread_end_time=time.time()
print(thread_end_time-thread_start_time)
