from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html><meta charset="utf-8"><body>
    <h3>XSS脆弱性を持つページ</h3>
    <h3>「< script>alert('hello')< /script>」(<の後ろのスペースは削除)をフォームに入力するとスクリプトが実行される
    <form action="/kakunin" method="get">
    名前： <input name="name">
    <input type="submit" value="送信">
    </form></body></html>
    '''

@app.route('/kakunin')
def kakunin():
    name = request.args.get('name', '')
    return '''
    <html><meta charset="utf-8"><body>
    <h1>名前は、{0}さんです。</h1>
    </body></html>
    '''.format(name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')