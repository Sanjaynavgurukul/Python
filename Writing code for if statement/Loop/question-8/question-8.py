index=30
count=0
while index<=420:
    if index % 8 == 0:
        count=count+index
        index=index+1
    else:
        index=index+1
print count
