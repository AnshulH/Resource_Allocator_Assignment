import json

# TODO: Fix this test 
def test_weight_value():
    expectedOutput = {'Output':
                           [{'region': 'New York', 'total_cost': 10150,
                             'machines': "[('8XLarge', 7), ('XLarge', 1), ('Large', 1)]"},
                            {'region': 'India', 'total_cost': 9520,
                             'machines': "[('8XLarge', 7), ('Large', 3)]"},
                            {'region': 'China', 'total_cost': 8570,
                             'machines': "[('8XLarge', 7), ('XLarge', 1), ('Large', 1)]"}]}


    import subprocess
    inputCmd = 'python3 ../main.py --units 1150 --hours 1'
    subprocess.run(inputCmd, shell=True)
    actualOutput = None
    with open('../output.json') as json_file:
        actualOutput = json.load(json_file)
    assert(actualOutput == expectedOutput), "Output is incorrect!"
    print("Test Successful!!!")


if __name__ == "__main__":
    test_weight_value()
