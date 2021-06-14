from flask import render_template
import os

from myproject import app


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host="172.0.0.1", port=int(os.environ.get("PORT", 5000)), debug=True)