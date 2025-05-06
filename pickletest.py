import pickle
import math
import hashlib

class B:
    def __init__(self):
        self.x = None
        self.y = None

def hash_object(obj):
    return hashlib.sha256(pickle.dumps(obj)).hexdigest()


def class_test():

    print("testing class")

    x = B()
    x.x = 1
    x.y = 2

    c = B()
    c.y = 2
    c.x = 1

    print("x = ", hash_object(pickle.dumps(x)))
    print("Y = ", hash_object(pickle.dumps(c)))

def recursive_test():

    print("testing recursive list")

    lst1 = []
    lst1.append(lst1)

    lst2 = []
    lst2.append(lst2)

    print("lst1 = ", hash_object(pickle.dumps(lst1)))
    print("lst2 = ", hash_object(pickle.dumps(lst2)))

def boundry_test():

    def testxy():
        print("x = ", hash_object(pickle.dumps(x)))
        print("y = ", hash_object(pickle.dumps(y)))
    
    nan = math.nan
    inf = math.inf
    negative_inf = -(float("inf"))
    zero = 0.0
    negative_zero = -0.0

    print("testing nan")
    x = nan
    y = nan
    testxy()
    
    print("testing inf")
    x = inf
    y = inf
    testxy()

    print("testing negative inf")
    x = negative_inf
    y = negative_inf
    testxy()

    print("testing zero")
    x = zero
    y = zero
    testxy()

    print("testing negative zero")
    x = negative_zero
    y = negative_zero
    testxy()

if __name__ == "__main__":
    class_test()
    print("--------------------------------------")
    recursive_test()
    print("--------------------------------------")
    boundry_test()
    print("--------------------------------------")

    