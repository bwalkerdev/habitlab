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


def remove_category(label, config):
    for category in config["categories"]:
        if category["label"] == label:
            config["categories"].remove(category)
            break


# Date and Time Functions
def update_last_modified(config):
    config["metadata"]["lastModified"]["date"] = str(date.today())
    config["metadata"]["lastModified"]["time"] = str(datetime.now().time())


def check_streak(config):
    last_modified = [
        int(x) for x in (config["metadata"]["lastModified"]["date"]).split("-")
    ]
    last_modified = date(last_modified[0], last_modified[1], last_modified[2])
    print(last_modified)
    current_date = date.today()
    delta = current_date - last_modified
    print("DEBUG ", delta.days)
    if delta.days == 0:
        pass
    elif delta.days > 1:
        config["metadata"]["streak"] = 0
    else:
        config["metadata"]["streak"] += 1


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
        "get": lambda: None,
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
    print(config)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
