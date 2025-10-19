import socket
import time

from Constants import URL_GAME
from Live import *


def main():
    # launch_flask_server()
    welcome("User")
    load_game()

    time.sleep(2)
    print("Game finished! 🎉")

    # ✅ After the game ends, launch the Flask server
    launch_flask_server()

    while True:
        load_game()  # play a round

        choice = input("\nDo you want to play again? (y/n): ").strip().lower()
        if choice != "y":
            print("Thanks for playing! Exiting...")
            break


def launch_flask_server():
    import os, subprocess, sys, webbrowser

    print("Starting score server...")

    # Kill old Flask processes (Linux)
    os.system("pkill -f MainScores_old.py")

    # Start Flask in background
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "", "MainScores_old.py")
    subprocess.Popen([sys.executable, script_path])

    # Wait until Flask is ready
    if wait_for_server():
        webbrowser.open(URL_GAME)
        print("✅ Score server running at {}".format(URL_GAME))
    else:
        print("❌ Flask server did not start in time")



def wait_for_server(host="127.0.0.1", port=5001, timeout=10):
    start = time.time()
    while True:
        try:
            with socket.create_connection((host, port), timeout=1):
                return True
        except OSError:
            if time.time() - start > timeout:
                return False
            time.sleep(0.2)

if __name__ == "__main__":
    main()