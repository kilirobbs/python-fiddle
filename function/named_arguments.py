def getnet(gross, taxrate=17.5, **others):
	neto = gross / (1.0 + taxrate*0.01)
	for more in others.keys():
		print "GETNET:",more," - ",others[more]
	return neto

print getnet(88,country="Slovenia",taxrate=20,
  year=2008,type="VAT") 