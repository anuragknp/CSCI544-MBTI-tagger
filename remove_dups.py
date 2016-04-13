import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')



hash = {}
for line in open(sys.argv[1]):
  hash[line] = 1

with open(sys.argv[1], 'wb') as f:
  for line in hash.keys():
    f.write(line)
  
