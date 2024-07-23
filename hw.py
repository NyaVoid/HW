x = 0
class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('step cannot be zero')
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        global x
        if ((self.stop - self.start) > 0 and self.step > 0) or ((self.stop - self.start) < 0 and self.step < 0):
            if x == 0:
                x += 1
                return self.pointer
        if (self.stop - self.start) > 0 and self.step > 0:
            if self.stop <= self.pointer:
                x = 0
                raise StopIteration
            self.pointer += self.step
            return self.pointer
        elif (self.stop - self.start) < 0 and self.step < 0:
            if self.stop >= self.pointer:
                x = 0
                raise StopIteration
            self.pointer += self.step
            return self.pointer
        else:
            raise StopIteration


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')