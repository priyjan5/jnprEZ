from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import threading
import csv 


class VlanDeployer(threading.Thread):
	def __init__(self , host , vlans):
		self.cred = host
		self.vlans = vlans
		threading.Thread.__init__(self)
		self.dev1 = None
		self.cu=None
	
	def run(self):
		self.dev1 = Device(host=self.cred[0] , user=self.cred[1] , password=self.cred[2])
		self.dev1.open()
		self.cu = Config(self.dev1)
		print "CONNECTED TO "+self.cred[0]

		for term in self.vlans:
			config_text= 'vlans{ ' + term['Vlan-name'] + '{description "'  + term['Desc'] + '"; vlan-id ' + term["Vlan-id"]+ ';}}'
			self.cu.load(config_text , format="text" , merge=True)

		self.cu.commit()
		self.dev1.close()
		print "CONF PUSHED TO "+ self.cred[0]

if __name__ =="__main__":

	host = ("192.168.1.1" , "root" , "lab123")
	dist = open("vlan_list.csv")
	reader = csv.DictReader(dist)
	thr1 = VlanDeployer(host , reader)
	thr1.start()
	thr1.join()



