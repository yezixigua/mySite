from flask import Flask, render_template, request, send_from_directory, abort
import db.model as db
import os, socket, json
from lib import md5util

dir_name, filename = os.path.split(os.path.abspath(__file__))
os.chdir(dir_name)
app = Flask(__name__, static_url_path='')

ads_dict = {}


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


@app.route('/python')
def python_page():
    # 本地没有配置nginx代理，本地调试的时候选用上面的
    # ip = request.remote_addr

    print(type(request))
    if 'X-Forwarded-For' in request.headers:
        ip = request.headers['X-Forwarded-For']
    else:
        ip = '6.6.6.6'
    db.add_data(ip)
    return render_template('index_python.html', ip=ip)


@app.route('/apk')
def download_apk():

    return send_from_directory('apk', "filereader-release.apk", as_attachment=True)


@app.route('/download/<path:url_path>/')
def download(url_path):
    if request.method == "GET":

        file_type = url_path.split('/')[0]
        name = url_path.split('/')[1]
        print(url_path)
        if os.path.isfile(os.path.join(file_type, name)):
            return send_from_directory(file_type, name, as_attachment=True)
        abort(404)


@app.route('/ads')
def request_ads():

    ip = socket.gethostbyname(socket.getfqdn(socket.gethostname()))

    if request.method == "GET":

        pic_dir = os.path.join(os.getcwd(), 'pic')
        pic_list = os.listdir(pic_dir)

        if len(ads_dict) == len(pic_dir):
            return ads_dict
        else:
            for pic in pic_list:
                pic_key = 'http://' + 'www.yezixigua.cn:3000' + '/download/pic/' + pic
                if pic_key not in ads_dict:
                    pic_md5 = md5util.get_file_md5(os.path.join(pic_dir, pic))
                    ads_dict[pic_key] = pic_md5

        return json.dumps(ads_dict)


if __name__ == '__main__':

    config = {
        'host': '0.0.0.0',
        'port': 80,
        'debug': True,
        # 'ssl_context': ('cer/1_www.yezixigua.cn_bundle.crt', 'cer/2_www.yezixigua.cn.key'),
    }
    # db.init_data()
    app.run(**config)
