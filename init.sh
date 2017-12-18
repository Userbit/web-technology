sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/nginx.conf 
sudo /etc/init.d/nginx restart
sudo gunicorn -c /home/box/web/hello.cfg hello:app
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start
#sudo ln -sf /home/box/web/hello.cfg /etc/gunicorn.d/hello.py
