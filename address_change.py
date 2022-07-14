%cpaste
wbns=[
(14907299950172,  110006,	[u'AMAR PURI RAM NAGAR, F/F, AB-483, New Delhi, -' ]),
(149082321355056, 400097, 	[u'Nagneshi , Art Malad (E)' ]),
(149082422382906, 124103, 	[u'bags villa, diamond chowk, near post office, near diamond telecom' ]),
(149082440780940, 124103, 	[u'bags villa, diamond chowk, near post office, near diamond telecom' ]),
(149082440780995, 124103, 	[u'bags villa, diamond chowk, near post office, near diamond telecom' ]),
(149082444548406, 110008, 	[u'Shadipur Main Bajaar,,  2663 Gali No Choti Chopal ' ]),
(1493175242856,  201010,	[u'96A/2C RACHNA SECTOR-2, VAISHALI,,GHAZIABAD,UTTAR PRADESH' ]),
(1493175250490,  201010,	[u'B-45, Ground Floor, Gali No-06,Joshi Colony,NEW DELHI,DELHI' ]),
(1493175286374,  110092,	[u'D-524-A,D-BLOCK GALI NO-29,OPP VIVEKANAND SCHOOL,,NEAR BANK COLONY HARSH VIHAR,DELHI' ]),
(1493175331314,  110093,	[u'B-4, LIG FLAT GTB enclave,,NEW DELHI,DELHI' ]),
(1493175217295,  110093,	[u'4402/5-A Opp HDFC Bank,Ansari Road Darya Ganj,NEW DELHI,DELHI' ]),
(1493175453140,  400064,	[u'Room No 19, Opp Tipco, Quarry Road, Malad East,Mumbai Suburban, Maharashtra, 400064,MUMBAI,MAHARASHTRA' ]),
(1493175259671,  421302,	[u'Room No. 101, Building Rajaram - A, Anand Dighe Pravesh Marg,Near Saibaba Temple, Kalher,BHIWANDI,MAHARASHTRA' ]),
(1493175330695,  110045,	[u'G1/58 Second Floor Sita Puri Part 2,,NEW DELHI,DELHI' ]),
(1493175331115,  110045,	[u'Second Floor, Shop AT-A-1A, SF KH NO-82/12/1, Yadav Complex,Gurudwara Road Mahavir Enclave, Palam, South West Delhi, Del,NEW DELHI,DELHI' ]),
(1493175571204,  110064,	[u'UB10 FIRST FLOOR USHA PARK,HARI NAGAR,NEW DELHI,DELHI' ])
]
#fetching the DC Code 
# r_add = [u'S Sakthivel 77/52perumal coil street near jeeva complex alapakkam chennai']
# rpin = 600116
#setting up the new dc. 
for wbn, rpin, radd in wbns:
    p=find_by_wbn(wbn)
    print("RETURN CENTRE DATA --- @@@@@@@@@$$$$$$",wbn , p.radd, p.rpin)
    p['radd'] = radd
    p['rpin'] = rpin
    p.save()
print('WBN RCNs are Updated!!!')
#print New DCs
print('Printing updated Data')
for wbn, rpin, radd in wbns:
    try: 
        p=find_by_wbn(wbn)
        print("NEW DATA - ", "wbn -- ",wbn, "radd - ", p.radd, "Rpin - ", p.rpin)
    except:
        print('unable to find data ', wbn)
--


:--
('NEW DATA - ', 'wbn -- ', 14907299950172, 'radd - ', [u'AMAR PURI RAM NAGAR, F/F, AB-483, New Delhi, -'], 'Rpin - ', 110006)
('NEW DATA - ', 'wbn -- ', 149082321355056, 'radd - ', [u'Nagneshi , Art Malad (E)'], 'Rpin - ', 400097)
('NEW DATA - ', 'wbn -- ', 149082422382906, 'radd - ', [u'bags villa, diamond chowk, near post office, near diamond telecom'], 'Rpin - ', 124103)('NEW DATA - ', 'wbn -- ', 149082440780940, 'radd - ', [u'bags villa, diamond chowk, near post office, near diamond telecom'], 'Rpin - ', 124103)
('NEW DATA - ', 'wbn -- ', 149082440780995, 'radd - ', [u'bags villa, diamond chowk, near post office, near diamond telecom'], 'Rpin - ', 124103)
('NEW DATA - ', 'wbn -- ', 149082444548406, 'radd - ', [u'Shadipur Main Bajaar,,  2663 Gali No Choti Chopal '], 'Rpin - ', 110008)
('NEW DATA - ', 'wbn -- ', 1493175242856, 'radd - ', [u'96A/2C RACHNA SECTOR-2, VAISHALI,,GHAZIABAD,UTTAR PRADESH'], 'Rpin - ', 201010)
('NEW DATA - ', 'wbn -- ', 1493175250490, 'radd - ', [u'B-45, Ground Floor, Gali No-06,Joshi Colony,NEW DELHI,DELHI'], 'Rpin - ', 201010)
('NEW DATA - ', 'wbn -- ', 1493175286374, 'radd - ', [u'D-524-A,D-BLOCK GALI NO-29,OPP VIVEKANAND SCHOOL,,NEAR BANK COLONY HARSH VIHAR,DELHI'], 'Rpin - ', 110092)
('NEW DATA - ', 'wbn -- ', 1493175331314, 'radd - ', [u'B-4, LIG FLAT GTB enclave,,NEW DELHI,DELHI'], 'Rpin - ', 110093)
('NEW DATA - ', 'wbn -- ', 1493175217295, 'radd - ', [u'4402/5-A Opp HDFC Bank,Ansari Road Darya Ganj,NEW DELHI,DELHI'], 'Rpin - ', 110093)
('NEW DATA - ', 'wbn -- ', 1493175453140, 'radd - ', [u'Room No 19, Opp Tipco, Quarry Road, Malad East,Mumbai Suburban, Maharashtra, 400064,MUMBAI,MAHARASHTRA'], 'Rpin - ', 400064)
('NEW DATA - ', 'wbn -- ', 1493175259671, 'radd - ', [u'Room No. 101, Building Rajaram - A, Anand Dighe Pravesh Marg,Near Saibaba Temple, Kalher,BHIWANDI,MAHARASHTRA'], 'Rpin - ', 421302)
('NEW DATA - ', 'wbn -- ', 1493175330695, 'radd - ', [u'G1/58 Second Floor Sita Puri Part 2,,NEW DELHI,DELHI'], 'Rpin - ', 110045)
('NEW DATA - ', 'wbn -- ', 1493175331115, 'radd - ', [u'Second Floor, Shop AT-A-1A, SF KH NO-82/12/1, Yadav Complex,Gurudwara Road Mahavir Enclave, Palam, South West Delhi, Del,NEW DELHI,DELHI'], 'Rpin - ', 110045)
('NEW DATA - ', 'wbn -- ', 1493175571204, 'radd - ', [u'UB10 FIRST FLOOR USHA PARK,HARI NAGAR,NEW DELHI,DELHI'], 'Rpin - ', 110064)
