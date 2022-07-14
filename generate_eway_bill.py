wbns = '''
1513366424421   
1513366605780   
1513366007626   
1513366029481   
'''

wbns = wbns.split('\n')
wbns1 = []
for i in wbns:
    if i != '':
        i = i.replace(" ", '')
        wbns1.append(i)

# print(wbns1)


-------EWAYBILL Generation-------

 p=find_by_wbn(1513342319641)
p.rs - To check if apckage is eligible for ewbn creation or not
p.flags
{u'add_spcfc': False,
 u'can_gen_ewbn': True, = This shpule be tru for ewaybill generation
 u'chk_one_scure': False,
 u'cvd_zn': u'R',
 u'esntl': False,
 u'frgl': None,
 u'is_ewbn_req': True,
 u'is_exmpt': False,
 u'is_rts': True,
 u'otp_secr': False,
 u'per_spcfc': False,
 u'rts': None,
 u'valid_ewbn': False}
p.cl - check the client


p.gst.update({'hsncode':[u'6217', u'6210', u'6015', u'6402', u'6103', u'6111', u'6206', u'6101',u'6201', u'6109', u'6403', u'6110', u'6404', u'6113', u'6114', u'4202', u'6203', u'6504', u'7117', u'7116', u'6104', u'6204', u'3926', u'6211', u'6505', u'6202', u'6403', u'9004', u'6105', u'6214', u'6205', u'6115', u'6212']

})

 u=connection.Ewaybill.find({'wbn':p.wbn})
u[0]
from package.tasks import *
generate_ewbn([p.wbn])