index=0

while index <= 10:
	var_input=int(raw_input('Enter a number which is divissible by 2:------'))
	if var_input % 2 == 0:
		print 'sahi hai :)'
		index=index+1
	else:
		print 'galat hay :('
		index=index+1

else:
	print ' your chaance is over sorry :( :( :( :('
