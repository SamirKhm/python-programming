import threading
import time

def worker(num):
    print(f"Thread {num}: starting")
    time.sleep(2)  # simulate some work
    print(f"Thread {num}: finishing")

threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()  # Corrected this line

for thread in threads:
    thread.join()  # wait for all threads to finish

print("All threads completed")  # Moved this line outside the loop
