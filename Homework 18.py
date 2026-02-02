import math

# Take angle input in degrees
angle_deg = float(input("Enter the angle in degrees: "))

# Convert degrees to radians
angle_rad = math.radians(angle_deg)

# Calculate sin, cos, and tan
sin_value = math.sin(angle_rad)
cos_value = math.cos(angle_rad)
tan_value = math.tan(angle_rad)

# Display results
print("Sin(", angle_deg, ") =", sin_value)
print("Cos(", angle_deg, ") =", cos_value)
print("Tan(", angle_deg, ") =", tan_value)
