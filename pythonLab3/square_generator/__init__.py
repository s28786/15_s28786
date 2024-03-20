from abc import ABC, abstractmethod

class SquareGenerator(ABC):
    @abstractmethod
    def e_squares(self, start, end):
        pass



class CubicGenerator(SquareGenerator):
    def e_squares(self, start, end):
        if end < start:
            raise ValueError("Start of range cannot be greater than end.")
        return [x * x for x in (range(start, end+1))]
    def e_cubes(self, start, end):
        if end < start:
            print("Error: End of range is less than start.")
            return []  # Return an empty list
        return [x ** 3 for x in range(start, end + 1)]