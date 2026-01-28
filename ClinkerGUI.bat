@echo off
chcp 65001 >nul
title Clinker GUI 启动器
echo ========================================
echo    Clinker GUI - 基因簇比对可视化工具
echo ========================================
echo.
echo 正在启动 GUI...
echo.

REM 使用 start 命令启动 Python GUI，让 cmd 窗口自动关闭
start "" pythonw clinker_gui.py

REM 如果 pythonw 不可用，尝试使用 python
if errorlevel 1 (
    start "" python clinker_gui.py
)

REM 脚本结束，cmd 窗口自动关闭
exit
