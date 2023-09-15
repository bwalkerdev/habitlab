# build_scripts.ps1

# Greeting
pyinstaller --clean --onefile -y -n "greeting-x86_64-pc-windows-gnu" greeting.py

# Check Config
pyinstaller --clean --onefile -y -n "check_config-x86_64-pc-windows-gnu" check_config.py

# Read-Write Config
pyinstaller --clean --onefile -y -n "read_write_config-x86_64-pc-windows-gnu" read_write_config.py

# Generate Tips
pyinstaller --clean --onefile -y -n "generate_tips-x86_64-pc-windows-gnu" generate_tips.py
