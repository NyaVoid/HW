import time
import multiprocessing as mp
def read_info(name):
    all_data = []
    with open(name, 'w+') as f:
        all_data.append(f.readline())
        f.close()
        
filenames = [f'./file {number}.txt' for number in range(1, 5)]

time_s1 = time.time()
for i in filenames:
    mp.Process(target=read_info, args=(i,)).start()
time_done1 = time.time() - time_s1
print(f'многопроцессный вызов: {time_done1}')

time_s = time.time()
for i in filenames:
    read_info(i)
time_done = time.time() - time_s
print(f'линейный вызов: {time_done}')

