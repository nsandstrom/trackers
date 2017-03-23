import datetime

class Tracker():
	def __init__( self, id, time=None, position=None ):
		#constructor with optional time and position
		self.id = id
		self.time = time
		self.position = position

	def update(self, time, position):
		self.time = time
		self.position = position

	def __str__(self):
		return "Tracker id: %s \n Position: %s \n Timestamp: %s \n" % (self.id, self.position, self.time)

class TrackerManager():
	def __init__( self, tracker_list = None):
		if tracker_list == None:
			#read from database
			self.trackers = []
		else:
			#read from dummy-data if present
			self.trackers = []
			for i in tracker_list:
				self.trackers.append(Tracker(i))

	def get(self, id):
		for tracker in self.trackers:
			if tracker.id == id:
				return tracker

	def add(self, id):
		self.trackers.append(Tracker(id))

	def handleUpdate(self, json_data):
		id = json_data["id"]
		time = datetime.datetime.strptime(json_data["time"], '%Y-%m-%dT%H:%M:%S')
		position = json_data["position"]
		tracker = self.get(id)
		if tracker != None:
			tracker.update(time, Position(position["lat"], position["long"]))


class Position():
	def __init__(self, x, y, z=None):
		self.x = x
		self.y = y
		self.z = z

	def height(self):
		return self.z

	def __str__(self):
		#prints position in WGS84-format
		return "%s, %s" % (self.x, self.y)
