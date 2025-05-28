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
        failed_tests = {}

        # Go through every test case
        for test_case, value in data_obj.items():
            # Check all diffrent versions/os against eachother
            for protocol, protocol_data in value.items():
                for os_and_version, data in protocol_data.items():
                    failed = False
                    for os_and_version_2, data_2 in protocol_data.items():
                        if os_and_version == os_and_version_2: continue
                        # Add sub test so the dynamicly added test shows (otherwise it will only say 'Ran 1 test')
                        # with self.subTest(test_case=test_case, from_os=os_and_version, protocol_in_use=protocol, to_os=os_and_version_2):
                        if not data == data_2:
                                if test_case in failed_tests:
                                    if not "Os or Version" in failed_tests[test_case]:
                                        failed_tests[test_case].append("Os or Version")
                                else:
                                    failed_tests[test_case] = ["Os or Version"]

                            # self.assertEqual(
                            #     data, data_2,
                            #     msg=f"Mismatch in test case '{test_case}' between '{os_and_version}' and '{os_and_version_2}'"
                            # )
                # Check protocols against eachother
                    for protocol_2, protocol_data_2 in value.items():
                        for os_and_version_2, data_2 in protocol_data_2.items():
                            if os_and_version != os_and_version_2 or protocol == protocol_2: continue
                            # Add sub test so the dynamicly added test shows (otherwise it will only say 'Ran 1 test')
                            # with self.subTest(test_case=test_case, from_os=os_and_version, from_protocol=protocol, to_os=os_and_version_2, to_protocol=protocol_2):
                            if not data == data_2:
                                if test_case in failed_tests:
                                    if not "protocol" in failed_tests[test_case]:
                                        failed_tests[test_case].append("protocol")
                                else:
                                    failed_tests[test_case] = ["protocol"]

                                # self.assertEqual(
                                #     data, data_2,
                                #     msg=f"Mismatch in test case '{test_case}' between '{os_and_version}' and '{os_and_version_2}'"
                                # )

        for test, errors in failed_tests.items():
            print(f"Test: {test}: Failed with:")
            for error in errors:
                print(f"Fail: {error}")


if __name__ == '__main__':
    data_obj = {}

    with open("./PickleDataFolder/data", 'r') as f:
        for data in f:
            data = data.split(',')
            test_name = data[1]
            os_and_version = f"{data[2]},{data[3]}"
            if test_name in data_obj:
                # Lägger till i den key
                if data[4] in data_obj[test_name]:
                    data_obj[test_name][data[4]][os_and_version] = data[0]
                else:
                    data_obj[test_name][data[4]] = {}
                    data_obj[test_name][data[4]][os_and_version] = data[0]
            else:
                # Skapa key och lägg till
                data_obj[test_name] = {}
                data_obj[test_name][data[4]] = {}
                data_obj[test_name][data[4]][os_and_version] = data[0]

    # Run every test
    unittest.main()