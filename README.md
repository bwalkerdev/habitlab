# Introduction
- Right now, HabitLab **only runs on Windows**. I can get it to compile for macOS, but I was unable to get the file system permissions working properly by the early submission date.
- Think of this as an early alpha. There are bugs. So many bugs. I had no help building or bug testing this project, so I’m certain that things have slipped through the cracks.
- The Python code is located in the `python` folder.

# Purpose
- The purpose is to visually identify trends throughout the month
![Pasted image 20230426221924](https://user-images.githubusercontent.com/99450073/234758607-45abd26c-8cac-4797-832b-f15cda1565d2.png)

# Known Issues
- You cannot delete habits. You have to go into the config manually to do it. You can overwrite habits using the UI.
- In one test, python was having trouble populating the config on first boot. If this happens, try and restart the application until it works.
- The config JSON does not check schema. If you modify it in a text editor without being careful, you will have to delete it. The config is regenerated if it does not exist.
- If the end time is before the start time, the button will show a task has been set, but it will not push to the JSON.
- Auto dark mode is not working. The switch is a little bugged too sometimes.
- Refresh is not working.
- **If you happen upon an issue, please submit it to the project GitHub. I would like to keep improving this project**

# Build this project
## Requirements
- Node.JS
- Rust
- Tauri CLI
- Python
- PyInstaller

## How to build this project
//todo

