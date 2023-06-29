from flask import Flask, render_template, session, redirect

app= Flask(__name__)
app.secret_key='secreto'

@app.route("/")
def contar():
    session['contador'] = session.get('contador', 0) + 1
    return render_template('index.html', contador=session['contador'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect ("/")

if __name__=="__main__":
    app.run( debug=True, port=5000)