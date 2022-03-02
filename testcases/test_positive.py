from airtest.core.api import *

def test_address_field_autopopulates(test_install_app):
    sleep(60.0)
    wait(Template(r"newlogin.png", record_pos=(0.002, 0.888), resolution=(1080, 2340)))
    touch(Template(r"newlogin.png", record_pos=(0.002, 0.888), resolution=(1080, 2340)))
    sleep(10)
    assert_exists(Template(r"loginpopup.png", record_pos=(0.003, 0.057), resolution=(1440, 2560)),
                  "Verify Loginpopup exists.")
    touch(Template(r"txtbxusername.png", record_pos=(0.0, -0.135), resolution=(1440, 2560)))
    sleep(10.0)
    text("accion")
    touch(Template(r"txtpassword.png", record_pos=(0.0, 0.098), resolution=(1440, 2560)))
    text("Password123", enter=False)
    touch(Template(r"btnloginpopup.png", record_pos=(0.244, -0.173), resolution=(1440, 2560)))
    assert_exists(Template(r"homepage.png", record_pos=(0.01, 0.798), resolution=(1440, 2560)), "Verify home page")
    sleep(10.0)
    if exists(Template(r"welcomeback.png", record_pos=(-0.002, -0.815), resolution=(1440, 2560))):
        sleep(2.0)
        touch(Template(r"closewelcomeback.png", record_pos=(0.389, -0.827), resolution=(1440, 2560)))
    if exists(Template(r"newgame.png", record_pos=(-0.002, -0.719), resolution=(1080, 2340))):
        sleep(3.0)
        touch(Template(r"newgameclose.png", record_pos=(0.394, -0.693), resolution=(1080, 2340)))
    wait(Template(r"shop.png", record_pos=(-0.188, 0.984), resolution=(1080, 2340)))
    touch(Template(r"shop.png", record_pos=(-0.188, 0.984), resolution=(1080, 2340)))
    wait(Template(r"newdeposit5.png", record_pos=(-0.31, -0.281), resolution=(1080, 2340)))
    touch(Template(r"newdeposit5.png", record_pos=(-0.31, -0.281), resolution=(1080, 2340)))
    sleep(10.0)
    if exists(Template(r"locationpopup.png", record_pos=(-0.001, 0.079), resolution=(1080, 2340))):
        touch(Template(r"btngiveaccess.png", record_pos=(0.186, 0.231), resolution=(1080, 2340)))
        touch(Template(r"optionallowdevicelocation.png", record_pos=(-0.006, 0.064), resolution=(1080, 2340)))
    sleep(10.0)
    if exists(Template(r"shopselected.png", record_pos=(-0.188, 0.984), resolution=(1080, 2340))):
        touch(Template(r"newdeposit5.png", record_pos=(-0.31, -0.281), resolution=(1080, 2340)))
        wait(Template(r"locationsettingspopup.png", record_pos=(-0.007, 0.061), resolution=(1080, 2340)))
        touch(Template(r"gotosettingsbtn.png", record_pos=(0.18, 0.228), resolution=(1080, 2340)))
        wait(Template(r"Swipeenablelocation.png", record_pos=(0.364, -0.625), resolution=(1080, 2340)))
        touch(Template(r"Swipeenablelocation.png", record_pos=(0.364, -0.625), resolution=(1080, 2340)))
        keyevent("BACK")
    wait(Template(r"addresswindow.png", record_pos=(0.008, -0.026), resolution=(1440, 2560)))
    assert_exists(Template(r"addresswindow.png", record_pos=(0.008, -0.026), resolution=(1440, 2560)),
                  "verify enter address window exists")
    touch(Template(r"addresstxtbx.png", record_pos=(-0.007, -0.041), resolution=(1440, 2560)))
    sleep(10.0)
    text("100 ", enter=False)
    sleep(10.0)
    assert_exists(Template(r"addressautopopulates.png", record_pos=(-0.028, -0.043), resolution=(1440, 2560)),
                  "Verify address field auto populates")