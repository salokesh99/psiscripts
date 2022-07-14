%cpaste
#here we check if a shipment is part of a bag. If yes, we remove it from bag. 
f=find_by_wbn
wbns='''
6981519978850
149082664065982
149082681840286
149082619095381
149082620276686
6981519717341
149082610138295
149082639379222
22497114335954
693736695255
14907321130142
149082657529135
5931442635895
14442612697450
'''

wbns = wbns.split('\n')
wbns1 = []
for i in wbns:
    if i != '':
        i = i.replace(" ", '')
        wbns1.append(i)

# print(wbns1)
wbns = wbns1


# +++++++++++++++++++++++++
for wbn in wbns:
    p=f(wbn)
    print("NEW DATA - ","bag id - ", p.pid )
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


for wbn in wbns:
    p=f(wbn)
    bag_id = p.pid
    print("BAG ID IS ---", p.pid)

    if bag_id is not None :
        print("It's already part of a bag")
        # user_input=input("Do you want to remove this package from the bag ? Type - Y/N")
        # if user_input == "Y" :
        p['pid'] = None
        p.save()
        print("Package removed from the bag!!!")
        # elif user_input == "N" :
        #     print("Abort!!!")

for wbn in wbns:
    p=f(wbn)
    bag_id=p.pid
    print("Updated Value --- Bag_id - ", bag_id )
--
