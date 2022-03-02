")""""Base conftest.py."""
import logging
from pathlib import Path

import self as self

from airtest.core.android import Android
import pytest
from airtest.core.api import *
from airtest.report.report import *
from airtest.report.report import simple_report

auto_setup(__file__, logdir=True)
ST.LOG_FILE = "log.txt"
set_logdir(str(Path().absolute().parent) + '\\log')
PKG = "com.gsn.worldwinner"
connect_device("Android:///")


# APK = str(Path().absolute().parent) + '\\app\\WorldWinner.apk'

@pytest.fixture(scope="function")
def test_install_app():
    connect_device("Android:///")
    if PKG not in device().list_app():
        install(r"C:\Users\RH0539\Downloads\WorldWinner.apk")
        start_app(PKG)
    else:
        stop_app(PKG)
        clear_app(PKG)
        start_app(PKG)
    yield
    stop_app(PKG)
    clear_app(PKG)
    simple_report(__file__, logpath=True, logfile=str(Path().absolute().parent) + '\\log\\log.txt',
                  output=str(Path().absolute().parent) + '\\log\\report.html')

    # h1 = LogToHtml(script_root=r'D:\test\1234.air', log_root=r"D:\test\1234.air\log", export_dir=r"D:\test\1234.air",
    #                logfile=r'D:\test\1234.air\log\log.txt', lang='en', plugins=["poco.utils.airtest.report"])

    # h1 = LogToHtml(script_root=str(Path().absolute().parent) + '\\testcases', log_root=str(Path().absolute().parent) + '\\log', export_dir=str(Path().absolute().parent) + '\\testcases',
    #                logfile=str(Path().absolute().parent) + '\\log\\log.txt', lang='en', plugins=["poco.utils.airtest.report"])
    # h1.report()
    # self.android.start_app(PKG)
    # self.android.uninstall_app(PKG)

# @pytest.fixture(scope="function")
# @pytest.fixture(scope="module")
# @pytest.fixture(scope="session")


# auto_setup(__file__, devices=["Android:///"], logdir=True)
# set_logdir(r'D:\log')
# APK = os.path.join(PWD, "C:/Users/RH0539/Downloads/WorldWinner.apk")
# simple_report(__file__, logpath=True, logfile=r"D:\log\log.txt", output=r"D:\log\report.html")
