from airtest.core.api import *

def test_startGame(test_install_app):
    wait(Template(r"newlogin.png", record_pos=(0.002, 0.888), resolution=(1080, 2340)),timeout=120, interval=3)
    touch(Template(r"newlogin.png", record_pos=(0.002, 0.888), resolution=(1080, 2340)))
    wait(Template(r"loginpopup.png", record_pos=(0.003, 0.057), resolution=(1440, 2560)),timeout=60, interval=3)
    assert_exists(Template(r"loginpopup.png", record_pos=(0.003, 0.057), resolution=(1440, 2560)),
                  "Verify Loginpopup exists.")
    touch(Template(r"txtbxusername.png", record_pos=(0.0, -0.135), resolution=(1440, 2560)))
    text("accion")
    touch(Template(r"txtpassword.png", record_pos=(0.0, 0.098), resolution=(1440, 2560)))
    text("Password123", enter=False)
    touch(Template(r"btnloginpopup.png", record_pos=(0.244, -0.173), resolution=(1440, 2560)))
    if exists(Template(r"welcomeback.png", record_pos=(-0.002, -0.815), resolution=(1440, 2560))):
        # need to handle world winner spinner
        sleep(6.0)
        touch(Template(r"closewelcomeback.png", record_pos=(0.389, -0.827), resolution=(1440, 2560)))
    if exists(Template(r"newgame.png", record_pos=(-0.002, -0.719), resolution=(1080, 2340))):
        # need to handle world winner spinner
        sleep(6.0)
        touch(Template(r"newgameclose.png", record_pos=(0.394, -0.693), resolution=(1080, 2340)))
    wait(Template(r"homepage.png", record_pos=(0.01, 0.798), resolution=(1440, 2560)), timeout=60, interval=3)
    assert_exists(Template(r"homepage.png", record_pos=(0.01, 0.798), resolution=(1440, 2560)), "Verify home page")
    wait(Template(r"bingo.png", record_pos=(-0.309, 0.035), resolution=(1440, 2560)),timeout=60, interval=3)
    touch(Template(r"bingo.png", record_pos=(-0.319, 0.033), resolution=(1440, 2560)))
    wait(Template(r"gameoverview.png", record_pos=(0.0, 0.05), resolution=(1440, 2560)),timeout=60, interval=3)
    assert_exists(Template(r"gameoverview.png", record_pos=(0.0, 0.05), resolution=(1440, 2560)))
    touch(Template(r"btnPickaTournament.png", record_pos=(0.216, 0.776), resolution=(1440, 2560)))
    wait(Template(r"btnPlay.png", record_pos=(0.31, 0.654), resolution=(1440, 2560)),timeout=60, interval=3)
    touch(Template(r"btnPlay.png", record_pos=(0.317, 0.652), resolution=(1440, 2560)))
    wait(Template(r"findingyourapponent.png", record_pos=(0.019, 0.4), resolution=(1440, 2560)),timeout=60, interval=3)
    wait(Template(r"btnstart.png", record_pos=(-0.004, 0.474), resolution=(1440, 2560)),timeout=60, interval=3)
    touch(Template(r"btnstart.png", record_pos=(-0.004, 0.474), resolution=(1440, 2560)))
    if exists(Template(r"howtoplay.png", record_pos=(0.067, -0.683), resolution=(1440, 2560))):
        touch(Template(r"close.png", record_pos=(0.343, -0.685), resolution=(1440, 2560)))
    wait(Template(r"btnstart.png", record_pos=(-0.014, 0.472), resolution=(1440, 2560)),timeout=60, interval=3)
    touch(Template(r"btnstart.png", record_pos=(-0.014, 0.472), resolution=(1440, 2560)))
    wait(Template(r"closeiconBingo.png", record_pos=(0.442, -0.844), resolution=(1440, 2560)),timeout=60, interval=3)
    double_click(Template(r"closeiconBingo.png", record_pos=(0.442, -0.844), resolution=(1440, 2560)))
    wait(Template(r"endgamepopup.png", record_pos=(-0.002, 0.266), resolution=(1440, 2560)),timeout=60, interval=3)
    assert_exists(Template(r"endgamepopup.png", record_pos=(-0.002, 0.266), resolution=(1440, 2560)))
    touch(Template(r"btnendgame.png", record_pos=(0.442, -0.844), resolution=(1440, 2560)))
    wait(Template(r"myscore.png", record_pos=(0.274, 0.529), resolution=(1440, 2560)),timeout=60, interval=3)
    assert_exists(Template(r"myscore.png", record_pos=(0.274, 0.529), resolution=(1440, 2560)),
                  "Verify My score")






# sleep(10.0)
# wait(Template(r"bingo.png", record_pos=(-0.309, 0.035), resolution=(1440, 2560)))
# touch(Template(r"bingo.png", record_pos=(-0.319, 0.033), resolution=(1440, 2560)))
# exists(Template(r"gameoverview.png", record_pos=(0.0, 0.05), resolution=(1440, 2560)))
# wait(Template(r"btnPickaTournament.png", record_pos=(0.216, 0.776), resolution=(1440, 2560)))
# touch(Template(r"btnPickaTournament.png", record_pos=(0.216, 0.776), resolution=(1440, 2560)))
# wait(Template(r"btnPlay.png", record_pos=(0.31, 0.654), resolution=(1440, 2560)))
# touch(Template(r"btnPlay.png", record_pos=(0.317, 0.652), resolution=(1440, 2560)))
#     # sleep(60.0)
# wait(Template(r"findingyourapponent.png", record_pos=(0.019, 0.4), resolution=(1440, 2560)))
# sleep(20.0)
# touch(Template(r"btnstart.png", record_pos=(-0.004, 0.474), resolution=(1440, 2560)))
# exists(Template(r"howtoplay.png", record_pos=(0.067, -0.683), resolution=(1440, 2560)))
# touch(Template(r"close.png", record_pos=(0.343, -0.685), resolution=(1440, 2560)))
# wait(Template(r"btnstart.png", record_pos=(-0.014, 0.472), resolution=(1440, 2560)))
# touch(Template(r"btnstart.png", record_pos=(-0.014, 0.472), resolution=(1440, 2560)))
#     # added
# sleep(10.0)
# wait(Template(r"closeiconBingo.png", record_pos=(0.442, -0.844), resolution=(1440, 2560)))
# touch(Template(r"closeiconBingo.png", record_pos=(0.442, -0.844), resolution=(1440, 2560)))
# sleep(6.0)
# wait(Template(r"endgamepopup.png", record_pos=(-0.002, 0.266), resolution=(1440, 2560)))
# exists(Template(r"endgamepopup.png", record_pos=(-0.002, 0.266), resolution=(1440, 2560)))
# touch(Template(r"btnendgame.png", record_pos=(0.442, -0.844), resolution=(1440, 2560)))
# sleep(6.0)
# assert_exists(Template(r"myscore.png", record_pos=(0.274, 0.529), resolution=(1440, 2560)),
#                   "Verify My score")







