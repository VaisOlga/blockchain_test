import json
import os
import uuid
import time

notes_dir = os.curdir + '/notes/'


def note(cur_id, title, text, date_create, date_update):
	data = {'id': cur_id,
			'title': title,
			'text': text,
			'date_create': date_create,
			'date_update': date_update}
	return data


def write(data, file_name):
	with open(file_name, 'w') as file:
		json.dump(data, file, indent=4)		


def create_note(title, text):
	cur_uuid = uuid.uuid4()
	cur_time = int(time.time())
	
	data = note(cur_id=str(cur_uuid), title=title, text=text, date_create=cur_time, date_update=cur_time)

	write(data, notes_dir + str(cur_uuid))


def get_files():
	files = os.listdir(notes_dir)
	return [file for file in files]


def get_notes():
	files = get_files()
	results = []

	for file in files:
		cur_file = json.load(open(notes_dir+file))
		results.append({'id': cur_file['id'],
						'title': cur_file['title'],
						'text': cur_file['text'],
						'date_create': cur_file['date_create'],
						'date_update': cur_file['date_update']})

	return results


def change_note(note_id, title, text):
	file_name = notes_dir + note_id
	if os.path.isfile(file_name):
		cur_file = json.load(open(file_name))

		cur_time = int(time.time())
		data = note(cur_id=note_id, title=title, text=text, date_create=cur_file['date_create'], date_update=cur_time)

		write(data=data, file_name=file_name)


def delete_note(note_id):
	file = notes_dir + note_id
	if os.path.isfile(file):
		os.remove(file)