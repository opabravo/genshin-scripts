import pyautogui


class KeyBoard:
    """Keyboard Manager"""
    @staticmethod
    def press(key: str):
        """Presses the key."""
        pyautogui.press(key)

    @staticmethod
    def open_multi_menu():
        """Opens the multi Player menu."""
        pyautogui.press("F2")

    @staticmethod
    def press_esc():
        """Presses the esc key."""
        pyautogui.press("esc")

