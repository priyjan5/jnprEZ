import csv 

dist = open("host.csv")
reader = csv.DictReader(dist)

for dev in reader:
	print dev['host']
	print dev['user']
	print dev['password']
	print "\n\n"
