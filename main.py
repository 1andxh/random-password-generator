import random

lower = "abcdefgijklmnopqrstuvwxyz"
upper = lower.upper()
symbol = '!@#$%^&*'
numbers = '1234567890'
all = lower + upper + symbol + numbers

password = ''
length = 10
for i in range(length):
    password = ''.join([password, random.choice(all)])
print(f'your password is : {password}')



