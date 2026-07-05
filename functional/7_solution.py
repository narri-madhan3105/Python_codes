def sum_all(*args):# can write (*chai) also just * is compulsory
    # spl type of parameters
    print(args) # gives in tuples
    for i in args:
        print(i * 2)
    return sum(args)

#print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))