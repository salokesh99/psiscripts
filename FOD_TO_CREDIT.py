# 
# WE NEED TO HIT API



# You may get this approved by anyone mentioned below. 
# Manzil.bhattacharya@delhivery.com, mohammed.ummer@delhivery.com, sambit.sahoo@delhivery.com, saneev.kumar11@delhivery.com, saurabh.singh@delhivery.com

# Please confirm if you want to change the payment mode to "BTC" or Credit, where the client will pay the charges at later stages i.e at the month-end. 



# FOD-CREDIT/BTC
# In HQ
# p['frt_ch']=None
# p['frt_md'] =None

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# %cpaste
# #we change MOP from FOD to credit.
# f=find_by_wbn
# wbn=6842410129124
# f=find_by_wbn
# p=f(wbn)
# p['frt_ch']=None
# p['frt_md']=None
# p.save()
# p=f(wbn)
# print('fre_ch',p.frt_ch, 'frt_md', p.frt_md)
# --


# https://ap-southeast-1.console.aws.amazon.com/dynamodbv2/home?region=ap-southeast-1#item-explorer?initialTagKey=&table=LorryReceiptsDataTable-prod
# freight_mode and freight_charges -->remove in lorry_receipt






# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # FOD to Credit 

# # HQ:-

# # frt_ch=None
# # frt_md =None


# # LM:-

# wbns = [

# 15362710226505

# ]

# for wbn in wbns :
#     p=f(wbn)
#     p.fod_charges=None
#     p.save()
# for wbn in wbns:
#     p=f(wbn)
#     print('fod_charges',p.fod_charges)



# wbns    15362710226505
# for wbn in wbns:
#     p=Package.objects.get(waybill=wbn)
#     p.fod_charges=None
#     p.save()
# for wbn in wbns:
#     p=Package.objects.get(waybill=wbn)
#     print('p.fod_charges', p.fod_charges)



# 230548381 230548294 


Docket No	HQ
223925540,	HONEYWELL 127780 B2B
223925270,	HONEYWELL 127780 B2B
223925287,	HONEYWELL 127780 B2B
223925297,	HONEYWELL 127780 B2B
223925299,	HONEYWELL 127780 B2B
223925788,	HONEYWELL 127780 B2B
222923089,	HONEYWELL 127780 B2B
223925253,	HONEYWELL 127780 B2B
223925709,	HONEYWELL 127780 B2B
223925713,	HONEYWELL 127780 B2B
223925520,	HONEYWELL 127780 B2B
223925544,	HONEYWELL 127780 B2B
223925512,	HONEYWELL 127780 B2B
223925798,	HONEYWELL 127780 B2B
223925797,	HONEYWELL 127780 B2B
223925803,	HONEYWELL 127780 B2B
223925701,	HONEYWELL 127780 B2B
223925828,	HONEYWELL 127780 B2B
223925830,	HONEYWELL 127780 B2B
223925831,	HONEYWELL 127780 B2B
223925832,	HONEYWELL 127780 B2B
223925834,	HONEYWELL 127780 B2B
223945408,	HONEYWELL 127780 B2B
223945443,	HONEYWELL 127780 B2B
223925759,	HONEYWELL 127780 B2B
223925266,	HONEYWELL 127780 B2B
223925631,	HONEYWELL 127780 B2B
222923802,	HONEYWELL 127780 B2B
222923833,	HONEYWELL 127780 B2B
223945426,	HONEYWELL 127780 B2B
223925849,	HONEYWELL 127780 B2B