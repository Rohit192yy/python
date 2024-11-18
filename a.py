import subprocess
from flask import Flask
import os

app = Flask(__name__)

# Set the port dynamically based on Render's environment
PORT = os.getenv('PORT', 5000)

@app.route('/')
def home():
    return 'Visit /terminal to access the web terminal!'

@app.route('/terminal')
def terminal():
    try:
        # Start ttyd as a subprocess
        subprocess.Popen(['ttyd', '-p', '8080', 'bash'])
        return "ttyd is running. Access it at <a href='http://localhost:8080'>http://localhost:8080</a>"
    except Exception as e:
        return f"Error starting ttyd: {e}"

if __name__ == '__main__':
    # Ensure the app runs on the correct port Render expects
    app.run(host='0.0.0.0', port=PORT)  # Flask app running on Render's specified port
