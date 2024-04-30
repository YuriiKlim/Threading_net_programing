import queue
import threading
import time
import multiprocessing as mp


def print_info(info):
    print(info)


def sort_array(arr):
    print(sorted(arr))


t1 = threading.Thread(target=print_info, args=("Thread1",))
t2 = threading.Thread(target=sort_array, args=([2, 3, 1, 5, 4],))

t1.start()
t2.start()

t1.join()
t2.join()

####################################################################

def print_info(info):
    for _ in range(10):
        print(info)


def sort_array(arr):
    for _ in range(10):
        print(sorted(arr))


t1 = threading.Thread(target=print_info, args=("Thread1",))
t2 = threading.Thread(target=sort_array, args=([2, 3, 1, 5, 4],))

t1.start()
t2.start()

t1.join()
t2.join()

#########################################################################

global_list = []
lock = threading.Lock()


def append():
    for _ in range(100000):
        global global_list

        lock.acquire()
        global_list.append(1)
        lock.release()


def remove():
    for _ in range(100000):
        global global_list

        lock.acquire()
        global_list.pop()
        lock.release()


t1 = threading.Thread(target=append, args=())
t2 = threading.Thread(target=remove, args=())

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Final result {global_list}")

#################################################################

def worker(thread_num):
    global tasks

    while True:
        task = tasks.get()

        if task is None:
            break

        print(f"Thread №{thread_num} work with {task}\n", end='')
        tasks.task_done()
        time.sleep(0.5)


tasks = queue.Queue()
num_threads = 3

for i in range(10):
    tasks.put(f"Task {i+1}")

for _ in range(num_threads):
    tasks.put(None)

threads = []
for i in range(num_threads):
    t = threading.Thread(target=worker, args=(i+1,))
    t.start()
    threads.append(t)


for t in threads:
    t.join()

##################################################################

def print_info(info):
    for _ in range(10):
        print(info)
        time.sleep(0.5)


def sort_array(arr):
    for _ in range(10):
        print(sorted(arr))
        time.sleep(0.5)


if __name__ == "__main__":
    # mp.freeze_support() # for Windows

    print("Max number of processes", mp.cpu_count())

    p1 = mp.Process(target=print_info, args=("Process 1",))
    p2 = mp.Process(target=sort_array, args=([1, 3, 6, 5, 3, 2],))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

########################################################################

def mean(arr):
    summa = sum(arr)

    return summa / len(arr)


def get_parts(arr, num=mp.cpu_count()):
    n = len(arr)
    part_len = n // num

    return [arr[(part_len*k) : part_len*(k+1)] for k in range(num)]


def get_arr(len=100_000):
    return list(range(len))


if __name__ == '__main__':
    arr = get_arr()
    parts = get_parts(arr)

    with mp.Pool() as pool:
        results = pool.map(func=mean, iterable=parts)

    print(f"Results of pool {results}")

    print(f"Computed mean value {mean(results)}")
    print(f"Real mean value {mean(arr)}")