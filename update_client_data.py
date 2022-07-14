counter=0
client_list=[]
error=[]
with open ('/tmp/wallet_enable_05072022.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
	  cl = row['Client']
	  email=row['Email']
	  ph=row['Contact']
	  try:
		  c=Client.objects.get(name=cl)
		  counter+=1
		  if counter % 1000 == 0:
		  	time.sleep(60)
		  	print 'time sleep for 2 minute'
		  index = c.pay_mode.keys().index('Wallet')
		  c.pay_mode.set_bit(index, True)
		  c.wallet_provider=u'DEL-MILES'
		  c.wallet_not_email=unicode(email)
		  c.wallet_not_mobile=unicode(ph)
		  c.billing_method=u'prepaid'
		  c.save()
		  client_list.append(cl)
		  print 'updated for '+ str(counter) + ' of clients'
	  except Exception as e:
	  	  print e
		  error.append(cl)