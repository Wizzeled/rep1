largest = None
smallest = None
print " "
print "When you are done, insert 'done'"
print " "
while True:
    num = raw_input('Enter a number:  ')
    if num == 'done' : break
    try :
        num = int(num)
    except :
        print "Invalid input"
        continue
    
    if smallest is None :
        smallest = num 
    if largest is None :
        largest = num
    elif largest < num :
        largest = num
    elif smallest > num : 
        smallest = num
    
print "Maximum is", largest
print "Minimum is", smallest