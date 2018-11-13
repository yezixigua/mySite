from flask import Flask, render_template, request
import db.model as db
import os

dir_name, filename = os.path.split(os.path.abspath(__file__))
os.chdir(dir_name)
app = Flask(__name__, static_url_path='')


@app.route('/')
def hello_world():
    ip = request.remote_addr
    print(ip)
    db.add_data(ip)
    return render_template('index.html', ip=ip)


if __name__ == '__main__':

    config = {
        'host': '0.0.0.0',
        'port': 3000,
        'debug': True,
    }
    db.init_data()
    app.run(**config)
