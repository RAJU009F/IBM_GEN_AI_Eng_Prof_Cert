"""

Flask app test app creation 

"""
from flask import Flask

app = Flask("Flask App ")

@app.route("/")
def main():
    """
    home method for default route
    """
    return {"message":"Hello world"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5050', debug=True)
