# app.py (updated)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/url/task')
def task_page():
    dynamic_data = "This is dynamic data!"
    return render_template('task.html', dynamic_data=dynamic_data)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
