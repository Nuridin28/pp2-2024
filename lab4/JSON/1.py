import json

with open("sampleData.json", "r") as js:
    x = json.load(js)


print("Interface Status \n================================================================================")
print("DN                                           Description           Speed    MTU  ")
print("------------------------------------------   -----------           ------  ------")
for i in x['imdata']:
    if(len(i['l1PhysIf']['attributes']['dn']) == 41):
        print(i['l1PhysIf']['attributes']['dn'], '   ', i['l1PhysIf']['attributes']['descr'], '                   ', i['l1PhysIf']['attributes']['speed'], ' ', i['l1PhysIf']['attributes']['mtu'])
    else:
        print(i['l1PhysIf']['attributes']['dn'], '  ', i['l1PhysIf']['attributes']['descr'], '                   ', i['l1PhysIf']['attributes']['speed'], ' ', i['l1PhysIf']['attributes']['mtu'])
    