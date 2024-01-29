import random

lower = "abcdefghijklmnopqrstuwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
numbers = "0123456789"
symbols = "-_@*!"

all = lower + upper + numbers + symbols
length = 16
password = "".join(random.sample(all, length))
password2 = "".join(random.sample(all, length))
password3 = "".join(random.sample(all, length))
password4 = "".join(random.sample(all, length))
password5 = "".join(random.sample(all, length))
password6 = "".join(random.sample(all, length))
password7 = "".join(random.sample(all, length))
password8 = "".join(random.sample(all, length))
password9 = "".join(random.sample(all, length))
password10 = "".join(random.sample(all, length))

print("GENERATOR PASSWORD")
print(f"1. {password}")
print(f"2. {password2}")
print(f"3. {password3}")
print(f"4. {password4}")
print(f"5. {password5}")
print(f"6. {password6}")
print(f"7. {password7}")
print(f"8. {password8}")
print(f"9. {password9}")
print(f"10. {password10}")

input()