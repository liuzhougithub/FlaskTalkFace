from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>简单Demo</title>
    </head>
    <body>
        <h1>输入0获取特定文字</h1>
        <form action="/" method="post">
            <input type="text" name="number" />
            <input type="submit" value="提交" />
        </form>
        {% if message %}
            <p>{{ message }}</p>
        {% endif %}
    </body>
    </html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ''
    if request.method == 'POST':
        number = request.form['number']
        if number == '0':
            message = '这里是0'
    return render_template_string(HTML, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

