import json
dic1={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
file=open("QUES9.json","w")
a=json.dump(dic1,file,indent=6)
file.close()