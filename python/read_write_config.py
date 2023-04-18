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


def main(operation, args):
    config_path = os.path.expanduser("~") + "\documents\HabitLab" + "/config.json"
    config = {}
    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)
        # print(config)
        match operation:
            case "get":
                pass
            case "add-category":
                append_category(args[0], args[1], config)
            case "remove-category":
                remove_category(args[0], config)
        # print(config)
    with open(config_path, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)
    print(config)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
