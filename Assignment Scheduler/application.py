from flask import Flask, render_template

# WSGI Application
app = Flask(__name__, template_folder='templateFiles', static_folder='StaticFiles')

@app.route('/Home')
def home():
    return render_template('ascheduler.html')


@app.route('/')
def index():
    return render_template('ascheduler.html')

@app.route('/sign-up.html')
def sign_up():
    return render_template('sign-up.html')

@app.route('/sign-in.html')
def sign_in():
    return render_template('sign-in.html')

if __name__ == '__main__':
    app.run()
    # app.run(debug = True)