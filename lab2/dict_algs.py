
ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
       }, {
        "name": "petya",
        "age": 10,
    }],
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [ {
        "name": "kirill",
        "age": 21,
       }, {
        "name": "pavel",
        "age": 15,
    }],
}

emps=[ivan,darja]

for i in emps:
    for j in i.get("children"):
        if j.get("age")>=18:
            print(i.get("name"))
            break
