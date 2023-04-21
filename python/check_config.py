import os
import json

schema = {
    "categories": [],
    "metadata": {
        "modified": {"date": "1970-01-01", "time": "00:00:00.000000"},
        "streak": 1,
    },
}


def main():
    # current_directory = os.getcwd()
    storage_path = os.path.join(os.path.expanduser("~"), "documents", "HabitLab")
    storage_path_exists = os.path.exists(storage_path)
    storage_json_path = os.path.join(storage_path, "config.json")
    storage_json_exists = os.path.exists(storage_json_path)
    created_path = False
    created_json = False

    # Create file and directory if they don't exist
    if not storage_path_exists:
        os.mkdir(storage_path)
        created_path = True
    if not storage_json_exists:
        with open(storage_json_path, "w") as f:
            json.dump(schema, f, indent=4)
        created_json = True
    genesis = (created_path, created_json)
    match genesis:
        case (True, True):
            print("Created directory and JSON at " + storage_json_path)
        case (False, True):
            print("Created JSON at " + storage_json_path)
        case (False, False):
            print("JSON already exists at " + storage_json_path)


if __name__ == "__main__":
    main()
