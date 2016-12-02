#URL lib Module
import urllib.request
import urllib.parse
#x = urllib.request.urlopen('https://teamplace.volvo.com/sites/3p-Onboard-Telematics/default.aspx')
#print(x.read()) 


#make a search request for keyword basic to pythonprogramming.nt and print out the raw response to the search request.
'''url = 'http://pythonprogramming.net'
values = {'s':'basic', 'submit':'search'}
print (values) 


data = urllib.parse.urlencode(values)
print (data)

data = data.encode('utf-8')
print (data)
req = urllib.request.Request(url, data)
print (req )

resp = urllib.request.urlopen(req )
respData = resp.read()

print (respData)
'''


try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
except Exception as e:
    print (str(e))
#Google will throw 403 rsp.


#Bypassing Googles filter
try:
    url = 'https://www.google.com/search?q=test'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()

except Exception as e:
    print (str(e))
