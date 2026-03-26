# import argparse
import sys
import subprocess
import redis
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "producer",
    help="Use random_log.py/custom_input.py/random_message.py",
)
parser.add_argument("-s", "--stream", required=True, help="Redis stream name")
parser.add_argument("--host", default="localhost", help="[OPTIONAL] Redis server ")
parser.add_argument(
    "--port", default=6379, type=int, help="[OPTIONAL] Redis server port"
)

args = parser.parse_args()

r = redis.Redis(host=args.host, port=args.port, db=0)

try:
    with subprocess.Popen(
        args=[sys.executable, "-u", args.producer],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    ) as proc:
        for line in proc.stdout:  # type: ignore
            line = line.rstrip("\n")

            print(line)

            r.xadd(args.stream, {"data": line})

except KeyboardInterrupt:
    print()
    print("You stopped producer")


print("The producer has exited")
# https://realpython.com/python-subprocess/
# https://stackoverflow.com/questions/230751/how-can-i-flush-the-output-of-the-print-function
# https://docs.python.org/3/library/subprocess.html#subprocess.Popen
