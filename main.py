import requests
from datetime import datetime

pixep = "https://pixe.la/v1/users"
ptkn = "er3frdvfdv"
puname = "aravindvas"
gid = "graph2"

parm = {
    "token": ptkn,
    "username": puname,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# rsp = requests.post(url=pixep, json=parm)
# print(rsp.text)
#abv 2 lines till creating user only

grep = f"{pixep}/{puname}/graphs"

grphcfg = {
    "id": gid,
    "name": "Python Course Graph",
    "unit":  "hours",
    "type": "float",
    "color": "sora"
}

hdrs = {
    "X-USER-TOKEN": ptkn
}
# rsp = requests.post(url=grep, json=grphcfg, headers=hdrs)
# print(rsp.text)
#abv 2 lines till creating graph only

pixcrt = f"{pixep}/{puname}/graphs/{gid}"

# for z in range(1,6):
tdy = datetime(year=2021, month=6, day=1)

pdat = {
    "date": tdy.strftime("%Y%m%d"),
    # "quantity": input("How many Hours did You spend learning python today?: ")
    "quantity": "2"
}

rsp = requests.post(url=pixcrt, json=pdat, headers=hdrs)
print(rsp.text)
#abv 2 lines used to post data

# ptdate = datetime(year=2021, month=5, day=30)
# putp = f"{pixep}/{puname}/graphs/{gid}/{ptdate.strftime('%Y%m%d')}"
#
# putd = {
#     "quantity": "1"
# }
#
# # rsp = requests.put(url=putp, json=putd, headers=hdrs)
# # print(rsp.text)
# #abv 2 lines used to update existing data
#
# deldate = datetime(year=2021, month=6, day=3)
# delep = f"{pixep}/{puname}/graphs/{gid}/{deldate.strftime('%Y%m%d')}"
#
# # rsp = requests.delete(url=delep, headers=hdrs)
# # print(rsp.text)
# #abv 2 lines used to delete existing data