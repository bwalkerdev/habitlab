#![cfg_attr(
    all(not(debug_assertions), target_os = "windows"),
    windows_subsystem = "windows"
)]

use dirs_next::home_dir;
use open;
use std::path::PathBuf;
use tauri::api::process::{Command, CommandEvent};

async fn execute_python_command(command_name: &str, args: Vec<String>) -> String {
    println!("Rust: Call {}", command_name);
    let (mut rx, child) = Command::new(command_name)
        .args(args)
        .spawn()
        .expect(&format!("Failed to spawn {}.py", command_name));
    let mut result = String::new();
    while let Some(event) = rx.recv().await {
        if let CommandEvent::Stdout(line) = event {
            result = line.clone();
            println!("Python: {}", line);
            break;
        }
    }
    child.kill().expect("Failed to kill child");
    result
}

#[tauri::command]
async fn py_greet() -> String {
    execute_python_command("greeting", vec![]).await
}

#[tauri::command]
async fn gen_tips(invoke_message: String) -> String {
    println!("data is {}", invoke_message);
    execute_python_command("generate_tips", vec![invoke_message]).await
}

fn get_habitlab_dir() -> Option<PathBuf> {
    let mut habitlab_path = home_dir()?;
    habitlab_path.push("Documents");
    habitlab_path.push("HabitLab");
    Some(habitlab_path)
}

#[tauri::command]
async fn open_config_folder() {
    if let Some(config_path) = get_habitlab_dir() {
        if let Err(err) = open::that(config_path) {
            println!("Failed to open the config directory: {}", err);
        }
    } else {
        println!("Unable to determine the config directory");
    }
}

#[tauri::command]
async fn get_config() -> String {
    execute_python_command("read_write_config", vec![String::from("get")]).await
}

#[tauri::command]
async fn check_config() -> String {
    execute_python_command("check_config", vec![]).await
}

#[tauri::command]
async fn add_category(category: String, color: String) -> String {
    execute_python_command(
        "read_write_config",
        vec![String::from("add-category"), category, color],
    )
    .await
}

#[tauri::command]
async fn remove_category(category: String) -> String {
    execute_python_command(
        "read_write_config",
        vec![String::from("remove-category"), category],
    )
    .await
}

#[tauri::command]
async fn check_streak() -> String {
    execute_python_command("read_write_config", vec![String::from("check-streak")]).await
}

#[tauri::command]
async fn add_habit_to_file(habit: String) -> String {
    execute_python_command(
        "read_write_config",
        vec![String::from("add-habit-to-file"), habit],
    )
    .await
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![
            py_greet,
            check_config,
            add_category,
            remove_category,
            get_config,
            check_streak,
            open_config_folder,
            add_habit_to_file,
            gen_tips
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
