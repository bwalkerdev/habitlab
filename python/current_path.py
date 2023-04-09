import os
import csv


def main():
    current_directory = os.getcwd()
    storage_path = os.path.expanduser("~") + "\documents\HabitLab"
    storage_path_exists = os.path.exists(storage_path)
    storage_csv_path = storage_path + "\storage.csv"
    storage_csv_exists = os.path.exists(storage_csv_path)
    print(current_directory, storage_path, storage_path_exists)

    if not storage_path_exists:
        os.mkdir(storage_path)
    if not storage_csv_exists:
        with open(storage_csv_path, "w") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "time", "url", "time_spent"])


if __name__ == "__main__":
    main()

# input("Press the any key: ")
