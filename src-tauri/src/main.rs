#![cfg_attr(
    all(not(debug_assertions), target_os = "windows"),
    windows_subsystem = "windows"
)]

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
async fn get_config() -> String {
    execute_python_command("read_write_config", vec![String::from("get")]).await
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![
            py_greet,
            check_config,
            add_category,
            remove_category,
            get_config
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
