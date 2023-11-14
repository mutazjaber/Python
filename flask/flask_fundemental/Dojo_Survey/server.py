from flask import Flask ,redirect ,render_template ,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    data = {
    "name"  : request.form['username'],
    "location":request.form['location'],
    "fav" : request.form['language'] ,
    "Comment" : request.form['Comment']
    }
    return render_template('result.html',data=data)




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)