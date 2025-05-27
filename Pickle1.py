import unittest
import sys
import os


current_os = sys.platform
info = sys.version_info
current_version = f"{info[0]}.{info[1]}"
file_path = "./PickleDataFolder"
python_version = [3.8, 3.9, 3.11]
os_arr = ["win32", "linux", "darwin"]

class Test_pickle(unittest.TestCase):
    def test_pickle(self):
        # Go through every test case
        for test_case, value in data_obj.items():
            # Check all diffrent versions/os against eachother
            for os_and_version, data in value.items():
                for os_and_version_2, data_2 in value.items():
                    if os_and_version == os_and_version_2: continue
                    # Add sub test so the dynamicly added test shows (otherwise it will only say 'Ran 1 test')
                    with self.subTest(test_case=test_case, from_os=os_and_version, to_os=os_and_version_2):
                        self.assertEqual(
                            data, data_2,
                            msg=f"Mismatch in test case '{test_case}' between '{os_and_version}' and '{os_and_version_2}'"
                        )

if __name__ == '__main__':
    data_obj = {}

    with open("./PickleDataFolder", 'r') as f:
        for data in f:
            data = data.split(',')
            test_name = data[1] + data[4]
            os_and_version = f"{data[2]},{data[3]},{data[4]}"
            if test_name in data_obj:
                # Lägger till i den key
                data_obj[test_name][os_and_version] = data[0]
            else:
                # Skapa key och lägg till
                data_obj[test_name] = {}
                data_obj[test_name][os_and_version] = data[0]

    # Run every test
    unittest.main()