@echo off
set/p option= please input ip and port (192.168.0.105:37005):

adb disconnect
adb connect %option%