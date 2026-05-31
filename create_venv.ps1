# Create a virtual environment named 'venv'
python -m venv venv 
#& "C:\Python310\python.exe" -m venv venv
# Activate on Windows (Command Prompt)
venv\Scripts\activate.bat
# Activate on Windows (PowerShell)
venv\Scripts\Activate.ps1
# Activate on macOS/Linux
source venv/bin/activate
pip install -r requirements.txt