from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Flask!<h1>'

@app.route('/signup')
def signup():
    return '회원가입 페이지입니다.'

@app.route('/shopping')
def signup():
    return '쇼핑 페이지입니다.'

# 애플리케이션 실행 코드
if __name__ == '__main__':
    app.run()
