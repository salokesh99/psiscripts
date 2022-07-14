%cpaste
#paste this on AWS terminal to change the DCs.
#script to update new dcs for wbns bulk
f=find_by_wbn
#paste the DC Unicode_name here
# new_dc='Faridabad_Sector24_L (Haryana)'
#Paste comma separated (wbn,DC) here
wbn_dcs=[ 





]
#setting up the new dc. 
for wbn, dc in wbn_dcs:
    #fetching the DC Code 
    dc=DeliveryCenter.get_center_from_faas(name_unicode=dc)
    dc_name=dc.unicode_name
    dc_code=dc.code
    if dc_name is not None and dc_code is not None :
    #setting up the new dc. 
        p=f(wbn)
        print(wbn, p.rcn, p.rcnid)
        p.rcn=dc_name
        p.rcnid=dc_code
        # p.radd = radd
        p.save()
    else:
        print('rdc_name  not None OR dc_code is not None ', 'rCN_name', dc_name, 'rCN_code', dc_code)

print('WBNS Updated!!!')

#print New DCs
print('Printing updated Data')

for wbn,_  in wbn_dcs:
    p=f(wbn)
    print("NEW DATA - ", wbn , p.rcn, p.rcnid)

--