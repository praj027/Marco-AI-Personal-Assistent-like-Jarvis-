import os
import shutil
import subprocess
import webbrowser
import time

import win32con
import win32gui


# =====================================================
# Bring Chrome To Front
# =====================================================

def bring_chrome_to_front():
    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)

            if "Chrome" in title:
                windows.append(hwnd)

    windows = []
    win32gui.EnumWindows(callback, windows)

    if windows:
        hwnd = windows[0]

        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

        try:
            win32gui.SetForegroundWindow(hwnd)
        except:
            pass

        return True

    return False


# =====================================================
# Open Chrome
# =====================================================

def open_chrome():
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]

    if bring_chrome_to_front():
        return True

    for path in chrome_paths:
        if os.path.exists(path):
            subprocess.Popen([path, "--new-window"])

            time.sleep(2)

            bring_chrome_to_front()

            return True

    print("❌ Chrome not found.")
    return False


# =====================================================
# Open YouTube
# =====================================================

def open_youtube():
    open_chrome()

    webbrowser.open("https://www.youtube.com")

    time.sleep(2)

    bring_chrome_to_front()

    return True


# =====================================================
# Open Notepad
# =====================================================

def open_notepad():
    subprocess.Popen("notepad")
    return True


# =====================================================
# Open Calculator
# =====================================================

def open_calculator():
    subprocess.Popen("calc")
    return True


# =====================================================
# Open VS Code
# =====================================================

def open_vscode():
    paths = [
        r"C:\Users\Tcs\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        r"C:\Program Files\Microsoft VS Code\Code.exe",
    ]

    for path in paths:
        if os.path.exists(path):
            subprocess.Popen([path])
            return True

    print("❌ VS Code not found.")
    return False


# =====================================================
# Generic App Launcher
# =====================================================

APP_ALIASES = {

    "chrome": [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ],

    "vscode": [
        r"C:\Users\Tcs\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        r"C:\Program Files\Microsoft VS Code\Code.exe",
    ],

    "notepad": ["notepad"],

    "calculator": ["calc"],

    "calc": ["calc"],

    "paint": ["mspaint"],

    "cmd": ["cmd"],

    "powershell": ["powershell"],

    "terminal": ["wt"],

    "explorer": ["explorer"],

    "word": ["winword"],

    "excel": ["excel"],

    "powerpoint": ["powerpnt"],

    "spotify": ["spotify"],

    "telegram": ["telegram"],

    "discord": ["discord"],

    "steam": ["steam"],

    # WhatsApp Desktop Windows App
    "whatsapp": [
        "shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"
    ],
}


# =====================================================
# Open Any App
# =====================================================

def open_app(app_name):

    app_name = app_name.lower().strip()

    # YouTube
    if app_name == "youtube":
        return open_youtube()

    # Chrome
    if app_name == "chrome":
        return open_chrome()

    candidates = APP_ALIASES.get(app_name, [app_name])

    for candidate in candidates:

        # -------------------------------------------------
        # Windows Shell / AppsFolder application
        # -------------------------------------------------

        if candidate.startswith("shell:"):

            try:
                subprocess.Popen(
                    ["explorer.exe", candidate],
                    shell=False
                )

                return True

            except Exception as e:

                print(
                    f"❌ Failed to launch {app_name}: {e}"
                )

                continue

        # -------------------------------------------------
        # Full executable path
        # -------------------------------------------------

        if os.path.exists(candidate):

            try:
                subprocess.Popen([candidate])

                return True

            except Exception as e:

                print(
                    f"❌ Failed to launch {app_name}: {e}"
                )

                continue

        # -------------------------------------------------
        # Program available in PATH
        # -------------------------------------------------

        if shutil.which(candidate):

            try:
                subprocess.Popen(candidate)

                return True

            except Exception as e:

                print(
                    f"❌ Failed to launch {app_name}: {e}"
                )

                continue

        # -------------------------------------------------
        # Windows command
        # -------------------------------------------------

        try:

            subprocess.Popen(candidate)

            return True

        except:

            pass

    print(f"❌ Could not open {app_name}")

    return False