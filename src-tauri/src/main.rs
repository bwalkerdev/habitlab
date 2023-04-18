#![cfg_attr(
    all(not(debug_assertions), target_os = "windows"),
    windows_subsystem = "windows"
)]

use tauri::api::process::{Command, CommandEvent};

#[tauri::command]
async fn py_greet() -> String {
    println!("Rust: Call PyGreet");
    let (mut rx, child) = Command::new("greeting")
        .spawn()
        .expect("Failed to spawn greeting.py");
    let mut result = String::new();
    while let Some(event) = rx.recv().await {
        if let CommandEvent::Stdout(line) = event {
            result = line.clone();
            println!("Python: {}", line);
            break; // Only lets python send one line. This is not ideal
        }
    }
    result
}

#[tauri::command]
async fn check_config() -> String {
    println!("Rust: Call check_config");
    let (mut rx, child) = Command::new("check_config")
        .spawn()
        .expect("Failed to spawn config.py");
    let mut result = String::new();
    while let Some(event) = rx.recv().await {
        if let CommandEvent::Stdout(line) = event {
            result = line.clone();
            println!("Python: {}", line);
            break; // Only lets python send one line. This is not ideal
        }
    }
    result
}

#[tauri::command]
async fn add_category(category: String, color: String) -> String {
    println!("Rust: Call read_write_config");
    let (mut rx, child) = Command::new("read_write_config")
        .args([String::from("add-category"), category, color])
        .spawn()
        .expect("Failed to spawn read_write_config.py");
    let mut result = String::new();
    while let Some(event) = rx.recv().await {
        if let CommandEvent::Stdout(line) = event {
            result = line.clone();
            println!("Python: {}", line);
            break; // Only lets python send one line. This is not ideal
        }
    }
    result
}

#[tauri::command]
async fn remove_category(category: String) -> String {
    println!("Rust: Call read_write_config");
    let (mut rx, child) = Command::new("read_write_config")
        .args([String::from("remove-category"), category])
        .spawn()
        .expect("Failed to spawn read_write_config.py");
    let mut result = String::new();
    while let Some(event) = rx.recv().await {
        if let CommandEvent::Stdout(line) = event {
            result = line.clone();
            println!("Python: {}", line);
            break; // Only lets python send one line. This is not ideal
        }
    }
    result
}

#[tauri::command]
async fn get_config() -> String {
    println!("Rust: Call read_write_config");
    let (mut rx, child) = Command::new("read_write_config")
        .args([String::from("get")])
        .spawn()
        .expect("Failed to spawn read_write_config.py");
    let mut result = String::new();
    while let Some(event) = rx.recv().await {
        if let CommandEvent::Stdout(line) = event {
            result = line.clone();
            println!("Python: {}", line);
            break; // Only lets python send one line. This is not ideal
        }
    }
    result
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
