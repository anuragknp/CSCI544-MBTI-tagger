__author__ = 'Anirudh'

import csv
import operator
train_path_template_file = "D:\Curriculum\Natural-Language-Processing\Directed-Research\AllData\Extracted\\17thApril\\out.txt"
infile = open(train_path_template_file,'r')

train_path_out_file = "D:\Curriculum\Natural-Language-Processing\Directed-Research\AllData\Extracted\\17thApril\\out_sorted.txt"
outfile = open(train_path_out_file,'w')

reader = csv.reader(infile, delimiter=',')

sortedlist = sorted(reader, key=operator.itemgetter(1), reverse=True)

writer = csv.writer(outfile,delimiter=',')

for line in sortedlist:
    writer.writerow(line)
