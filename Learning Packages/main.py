########### Calculator package ##############
from Calculator.BasicCalculator.add import Add
from Calculator.BasicCalculator.subtract import Subtract
from Calculator.BasicCalculator.multiply import Multiply
from Calculator.BasicCalculator.division import Division


def main():
    objAdd = Add()
    result = objAdd.add_two_numbers(10, 5)
    print("Addition Result = " + str(result))

    objSub = Subtract()
    result = objSub.sub_two_numbers(10, 5)
    print("Subtraction Result = " + str(result))

    objMul = Multiply()
    result = objMul.multiply_two_numbers(10, 5)
    print("Multification Result = " + str(result))

    objDiv = Division()
    result = objDiv.division_two_numbers(10, 5)
    print("Division Result = " + str(result))


if __name__ == "__main__":
    main()







