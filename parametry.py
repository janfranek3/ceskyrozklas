import argparse

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

parser.add_argument('--source_file')           # positional argument
parser.add_argument('--output_file')      # option that takes a value
parser.add_argument('--otype')      # option that takes a value

args = parser.parse_args()



print(args.source_file)
print(args.output_file)

config = vars(args)

#python parametry.py --source_file="Ahoj" --output_file="test"