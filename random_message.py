import random
import time
from datetime import datetime


def main():
    random_time = random.randint(30, 45)
    print(f"Hello there! Messages will print for {random_time} seconds")
    print()
    try:
        for _ in range(random_time):
            print(f"This message was printed at {datetime.now()}")
            time.sleep(1)
    except KeyboardInterrupt:
        print()
        print("The Program was interrupted!")
    print("Good bye!")


if __name__ == "__main__":
    main()
