# Xiamen-University-Daily-Health-
##原理：
利用selenium库和chrome-driver 进行网页自动操作
##安装环境
```
pip install selenium
sudo apt-get install chromium
sudo apt-get install chromium-chromedriver
```
## cron自动运行
```
crontab -e

0   8  *   *    *     cd ~; python3 ~/daka.py
```
