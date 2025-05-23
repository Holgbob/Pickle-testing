import pickle
import math
import hashlib
import sys
import random

system_os = sys.platform
info = sys.version_info
python_version = f"{info[0]}.{info[1]}"
data_folder = "./PickleDataFolder/"
file_path = f"{system_os},{python_version}.txt"

def hash_object(obj):
    return hashlib.sha256(pickle.dumps(obj)).hexdigest()

# Test function
def function_object():
    x = 1 + 1
    y = 5 + 5
    x += y
    return x

# Test class
class Class_object:
    pass

# Create a custom object to test get state pickling
class CustomObject:
    def __init__(self, data):
        self.data = data

    def __getstate__(self):
        return {'data': self.data}

# Returns the given list as a max_depth recursive list
def recursive_lst_helper(lst, max_depth=20, depth=1):
    if depth >= max_depth:
        return lst
    return [recursive_lst_helper(lst, depth=depth+1, max_depth=max_depth)]

# returns a string n long
def string_helper(n):
    string = ""
    for _ in range(0, n):
        string += chr(random.randint(32,126))
    return string

def pickle_and_save(obj, test_name):
    '''
    Pickles, hashes and saves the passed objects into
    a specific folder. Name of the files represents 
    what test, version and os that was used. 
    '''
    with open(f"{data_folder}data", 'a') as f:
        data = hash_object(pickle.dumps(obj))
        data += f",{test_name},{file_path}\n"
        f.write(data)


if __name__ == '__main__':
    
    ########## Class and function ##########
    random.seed(10)

    # Create files for class object
    test_class = Class_object()
    test_class.x = 1
    test_class.y = 2
    pickle_and_save(test_class, "test_class")
    
    # Create files for function object   
    pickle_and_save(function_object, "test_def") 

    ########## Different data-structures ##########

    # Create files for lists
    lst = []
    lst = recursive_lst_helper(lst, 30)
    pickle_and_save(lst, "test_list") 

    # Create files for dicts
    test_dict = {"Test": "Dict", "Number": 129}
    pickle_and_save(test_dict, "test_dict") 

    # Create files for sets
    test_set = {"Test", "Set", False, 10002}
    pickle_and_save(test_set, "test_set") 
    
    # Create files for tuples
    test_tuple = (1, 100, 5, 56, 99)
    pickle_and_save(test_tuple, "test_tuple") 

    ########## Extensive numbers ##########

    # Create files for floats
    test_float = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566
    pickle_and_save(test_float, "test_floating") 
        
    # Create files for complex
    complex_number = 102 + 56j
    pickle_and_save(complex_number, "test_complex") 

    # Test long (Over 2**63 to guarantee it's more than a simple integeer, i.e independent on system architecture 32 and 64)
    test_long = 2**70
    pickle_and_save(test_long, "test_long")

    ########## Bytes ##########

    # Create files for bytes
    test_byte = bytes("Testing bytes. Hopefully no problems!", 'utf-8')
    pickle_and_save(test_byte, "test_byte") 
    
    # Create files for byte arrays
    lst = [0, 63, 129, 245]
    test_byte_array = bytearray(lst)
    pickle_and_save(test_byte_array, "test_bytearray") 

    ########## Boundary ##########

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
    zero = 0
    pickle_and_save(zero, "test_boundary_zero") 
        
    # Create files for negative zero
    negative_zero = -0.0
    pickle_and_save(negative_zero, "test_boundary_negative_zero") 

    ########## String values ##########
    
    # Create files for string
    test_string = string_helper(500)
    pickle_and_save(test_string, "test_string") 

    # Create files for empty string
    test_empty_string = ""
    pickle_and_save(test_empty_string, "test_empty_string") 
    
    ########## Booleans ##########

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

    ########## get_state ##########

    # Test get state
    obj = CustomObject([500, 99, 10002])
    pickle_and_save(obj, "test_get_state")

    # Test big number
    big_number = 2**64
    pickle_and_save(big_number, "test_big_number")

    ########## Unicode ##########

    # Test unicode
    unicode_char = chr(0x10FCFF)
    pickle_and_save(unicode_char, "test_unicode")