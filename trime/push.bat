:: trime.bat
@REM adb push init_rime/. /sdcard/rime
@REM adb push rimerc_easy_en/. /sdcard/rime
adb push rime/. /sdcard/rime
@REM adb shell am broadcast -a com.osfans.trime.deploy