import pyautogui
from utils.common import get_genshin_box
from utils.logger import logger
from utils.constants import ASSEST_PATH


class Locator:
    """Locate elements in Genshin Impact."""

    def __init__(self):
        self.region = get_genshin_box()
        logger.debug(f"Genshin Window Location: {self.region}")

    def locate_all(self, image: str, grayscale: bool = True, confidence: float = 0.9) -> tuple:
        """Locate all images on the screen."""
        return pyautogui.locateAllOnScreen(image, region=self.region, grayscale=grayscale, confidence=confidence)

    def locate(self, image: str, grayscale: bool = True, confidence: float = 0.9) -> tuple:
        """Locate an image on the screen."""
        return pyautogui.locateOnScreen(image, minSearchTime=2, region=self.region, grayscale=grayscale,
                                        confidence=confidence)

    def multi_player_count(self, player_count: int) -> tuple:
        """Locate the text that match specific multi player count."""
        return self.locate_all(f'{ASSEST_PATH}/txt_{player_count}_players.png')

    def join_btn(self) -> tuple:
        """Locate the join button."""
        return self.locate(f'{ASSEST_PATH}/join_btn.png')
