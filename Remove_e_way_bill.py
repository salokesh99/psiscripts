# ---------for remove E waybill------------
p=find_by_wbn(4577311306546)
p.ewbn
[]
p.ewbn=[]
p.save()
u=connection.Ewaybill.find({'wbn':p.wbn})
u[0]
# {u'_id': ObjectId('60250918e131d8354bf65e6b'),
# u'date': {u'ext_expiry': datetime.datetime(2021, 2, 13, 8, 23, 27, 992000)},
# u'dcn': u'20654033',
# u'ewbn': u'661266243569',
# u'expiry': datetime.datetime(2021, 2, 20, 0, 0),
# u'is_active': False,
# u'is_valid': False,
# u'rs': 31246.22,
# u'src': u'Manifest',
a=u[0]
a.is_valid=False
a.is_active=False
a.save()

