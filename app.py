from flask import Flask
app = Flask(__name__)


@app.route("/")
def main():
    return "Welcome people again!! This is weird"

if __name__ == "__main__":
    app.run()
