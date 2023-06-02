# python进程监视器
监视系统进程和内存占用率，高于70% 即发送邮件到邮箱，低于70% 发送解除警告邮件

## Start
- 1.使用python包管理pip 安装必要的库
```
pip install -r requirements.txt
```

- 2.修改配置文件config.py
  修改下面的内容
  依次为qq号码，qq邮箱，接受人的邮箱，授权码,网卡名称（默认WLAN）
```
    self.qq_number = "xxxxx"
    self.mail = "xxxxx"
    self.receiver = "xxxxx"
    self.pwd = "xxxxx"
    self.network_name = "WLAN"
```

- 3.运行process.py
