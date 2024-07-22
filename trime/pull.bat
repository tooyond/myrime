@REM 清空目录
rmdir /s /Q rime_by_pull
md rime_by_pull
adb pull /sdcard/rime/build/ rime_by_pull/build/
@REM adb pull /sdcard/rime/trime.yaml rime_by_pull/trime.yaml
@REM adb pull /sdcard/rime/tongwenfeng.trime.yaml rime_by_pull/tongwenfeng.trime.yaml
@REM adb pull /sdcard/rime/user.yaml rime_by_pull/user.yaml