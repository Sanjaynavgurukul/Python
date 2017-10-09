index = 0
sum_age = 0
sum_average = 0
while index <= 11:
    value_input = int (raw_input('Please enter your age :)'))
    sum_age=sum_age + value_input
    index =index + 1
    sum_average = sum_age/11
print sum_average
if sum_average % 5 == 0:
    print 'It can be divided by the 5 :):)
else:
    print 'divissible nahi hhay'

