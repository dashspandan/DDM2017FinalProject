from astropy.table import Table
import csv

t = Table.read('PhotoZFileB.vot', format = 'votable')

header = ['Counter', 'mag_r', 'u-g', 'g-r', 'r-i', 'i-z', 'z_spec']

with open('Testdata.csv', "w") as csvfile:
	writer = csv.writer(csvfile, lineterminator='\n')
	writer.writerow(header)
	writer.writerows(t)
