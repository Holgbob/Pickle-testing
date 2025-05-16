import unittest
import pickle
import sys
import hashlib
import os


current_os = sys.platform
info = sys.version_info
current_version = f"{info[0]}.{info[1]}"
file_path = "./PickleDataFolder"
python_version = [3.6, 3.7, 3.8, 3.9, 3.11]
os_arr = ["win32", "linux", "darwin"]

class Test_pickle(unittest.TestCase):
    def test_pickle(self):
        # Go through every test case
        for test_case, value in data_obj.items():
            # Check all diffrent versions/os against eachother
            for os_and_version, data in value.items():
                for os_and_version_2, data_2 in value.items():
                    if os_and_version == os_and_version_2: continue
                    print(os_and_version)
                    self.assertEqual(data, data_2, msg=f"Mismatch in test case '{test_case}' between '{os_and_version}' and '{os_and_version_2}")

if __name__ == '__main__':
    data_obj = {}
    
    for (root,dirs,files) in os.walk(file_path):
        for file in files:
            file_prop = file.split(',')
            if (len(file_prop) < 2): continue
            test_name = file_prop[0]
            os_and_version = f"{file_prop[1]},{file_prop[2]}"
            if test_name in data_obj:
                # Lägger till i den key
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    data_obj[test_name][os_and_version] = f.read()
            else:
                # Skapa key och lägg till
                data_obj[test_name] = {}

                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    data_obj[test_name][os_and_version] = f.read()

            data_obj[file.split(',')[0]]

    print(data_obj)
    unittest.main()