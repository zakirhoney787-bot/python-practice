import requests as req
import pandas as pd
data1 = req.get(
    "https://jsonplaceholder.typicode.com/users"
)
# data=pd.DataFrame(data)
# print(data1.headers["Content-Type"],'\n\n')
# print(data1.headers.keys(),'\n\n')
# print(data1.text,'\n')
# print(data1.json(),'\n')

print(data1.status_code,'\n')
print(data21tus_code)
# print(data1[0]['body'],'\n')
# print(data1[0].keys())
# print(data[8]["company"])

# data2 = req.post(
#     "https://jsonplaceholder.typicode.com/users",json={'zakir':'Honey'}
# ).json()

# print(type(data2))
# print(data2["zakir"])
# print(data2["id"])