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
    config["metadata"]["modified"]["date"] = str(date.today())
    config["metadata"]["modified"]["time"] = str(datetime.now().time())


def check_streak(config):
    last_modified = [
        int(x) for x in (config["metadata"]["modified"]["date"]).split("-")
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
    update_last_modified(config)
    print(config["metadata"]["streak"])


# Data Functions
def add_habit_to_file(habit, config):
    # print(f"Add_habit called with {habit}")
    habit = json.loads(habit)
    task = habit["task"]
    color = habit["color"]
    from_date = habit["from"]["date"]
    from_hour = int(habit["from"]["hour"])
    from_ampm = habit["from"]["AMPM"]
    to_date = habit["to"]["date"]
    to_hour = int(habit["to"]["hour"])
    to_ampm = habit["to"]["AMPM"]

    # Convert to Military Time
    from_hour = convert_to_24_hour(from_hour, from_ampm)
    to_hour = convert_to_24_hour(to_hour, to_ampm)

    # Update habits
    habits = config["habits"]
    if from_date not in habits:
        habits[from_date] = {}

    for hour in range(from_hour, to_hour + 1):
        hour_str = f"{hour:02d}:00"
        habits[from_date][hour_str] = {"task": task, "color": color}

    # Update metadata
    config["metadata"]["modified"]["date"] = str(datetime.now().date())
    config["metadata"]["modified"]["time"] = str(datetime.now().time())
    print(config)


# Helper Functions
def convert_to_24_hour(hour, ampm):
    if ampm == "PM" and hour != 12:
        return hour + 12
    elif ampm == "AM" and hour == 12:
        return 0
    else:
        return hour


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
    fake_data = {
        "task": "Satanic Rituals",
        "color": "#24d996",
        "from": {"date": "2023-04-22", "hour": "12", "AMPM": "PM"},
        "to": {"date": "2023-04-22", "hour": "3", "AMPM": "PM"},
    }

    operations = {
        "get": lambda: print(config),
        "add-category": lambda: append_category(args[0], args[1], config),
        "remove-category": lambda: remove_category(args[0], config),
        "check-streak": lambda: check_streak(config),
        # Need to change data to args[0]. You will hate yourself if you don't.
        "add-habit-to-file": lambda: add_habit_to_file(args[0], config),
    }

    if operation in operations:
        operations[operation]()
    else:
        raise ValueError(f"Invalid operation: {operation}")

    save_config(config, config_path)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
