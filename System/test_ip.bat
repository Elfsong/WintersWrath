@echo off
echo 执行中，请稍后...
echo ping日期：%date%>>pingall.txt
echo ping时间：%time%>>pingall.txt
echo.>>pingall.txt
echo 具体数据：>>pingall.txt
for /l %%i in (1,1,255) do ping -n 1 -w 60  10.23.27.%%i | find "回复" >> pingall.txt
echo ----------------------------------------------------------->> pingall.txt
echo 执行结束，请打开pingall.txt查看。
