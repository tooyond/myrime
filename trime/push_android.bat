:: trime.bat
adb push bak/. /sdcard/rime
adb push rime/. /sdcard/rime
@REM adb shell am broadcast -a com.osfans.trime.deploy