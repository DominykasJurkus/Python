from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!' 

@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the universe, and everything', 'eiru,!'))

def search4letters(phrase:str, letters:str='aeiou') -> set:
    return set(letters).intersection(set(phrase))

app.run()