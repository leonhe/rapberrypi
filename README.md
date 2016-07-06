##Rapberry PI Script Tools
====
树莓派中正在使用的一些脚本
====
## 相关目录说明
 * [domain](/domain) : 域名相关
   - domain_update.py
     根据万网域名API在路由器外网IP地址发生变动时自动更新域名的绑定IP
     1. `sudo pip install aliyunsdkcore`
     2. 更新脚本文件中你的AccessKey，AccessSecret，需要修改的域名
     3. 在树莓派中执行：`sudo cronetab -e`
     4. 在文件尾加入：`*/15 * * * * /usr/bin/python domain_update.py文件的绝对路径`

