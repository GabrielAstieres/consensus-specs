import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--test_name', type=str, required=True, help='Test desired')
args = parser.parse_args()
test_name = args.test_name
