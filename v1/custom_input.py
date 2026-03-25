def main():
    print("Please send a message to the Redis stream, 'exit' or 'q' ends the program")

    while True:
        try:
            user_in = input()
            if "exit" in user_in:
                print("Ending....")
                break
            else:
                print(user_in)

        except KeyboardInterrupt:
            print()
            print("The program was interputed..")
            break


if __name__ == "__main__":
    main()
