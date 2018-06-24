from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
from note import *

app = Flask(__name__)


@app.route('/', methods={'GET'})
def base():
	return render_template('base.html')


@app.route('/create', methods={'POST', 'GET'})
def create():

	if request.method == 'POST':
		title = request.form['title']
		text = request.form['text']

		create_note(title=title, text=text)
		return redirect(url_for('info'))

	return render_template('create.html')


@app.route('/info', methods={'GET'})
def info():
	results = get_notes()
	return render_template('info.html', results = results)


@app.route('/change', methods={'POST', 'GET'})
def change():

	if request.method == "POST":
		note_id = request.form['note_id']
		title = request.form['title']
		text = request.form['text']
		change_note(note_id=note_id, title=title, text=text)
		return redirect(url_for('info'))

	return render_template('change.html')


@app.route('/delete', methods={'POST', 'GET'})
def delete():
	
	if request.method == 'POST':
		note_id = request.form['note_id']

		delete_note(note_id=note_id)
		return redirect(url_for('info'))

	return render_template('delete.html')


if __name__ == '__main__':
	app.run(host='127.0.0.1',port = 8080,debug = True)