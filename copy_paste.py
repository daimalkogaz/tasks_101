import shutil
import requests
import json

source = input('Where is the file?: ')
destination = input('Where do you want it?: ')
shutil.copy(source, destination)
print('Done')

# GET REQ
# So basically we use the requests.get method that sends the get request towards the localhost link
# and store the reply in the get_req var which if it's 200 (OK) we move to the extraction of the dirtyBytes
# with the help of the json.loads() function we store the response in the data var which we in turn use
# to validate if it is NOT equal to 0, in which case we make another(dangerous) GET request until we are satisfied
# with the result, meaning it is equal to 0

get_req = requests.get('http://localhost:7778/cache/info')
if get_req.status_code == 200:
	data = json.loads(get_req.content)
	while data["dirtyBytes"] != 0:
		get_req = requests.get('http://localhost:7778/cache/info')
		data = json.loads(get_req.content)
	print('dirtyBytes is 0. Upload complete.')
# PUT REQ - self explanatory, really if we followed the syntax of te get request
# we send an empty put to the link below and expect an OK return code, meaning
# the files have been synchronized
put_req = requests.put('http://localhost:7778/app/sync')
if put_req.status_code == 200:
	print('File index changes are synchronized with the cloud')
else:
	print('Uh oh. Something\'s not right')
