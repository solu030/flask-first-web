from flask import Flask,render_template

app = Flask(__name__)

@app.route('/show/info')
def index():
    return render_template('main_web.html')

@app.route('/get/news')
def news():
    return render_template('news.html')

@app.route('/goods/list')
def goods():
    return render_template('goods.html')

@app.route('/user/list')
def user():
    return render_template('user.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run()