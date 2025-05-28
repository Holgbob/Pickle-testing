def get_test_data():
    """
    Gets all data from different os, python versions
    and protocols and save in data_obj variable.
    """

    data_obj = {}
    # Get data from file.
    with open("./PickleDataFolder/data", 'r') as f:
        for data in f:
            # Get different information by split.
            data = data.split(',')
            test_name = data[1]
            os_and_version = f"{data[2]},{data[3]}"
            if test_name in data_obj:
                # If key exist.
                if data[4] in data_obj[test_name]:
                    # If protocol exist's then add data there.
                    data_obj[test_name][data[4]][os_and_version] = data[0]
                else:
                    # If protocol does not exist's then create that key then add data there.
                    data_obj[test_name][data[4]] = {}
                    data_obj[test_name][data[4]][os_and_version] = data[0]
            else:
                # If key does not exist.
                data_obj[test_name] = {}
                data_obj[test_name][data[4]] = {}
                data_obj[test_name][data[4]][os_and_version] = data[0]

    return data_obj
    

def test_pickle(data_obj):
    failed_tests = {}

    # Go through every test case, protocol and operatingsystem/version
    for test_case, value in data_obj.items():
        for protocol, protocol_data in value.items():
            for os_and_version, data in protocol_data.items():
                    
                # Check different operatingsystem and python versions against eachother
                for os_and_version_2, data_2 in protocol_data.items():
                    if os_and_version == os_and_version_2: continue # Don't check same hash
                    # If not the same, add it to failed_tests
                    if data != data_2:
                            if test_case in failed_tests:
                                if not "Os or Version" in failed_tests[test_case]:
                                    failed_tests[test_case].append("Os or Version")
                            else:
                                failed_tests[test_case] = ["Os or Version"]

                # Check protocols against eachother
                for protocol_2, protocol_data_2 in value.items():
                    for os_and_version_2, data_2 in protocol_data_2.items():
                        # Only check same operating system but not same protocol
                        if not os_and_version != os_and_version_2 or protocol == protocol_2: continue
                        # If not the same, add it to failed_tests
                        if data != data_2:
                            if test_case in failed_tests:
                                if not "protocol" in failed_tests[test_case]:
                                    failed_tests[test_case].append("protocol")
                            else:
                                failed_tests[test_case] = ["protocol"]

    # Print out what test that failed 
    # and why (Only 'operatingsystem/version' and 'protocol' are possible errors)
    for test, errors in failed_tests.items():
        print(f"Test: {test}: Failed with:")
        for error in errors:
            print(f"Fail: {error}")
        print("\n")


if __name__ == '__main__':
    data_obj = get_test_data()
    test_pickle(data_obj)    