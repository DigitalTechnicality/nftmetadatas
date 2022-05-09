import json
import os

tracker = 0
os.chdir('/Users/adam/PycharmProjects/pythonProject2')
print(os.getcwd())
for file in os.listdir('wosassets'):
    #print(files)
    name = file[-1]
    full_filename = "%s/%s" % ('/Users/adam/PycharmProjects/pythonProject2/wosassets', file)
    if name == 'n':
        with open(full_filename, 'r') as f:
            data = json.load(f)
            new_list = data['attributes'][0]
            lister2 = []
            lister2.append(new_list)
            data['attributes'] = lister2
    #print(lister2)
    #json.dump(data, f)

    #with open(files, 'w') as f:
    #print("here")
    #json.dump(data, f)

        with open(full_filename, 'w') as f:
            print("here")
            json.dump(data, f)
            #tracker += 1
            #print(name)

    #print(tracker)



#print(data['collection'])
#print(data['attributes'][0])
#data['attributes'] = data['attributes'][0]
#new_list = data['attributes'][0]
#json_dump = json.dumps(new_list)
#lister = []
#lister2 = []
#lister.append(json_dump)
#lister2.append(new_list)
#print(lister)
#print(lister2)
#print(new_list)
#data['attributes'] = lister2
#del data['attributes']
#print(data)
