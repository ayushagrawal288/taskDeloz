import requests, json

token = 'your token'	
auth = {'Authorization': 'token '+str(token)}
url = 'https://api.github.com/search/repositories?q=django&sort=stars'

file = open('output1.txt', 'w')
file.write('Name\tScore\tRepo\n')

request = requests.get(url,headers=auth)
data = json.loads(request.content)

if request.ok:
	# print(data.keys(),data['total_count'])
	d = data['items'][:20]
	# print(len(d))
	for i in range(len(d)):
		# print(d[i]['name'],d[i]['score'],d[i]['full_name'])
		file.write(d[i]['name']+'\t'+str(d[i]['score'])+'\t'+d[i]['full_name']+'\n')
# print(request.url,request.json)