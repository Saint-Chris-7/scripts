import argparse 
import os 
import sys


#creating the parser object
my_parser = argparse.ArgumentParser(
    prog="List_dir",
    usage= "options path",
    description="List all the contents of a directory",
    epilog="Enjoy the program",
    prefix_chars="/"
    )

#create the arguments
my_parser.add_argument(
    "Path",
    metavar="path",
    type=str
)

args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print("The specified path does not exist")
    sys.exit()
print("\n".join(os.listdir(input_path)))

