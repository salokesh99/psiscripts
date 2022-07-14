%cpaste
wbns = [ ('14907312160412',	172026,	172026,	355640),
('3444229689784',	501359,	248001,	500067),
('3444226116155',	110037,	160062,	110064),
('7582011563332',	700056,	582209,	700056),
('1649811339656',	421302,	673508,	421302) ]


for wbn, fpin, pin, rpin in wbns :
    p=f(wbn)
    print(p.wbn, p.fpin, p.pin, p.rpin)
    p.fpin=fpin
    p.pin = pin
    p.rpin=rpin
    p.save()

for wbn, fpin, pin, rpin in wbns :
    p=f(wbn)
    print(p.wbn, p.fpin, p.pin, p.rpin)
--