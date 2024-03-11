# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/url/task')
def task_page():
    return render_template('task.html')

if __name__ == '__main__':
    app.run(port=8000, debug=True)
