## 斗地主 &nbsp;&nbsp;
[![Build Status](https://travis-ci.org/mailgyc/doudizhu.svg?branch=master)](https://travis-ci.org/mailgyc) &nbsp;&nbsp;
[![Coverage Status](https://coveralls.io/repos/github/mailgyc/doudizhu/badge.svg?branch=master)](https://coveralls.io/github/mailgyc/doudizhu?branch=master) &nbsp;&nbsp;
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)  


斗地主游戏，后端基于Python+Tornado+MySQL开发，前端 Phaser 引擎

修改使得代码可以在windows下运行，修改了一个路径问题

**Dependencies**

* Python3.8+
* Mysql5.7+


Quick Start 主要看我的注释
```shell
    git clone https://github.com/mailgyc/doudizhu
    cd doudizhu
    mysql --user=root -p < schema.sql
    #如果有问题，请不要使用powershell，使用cmd
    # pip3 install -r requirements.txt
    # 我忘记是要装哪些库了，windows不用装uvloop，运行不会报错，别的库根据log提示安装
    cd server
    export DATABASE_URI=mysql+aiomysql://root:123456@127.0.0.1:3306/ddz
    #注意root密码是123456，数据库名是ddz，根据自己情况修改，密码不一样要改成自己的密码，数据库名不一样要改成自己的数据库名
    # 如果数据库连接不上，检查数据库是否启动，数据库用户名密码是否正确，数据库是否创建成功
    #export在windows下是用不了的，所以需要手动设置环境变量，变量名是DATABASE_URI，值是mysql+aiomysql://root:123456@127.0.0.1:3306/ddz
    # 或者：set DATABASE_URI=mysql+aiomysql://root:123456@127.0.0.1:3306/ddz
    python app.py
    # 现在访问 http://127.0.0.1:8080
```


运行截图

![](https://raw.githubusercontent.com/mailgyc/doudizhu/master/screenshot/a.png)
![](https://raw.githubusercontent.com/mailgyc/doudizhu/master/screenshot/c.png)
![](https://raw.githubusercontent.com/mailgyc/doudizhu/master/screenshot/d.png)
