import argparse

des = [
    "example: webscanner -sN 127.0.0.1 --open",

]
parser = argparse.ArgumentParser(description="example: webscanner -sN 127.0.0.1 --open\n")
parser.add_argument("-sN", "--scanNetwork", help="scan ip address", action="store_true")

args = parser.parse_args()

print(args)
