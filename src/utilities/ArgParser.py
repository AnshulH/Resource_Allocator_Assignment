import argparse

# Method to specify the arguments from command line and parse them
def parse_args(args):
    parser = argparse.ArgumentParser()

    parser.add_argument('-u', '--units', type = int ,help = "Number of units required (Multiples of 10)")
    parser.add_argument('-t', '--hours', type = int ,help = "Number of hours the units are required for")

    return parser.parse_args()
