list1 = [3,2,1,5,2,6,3,4,64,235,4]


filename = open('filename.txt', 'w')

for item in list1:
	filename.write("%s\n" % item)
