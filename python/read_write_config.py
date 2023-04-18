import os
import json
import sys

# Example usage: c:/GitHub/habitlab/python/read_write_config.py add-category sleep "#8d46fa"


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
    }

    if operation in operations:
        operations[operation]()
    else:
        raise ValueError(f"Invalid operation: {operation}")

    save_config(config, config_path)
    print(config)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
