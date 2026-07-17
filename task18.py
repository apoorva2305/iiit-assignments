#equilateral scalene isosceles triangle
def check_triangle_type(a, b, c):
    # Step 1: Validate triangle inequality theorem
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Invalid Triangle (Sides cannot form a triangle)"
    
    # Step 2: Check for Equilateral
    if a == b == c:
        return "Equilateral Triangle"
    
    # Step 3: Check for Isosceles
    elif a == b or b == c or a == c:
        return "Isosceles Triangle"
    
    # Step 4: If neither, it must be Scalene
    else:
        return "Scalene Triangle"

# Example Usage:
side_a = float(input("Enter length of side A: "))
side_b = float(input("Enter length of side B: "))
side_c = float(input("Enter length of side C: "))

result = check_triangle_type(side_a, side_b, side_c)
print(f"The triangle is: {result}")
