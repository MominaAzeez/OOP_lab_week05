import math

class Triangle:
    __objcount = 0  # Class variable to track number of Triangle objects

    def __init__(self, SideA=None, SideB=None, SideC=None):
        Triangle.__objcount += 1
        # Clone constructor
        if isinstance(SideA, Triangle) and SideB is None and SideC is None:
            other = SideA
            self.sideA = other.sideA
            self.sideB = other.sideB
            self.sideC = other.sideC
        # Default constructor
        elif SideA is None and SideB is None and SideC is None:
            self.sideA = 1.0
            self.sideB = 1.0
            self.sideC = 1.0
        # One parameter constructor (Equilateral)
        elif SideA is not None and SideB is None and SideC is None:
            self.sideA = SideA
            self.sideB = SideA
            self.sideC = SideA
        # Two parameter constructor (Isosceles)
        elif SideA is not None and SideB is not None and SideC is None:
            self.sideA = SideA
            self.sideB = SideA
            self.sideC = SideB
        # Three parameter constructor (Scalene)
        elif SideA is not None and SideB is not None and SideC is not None:
            self.sideA = SideA
            self.sideB = SideB
            self.sideC = SideC
        else:
            raise ValueError("Invalid arguments for Triangle constructor")

    # Properties for sideA
    @property
    def sideA(self):
        return self._sideA

    @sideA.setter
    def sideA(self, value):
        if value <= 0:
            raise ValueError("Side A must be greater than 0")
        self._sideA = value

    # Properties for sideB
    @property
    def sideB(self):
        return self._sideB

    @sideB.setter
    def sideB(self, value):
        if value <= 0:
            raise ValueError("Side B must be greater than 0")
        self._sideB = value

    # Properties for sideC
    @property
    def sideC(self):
        return self._sideC

    @sideC.setter
    def sideC(self, value):
        if value <= 0:
            raise ValueError("Side C must be greater than 0")
        self._sideC = value

    # Calculate perimeter
    def parimeter(self):
        return self.sideA + self.sideB + self.sideC

    # Check if triangle is right-angled using Pythagoras
    def IsRightAngle(self):
        sides = sorted([self.sideA, self.sideB, self.sideC])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9)

    # Class method to return object count
    @classmethod
    def ObjectCount(cls):
        return cls.__objcount

    # String representation
    def __str__(self):
        return f"Triangle with sides: {self.sideA}, {self.sideB}, {self.sideC}"

