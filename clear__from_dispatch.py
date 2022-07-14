%cpaste
#items to be changed when there a dispatch needs to be cleared

wbns = [
5963061803414,
131527467333,
131524621192,
131552684752
]


f=find_by_wbn
# for wbn in wbns :
#     p=f(wbn)
#     # print("p.dd.id", p.dd.id,"p.dd.t", p.dd.t, "P.cs", p.cs)


for wbn in wbns :
    p=f(wbn)
    did = p.dd.id
    if did is not None :
        print("p.dd.id", p.dd.id,"p.dd.t", p.dd.t)
    #clear the dispaatch params.
        p.dd.id = None
        p.dd.t = None
        p.dto = False
        p.rto = False
        p.save()


for wbn in wbns :
    p=f(wbn)
    print("p.dd.id", p.dd.id,"p.dd.t", p.dd.t)

--