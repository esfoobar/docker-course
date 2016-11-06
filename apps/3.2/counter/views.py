from app import app

@app.route('/')
def init():
    return "Hello, World"
