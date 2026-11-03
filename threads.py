from threading import Thread
from time import sleep,time
from multiprocessing import Process


#OPTION 1 : USING THREAD CLASS
class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello",i+1)
            sleep(0.3)


class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi",i+1)
            sleep(0.3)

if __name__ == "__main__":
    h1 = hello()
    h2 = hi()

    h1.start()
    sleep(0.2)
    h2.start()


#OPTION 2 : USING THREAD with functions only

def hello():
    for i in range(5):
        print("Hello",i+1)
        sleep(0.3)
            


def hi():
    for i in range(5):
        print("Hi",i+1)
        sleep(0.3)
            

if __name__ == "__main__":
    h1 = Thread(target=hello)
    sleep(0.2)
    h2 = Thread(target=hi)

    h1.start()
    h2.start()

    h1.join()
    h2.join()

    print("Bye")



#USE CASE : Downloading files using threads

def download_file(file):
    print("Downloading...",file)
    sleep(0.5)
    print("downloaded!")

if __name__ == "__main__":
    files = ["audio.MP3","video.MP4","image.JPG","image.PNG","data.CSV"]
    start = time()
    for f in files:
        download_file(f)
        
    end = time()

    print(f"Time taken while using serial:{end-start : .2f} seconds")
    threads = []
    for f in files:
        t = Thread(target=download_file, args=(f,))
        threads.append(t)

    start = time()

    for t in threads:
        t.start()
    
    for t in threads:
        t.join()
    
    end = time()

    print(f"Time taken while using parallely:{end-start : .2f} seconds")

    print("BYE!!")



#more advanced example of threads
def  calculate(n1, n2):
    sum  = 0
    for n in range(n1,n2):
        sum += n*n


if __name__ == "__main__":
    num = 50_000_000
    start = time()
    calculate(0,num)
    end = time()
    print(f"Time taken while using series:{end-start : .2f} seconds")

    mid = num//2
    
    t1 = Thread(target=calculate, args=(0,mid))
    t2 = Thread(target=calculate, args=(mid,num))
    
    start = time()
    t1.start()
    t2.start()

    t1.join()
    t2.join()   
    end = time()
    print(f"Time taken while using parallely:{end-start : .2f} seconds")


#using process to do the heavy calculation parallely it takes significantly less time than using threads
    t1 = Process(target=calculate, args=(0,mid))
    t2 = Process(target=calculate, args=(mid,num))
    
    start = time()
    t1.start()
    t2.start()

    t1.join()
    t2.join()   
    end = time()
    print(f"Time taken while using parallely:{end-start : .2f} seconds")