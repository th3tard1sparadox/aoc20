import time


time1 = time.time()
def func():
    input_f = open('input_1.1.txt', 'r')
    input_d = set(int(i) for i in input_f.read().split())

    for i in input_d:
        if 2020 - i in input_d:
            return i * (2020 - i)


print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
