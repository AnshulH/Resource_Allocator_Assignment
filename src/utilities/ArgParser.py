import argparse


def cli_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('--units', action='store', type=int, help="Number of units required (Multiples of 10)")
    parser.add_argument('--hours', action='store', type=int, help="Number of hours the units are required for")
    all_args = parser.parse_args()
    args_dict = {
        'units': all_args.units,
        'hours': all_args.hours
    }
    return args_dict
