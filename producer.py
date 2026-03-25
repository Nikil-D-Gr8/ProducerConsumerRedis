import argparse
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument(
    "producer",
    help="Use the logproducer.py/customproducer.py to produce logs",
)

args = parser.parse_args()

producer = args.producer

try:
    subprocess.run(
        [],
        check=True,
        shell=True,
    )
except subprocess.CalledProcessError as exc:
    print(
        f"Process failed because it did not return a successful return code. "
        f"Returned {exc.returncode}\n{exc}"
    )


# https://realpython.com/python-subprocess/
# https://stackoverflow.com/questions/230751/how-can-i-flush-the-output-of-the-print-function
