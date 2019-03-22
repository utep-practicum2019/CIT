import re


class Session():
	username = ""
	public_ip = "192.168.0.1"
	start_time = "-"
	end_time = "-"
	status = "disconnected"
	connection_type = ""

	def __init__(self, username, public_ip, start_time, end_time, status, connection_type):
		self.username = username
		self.public_ip = public_ip
		self.start_time = start_time
		self.end_time = end_time
		self.status = status
		self.connection_type = connection_type

	def get_status(self):
		if self.end_time == '-':
			self.status = "connected"
		else:
			self.status = "disconnected"
		return self.status

	def validity_check(self):
		error_code = []
		if type(self.username) != str or self.username.find("user") == -1:
			error_code.append("Invalid username")
		if type(self.public_ip) != str or not re.match('(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))', self.public_ip):
			error_code.append("Invalid IP address")
		if type(self.start_time) != str or not re.match('^([0-1][0-9]|[2][0-3]):([0-5][0-9])$', self.start_time):
			error_code.append("Invalid start time")
		if type(self.end_time) != str or not re.match('^([0-1][0-9]|[2][0-3]):([0-5][0-9])$', self.end_time) and self.end_time != "-":
			error_code.append("Invalid end time")
		if type(self.status) != str or self.status != "disconnecting" and self.status != "connected":
			error_code.append("Invalid status")
		if type(self.connection_type) != str or self.connection_type not in "ppp":
			error_code.append("Invalid connection type")
		return error_code
