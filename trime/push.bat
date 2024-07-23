:: trime.bat
@REM adb push init_rime/. /sdcard/rime
@REM adb push rimerc_easy_en/. /sdcard/rime
@REM adb push wubi86/. /sdcard/rime
adb push schema_tiger/. /sdcard/rime
adb push rime/. /sdcard/rime
@REM adb shell am broadcast -a com.osfans.trime.deploy