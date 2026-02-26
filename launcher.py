import threading
import time
from bot_telegram import main as run_bot
from web_server import run_flask


def run_web_server():
    """Run Flask web server in a separate thread"""
    print("🌐 Starting Flask web server...")
    run_flask()


def run_telegram_bot():
    """Run Telegram bot in main thread"""
    print("🤖 Starting Telegram bot...")
    # Optional: wait a moment to ensure web server is running
    time.sleep(2)
    run_bot()


if __name__ == "__main__":
    print("🚀 Starting M.h4ck Camera Tracking System...")
    
    # Start web server thread
    web_thread = threading.Thread(target=run_web_server, daemon=True)
    web_thread.start()
    
    # Give web server a moment to initialize
    time.sleep(3)
    
    # Start bot in main thread
    run_telegram_bot()
