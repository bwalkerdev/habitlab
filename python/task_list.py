import os
import csv
import sys


def read_and_return(path):
    with open(path, "r") as f:
        reader = csv.reader(f)
        csv_f = list(reader)
        arr = []
        for row in csv_f:
            for text in row:
                arr.append(text)
        return arr


def write_to_csv(path, string):
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([string])
    return read_and_return(path)


def remove_from_csv(path, string):
    csv_list = []
    with open(path, "r") as f:
        reader = csv.reader(f)
        csv_list = list(reader)
        csv_list = csv_list.remove([string])
    with open(path, "w") as f:
        f.truncate()
        if csv_list:
            f.write(csv_list)
    return read_and_return(path)


def main(operation, *args):
    # current_directory = os.getcwd()
    storage_path = os.path.expanduser("~") + "\documents\HabitLab"
    storage_path_exists = os.path.exists(storage_path)
    storage_csv_path = storage_path + "/task-list.csv"
    storage_csv_exists = os.path.exists(storage_csv_path)

    # Create file and directory if they don't exist
    if not storage_path_exists:
        os.mkdir(storage_path)

    # Perform Operation
    match operation:
        case "get":
            return read_and_return(storage_csv_path)
        case "add":
            return write_to_csv(storage_csv_path, args)
        case "remove":
            return remove_from_csv(storage_csv_path, args)


# main(sys.argv[1], sys.argv[2:])

if __name__ == "__main__":
    print(main("get"))

# input("Press the any key: ")
