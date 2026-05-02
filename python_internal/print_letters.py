# Thread is the smallest unit of execution,by default,your python program runs on one thread
import threading

def print_numbers():
    for i in range(5):
        print(f"Number:{i}")

def print_letters():
    for c in ['a','b','c','d','e']:
        print(f"Letters:{c}")


t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done")
