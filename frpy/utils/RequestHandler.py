import requests

class RequestHandler:
	__session = None
	@staticmethod
	def request(*args, **kwargs):
		args = list(args)
		app_signed_request = kwargs.pop('token', RequestHandler.__session and RequestHandler.__session.get('token') if args[-1] != False else None)
		if isinstance(args[-1], bool):
			if args[-1] == True and not RequestHandler.__session.get('token'):
				raise Exception("Client is not logged in!")

		method = kwargs.pop('method', 'get')
		response = getattr(requests, method)(f'https://www.freeriderhd.com{kwargs.pop("path", args.pop(0))}?ajax=true&t_1=ref&t_2=desk&app_signed_request=' + app_signed_request, **kwargs)
		response.raise_for_status()  # raises exception when not a 2xx response
		if response.status_code != 204:
			if response.headers['content-type'].strip().startswith('application/json'):
				response = response.json()
				if response.get('result') == False or response.get('code') == False:
					raise Exception(response.get('msg'))
				return response
			return response.text

	@staticmethod
	def get(*args, **kwargs):
		return RequestHandler.request(*args, **kwargs)

	@staticmethod
	def post(*args, **kwargs):
		return RequestHandler.request(*args, **kwargs, method = 'post')

	@staticmethod
	def assertToken(token):
		response = RequestHandler.get('/account/settings', token = token)
		if 'user' not in response:
			raise Exception("Invalid token!")

		RequestHandler.__session = {
			'token': token,
			'user': response.get('user')
		}

		return response.get('user')

	@staticmethod
	def deleteToken():
		RequestHandler.__session = None

	@staticmethod
	def clientUser():
		return RequestHandler.__session and RequestHandler.__session.get('user')