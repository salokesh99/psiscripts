%cpaste
#paste this on AWS terminal to change the DCs.
#script to update new dcs for wbns bulk
f=find_by_wbn
#paste the DC Unicode_name here
# new_dc='Faridabad_Sector24_L (Haryana)'
#Paste comma separated (wbn,DC) here
wbn_dcs=[ (15154110483840,	u'Lucknow_OmaxeCity_L (Uttar Pradesh)', u'INUPAREB'),
(14897410138880,	u'Lucknow_OmaxeCity_L (Uttar Pradesh)', u'INUPAREB'),
(14897410158826,	u'Lucknow_OmaxeCity_L (Uttar Pradesh)', u'INUPAREB'),
(15340710025056,	u'Pataudi_Tajnagar_L (Haryana)',        u'INUPAREB'),
(15896224722573,	u'Lucknow_OmaxeCity_L (Uttar Pradesh)', u'INUPAREB'),
(15896224722573,	u'Lucknow_OmaxeCity_L (Uttar Pradesh)', u'INUPAREB'),
(15896224722567,	u'Lucknow_OmaxeCity_L (Uttar Pradesh)', u'INUPAREB'),
(15896226171785,	u'Lucknow_OmaxeCity_L (Uttar Pradesh)', u'INUPAREB')
]
#setting up the new dc. 
for wbn,dc, cnid in wbn_dcs:
    #fetching the DC Code 
    # dc=DeliveryCenter.get_center_from_faas(name_unicode=dc)
    # dc_name=dc.unicode_name
    # dc_code=dc.code
    if dc is not None and cnid is not None :
    #setting up the new dc. 
        p=f(wbn)
        print(wbn, p.cn, p.cnid)
        p.cn=dc
        p.cnid=cnid
        p.save()
    else:
        print('dc_name  not None OR dc_code is not None ', 'dc_name', dc_name, 'dc_code', dc_code)

print('WBNS Updated!!!')

#print New DCs
print('Printing updated Data')

for wbn,_,_ in wbn_dcs:
    p=f(wbn)
    print("NEW DATA - ", wbn , p.cn, p.cnid)

--