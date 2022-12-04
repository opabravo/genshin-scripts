"""Common utils for Genshin Impact."""
import ctypes
import sys
import pyautogui


def gain_admin_priv():
    """Gain admin priviledge if not running as admin."""
    if ctypes.windll.shell32.IsUserAnAdmin() != 1:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


def switch_to_genshin():
    """Switches to the genshin window."""
    pyautogui.getWindowsWithTitle('原神')[0].activate()


def get_genshin_box():
    """Gets the genshin window box."""
    return pyautogui.getWindowsWithTitle('原神')[0].box
