#change of mode from FOD to Prepaid/Credit
'''
p=find_by_wbn(14994810001260)
p.frt_ch
{u'bs': {u't': 293.33, u'uc': 5.5},
 u'chwt': 53.33,
 u'fl': {u't': 108.53, u'uc': 37.0},
 u'gst': {u'ptl': 12.0, u't': 83.46},
 u'rov_in': False,
 u't': 778.92}

In [43]: p.frt_md
Out[43]: u'FoD'

In [44]: p['frt_ch']=None

In [45]: p['frt_md']=None

In [46]: p.save()


then go here - to clear these flags 



LTL:-

https://ap-southeast-1.console.aws.amazon.com/dynamodbv2/home?region=ap-southeast-1#item-explorer?initialTagKey=&table=LorryReceiptsDataTable-prod


and clear the  frt_md json object from LR details page.


  "freight_mode": {
    "S": "FoD"
  },

  
'''



%cpaste
f=find_by_wbn
wbn_list = [

1700213313962

]

for wbn in wbn_list :
    p=f(wbn)
    print('frt_ch - ', p.frt_ch, 'ftr_md - ', p.frt_md)
    if p['frt_ch'] is not None and p['frt_md'] is not None :
        p['frt_ch']=None
        p['frt_md']=None
        p.save()
    print('frt_ch - ', p.frt_ch, 'ftr_md - ', p.frt_md)
--