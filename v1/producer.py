import argparse
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument(
    "producer",
    help="Use the logproducer.py/customproducer.py to produce logs",
)

args = parser.parse_args()

producer = args.producer
print(producer)


# https://realpython.com/python-subprocess/
# https://stackoverflow.com/questions/230751/how-can-i-flush-the-output-of-the-print-function
