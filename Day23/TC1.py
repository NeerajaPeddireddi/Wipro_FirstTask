import requests,threading,time

urls=[
    "https://www.google.com",
    "https://www.yahoo.com",
    "https://www.rediff.com",
    "https://www.amazon.in"
]
def download_file(url):
    try:
        response = requests.get(url)
        filename=url.split("/")[-1]+".txt"

        with open(filename,"w",encoding="utf-8") as f:
            f.write(response.text)
        print(f"Downloaded file name:{filename}")
    except Exception as e:
        print(f"ERROR Downloading {url}:{e}")
starttime=time.time()
for url in urls:
    download_file(url)
sequential_time=time.time()-starttime
print(f"\nSequential download time:{sequential_time}")

threads=[]
start_time1=time.time()
for url in urls:
    thread=threading.Thread(target=download_file,args=(url,))
    threads.append(thread)
    thread.start()
threading_time=time.time()-start_time1
print(f"\nThreading download time:{threading_time}")
