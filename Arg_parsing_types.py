import argparse
import sys
import pytest

"""
def test_help():
    parser = argparse.ArgumentParser(description='Comparing Two files',prog = sys.argv[0])
    parser.add_argument("-n", type=str, required=True, help="Name of file1", conflict_handler='resolve')
    parser.parse_args(sys.argv[1:])

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
"""
parser = argparse.ArgumentParser(description='Comparing Two files',prog = sys.argv[0])
parser.add_argument("test string", type=str, required=True, help="Name of file1", conflict_handler='resolve')
parser.parse_args(sys.argv[1:])