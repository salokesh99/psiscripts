%cpaste
from bag.tasks import *
# put bag id in there in bs
bs=[

'BAG704930462',
'BAG364760626'

]
for b in bs:
    p=find_by_bs(b)
    #change the name
    p.s.append({u'sd': datetime.datetime.now(),u'sl':p.cs.sl,'slid':p.cs.slid,u'ss': u'Complete',u'sr':u'As Requested',u'u':u'Lokesh.k4',u'ud': datetime.datetime.now()})
    p.cs=p.s[-1]
    super(Bag, p).save()
--




# bs = ''' 
# ''' 
# bs = bs.split('\n') 
# bs.remove('') 
# len(bs) 
 
# for t in bs: 
# p = find_by_bs(str(t)) 
# if type(p) != 'NoneType': 
# print(type(p)) 
# p.s.append({u'sd': datetime.datetime.now(),u'sl':p.cs.sl,'slid':p.cs.slid,u'ss':u'Complete',u'sr':u'As Requested by ops',u'u':u'mukti.das',u'ud': datetime.datetime.now()}) 
# p.cs=p.s[-1] 
# super(Bag, p).save()