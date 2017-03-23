class CustomerManager():
	def __init__(self, data_list = None):
		if data_list == None:
			#read from database
			self.customers = []
		else:
			#read from dummy-data if present
			self.customers = []
			for customer in data_list:
				id = customer["id"]
				trackers = customer["trackers"]
				self.customers.append(Customer(id,trackers ))


	def get(self, id):
		for customer in self.customers:
			if customer.id == id:
				return customer

	def addTracker(self, customer_id, tracker_id):
		self.get(customer_id).addTracker(tracker_id)

	def removeTracker(self, customer_id, tracker_id):
		self.get(customer_id).removeTracker(tracker_id)


class Customer():
	def __init__(self, id, trackers):
		self.id = id
		self.trackers = trackers #array with sensor id's

	def listTrackers(self):
		return self.trackers

	def addTracker(self, tracker_id):
		self.trackers.append(tracker_id)

	def removeTracker(self, tracker_id):
		while self.trackers.count(tracker_id) > 0:
			self.trackers.remove(tracker_id)