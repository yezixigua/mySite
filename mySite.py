from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='')


@app.route('/')
def hello_world():
    ip = request.remote_addr
    return render_template('index.html', ip=ip)


if __name__ == '__main__':

    config = {
        'host': '0.0.0.0',
        'port': 3000,
        'debug': True,
    }
    app.run(**config)
