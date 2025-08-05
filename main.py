from Triangle import Triangle

print("========== TRIANGLE TEST ==========\n")

# 1. Default Triangle
t1 = Triangle()
print("Triangle 1 (Default):", t1)
print("Perimeter:", t1.parimeter())
print("Right-angled?", t1.IsRightAngle())
print("-----------------------------------")

# 2. Equilateral Triangle
t2 = Triangle(4)
print("Triangle 2 (Equilateral):", t2)
print(f"Perimeter: {t2.parimeter():.2f}")
print(f"Right-angled? {'Yes' if t2.IsRightAngle() else 'No'}")
print("-----------------------------------")

# 3. Isosceles Triangle
t3 = Triangle(5, 8)
print("Triangle 3 (Isosceles):", t3)
print("Perimeter =", t3.parimeter())
print("Is this a right-angled triangle?", t3.IsRightAngle())
print("-----------------------------------")

# 4. Scalene Triangle
t4 = Triangle(6, 8, 10)
print("Triangle 4 (Scalene):", t4)
print(f"Perimeter: {t4.parimeter()}")
print("Right-angled Triangle?", t4.IsRightAngle())
print("-----------------------------------")

# 5. Cloned Triangle
t5 = Triangle(t4)
print("Triangle 5 (Clone of Triangle 4):", t5)
print("Perimeter of cloned triangle:", t5.parimeter())
print("Right-angled?", t5.IsRightAngle())
print("-----------------------------------")

# Total count of objects
print(f"Total Triangles created: {Triangle.ObjectCount()}")
print("===================================")
