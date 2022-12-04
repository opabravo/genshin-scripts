import time
from utils.checker import check_genshin_window, check_join_btn
from utils.common import switch_to_genshin, gain_admin_priv, get_genshin_box
from utils.keyboard import KeyBoard
from utils.mouse import Mouse

if __name__ == "__main__":
    gain_admin_priv()
    scroll_count = 0

    switch_to_genshin()
    time.sleep(0.5)
    KeyBoard().open_multi_menu()

    while 1:
        check_genshin_window()
        # time.sleep(0.5)
        check_join_btn()
        Mouse().click_multi(3)
        Mouse().click_multi(2)

        genshin_box = get_genshin_box()
        multi_bottom_x = genshin_box.left + genshin_box.width / 2
        multi_bottom_y = genshin_box.top + genshin_box.height - 150
        multi_menu_top_y = genshin_box.top + 200
        Mouse().drag((multi_bottom_x, multi_bottom_y), (multi_bottom_x, multi_menu_top_y))
        scroll_count += 1
        # One Multi Player Page will have to scroll 8 times to get to the bottom
        if scroll_count % 10 == 0:
            KeyBoard().press_esc()
            time.sleep(0.5)
            KeyBoard().open_multi_menu()
