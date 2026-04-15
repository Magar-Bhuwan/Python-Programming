# for loop with break
# 'break' is used to come out/ exit the loop when encountered.

for i in range(100):
    if(i == 54):
        break       # Immediate Exit the loop 
    print(i)


# for loop with continue
# 'continue' is used to stop the current iteration of the loop and continue with the next one. skip

for i in range(100):
    if(i == 54):
        continue      # skip this iteration(54)
    print(i)