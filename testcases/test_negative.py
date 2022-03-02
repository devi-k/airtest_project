from airtest.core.api import *


def test_invalid_login(test_install_app):
    sleep(50.0)
    wait(Template(r"newlogin.png", record_pos=(0.002, 0.888), resolution=(1080, 2340)))
    touch(Template(r"newlogin.png", record_pos=(0.002, 0.888), resolution=(1080, 2340)))
    sleep(10)
    assert_exists(Template(r"loginpopup.png", record_pos=(0.003, 0.057), resolution=(1440, 2560)),
                  "Verify Loginpopup exists.")
    touch(Template(r"txtbxusername.png", record_pos=(0.0, -0.135), resolution=(1440, 2560)))
    sleep(10.0)
    text("accion")
    touch(Template(r"txtpassword.png", record_pos=(0.0, 0.098), resolution=(1440, 2560)))
    text("Password1234", enter=False)
    touch(Template(r"btnloginpopup.png", record_pos=(0.244, -0.173), resolution=(1440, 2560)))
    assert_exists(Template(r"invaliduname&pwd.png", record_pos=(0.077, 0.215), resolution=(1440, 2560)),
                  "Verify Invalid username /Password combo text")

# def test_address_field_autopopulates_old(test_install_app):
#
#     sleep(100.0)
#     assert_exists(Template(r"ageverificationscreen.png", record_pos=(-0.007, -0.621), resolution=(1440, 2560)),
#                   "Verify image exists.")
#     touch(Template(r"agecheckbox.png", record_pos=(-0.388, 0.392), resolution=(1440, 2560)))
#     wait(Template(r"btnletsplay.png", record_pos=(-0.002, 0.649), resolution=(1440, 2560)))
#     exists(Template(r"btnletsplay.png", record_pos=(-0.002, 0.649), resolution=(1440, 2560)))
#     touch(Template(r"btnletsplay.png", record_pos=(-0.002, 0.649), resolution=(1440, 2560)))
#     wait(Template(r"practicegamepopup.png", record_pos=(-0.002, -0.019), resolution=(1440, 2560)))
#     assert_exists(Template(r"practicegamepopup.png", record_pos=(-0.002, -0.019), resolution=(1440, 2560)),
#                   "Verify practice game popup exists.")
#     touch(Template(r"btnokaypracticegame.png", record_pos=(-0.004, 0.079), resolution=(1440, 2560)))
#     wait(Template(r"btnlogin.png", record_pos=(0.348, -0.815), resolution=(1440, 2560)))
#     touch(Template(r"btnlogin.png", record_pos=(0.348, -0.815), resolution=(1440, 2560)))
#     assert_exists(Template(r"loginpopup.png", record_pos=(0.003, 0.057), resolution=(1440, 2560)),
#                   "Verify Loginpopup exists.")
#     touch(Template(r"txtbxusername.png", record_pos=(0.0, -0.135), resolution=(1440, 2560)))
#     sleep(10.0)
#     text("accion")
#     touch(Template(r"txtpassword.png", record_pos=(0.0, 0.098), resolution=(1440, 2560)))
#     text("Password123", enter=False)
#     touch(Template(r"btnloginpopup.png", record_pos=(0.244, -0.173), resolution=(1440, 2560)))
#     assert_exists(Template(r"homepage.png", record_pos=(0.01, 0.798), resolution=(1440, 2560)), "Verify home page")
#     sleep(10.0)
#     if exists(Template(r"welcomeback.png", record_pos=(-0.002, -0.815), resolution=(1440, 2560))):
#         touch(Template(r"closewelcomeback.png", record_pos=(0.389, -0.827), resolution=(1440, 2560)))
#     wait(Template(r"shop.png", record_pos=(-0.188, 0.984), resolution=(1080, 2340)))
#     touch(Template(r"shop.png", record_pos=(-0.188, 0.984), resolution=(1080, 2340)))
#     wait(Template(r"depositlbl.png", record_pos=(-0.013, -0.827), resolution=(1080, 2340)))
#     assert_exists(Template(r"depositlbl.png", record_pos=(-0.013, -0.827), resolution=(1080, 2340)),
#                   "verify deposit screen")
#     touch(Template(r"deposit5.png", record_pos=(-0.291, -0.158), resolution=(1080, 2340)))
#     sleep(10.0)
#     if exists(Template(r"locationpopup.png", record_pos=(-0.001, 0.079), resolution=(1080, 2340))):
#         touch(Template(r"btngiveaccess.png", record_pos=(0.186, 0.231), resolution=(1080, 2340)))
#         touch(Template(r"optionallowdevicelocation.png", record_pos=(-0.006, 0.064), resolution=(1080, 2340)))
#     wait(Template(r"addresswindow.png", record_pos=(0.008, -0.026), resolution=(1440, 2560)))
#     assert_exists(Template(r"addresswindow.png", record_pos=(0.008, -0.026), resolution=(1440, 2560)),
#                   "verify enter address window exists")
#     touch(Template(r"addresstxtbx.png", record_pos=(-0.007, -0.041), resolution=(1440, 2560)))
#     sleep(10.0)
#     text("100 ", enter=False)
#     sleep(10.0)
#     assert_exists(Template(r"addressautopopulates.png", record_pos=(-0.028, -0.043), resolution=(1440, 2560)),
#                   "Verify address field auto populates")


# def test_invalid_login_old(test_install_app):
#     sleep(100.0)
#     assert_exists(Template(r"ageverificationscreen.png", record_pos=(-0.007, -0.621), resolution=(1440, 2560)),
#                   "Verify image exists.")
#     touch(Template(r"agecheckbox.png", record_pos=(-0.388, 0.392), resolution=(1440, 2560)))
#     wait(Template(r"btnletsplay.png", record_pos=(-0.002, 0.649), resolution=(1440, 2560)))
#     exists(Template(r"btnletsplay.png", record_pos=(-0.002, 0.649), resolution=(1440, 2560)))
#     touch(Template(r"btnletsplay.png", record_pos=(-0.002, 0.649), resolution=(1440, 2560)))
#     wait(Template(r"practicegamepopup.png", record_pos=(-0.002, -0.019), resolution=(1440, 2560)))
#     assert_exists(Template(r"practicegamepopup.png", record_pos=(-0.002, -0.019), resolution=(1440, 2560)),
#                   "Verify practice game popup exists.")
#     touch(Template(r"btnokaypracticegame.png", record_pos=(-0.004, 0.079), resolution=(1440, 2560)))
#     wait(Template(r"btnlogin.png", record_pos=(0.348, -0.815), resolution=(1440, 2560)))
#     touch(Template(r"btnlogin.png", record_pos=(0.348, -0.815), resolution=(1440, 2560)))
#     assert_exists(Template(r"loginpopup.png", record_pos=(0.003, 0.057), resolution=(1440, 2560)),
#                   "Verify Loginpopup exists.")
#     touch(Template(r"txtbxusername.png", record_pos=(0.0, -0.135), resolution=(1440, 2560)))
#     sleep(10.0)
#     text("accion")
#     touch(Template(r"txtpassword.png", record_pos=(0.0, 0.098), resolution=(1440, 2560)))
#     text("Password1234", enter=False)
#     touch(Template(r"btnloginpopup.png", record_pos=(0.244, -0.173), resolution=(1440, 2560)))
#     assert_exists(Template(r"invaliduname&pwd.png", record_pos=(0.077, 0.215), resolution=(1440, 2560)),
#                   "Verify Invalid username /Password combo text")


# Sampad
# try:
#     assert_equal("Real opponents", "Sampad", "Checking the text exist")
# except AssertionError:
#     log("Assertion error", timestamp=time.time(), desc="Assertion error", snapshot=True)

# def setup_module(module):
#     print("before each module")
#
#
# def teardown_module(module):
#     print("after each module")
#
#
# def setup_function(function):
#     print("before each test")
#
#
# def teardown_function(function):
#     print("after each test")

# @pytest.mark.usefixtures("test_install_app")
# def test_login_popup_exists(test_install_app):
#     sleep(20.0)

# Sampad
# try:
#     assert_equal("Real opponents", "Rddeal opponents", "Checking the text exist")
# except AssertionError:
#     log("Assertion error", timestamp=time.time(), desc="Assertion error", snapshot=False)

# def test_name1(request):
#     testname = request.node.name
#     assert testname == 'test_name1'

# wait(".\\images\\ageCheckbox.png")
# touch(Template(".\\images\\ageCheckbox.png"))
# wait(Template(".\\images\\btnLetsPlay.png"))
# allure.attach(snapshot(filename="123.jpg",msg="Homepage screenshot",quality=90,max_size=800))
# touch(Template(".\\images\\btnLetsPlay.png"))
# wait(Template(".\\images\\popupPracticegame.png"))
# touch(Template(".\\images\\btnOkayPracticegame.png"))
# wait(Template(".\\images\\btnLogin.png"))
# touch(Template(".\\images\\btnLogin.png"))
# wait(Template(".\\images\\popupLogin.png"))
# assert_exists(Template(".\\images\\popupLogin.png"), "verify login popup exists")


# wait(Template(r"txtbxUsernameLogin.png", record_pos=(-0.022, -0.139), resolution=(1440, 2560)))
# touch(Template(r"tpl1644288890150.png", record_pos=(-0.022, -0.139), resolution=(1440, 2560)))
# wait(Template(r"tpl1644469091319.png", record_pos=(-0.002, -0.106), resolution=(1440, 2560)))
# text("accionlabs", enter=True)
# touch(Template(r"tpl1644288550917.png", record_pos=(0.003, 0.096), resolution=(1440, 2560)))
# wait(Template(r"tpl1644469195863.png", record_pos=(0.001, 0.007), resolution=(1440, 2560)))
# text("Password123", enter=False)
# touch(Template(r"tpl1644288614104.png", record_pos=(0.244, 0.448), resolution=(1440, 2560)))
# assert_exists(Template(r"tpl1644485252051.png", record_pos=(0.077, 0.215), resolution=(1440, 2560)),
#               "Verify Invalid username /Password combo")

# def test_second(test_install_app):
#     sleep(30.0)
#     wait(Template(r"tpl1644288160934.png", record_pos=(-0.385, 0.395), resolution=(1440, 2560)))
#     touch(Template(r"tpl1644288160934.png", record_pos=(-0.385, 0.395), resolution=(1440, 2560)))
#     exists(Template(r"tpl1644288260454.png", record_pos=(-0.002, -0.017), resolution=(1440, 2560)))
