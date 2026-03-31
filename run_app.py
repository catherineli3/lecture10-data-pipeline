import subprocess
import sys
import webbrowser
import time
from pathlib import Path

def main():
    # Start Flask server
    print("Starting Flask application...")
    process = subprocess.Popen(
        [sys.executable, 'app.py'],
        cwd=Path(__file__).parent
    )
    
    # Wait for server to start
    print("Waiting for server to start...")
    time.sleep(3)
    
    # Open browser
    url = "http://localhost:5000"
    print(f"Opening browser at {url}")
    webbrowser.open(url)
    
    print("\nFlask app is running!")
    print("Press Ctrl+C to stop the server")
    
    try:
        process.wait()
    except KeyboardInterrupt:
        print("\nStopping server...")
        process.terminate()
        process.wait()

if __name__ == '__main__':
    main()
