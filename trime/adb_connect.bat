@echo off
set/p option= please input ip and port (192.168.0.101:39857):

adb connect %option%