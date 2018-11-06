

# 建立对应软件的配置软连接，将配置源文件放在项目本地，在对应软件目录下生成链接，链接到本地
ln -s /home/an/gitcode/mySite/config/supervisor.conf /etc/supervisor/conf.d/mySite.conf
ln -s /home/an/gitcode/mySite/config/nginx_config /etc/nginx/sites-enabled/mySite

# 重启服务
sudo service supervisor restart
sudo service nginx restart

