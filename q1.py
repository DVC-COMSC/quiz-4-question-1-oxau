
# ******************************
# Make your Code
# ******************************
iter = 0
even = 0
preval = 0
while iter < 10:
    val = int(input('Enter a number: '))
    iter += 1
    if (val%2) == 0:
        val = preval
    if val % 2 == 0 and preval % 2 == 0:
        even +=1
    else: 
        even += 0
print (even)


    






# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
