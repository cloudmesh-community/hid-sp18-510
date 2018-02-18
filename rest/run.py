from eve import Eve
import platform
import psutil
import json
import flask	
from flask import Response
import getpass
import shutil

app = Eve()

def format_response(resp_data):
	response = Response()
	response.headers["status"] = 200
	response.data = resp_data
	return response

@app.route('/processor', methods=['GET'])	
def get_processor():
	proc =  platform.processor()
	resp_data = {'processor_name' : proc}
	fmtd_resp = flask.jsonify(**resp_data)
	#fmtd_resp =  format_response(resp_data)
	return fmtd_resp

@app.route('/cpu/count', methods=['GET'])
def get_cpu_count():
	cpu =  psutil.cpu_count()
	resp_data = {'cpu_count' : cpu}
	fmtd_resp = flask.jsonify(**resp_data)
	#fmtd_resp =  format_response(resp_data)
	return fmtd_resp

@app.route('/cpu/stats', methods=['GET'])
def get_cpu_stats():
	cpu =  psutil.cpu_stats()
	data = cpu.__dict__
	fmtd_resp = flask.jsonify(**data)
	#fmtd_resp =  format_response(data)
	return fmtd_resp

@app.route('/disk/usage', methods=['GET'])	
def get_disk_usage():
	du = psutil.disk_usage('/')
	data = du.__dict__
	#fmtd_resp =  format_response(data)
	fmtd_resp = flask.jsonify(**data)
	return fmtd_resp

@app.route('/mem', methods=['GET'])	
def get_mem():
	vm = psutil.virtual_memory()
	data = vm.__dict__
	#fmtd_resp =  format_response(data)
	
	fmtd_resp = flask.jsonify(data)
	return fmtd_resp
	
if __name__ == '__main__':
	app.run()

