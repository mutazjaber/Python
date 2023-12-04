from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def countVisits():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1

    return render_template('Counter.html', name_on_template=session['count'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return render_template('Counter.html')


if __name__ == "__main__":
    app.run(debug=True)