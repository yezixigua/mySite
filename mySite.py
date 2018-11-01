from flask import Flask, render_template

app = Flask(__name__, static_url_path='')


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':

    config = {
        'host' : '0.0.0.0',
        'port' : 3000,
        'debug': True,
    }
    app.run(**config)
