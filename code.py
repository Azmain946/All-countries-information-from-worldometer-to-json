import re
import requests
import json

url='https://www.worldometers.info/geography/alphabetical-list-of-countries/'
res=requests.get(url) #sending requests

page_content=res.text

#using regular expression
regex=re.compile('bold; font-size:15px">(.*?)</td> <td style="font-weight: bold; text-align:right"><a href.*?/">(.*?)</a></td> <td style="text-align:right">(.*?)</td> <td style="text-align:right">(.*?)?</td> </tr> <tr> <td>(.*?)</td>',re.M)
li=regex.findall(page_content)

data={}
data["Country"]=[]

for i in li:
	data["Country"].append({
		"Name":i[0],
		"Population(2020)":i[1],
		"Land Area(Km^2)":i[2],
		"Density(P/km^2)":i[3]
		})
with open("List_of_country.txt",'w',encoding=res.encoding) as outfile: #creating json file
	json.dump(data,outfile)
