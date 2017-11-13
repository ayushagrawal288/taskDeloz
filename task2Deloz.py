import requests, json
from pprint import pprint

auth = {'Authorization': 'token 10941eae442b56741da1669807b7d711ae0fe978'}
url = 'https://api.github.com/search/repositories?q=django&sort=stars'

outputfile = open('output2.txt', 'w')
outputfile.write('Library\t\tFrequency\n')

print("It may take a few minutes to fetch the required data")
request = requests.get(url,headers=auth)
data = json.loads(request.content)

if request.ok:
	da = data['items'][:20]
	url2 = 'https://api.github.com/search/code?q=filename:requirements.txt+repo:'
	url3 = 'https://api.github.com/search/code?q=filename:requirements-dev.txt+repo:'
	dic = {}
	for i in range(len(da)):
		req = requests.get(url2+da[i]['full_name'],headers=auth)
		data2 = json.loads(req.content)
		if 'total_count' not in data2.keys():
			continue
		if data2['total_count'] == 0:
			eq = requests.get(url3+da[i]['full_name'],headers=auth)
			data2 = json.loads(req.content)
			if 'total_count' not in data2.keys() or data2['total_count'] == 0:
				continue
		for j in range(len(data2['items'])):
			d = data2['items'][j]
			print(d['url'])
			file = requests.get(d['url'],headers=auth)
			filedata = json.loads(file.content)
			if 'download_url' not in filedata.keys():
				continue
			s = requests.get(filedata['download_url'])
			s=s.content
			s=s.split('\n')
			for k in s:
				if k in dic.keys():
					dic[k]+=1
				else:
					dic[k]=1
	l = sorted(dic.items(), key=lambda x: x[1])
	l.pop()
	for i in range(len(l)):
		outputfile.write(str(l[i])+'\n')
