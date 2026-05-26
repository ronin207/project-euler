terms = [1, 2]

a_1 = 1
a_2 = 2

#a_n = an-2 + an-1


i = 0
m = 0

terms[len(terms)] = terms[len(terms)-len(terms)] + terms[len(terms)-len(terms)+1] + terms[len(terms)-len(terms)+2]

print(terms[len(terms)])