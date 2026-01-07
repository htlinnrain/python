class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start
    
    def __iter__(self):
        return self  # Muss self zurückgeben!
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1  # 5,4,3,2,1,0

# Verwendung:
for num in Countdown(5):
    print(num)
# Ausgabe: 5 4 3 2 1 0



class FibIterator:
    def __init__(self):
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

class FibSequence:
    def __iter__(self):
        return FibIterator()

# Infinite Fibonacci – nimm nur die ersten 10:
fib_seq = FibSequence()
print([next(fib_seq) for _ in range(10)])
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
