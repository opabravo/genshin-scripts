import os
from utils.common import get_genshin_box


ASSEST_PATH = os.path.join(os.path.dirname(__file__), 'assets')
#screen_width, screen_height = pyautogui.size()
BOX = get_genshin_box()
print(BOX)