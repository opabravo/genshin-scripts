import time
from utils.common import switch_to_genshin, gain_admin_priv
from utils.checker import check_genshin_window, check_join_btn
from utils.mouse import Mouse
from utils.keyboard import KeyBoard


if __name__ == "__main__":
    gain_admin_priv()
    scroll_count = 0
    
    # print("Starting in...", end="", flush=True)
    # for i in range(3,0,-1):
    #     print(i, end="", flush=True)
    #     time.sleep(1)
    
    switch_to_genshin()
    time.sleep(0.5)
    KeyBoard().open_multi_menu()
    
    while 1:
        check_genshin_window()
        #time.sleep(0.5)
        check_join_btn()
        
        Mouse().click_multi(3)
        Mouse().click_multi(2)
        Mouse().drag((1112, 800), (1112, 250), 0.3)
        scroll_count+=1

        # One Multi Player Page will have to scroll 8 times to get to the bottom
        if scroll_count % 8 == 0:
            KeyBoard().press_esc()
            time.sleep(0.5)
            KeyBoard().open_multi_menu()
