from Calculator.BasicCalculator.add import Add
from Calculator.BasicCalculator.subtract import Subtract
from Calculator.BasicCalculator.multiply import Multiply
from Calculator.BasicCalculator.division import Division
import pytest 

@pytest.mark.one
def test_method_add1():
    assert objAdd.add_two_numbers(10, 5) == 5

@pytest.mark.two
def test_method_add2():
    assert objAdd.add_two_numbers(10, 5) == 15

@pytest.mark.three
def test_method_division():
    assert objDiv.division_two_numbers(20, -2) == -10









objAdd = Add()
objSub = Subtract()
objMul = Multiply()
objDiv = Division()