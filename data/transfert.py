import json
from firebase import firebase

firebase = firebase.FirebaseApplication('https://la-panacee.firebaseio.com/catalogue', None)


with open("lapanarchive.json") as json_file:
    json_data = json.load(json_file)
    for aw in json_data:
    	aw.pop("id")
    	artists = aw["artists"]
    	aw.pop("artists")
    	aw["artists"] = []
    	for a in artists:
    		aw["artists"].append(a.title())
    	firebase.post('/artworks', aw)


