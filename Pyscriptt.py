import requests
import time
import json

tmn=1000
pepe=0
while(1):
	addr='https://api.wallex.ir/v1/udf/history?symbol=PEPETMN&resolution=1&from='+str(round(time.time())-90)+'&to='+str(round(time.time()))
	print(addr)
	out=requests.get(addr)
	outt = out.json()
	temp = 0
	if outt["s"]=='ok':
		if float(outt['o'][-1]) >= float(outt['c'][-1]):
			tmnp = tmn
			print(000,tmn)
			tmn=tmn-tmnp/3
			print(0000,tmn)
			temp = float(outt['c'][-1])
			pepe=((tmnp/3)/temp)+pepe

		else:
			if temp != 0:
			   temp2=float(outt['c'][-1])
			   pepep=pepe
			   pepe=(2-(temp2/temp))*pepep
			   print(100,tmn)
			   tmn = tmn + (pepep-pepe)*temp2
			   print(1000,tmn)
			   temp=temp2
		print("tmn=%s", tmn+pepe*float(outt['c'][-1]))
		time.sleep(60)
	

