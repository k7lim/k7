import random
import sys

def randbit():
    return random.randrange(2)
    
def randbit_to_int():
    bit1 = randbit()
    bit2 = randbit()
    
    while bit1 == 0 and bit2 == 0:
        bit1 = randbit()
        bit2 = randbit()
    
    bitstr = str(bit1) + str(bit2)
    return int(bitstr, 2)
    
    
if __name__ == "__main__":
    trials = 500000
    results = {}
    for i in range(trials):
        curr = randbit_to_int()
        if curr not in results:
            results[curr] = 1
        else:
            results[curr] = results[curr] + 1
        
    print results
    print "expected val: " + str(trials/3.0)