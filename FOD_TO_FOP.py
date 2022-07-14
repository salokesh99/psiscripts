# You may get this approved by anyone mentioned below. 
# manzil.bhattacharya@delhivery.com, mohammed.ummer@delhivery.com, sambit.sahoo@delhivery.com, saneev.kumar11@delhivery.com, saurabh.singh@delhivery.com

# Please confirm if you want to change the payment mode to "BTC" or Credit, where the client will pay the charges at later stages i.e at the month-end. 


# Hi, 
# Please get this approved by the finance team. 
# You may get this approved by anyone mentioned below. 
# manzil.bhattacharya@delhivery.com, mohammed.ummer@delhivery.com, sambit.sahoo@delhivery.com, saneev.kumar11@delhivery.com, saurabh.singh@delhivery.com

# Also, 
# Please check if there are any locks imposed on these packages, if yes, kindly get them unlocked, without which we will not be able to change the payment mode.




## Check the locks

# HQ:-


%cpaste
wbns = [
15504110000048,
15504110000072 
]
for i in wbns :
    p=find_by_wbn(i)
    p['frt_md']=u'FoP'
    p.save()
    print('frt_md', p.frt_md, p.lrn)
--

# LM:-


wbns = [
15504110000048,
15504110000072 
]
for i in wbns :
    p=Package.objects.get(waybill=i)
    print('p.fod_charges', p.fod_charges)
    p.fod_charges=None
    p.save()

for i in wbns :
    p=Package.objects.get(waybill=i)
    print('p.fod_charges', p.fod_charges, p.lr_number)



# LTL:-

# https://ap-southeast-1.console.aws.amazon.com/dynamodbv2/home?region=ap-southeast-1#item-explorer?initialTagKey=&table=LorryReceiptsDataTable-prod

# Update the below keys in LorryReceipt Table 

# "freight_mode": "FoP" 


#  "FOP": {
#    "txn_id": "yc50E5w7VO9g",
#    "mode": "PLOD",
#    "created_at": "1649224292434",
#    "sec_mode": "DC",
#    "payment_id": "fCV5jTruOt5iba1mKB8twUgwsksMD",
#    "status": "SUCCESS"
#   }



# Delhivery Corporate Office - Goa, 2nd floor, Edificio Da Menezes E Silva, Sangolda, Goa 403501