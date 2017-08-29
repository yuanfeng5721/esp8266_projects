# esp8266_projects

这是一个基于Micropython的esp8266工程，是基于mqtt实现远程控制led的功能。需要一块esp8266开发板；一台ubuntu pc，需要配置EMQ mqtt服务器。

## 如何使用 ##
1. esp8266 下载Micropython固件，可以参考[http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html](http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html "esp8266 Mircopython参考文档")
2. 将esp8266_board文件夹中的main.py,subscribe.py两个文件使用uPyLoader传入esp8266开发板中。
3. 在ubuntu pc中配置EMQ mqtt服务器，可以参考[http://emqtt.com/docs/v2/index.html](http://emqtt.com/docs/v2/index.html "EMQ配置文档")
4. 在ubuntu pc上安装python版本的paho mqtt框架
   `pip install paho-mqtt`
   然后运行pc_publish文件夹下的esp8266_pub_led.py
   `python esp8266_pub_led.py`

## 后记 ##
如有问题可以发邮件到wangkun5721@163.com，会尽快给予回复，谢谢！
