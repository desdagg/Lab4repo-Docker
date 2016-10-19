from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route("/hello")
def hi():
	return "hello\n"

@app.route("/user/<username>")
def user(username):
	return 'user %s ' % username

@app.route("/post/80")
def post():
	return "Post 80\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

