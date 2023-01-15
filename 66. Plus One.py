digits = [1,2,3]
output = []
# str = []
# s = [str(i) for i in digits]

# v1 = int("".join(digits))
# v1 = (digits.strip(","))
# print(v1)

# for i in digits:
#     v1 = int((i, end=""))
#     # print(v1)
# print(v1)

res = int("".join(map(str, digits)))

# print(res)
# v1 = res+1
# output.append(v1)

# output = list(map(int, str(digits[0])))

output = [int(x) if x.isdigit() else x 
          for z in input for x in str(z)]

print(output)