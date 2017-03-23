#instantiate trackers
import datetime
from tracker import Tracker, TrackerManager, Position
from customer import Customer, CustomerManager

def addTracker(customer_id, tracker_id):
	tracker_manager.add(tracker_id)
	customer_manager.addTracker(customer_id, tracker_id)

def removeTracker(customer_id, tracker_id):
	# tracker_manager.remove(tracker_id)
	customer_manager.removeTracker(customer_id, tracker_id)


tracker_database = [1,2,3,4,5,6,9]
customer_database = [	{ "id" : 12, "trackers": [1,2,5,6]},
						{ "id" : 13, "trackers": [3,4,9]},	 ]

tracker_manager = TrackerManager(tracker_database)
customer_manager = CustomerManager(customer_database)


# update sensor 2 directly
time1 = datetime.datetime(1989, 12, 13, 17, 31)
pos1 = Position(59.345379, 18.023157)
tracker_manager.get(2).update(time1, pos1)


#Update trackers with Json data (received by the trackers)
json_from_sensor_1 = { "id" : 1, "time" : "2017-03-23T13:31:00", "position" : { "lat" : 59.345379, "long" : 18.023157 } }
json_from_sensor_2 = { "id" : 3, "time" : "2017-03-22T12:12:34", "position" : { "lat" : 59.735593, "long" : 19.234673 } }
json_from_sensor_3 = { "id" : 4, "time" : "2017-03-22T19:01:23", "position" : { "lat" : 58.526638, "long" : 18.426364 } }

tracker_manager.handleUpdate(json_from_sensor_1)
tracker_manager.handleUpdate(json_from_sensor_2)
tracker_manager.handleUpdate(json_from_sensor_3)


# add new tracker to customer 12
addTracker(12, 99)

# remove tracker from customer 12
removeTracker(12, 6)

print("\n----List all customers (with trackers)")
for customer in customer_manager.customers:
	print(customer.id, customer.trackers)

print("\n----List all trackers")
for tracker in tracker_manager.trackers:
	print(tracker)

print("----List customer 12's trackers")
customer = customer_manager.get(12)
for tracker_id in customer.listTrackers():
	print (tracker_manager.get(tracker_id))

print("----List customer 13's trackers")
customer = customer_manager.get(12)
for tracker_id in customer.listTrackers():
	print (tracker_manager.get(tracker_id))

