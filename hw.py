import threading
import time

x = 0
threads = threading.Thread(None)
y = 0
def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(word_count):
            f.write(f'Какое-то слово № {i+1}\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

def run_something(word_count, file_name):
    t = threading.Thread(target=write_words, args=(word_count, file_name))
    t.start()


start_time = time.time()
run_something(10, 'exemple5.txt')
run_something(30, 'exemple6.txt')
run_something(200, 'exemple7.txt')
run_something(100, 'exemple8.txt')
while threading.active_count() != 1:
    time.sleep(1)
    pass

end_time = time.time()
print(f'Работа потоков: {end_time - start_time}')
