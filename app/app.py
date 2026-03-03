from flask import Flask, jsonify
import socket
import time
import os

app = Flask(__name__)
start_time = time.time()

@app.route('/')
def home():
    hostname = socket.gethostname()
    uptime = int(time.time() - start_time)
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Pipeline Demo</title>
        <style>
            body {{ font-family: Arial; text-align: center; padding: 50px; background: #f0f0f0; }}
            .box {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #333; }}
            .version {{ color: #0066cc; font-weight: bold; }}
            .hostname {{ color: #666; }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 Simple DevOps Project</h1>
            <p>Version: <span class="version">1.0.1</span></p>
            <p>Hostname: <span class="hostname">{hostname}</span></p>
            <p>Uptime: <span class="hostname">{uptime} seconds</span></p>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy", 
        "uptime": int(time.time() - start_time),
        "hostname": socket.gethostname()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)