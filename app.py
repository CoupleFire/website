from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/usaco')
def usaco():
    return render_template('usaco.html')
@app.route('/machinelearning')
def machinelearn():
    return render_template('machinelearning.html')
    
if __name__ == "__main__":
    app.run(debug=True,port=10444)