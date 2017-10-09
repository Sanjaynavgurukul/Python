index=0
guess=55
while index<=5:
	number_input=int(raw_input('Guess What is my number :) --'))
	if number_input<guess:
		print 'chota hai'
		index=index+1
	else:
		if number_input>guess:
			print 'bada hai'
			index=index+1
		else:
			print 'right guess'
			break
else:
	print 'chance over'