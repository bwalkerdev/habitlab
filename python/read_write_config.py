import os
import json
import sys
from datetime import date, datetime

# Example usage: c:/GitHub/habitlab/python/read_write_config.py add-category sleep "#8d46fa"


# Task Category Functions
def create_category(label, color):
    category = {"label": label, "color": color}
    return category


def append_category(label, color, config):
    if "categories" not in config:
        config["categories"] = []

    config["categories"].append(create_category(label, color))
    print(config)


def remove_category(label, config):
    for category in config["categories"]:
        if category["label"] == label:
            config["categories"].remove(category)
            break
    print(config)


# Date and Time Functions
def update_last_modified(config):
    build_meta_if_not_exists(config)
    config["metadata"]["lastModified"]["date"] = str(date.today())
    config["metadata"]["lastModified"]["time"] = str(datetime.now().time())


def build_meta_if_not_exists(config):
    if "metadata" not in config:
        config["metadata"] = {}
    if "lastModified" not in config["metadata"]:
        config["metadata"]["lastModified"] = {
            "date": str(date.today()),
            "time": str(datetime.now().time()),
        }
    if "streak" not in config["metadata"]:
        config["metadata"]["streak"] = 0


def check_streak(config):
    build_meta_if_not_exists(config)
    last_modified = [
        int(x) for x in (config["metadata"]["lastModified"]["date"]).split("-")
    ]
    last_modified = date(last_modified[0], last_modified[1], last_modified[2])
    current_date = date.today()
    delta = current_date - last_modified
    if delta.days == 0:
        pass
    elif delta.days > 1:
        config["metadata"]["streak"] = 0
    else:
        config["metadata"]["streak"] += 1
    print(config["metadata"]["streak"])


# Main Functions
def load_config(config_path):
    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_config(config, config_path):
    with open(config_path, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)


def main(operation, args):
    config_path = os.path.join(
        os.path.expanduser("~"), "documents", "HabitLab", "config.json"
    )
    config = load_config(config_path)

    operations = {
        "get": lambda: print(config),
        "add-category": lambda: append_category(args[0], args[1], config),
        "remove-category": lambda: remove_category(args[0], config),
        "check-streak": lambda: check_streak(config),
    }

    if operation in operations:
        operations[operation]()
    else:
        raise ValueError(f"Invalid operation: {operation}")

    update_last_modified(config)
    save_config(config, config_path)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
