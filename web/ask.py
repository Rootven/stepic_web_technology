def app (environ, start_response):
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	resp = "Hello"
	start_response(status, headers)
	return ([bytes(r, 'utf-8') for r in resp])
