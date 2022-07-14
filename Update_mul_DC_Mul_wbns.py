%cpaste
#paste this on AWS terminal to change the DCs.
#script to update new dcs for wbns bulk
f=find_by_wbn
#paste the DC Unicode_name here
# new_dc='Faridabad_Sector24_L (Haryana)'
#Paste comma separated (wbn,DC) here
wbn_dcs=[ 

(12331510002004  , 		'Gurgaon_Sector17_L'),
(14716010033224   ,	 	'Gurgaon_Sector17_L'),
(14821210000313   	 ,   'Gurgaon_Sihi_L'),
(14938910008665  , 		'Gurgaon_Sihi_L'),
(14938910008676  , 		'Gurgaon_Sihi_L'),
(15145710003835   	 ,   'Gurgaon_Sihi_L'),
(15173010023553   	 ,   'Gurgaon_Sector17_L'),
(15286010002262   	 ,   'Gurgaon_Sector17_L'),
(15310710002494   	 ,   'Gurgaon_Sector17_L'),
(15310710002520   	 ,   'Gurgaon_Sector17_L'),
(15310710002531   	 ,   'Gurgaon_Sector17_L'),
(15310710002542   	 ,   'Gurgaon_Sector17_L'),
(15310710002553   	 ,   'Gurgaon_Sector17_L'),
(15310710002564   	 ,   'Gurgaon_Sector17_L'),
(15310710002575   	 ,   'Gurgaon_Sector17_L'),
(15327610001676   	 ,   'Gurgaon_Sector17_L'),
(15337610013705   	 ,   'Gurgaon_Sector17_L'),
(15713210002192   	 ,   'Gurgaon_Sihi_L'),
(15896222622793  , 		'Gurgaon_Sihi_L'),
(15896223277577  , 		'Gurgaon_Sihi_L'),
(4377510029935   	 ,   'Gurgaon_Sector17_L'),
(4617113086915   	 ,   'Gurgaon_Sihi_L'),
(4617113170871   	 ,   'Gurgaon_Sihi_L'),
(4842811487975  , 		'Gurgaon_Sector17_L')





]
#setting up the new dc. 
for wbn,dc in wbn_dcs:
    #fetching the DC Code 
    dc=DeliveryCenter.get_center_from_faas(name_unicode=dc)
    dc_name=dc.unicode_name
    dc_code=dc.code
    if dc_name is not None and dc_code is not None :
    #setting up the new dc. 
        p=f(wbn)
        print(wbn, p.cn, p.cnid)
        p.cn=dc_name
        p.cnid=dc_code
        p.save()
    else:
        print('dc_name  not None OR dc_code is not None ', 'dc_name', dc_name, 'dc_code', dc_code)

print('WBNS Updated!!!')

#print New DCs
print('Printing updated Data')

for wbn,_ in wbn_dcs:
    p=f(wbn)
    print("NEW DATA - ", wbn , p.cn, p.cnid)

--