import pickle
import math
import hashlib
import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

system_os = sys.platform
info = sys.version_info
python_version = f"{info[0]}.{info[1]}"
data_folder = "./PickleDataFolder/"
file_path = f"{system_os},{python_version}.txt"

def hash_object(obj):
    return hashlib.sha256(pickle.dumps(obj)).hexdigest()

def function_object():
        x = 1 + 1
        y = 5 + 5
        x += y
        return x

class Test_class:
        pass

def pickle_and_save(obj, test_name):
    with open(f"{data_folder}{test_name},{file_path}", 'w') as f:
        data = hash_object(pickle.dumps(obj))
        f.write(data)

# Create a custom object to test get state pickling
class CustomObject:
    def __init__(self, data):
        self.data = data

    def __getstate__(self):
        return {'data': self.data}

if __name__ == '__main__':
    
    ##### Class and function #####

    # Create files for class object
    test_class = Test_class()
    test_class.x = 1
    test_class.y = 2
    pickle_and_save(test_class, "test_class")
    
    # Create files for function object   
    pickle_and_save(function_object, "test_def") 

    ##### Different data-structures #####

    # Create files for lists
    lst = []
    lst.append(lst)
    pickle_and_save(lst, "test_list") 

    # Create files for dicts
    test_dict = {"test1": "ett", "number": 1}
    pickle_and_save(test_dict, "test_dict") 

    # Create files for sets
    test_set = {"uh", "uhh", "uhhh"}
    pickle_and_save(test_set, "test_set") 
    
    # Create files for tuples
    test_tuple = (1, 2, 3, 4, 5)
    pickle_and_save(test_tuple, "test_tuple") 

    ##### Extensive numbers #####

    # Create files for floats
    test_float = 0.151515615651611565142112515212518945182958918259128590859018590287509128795012785901287509187250981802514642356312341424141242414124141241414124141241241512562153156123713712312
    pickle_and_save(test_float, "test_floating") 
        
    # Create files for complex
    complex_number = 7 + 2j
    pickle_and_save(complex_number, "test_complex") 

    ##### Bytes #####

    # Create files for bytes
    test_byte = bytes()
    pickle_and_save(test_byte, "test_byte") 
    
    # Create files for byte arrays
    lst = [0, 1, 2, 3]
    test_byte_array = bytearray(lst)
    pickle_and_save(test_byte_array, "test_bytearray") 

    ##### Boundary #####

    # Create files for nan
    nan = math.nan
    x = nan
    pickle_and_save(x, "test_boundary_nan") 

    # Create files for inf
    inf = math.inf
    pickle_and_save(inf, "test_boundary_inf") 

    # Create files for negative inf
    negative_inf = -(float("inf"))
    pickle_and_save(negative_inf, "test_boundary_neg_inf") 

    # Create files for zero
    zero = 0.0
    pickle_and_save(zero, "test_boundary_zero") 
        
    # Create files for negative zero
    negative_zero = -0.0
    pickle_and_save(negative_zero, "test_boundary_negative_zero") 

    ##### String values #####
    
    # Create files for string
    test_string = "iaujwfhauyhfga nmcsjlkmnciauHBWYud nbwaidj nmjudiahw8yduahiuwdjanwmoiujdxc hniydwgcdswb"
    pickle_and_save(test_string, "test_string") 

    # Create files for empty string
    test_empty_string = ""
    pickle_and_save(test_empty_string, "test_empty_string") 
    
    ##### Booleans #####

    # Create files for none
    none_value = None
    pickle_and_save(none_value, "test_none") 

    # Create files for true
    true_value = True
    pickle_and_save(true_value, "test_true") 

    # Create files for false
    false_value = False
    pickle_and_save(false_value, "test_false") 

    # Create files for ellipsis
    ellipsis_value = ...
    pickle_and_save(ellipsis_value, "test_ellipsis")

    ##### get_state #####

    # Test get state
    obj = CustomObject([1, 2, 3])
    pickle_and_save(obj, "test_get_state")