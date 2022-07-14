%cpaste
lrns = '''
225060766 
225060765
'''

lrns = lrns.split('\n')
lrns1 = []
for i in lrns:
    if i != '':
        i = i.replace(" ", '')
        lrns1.append(i)

print(lrns1)
lrns = lrns1
wbns = []

# print(lrns)
for i in lrns :
    data = get_package_from_lrn([i])
    # print(data)
    wbns.append(data[0])

print("wbns  -------- ", wbns)


for i in wbns :
    p=f(i)
    try: 
        print(i, "P-NCC", p.ncc, "P.cs.ss, st", p.cs.st, p.cs.ss, p.cs.sr)
    except:
        print(i, "NO NCC Found!!!", "P.cs.ss, st", p.cs.st, p.cs.ss, p.cs.sr)

--