keys=["name","designation","age","salary"]
emp1=["neelam","programer","24","2400",]
i=0

my_dic1={}
length=len(keys)
while i<length:
    new_dict={keys[i]:emp1[i]}
    my_dic1.update(new_dict)
    i=i+1
d="employee1",(my_dic1)

emp2= ["komal","trainer","24","20000"]
i=0
my_dic2={}
length=len(keys)
while i<length:
    new_dict={keys[i]:emp2[i]}
    my_dic2.update(new_dict)
    i=i+1
c="employee2",(my_dic2)

emp3= ["anuradha","HR","25","40000"]
i=0
my_dic3={}
length=len(keys)
while i<length:
    new_dict={keys[i]:emp3[i]}
    my_dic3.update(new_dict)
    i=i+1
b="employee3",(my_dic3)

emp4= ["Abhishek","manager","29","63000"]
i=0
my_dic4={}
length=len(keys)
while i<length:
    new_dict={keys[i]:emp4[i]}
    my_dic4.update(new_dict)
    i=i+1
a="employee4",(my_dic4)
f=a,b,c,d


import json
l=open("mydoc.json","w")
json.dump(f,l,indent=3)
l.close()
