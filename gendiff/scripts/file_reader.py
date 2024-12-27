import json


with open('file1.json') as f:
    templates = json.load(f)
with open('file2.json') as f:
    templates2 = json.load(f)

print(f'first: {templates}\n' 
      f'second: {templates2}')

for section, commands in templates.items():
    print(f'{section} : {commands}')

json.load(open('file1.json'))


# for section, commands in templates.items():
#     print(section)
#     print('\n'.join(commands))

