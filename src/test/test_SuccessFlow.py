import json

# TODO: Fix this test 
def test_weight_value():
    expected_output = {'Output':
                           [{'region': 'New York', 'total_cost': 10150,
                             'machines': "[('8XLarge', 7), ('XLarge', 1), ('Large', 1)]"},
                            {'region': 'India', 'total_cost': 9520,
                             'machines': "[('8XLarge', 7), ('Large', 3)]"},
                            {'region': 'China', 'total_cost': 8570,
                             'machines': "[('8XLarge', 7), ('XLarge', 1), ('Large', 1)]"}]}


    import subprocess
    input_cmd = 'python3 ../main.py --units 1150 --hours 1'
    subprocess.run(input_cmd, shell=True)
    actual_output = None
    with open('../output.json') as json_file:
        actual_output = json.load(json_file)
    assert(actual_output == expected_output), "Output is incorrect!"
    print("Test Successful!!!")


if __name__ == "__main__":
    test_weight_value()
