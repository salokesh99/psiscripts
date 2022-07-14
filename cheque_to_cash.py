%cpaste
# from dataclasses import replace


wbns = '''
11168810218267   
11168810231802   
11168810232093   
11168810232122   
14913710000766   
15022910011981   
17780710004362 
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
# for i in wbns :
#     p=find_by_wbn(i)
#     p.pop('txtyp', None)
#     p.save()

for i in wbns :
    p=find_by_wbn(i)
    try: 
        print('p.txtyp', p.txtyp)
    except :
        print('No Txtyp, cash may be...')

--