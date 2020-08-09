from pymongo import MongoClient
import json 
import pprint

client=MongoClient()
db=client.events
with open(r'C:\Users\Prashant\Desktop\data_file.json', encoding='utf-8-sig') as f:
    data=json.load(f)
event=db.event
event.insert_one(data)

#printing the data 
#pprint.pprint(events_data.find_one())
#pprint.pprint(events_data.find({},{"Date":1, "_id":0}))
#print(events_data.index_information())
#pprint.pprint(data.values())
#pprint.pprint(event.find_one())