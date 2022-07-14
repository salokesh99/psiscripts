%cpaste
wbns = [ 15131310053690,
15131310053701,
15131310053712,
15131310053723
]

for i in wbns :
    p=f(i)
    print(p.cs.st, p.cs.ss, p.cs.sr )
--

%cpaste
wbns = [ 

15896224407177,
15896226036147
]

for i in wbns :
    p=f(i)
    print(p.cs.st, p.cs.ss, p.cs.sr , p.cn, p.rcn )
    print(p.cs.sl)
    # print p.add_status(datetime.datetime.now(),p.cs.sl,'As Requested-by ops','In Transit','lokesh.k4', st=u'UD')


    # print p.add_status(datetime.datetime.now(),p.cs.sl,'As Requested','In Transit','lokesh.k4', st='RT',nsl_code=u'U-')


    print p.add_status(datetime.datetime.now(),p.cs.sl,'As Requested-by ops','In Transit','lokesh.k4', st=u'UD')


for i in wbns :
    p=f(i)
    print(p.cs.st, p.cs.ss, p.cs.sr )
--


