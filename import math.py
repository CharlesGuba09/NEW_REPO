import math

class RegularPolygon:
    # Class variable to track the number of RegularPolygon objects
    num_polygons = 0

    def __init__(self, n, side): #Constructor
        """Initialize a RegularPolygon with n sides of length side."""
        self.n = n
        self.side = side
        # Increment the class variable each time a new object is created
        RegularPolygon.num_polygons += 1

    def area(self):
        """Calculate and return the area of the polygon."""
        return (self.n * (self.side ** 2)) / (4 * math.tan(math.pi / self.n))

    def perimeter(self):
        """Calculate and return the perimeter of the polygon."""
        return self.n * self.side

    def __str__(self):
        """Return a string representation of the polygon."""
        return f"{self.n} sides of length {self.side}"

# Test program
# Create first polygon: 5 sides, length 3.0
polygon1 = RegularPolygon(5, 3.0)
print("Polygon #1:", polygon1)
print(" Area:", round(polygon1.area(), 1))  # Round area to 1 decimal place
print(" Perimeter:", polygon1.perimeter())
print()  # Blank line for separation

# Create second polygon: 8 sides, length 2.5
polygon2 = RegularPolygon(8, 2.5)
print("Polygon #2:", polygon2)
print(" Area:", round(polygon2.area(), 1))  # Round area to 1 decimal place
print(" Perimeter:", polygon2.perimeter())

# Print total number of polygons created
print("Number of regular polygons created:", RegularPolygon.num_polygons)