%cpaste
# from dataclasses import replace


wbns = '''
14743610002100   
14751210001330   
14775210009052   
14775210009601   
14913710001175   
15126910017356   
15126910029735   
15254110007475   
15254110007792   
15384610034333   
15384610035000   
15384610035184   
15384610035711   
15585910008886   
17780710002564   
17780710005294   
2331410515712   
2331410536491   
2331410551644   
4841111135691   
4841111137721   
4841111242010   
4841111274044   
4841111290203   
7465610048241  
'''
wbns = wbns.split('\n')
wbns1 = []
for i in wbns:
    if i != '':
        i = i.replace(" ", '')
        wbns1.append(i)

print(wbns1)
for i in wbns :
    p=find_by_wbn(i)
    try: 
        print('p.txtyp', p.txtyp)
    except :
        print(i, 'No Txtyp, cash may be...')

#####################################################

wbns = wbns1

print(wbns)
for i in wbns :
    p=find_by_wbn(i)
#     # print('txtyp', p.txtyp)
#     # p['txtyp']=u'cash'
#     # p.pop('txtyp', None)
    p['txtyp']=u'cheque'
    p.save()

for i in wbns :
    p=find_by_wbn(i)
    try: 
        print('p.txtyp', p.txtyp)
    except :
        print('No Txtyp, cash may be...')

--