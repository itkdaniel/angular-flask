import os
from flask import Flask, request, abort, jsonify, send_from_directory, send_file, Blueprint
from werkzeug.utils import secure_filename
from src import UPLOAD_DIRECTORY, logger
from datetime import datetime, timezone,timedelta

logger = logger.create_logger('FileLogger')

files_blueprint = Blueprint('files', __name__)


@files_blueprint.route('/api/files/cwd', methods=['GET'])
def getcwd():
	"""Endpoint to list files on the server."""
	cwd = os.getcwd()
	dirs = os.listdir(cwd)
	return jsonify({'dirs': dirs, 'upload_dir': UPLOAD_DIRECTORY})

@files_blueprint.route('/api/files', methods=['GET'])
def list_files():
	"""Endpoint to list files on the server."""
	files = []
	for filename in os.listdir(UPLOAD_DIRECTORY):
		path = os.path.join(UPLOAD_DIRECTORY, filename)
		if os.path.isfile(path):
			files.append(filename)
	return jsonify(files)

@files_blueprint.route('/api/files/upload', methods=['POST'])
def upload_file():
	"""Upload a file."""
	f = request.files['file']
	filename = secure_filename(f.filename)
	response = f.save(os.path.join(UPLOAD_DIRECTORY,filename))
	file = open(os.path.join(UPLOAD_DIRECTORY,filename),"rb")
	# content = file.read()
	response = {'status': 'success',
				'creation_date':datetime.fromtimestamp(os.path.getctime(os.path.join(UPLOAD_DIRECTORY, filename))),
				'modification_date':datetime.fromtimestamp(os.path.getmtime(os.path.join(UPLOAD_DIRECTORY, filename))),
				'file_size':os.path.getsize(os.path.join(UPLOAD_DIRECTORY, filename)),
				'file_stats':os.stat(os.path.join(UPLOAD_DIRECTORY, filename))}
	return jsonify(response), 201

@files_blueprint.route("/api/files/<path:filename>")
def download_file(filename):
	"""Download a file."""
	response = send_from_directory('api/uploaded_files',filename)
	# return jsonify(UPLOAD_DIRECTORY)
	# response = os.path.join(UPLOAD_DIRECTORY,filename)
	return response, 200

@files_blueprint.route('/api/files/read/<filename>', methods=['GET','POST'])
def read_file_content(filename):
	response = {'status':'failed'}
	filename = secure_filename(filename)
	if os.path.exists(os.path.join(UPLOAD_DIRECTORY,filename)):
		try:
			with open(os.path.join(UPLOAD_DIRECTORY,filename), 'rb') as file:
				content = file.read()
				logger.debug(f'content read before decode - {content}')
				response['status'] = 'success'
				response['content'] = content.decode('ascii')
				data = response['content']
				logger.debug(f'content read after decode - {data}')
				return jsonify(response), 200
		except requests.exceptions.HTTPError as e:
			logger.error(f'ERROR - {e}')
			return jsonify(response), 404
	response['message'] = 'file does not exist'
	return jsonify(response), 404

