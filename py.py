a = int(input(">> "))
b = int(input(">> "))
if a >= b:
    m = a
    n = b
else:
    m = b
    n = a

q = int(m / n)
r = int(m - n * q)
while r != 0:
    print(r)
    m = n
    n = r
    q = int(m/n)
    r = int(m - n * q)
print(f"Q = {q} R = {r} N = {n}")