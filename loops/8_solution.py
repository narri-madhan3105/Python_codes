
number =29
isprime=True
if number <= 1:
    isprime = False
else:
    for i in range(2, number):
        if number % i == 0:#number +1 no need bcz 29 is always div by itself
            isprime = False # so just check upto 28
            break
print(isprime)