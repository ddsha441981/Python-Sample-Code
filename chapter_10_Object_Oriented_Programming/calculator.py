class Calculator:
    brand = ""
    def _init_(self,brand):
        self.brand = brand

    def add(self, a, b,brand):

        print(brand)

        return a + b


my_calc = Calculator()
add = my_calc.add(2, 4,"Samsung")
print(f"Method Calling Result {add}")

brand = my_calc.brand
print("Hello " + brand)

