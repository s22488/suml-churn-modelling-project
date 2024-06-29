import subprocess

# Launch frontend after backend is done
subprocess.run(["streamlit", "run", "streamlit/app.py"], check=False)
