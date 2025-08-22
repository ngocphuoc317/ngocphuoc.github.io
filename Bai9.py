import math

# Tính hàm y1 = 4(x² + 10x√x + 3x + 1)
print("Hàm y1 = 4(x² + 10x√x + 3x + 1)")
print("Chỉ tính được khi x >= 0")
print()

# Tính y1 với x = 0
x = 0
if x >= 0:
    y1 = 4 * (x**2 + 10*x*math.sqrt(x) + 3*x + 1)
    print("Khi x =", x)
    print("y1 =", y1)
print()

# Tính y1 với x = 1
x = 1
if x >= 0:
    y1 = 4 * (x**2 + 10*x*math.sqrt(x) + 3*x + 1)
    print("Khi x =", x)
    print("y1 =", y1)
print()

# Tính y1 với x = 4
x = 4
if x >= 0:
    y1 = 4 * (x**2 + 10*x*math.sqrt(x) + 3*x + 1)
    print("Khi x =", x)
    print("y1 =", y1)
print()

print("=" * 50)

# Tính hàm y2 = (sin(πx²) + √(x²+1)) / (e^(2x) + cos(πx/4))
print("Hàm y2 = (sin(πx²) + √(x²+1)) / (e^(2x) + cos(πx/4))")
print()

# Tính y2 với x = 0
x = 0
tu_so = math.sin(math.pi * x**2) + math.sqrt(x**2 + 1)
mau_so = math.exp(2*x) + math.cos(math.pi * x / 4)
y2 = tu_so / mau_so
print("Khi x =", x)
print("y2 =", y2)
print()

# Tính y2 với x = 1
x = 1
tu_so = math.sin(math.pi * x**2) + math.sqrt(x**2 + 1)
mau_so = math.exp(2*x) + math.cos(math.pi * x / 4)
y2 = tu_so / mau_so
print("Khi x =", x)
print("y2 =", y2)
print()

# Tính y2 với x = -1
x = -1
tu_so = math.sin(math.pi * x**2) + math.sqrt(x**2 + 1)
mau_so = math.exp(2*x) + math.cos(math.pi * x / 4)
y2 = tu_so / mau_so
print("Khi x =", x)
print("y2 =", y2)