
# 每次都需要手动更新supervisord 不太清楚原因

# 需要添加该数据库权限部分
sudo chmod 777 db/test3.db

# 关闭服务
supervisorctl stop mySite
service nginx stop

# 删除原本建立的软连接
rm /etc/supervisor/conf.d/mySite.conf
rm /etc/nginx/sites-enabled/mySite

# 建立对应软件的配置软连接，将配置源文件放在项目本地，在对应软件目录下生成链接，链接到本地
ln -s /home/an/space/mySite/config/supervisor.conf /etc/supervisor/conf.d/mySite.conf
ln -s /home/an/space/mySite/config/nginx_config /etc/nginx/sites-enabled/mySite

supervisorctl reload

# 重启服务
supervisorctl start mySite
service nginx restart

