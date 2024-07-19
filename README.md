## 描述

这是一个干超星，模拟正常人刷网课的代码。

## 使用方法

1. 文件夹 `chaoxing` 是已经配置好的 conda 虚拟环境。首先，解压缩然后导入Anaconda,激活该环境。并且要自行下载安装最新版的chrome浏览器。
          当然也可以自行搭建环境，需要安装Anaconda, 创建新虚拟环境后pip安装selenium, requests, bs4, time等库，并自行准备好chromedriver和chrome浏览器。
3. 打开并运行 `attackchaoxing.py`。此时会弹出两个窗口：一个是超星的登录界面，另一个是 Python 终端。
4. 在终端的提示下输入手机号账户和密码（暂时不支持院校登录方式）。登录后，输入要浏览的课程全名（在超星软件中的全名）。此脚本将自动浏览课程章节中的所有视频内容。
5. 刷视频的过程是全自动的，请尽量不要乱点。

## 注意事项

1. 网页窗口一定要打开，强烈建议全屏，最起码要保持窗口大小不变。不要为了挂机而调小窗口，甚至关闭窗口，否则可能会在浏览时出错，导致找不到你要看的课程视频。
2. 代码还在逐渐完善中，难免会出现各种问题。
3. 本代码输入的密码和账号仅用于模拟你学习超星视频课程时的登录，不会被储存或用于其他用途。
4. 由于使用本代码恶意刷课导致超星课程学习出现异常记录、课程不合格等，与本代码作者无关，请自行承担可能的风险。

## 作者信息

一个大三社畜
代码开源且公开，可以随意保存到你的电脑本地复制粘贴和修改，但是禁止拿来倒卖

以下是经过chatgpt翻译后的内容,如有疑问请参照中文版readme.md：
this document is translated by chatgpt, please refer to readme(Chinese).md if you have any problems:

## Description

This is a script for automating video course viewing on the Chaoxing platform, simulating normal user behavior.

## Usage

1. The `chaoxing` folder contains a pre-configured conda virtual environment. First, activate the environment.
2. Open and run `attackchaoxing.py`. This will open two windows: a Chaoxing login page and a Python terminal.
3. In the terminal, you will be prompted to enter your phone number and password (currently, institutional login is not supported). After logging in, enter the full name of the course you want to browse as it appears in the Chaoxing software. The script will automatically browse all video content in the course chapters.
4. The process of watching videos is fully automated. Please avoid clicking around unnecessarily.

## Notes

1. The browser window must remain open. It is strongly recommended to keep it full-screen or at least the same size as when it opened. Do not minimize or close the window to avoid errors in locating the course videos.
2. The code is still being improved and may have various issues.
3. The entered account and password are used solely for simulating login to watch Chaoxing video courses and will not be stored or used for any other purpose.
4. Any issues arising from malicious use of this script, such as abnormal course records or course failures, are not the responsibility of the script author. Use at your own risk.

## Author Information
The code is open source and public. You can freely save, copy, paste, and modify it locally, but reselling it is prohibited. 
