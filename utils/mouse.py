import time
import pyautogui
from utils.locator import Locator


class Mouse:
    """Mouse Manager"""
    @staticmethod
    def click_multi(player_count: int):
        """Clicks and join world depending on the player count."""
        positions = Locator().multi_player_count(player_count)
        for position in positions:
            print(f"{player_count} Players : | Found {position}")
            pyautogui.click(position.left, position.top+35)
            time.sleep(0.1)

    @staticmethod
    def scroll(times: int):
        """Scrolls the mouse wheel down for n times."""
        for _ in range(times):
            pyautogui.scroll(-100)
            time.sleep(0.01)

    @staticmethod
    def drag(start: tuple[int, int], end: tuple[int, int], duration: float = 0.3):
        """Drags the mouse from start to end."""
        pyautogui.moveTo(start[0], start[1])
        pyautogui.dragTo(end[0], end[1], button='left', duration=duration)
        pyautogui.click(end[0], end[1], button='left')
