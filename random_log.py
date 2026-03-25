import logging
import random
import time

logger = logging.getLogger(name=__name__)


def main():
    random_time = random.randint(30, 45)
    logging.basicConfig(level=logging.INFO, format="%(message)s %(asctime)s")
    print(f"Logs will print for {random_time} seconds")
    print()
    try:
        for _ in range(random_time):
            logger.info("This log was printed at :")
            time.sleep(1)
    except KeyboardInterrupt:
        print()
        print("The Program was interrupted!")


if __name__ == "__main__":
    main()

# https://docs.python.org/3/library/logging.html
