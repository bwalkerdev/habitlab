import datetime


def main():
    now = datetime.datetime.now()
    now = now.hour
    if now < 12:
        print("Good Morning")
    elif now < 18:
        print("Good Afternoon")
    else:
        print("Good Evening")


if __name__ == "__main__":
    main()

# input("Press the any key: ")
