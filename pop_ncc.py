%cpaste
# from dataclasses import replace


wbns = '''
13458210042630
28449199093844
1831010051634
'''
wbns = wbns.split('\n')
wbns1 = []
for i in wbns:
    if i != '':
        i = i.replace(" ", '')
        wbns1.append(i)

print(wbns1)
wbns = wbns1

# print(wbns)
for i in wbns :
    p=find_by_wbn(i)
    try: 
        print(p.ncc)
    except:
        print('No NCC')


    p.pop('ncc', None)
    p.save()

for i in wbns :
    p=find_by_wbn(i)
    try: 
        print(p.ncc)
    except:
        print('No NCC')
--