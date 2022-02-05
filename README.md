# Xiamen-University-Daily-Health-
##功能：

本程序是基于Python的selenium库进行代替自己的操作，将进入网页打卡，变为双击程序打卡，有心的同学可以将程序设置为windows开机自动运行或者直接在Linux 中设置定时运行，这里只提供模板，欢迎大家探索知识。

##原理：

利用selenium库和chrome-driver 进行网页自动操作

##安装环境
安装selenium库和chromium和对应的driver
```
pip install selenium
sudo apt-get install chromium
sudo apt-get install chromium-chromedriver
```
## cron自动运行

cron 中自动运行

```
crontab -e

0   8  *   *    *     cd ~; python3 ~/daka.py
```
