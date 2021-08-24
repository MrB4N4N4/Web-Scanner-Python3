import argparse

parser = argparse.ArgumentParser(description="you can use localhost as 127.0.0.1",
                                 usage="scanner -sN 127.0.0.1 | scanner -sP 127.0.0.30")
parser.add_argument("-sN", "--scanNetwork", metavar="",
                    help="scan Network. Put host's bandwidth")
parser.add_argument("-sP", "--scanPort", metavar="",
                    help="scan opened ports of Host. Put host's address")
