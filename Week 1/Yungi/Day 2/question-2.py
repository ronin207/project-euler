def fibonacci_add(lst):
    new_val = (lst[len(lst)-2]) + (lst[len(lst)-1])
    lst.append(new_val)
    
    return lst


initial = [1, 2]


while fibonacci_add(initial)[-1] < 4000000:
    fibonacci_add(initial)

answer = 0
for i in range(len(initial)):
  if initial[i] % 2 == 0:
    answer += initial[i]

print(answer)
