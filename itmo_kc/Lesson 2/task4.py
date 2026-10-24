a = int(input())
b = int(input())
c = int(input())

x_1 = (-b + ((b**2) - (4*a*c)) ** 0.5 ) / (2 * a)

x_2 = (-b - ((b**2) - (4*a*c)) ** 0.5 ) / (2 * a)

print(x_1, x_2)