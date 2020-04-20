from flask import Flask, render_template, request
import db.model as db
import os

dir_name, filename = os.path.split(os.path.abspath(__file__))
os.chdir(dir_name)
app = Flask(__name__, static_url_path='')


@app.route('/')
def hello_world():
    # 本地没有配置nginx代理，本地调试的时候选用上面的
    # ip = request.remote_addr

    print(type(request))
    if 'X-Forwarded-For' in request.headers:
        ip = request.headers['X-Forwarded-For']
    else:
        ip = '6.6.6.6'
    db.add_data(ip)
    return render_template('index_android.html', ip=ip)


if __name__ == '__main__':

    config = {
        'host': '0.0.0.0',
        'port': 443,
        'debug': True,
        'ssl_context': ('cer/1_www.yezixigua.cn_bundle.crt', 'cer/2_www.yezixigua.cn.key'),
    }
    # db.init_data()
    app.run(**config)
