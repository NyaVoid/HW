import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'w+') as f:
        all_data.append(f.readline())
        f.close()


filenames = [f'./file {number}.txt' for number in range(1, 5)]

time_s = time.time()
for i in filenames:
    read_info(i)
time_done = time.time() - time_s
print(f'линейный вызов: {time_done}')

if __name__ == '__main__':
    time_s1 = time.time()
    with Pool(process=4) as p:
        p.map(read_info, filenames)
    time_done1 = time.time() - time_s1
    print(f'многопроцессный вызов: {time_done1}')
