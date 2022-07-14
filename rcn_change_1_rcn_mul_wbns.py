%cpaste
#paste this on AWS terminal to change the DCs.
#script to update new dcs for wbns bulk
f=find_by_wbn
#paste the DC Unicode_name here
new_dc='Karnal_Gharaunda_D'
# rpin = 122004 
# radd = [u'FRUGAL LOGISTICS PVT LTD KHASARA NO-100/73, OPP. GOVT. PRIMARY SCHOOL, VILLAGE SIHI, MAIN ROAD SIHI-KHERKI DAULA, DISTT. GURGAON- 122004(HR)']
#Paste comma separated wbns here you may paste without state as well.
wbns='''
14907313767726
14907331645763
14907338397576
149082588708263
149082605625104
149082605867960
149082607171360
149082620017303
149082620676832
149082644522074
149082652401580
149082652551855
149082663100332
19504803653744
19504816726056
19504822590855
3448341825076
5931438365921
5931439346934
5931439570676
5931440075730
5931440224071
5931440421681
5931440452783
5931441082610
5931441108160
5931441358616
5931441547723
5931441637312
5931441746733
5931441775794
5931441803175
5931442127861
5931442248854
5931442699422
5931442826111
5931442945940
5931443011375
5931443154831
5931443159451
5931443170334
5931443245606
'''

wbns = wbns.split('\n')
wbns1 = []
for i in wbns:
    if i != '':
        i = i.replace(" ", '')
        wbns1.append(i)

# print(wbns1)
wbns = wbns1


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
for wbn in wbns:
    p=f(wbn)
    print("NEW DATA - ", "WBN -- ",wbn, "Rcn -", p.rcn, "RCN ID - ", p.rcnid )
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#fetching the DC Code 
dc=DeliveryCenter.get_center_from_faas(name_unicode=new_dc)
dc_name=dc.unicode_name
dc_code=dc.code

#setting up the new dc. 
for i in wbns:
    p=f(i)
    print("RETURN CENTRE DATA --- @@@@@@@@@$$$$$$",i, p.rcn, p.rcnid)
    if dc_name is not None and dc_code is not None :
        p.rcn=dc_name
        p.rcnid=dc_code

        ###############
        ###############
        # p.rpin = rpin
        # p.radd = radd

        p.save()
    else:
        print('dc_name  not None OR dc_code is not None ', 'dc_name', dc_name, 'dc_code', dc_code)

print('WBN RCNs are Updated!!!')

#print New DCs
print('Printing updated Data')

for wbn in wbns:
    p=f(wbn)
    print("NEW DATA - ", "WBN -- ",wbn, "RCN - ", p.rcn, "RCNID - ", p.rcnid)
    # print(p.radd)
--