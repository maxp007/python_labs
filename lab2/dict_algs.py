
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
    for j in i.pop("children"):
        if j.pop("age")>=18:
            print(i.pop("name"))
            break;
