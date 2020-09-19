from flask import Flask, render_template, request

app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req, res, file=log)

@app.route('/search4', methods=['POST']) 
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters)) 
    log_request(request, results)
    return render_template('results.html',
                            the_title=title, 
                            the_phrase=phrase, 
                            the_letters=letters,
                            the_results=results,)

@app.route('/') 
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to... web!')

def search4letters(phrase:str, letters:str='aeiou') -> set:
    return set(letters).intersection(set(phrase))

@app.route('/viewlog')
def view_the_log() -> str:
    with open('vsearch.log') as log:
        contents = log.read()
    return contents

if __name__ == '__main__': 
    app.run(debug=True)