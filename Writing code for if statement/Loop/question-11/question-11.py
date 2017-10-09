index=0
guess=5
while index<=3:
	number_input=int(raw_input('Guess What is my number :) --'))
	if number_input==guess:
		print 'Yes this is my number right guess :) :)'
		break
	else:
		inde=index+1
print 'you did not guess my number :( :( :('