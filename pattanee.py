import requests
import re
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def getTemple():
    return results

url = "https://th.wikipedia.org/wiki/%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B9%83%E0%B8%99%E0%B8%88%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B8%9B%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B2%E0%B8%99%E0%B8%B5"
response = requests.get(url).text


li= re.findall('>(.*?)<', response)
li = [i for i in li if re.match('^วัด',i)]
li = [i for i in li if re.match('(?!วัดราษฏร์)',i)]


for i in range(len(li)):
    li[i] = re.sub(" .*", "",  li[i])

result = li[:-4]
results = {"temple": result}
print(len(result))

