from flask import Flask , render_template
import string
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html', count=3, color='blue')
@app.route('/play/<x>')
def play_x(x):
    return render_template('index.html', count=int(x), color='blue')

@app.route('/play/<int:x>/<color>')
def play_x_color(x,color):
    return render_template('index.html', count=int(x), colore=color)


if __name__ == '__main__':
    app.run(debug=True)
