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

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![py_greet])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
