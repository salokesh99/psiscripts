%cpaste
wbns = '''
14810010290614

14810010290872
14810010290625   
14810010290636   
14810010290640   
14810010290651   
14810010290662   
14810010290673   
14810010290684   
14810010290695   
14810010290706   
14810010290710   
14810010290721   
14810010290732   
14810010290743   
14810010290754   
14810010290765   
14810010290776   
14810010290780   
14810010290791   
14810010290802   
14810010290813   
14810010290824   
14810010290835   
14810010290846   
14810010290850   
14810010290861
'''

wbns = wbns.split('\n')
wbns1 = []
for i in wbns:
    if i != '' :
        i = i.replace(" ", '')
        wbns1.append(i)

# print(wbns1)
wbns = wbns1

for i in wbns :
    p=f(i)
    try: 
        print(i, "P-NCC", p.ncc, "P.cs.ss, st", p.cs.nsl, p.cs.st, p.cs.ss)
    except:
        print(i ,"NO NCC Found!!!", "P.cs.ss, st", p.cs.st, p.cs.ss, p.cs.sr, 'dd.ID - ',p.dd.id, p.dd.t, p.cs.sl, p.cs.cn, p.pin, p.add )

--

print p.add_status(datetime.datetime.now(),p.cs.sl,'As Requested-by ops','Manifested','lokesh.k4', st=p.cs.st,nsl_code='U-PIE') 