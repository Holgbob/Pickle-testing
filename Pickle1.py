import unittest
import pickle
import sys
import hashlib
import os


current_os = sys.platform
info = sys.version_info
current_version = f"{info[0]}.{info[1]}"
file_path = "/PickleDataFolder"
python_version = [3.8, 3.9, 3.11]
os_arr = ["win32", "linux", "darwin"]

# def hash_object(obj):
#     return hashlib.sha256(pickle.dumps(obj)).hexdigest()

# class TestClass(unittest.TestCase):
#     class B:
#         pass

#     def test_pickle_same_objects(self):
#         first = self.B()
#         first.x = 1
#         first.y = 2

#         for os in os_arr:
#             for version in python_version:
#                 if current_version == version and os == current_os: continue

#                 with open(f"{file_path},test_pickle_same_objects", 'rb') as f:
#                     file_data = f.read()
#                     data = hash_object(pickle.dumps(first))
#                     self.assertEqual(file_data, data)

        

#     def test_unpickle_same_objects(self):
#         first = self.B()
#         first.x = 1
#         first.y = 2

#         with open(f"{file_path},test_unpickle_same_objects", 'wb') as f:
#             data = hash_object(pickle.dumps(first))
#             f.write(data)

class TestPickle(unittest.TestCase):
    def TestPickle(self):
        # Go through every test case
        for test_case, value in data_obj.items():

            # Check all diffrent versions/os against eachother
            for os_and_version, data in value.items():
                for os_and_version_2, data_2 in value.items():
                    if os_and_version == os_and_version_2: continue
                    self.assertEqual(data, data_2, msg=f"Mismatch in test case '{test_case}' between '{os_and_version}' and '{os_and_version_2}")

if __name__ == '__main__':
    data_obj = {}
    
    for (root,dirs,files) in os.walk(file_path):
        for file in files:
            file_prop = file.split(',')
            test_name = file_prop[2]
            version_and_os = f"{file_prop[0]},{file_prop[1]}"
            if test_name in data_obj:
                # Lägger till i den key
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    data_obj[test_name][version_and_os] = f.read()
            else:
                # Skapa key och lägg till
                data_obj[test_name] = {}

                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    data_obj[test_name][version_and_os] = f.read()

            data_obj[file.split(',')[2]]

            
    print(data_obj)
    unittest.main()