# Greeting
```pyinstaller --clean --onefile -y -n "greeting-x86_64-pc-windows-msvc" greeting.py```
# Check Config
```pyinstaller --clean --onefile -y -n "check_config-x86_64-pc-windows-msvc" check_config.py```
# Read-Write Config
```pyinstaller --clean --onefile -y -n "read_write_config-x86_64-pc-windows-msvc" read_write_config.py```

# Required Packages
`pip install openai`

# Required Files
You must provide a `creds.py` with your own OpenAI API key in the form of 
```open_ai_api_key = "xxxxxx"```