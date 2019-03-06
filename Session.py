
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
		self.connection_type
     
	def get_status(self):
		return end_time == '-'
