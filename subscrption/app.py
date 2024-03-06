from flask import Flask


app = Flask(__name__)
app.register_blueprint(, url_prefix='/api')
@app.route('/')
def root():
    return """
    <h1>Subscription module</h1>
    """


if __name__ == '__main__':
    app.run(debug=True)
