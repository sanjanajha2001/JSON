import json
a={"name": "David",
     "class":"I",
     "age": 6}
data=open("QUES2.json", "w")

json.dump(a,data, indent = 4)

data.close() 