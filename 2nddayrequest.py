#tutorial used- https://www.youtube.com/watch?v=tb8gHvYlCFs
import requests
payload={'page':2,'count':25}
r=requests.get(' https://imgs.xkcd.com/comics/angular_momentum.jpg')
print(r)
print (dir(r))
print(help(r))
print(r.text)
print(r.content)
with open ('asdasa.png','wb')as f:
    f.write(r.content)
print(r.status_code)
print(r.ok)
print(r.headers)
r=requests.get('https://httpbin.org/get',params=payload)
print(r.text)
payload={'username':'nikhil','password':'testing'}
r=requests.post('https://httpbin.org/post',data=payload)
print(r.text)
print(r.json())
rdict=r.json()
print(rdict['form'])
r=requests.get('https://httpbin.org/basic-auth/nikhil/dugar',auth=('nikhil','dugar'))
print(r)
r=requests.get('https://httpbin.org/delay/6',timeout=3)
print(r)
