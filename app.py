from flask import Flask, render_template
from question import question_bp

app = Flask(__name__)

app.register_blueprint(question_bp, url_prefix='/question')

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/code')
def code():
    return render_template('code.html')

@app.route('/pdf')
def pdf():
    return render_template('pdf.html')

@app.route('/office/<type>')
def office(type):
    return render_template(f'office/{type}.html')

if __name__ == '__main__':
    app.run(debug=True)