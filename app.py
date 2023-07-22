from flask import Flask, render_template, request
from func import solve

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lhs = request.form['lhs']
        rhs = request.form['rhs']
        var = 'x'

        solution = solve(lhs, rhs, var)

        return render_template('index.html', solution=solution)
    
    return render_template('index.html', solution='')

if __name__ == "__main__":
    app.run()