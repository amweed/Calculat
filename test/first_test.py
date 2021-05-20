import pytest
from app.calculator import Calculator
class TestCalc:
    def stup(self):
        self.calc = Calculator
    def test_multyply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4
    def test_multiply_calculat9on_failed(self):
        assert self.calc.multiply(self,2,2) == 5