import pickle
import math
import hashlib
import unittest

def hash_object(obj):
    return hashlib.sha256(pickle.dumps(obj)).hexdigest()

class TestClass(unittest.TestCase):
    class B:
        def __init__(self):
            self.x = None
            self.y = None

    def test_pickle_same_objects(self):
        first = self.B()
        first.x = 1
        first.y = 2

        second = self.B()
        second.y = 2
        second.x = 1
        self.assertEqual(hash_object(pickle.dumps(first)), hash_object(pickle.dumps(second)))

    def test_unpickle_same_objects(self):
        first = self.B()
        first.x = 1
        first.y = 2

        second = self.B()
        second.y = 2
        second.x = 1
        pickled_first = pickle.dumps(first)
        pickled_second = pickle.dumps(second)
        self.assertEqual(hash_object(pickle.loads(pickled_first)), hash_object(pickle.loads(pickled_second)))
    

class TestRecursive(unittest.TestCase):
    def test_list(self):
        lst1 = []
        lst1.append(lst1)

        lst2 = []
        lst2.append(lst2)
        self.assertEqual(hash_object(pickle.dumps(lst1)), hash_object(pickle.dumps(lst1)))

class TestFloating(unittest.TestCase):
    def test_floating(self):
        first_float = 0.25
        expected_hash = hash_object(pickle.dumps(first_float))
        for _ in range(100):
            current_hash = hash_object(pickle.dumps(first_float))
            self.assertEqual(current_hash, expected_hash)
        
    def test_floating_add(self):
        third_float = 0.25 + 0.25
        fourth_float = 0.25 + 0.25
        self.assertEqual(hash_object(pickle.dumps(third_float)), hash_object(pickle.dumps(fourth_float)))


class TestBoundary(unittest.TestCase):
    def test_boundary_nan(self):
        nan = math.nan
        x = nan
        y = nan
        self.assertEqual(hash_object(pickle.dumps(x)), hash_object(pickle.dumps(y)))

    def test_boundary_inf(self):
        inf = math.inf
        x = inf
        y = inf
        self.assertEqual(hash_object(pickle.dumps(x)), hash_object(pickle.dumps(y)))

    def test_boundary_neg_inf(self):
        negative_inf = -(float("inf"))
        x = negative_inf
        y = negative_inf
        self.assertEqual(hash_object(pickle.dumps(x)), hash_object(pickle.dumps(y)))

    def test_boundary_zero(self):
        zero = 0.0
        x = zero
        y = zero
        self.assertEqual(hash_object(pickle.dumps(x)), hash_object(pickle.dumps(y)))
        
    def test_boundary_negative_zero(self):
        negative_zero = -0.0
        x = negative_zero
        y = negative_zero
        self.assertEqual(hash_object(pickle.dumps(x)), hash_object(pickle.dumps(y)))


if __name__ == '__main__':
    unittest.main()