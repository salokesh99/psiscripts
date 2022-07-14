%cpaste
#paste this on AWS terminal to change the DCs.
#script to update new dcs for wbns bulk
f=find_by_wbn
#paste the DC Unicode_name here you may paste without state as well.
new_dc='Gurgaon_Sector17_L'
#Paste comma separated wbns here
wbns=[
15092910010500,
12331510002236,
14751010017662,
15346010007206,
15346010007254,
9320210209344,
2394912285835,
3851610220345,
3851610220356,
3851610220371,
5327110448431,
7110310000543

]
#fetching the DC Code 
dc=DeliveryCenter.get_center_from_faas(name_unicode=new_dc)

dc_name=dc.unicode_name
dc_code=dc.code

#setting up the new dc. 
for i in wbns:
    if dc_name is not None and dc_code is not None :
        p=f(i)
        print(i, p.cn, p.cnid)
        p.cn=dc_name
        p.cnid=dc_code
        # p.pin=141112
        p.save()
    else:
        print('dc_name  not None OR dc_code is not None ', 'dc_name', dc_name, 'dc_code', dc_code)
    

print('WBNS Updated!!!')

#print New DCs
print('Printing updated Data')

for i in wbns:
    p=f(i)
    print("NEW DATA - ", i, p.cn, p.cnid)

--