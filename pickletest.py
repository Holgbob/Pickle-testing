import pickle
import math
import hashlib
import unittest
import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

system_os = sys.platform
info = sys.version_info
python_version = f"{info[0]}.{info[1]}"
data_folder = "./PickleDataFolder"
file_path = f"{data_folder}/{system_os},{python_version}.txt"

def hash_object(obj):
    return hashlib.sha256(pickle.dumps(obj)).hexdigest()

class TestClass(unittest.TestCase):
    class B:
        pass

    def test_pickle_same_objects(self):
        first = self.B()
        first.x = 1
        first.y = 2

        with open(f"test_pickle_self_class,{file_path}", 'w') as f:
            data = hash_object(pickle.dumps(first))
            f.write(data)

    def test_unpickle_same_objects(self):
        first = self.B()
        first.x = 1
        first.y = 2

        with open(f"test_unpickle_self_class,{file_path}", 'w') as f:
            data = hash_object(pickle.dumps(first))
            f.write(data)

class TestRecursive(unittest.TestCase):
    def test_list(self):
        lst = []
        lst.append(lst)

        with open(f"test_list,{file_path}", 'w') as f:
            data = hash_object(pickle.dumps(lst))
            f.write(data)

class TestFloating(unittest.TestCase):
    def test_floating(self):
        first_float = 0.25

        with open(f"test_floating,{file_path}", 'w') as f:
            data = hash_object(pickle.dumps(first_float))
            f.write(data)
        
    def test_floating_add(self):
        third_float = 0.25 + 0.25
        with open(f"test_floating_add,{file_path}", 'w') as f:
            data = hash_object(pickle.dumps(third_float))
            f.write(data)

class TestBoundary(unittest.TestCase):
    def test_boundary_nan(self):
        nan = math.nan
        x = nan
        with open(f"test_boundary_nan,{file_path}", 'w') as f:
            data = hash_object(pickle.dumps(x))
            f.write(data)

    def test_boundary_inf(self):
        inf = math.inf

        with open(f"test_boundary_inf,{file_path}", 'w') as f:
            data = hash_object(pickle.dumps(inf))
            f.write(data)

    def test_boundary_neg_inf(self):
        negative_inf = -(float("inf"))

        with open(f"test_boundary_neg_inf,{file_path}", 'w') as f:
            data = hash_object(pickle.dumps(negative_inf))
            f.write(data)

    def test_boundary_zero(self):
        zero = 0.0

        with open(f"test_boundary_zero,{file_path}", 'w') as f:
            data = hash_object(pickle.dumps(zero))
            f.write(data)
        
    def test_boundary_negative_zero(self):
        negative_zero = -0.0

        with open(f"test_boundary_negative_zero,{file_path}", 'w') as f:
            data = hash_object(pickle.dumps(negative_zero))
            f.write(data)

class Test_string_values(unittest.TestCase):
    def test_string(self):
        string1 = "iaujwfhauyhfga nmcsjlkmnciauHBWYud nbwaidj nmjudiahw8yduahiuwdjanwmoiujdxc hniydwgcdswb"


        with open(f"test_string,{file_path}", 'w') as f:
            data = hash_object(pickle.dumps(string1))
            f.write(data)
    
    def test_empty_string(self):
        string1 = ""

        with open(f"test_empty_string,{file_path}", 'w') as f:
            data = hash_object(pickle.dumps(string1))
            f.write(data)
    
    def test_string_dict(self):
        dict1 = {"test1": "ett", "number": 1}

        with open(f"test_string_dict,{file_path}", 'w') as f:
            data = hash_object(pickle.dumps(dict1))
            f.write(data)

    def test_set(self):
        set1 = {"uh", "uhh", "uhhh"}
        
        with open(f"test_set,{file_path}", 'w') as f:
            data = hash_object(pickle.dumps(set1))
            f.write(data)

if __name__ == '__main__':
    # unit test start
    unittest.main()