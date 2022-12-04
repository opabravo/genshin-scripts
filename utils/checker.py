"""Genshin Checker"""
import sys
from win32gui import GetWindowText, GetForegroundWindow
from utils.logger import logger
from utils.locator import Locator


def check_join_btn():
    """Checks if the join button is visible."""
    pos = Locator().join_btn()
    if not pos:
        logger.info("No Join Button Found... Auto quit")
        sys.exit()


def check_genshin_window():
    """Checks if the genshin window is active."""
    if GetWindowText(GetForegroundWindow()) != "原神":
        logger.info("Genshin Window not active... Auto quit")
        sys.exit()
