import argparse
from redis import ConnectionPool, Redis

parser = argparse.ArgumentParser()
parser.add_argument(
    "-b",
    "--beginning",
    help="Prints the stream from the beginning",
    action="store_true",
)
parser.add_argument("--host", help="[OPTIONAL] Host name of the Redis Server")
parser.add_argument(
    "--port", help="[OPTIONAL] Port in which the Redis Server is running"
)
parser.add_argument(
    "--stream", help="Stream id to which you want to subscribe", required=True
)
args = parser.parse_args()

host = args.host or "localhost"
port = args.port or 6379

if args.beginning:
    print(
        f"The stream is beginning from first with the Redis instance running in {host}:{port}"
    )
    start_id = "0"
else:
    print(f"The stream is continuing with the Redis instance running in {host}:{port}")
    start_id = "$"


pool = ConnectionPool(
    host=host,
    port=port,
    db=0,
)

r = Redis(connection_pool=pool)

while True:
    try:
        messages = r.xread(
            streams={args.stream: start_id},
            block=0,
        )

        if not messages:
            continue

        for stream_name, entries in messages:
            for message_id, fields in entries:
                print(fields.get("data"))
                start_id = message_id

    except KeyboardInterrupt:
        print("Log streaming Ended")
        break

# https://redis.io/docs/latest/commands/xread/
