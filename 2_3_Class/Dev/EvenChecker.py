class EvenChecker:

    def is_even(self, number) -> bool:
        if number % 2 == 0:
            logic_flag = True
        else:
            logic_flag = False
        return logic_flag

even_checker = EvenChecker()
if even_checker.is_even(24):
    print("Четное число")
else:
    print("Нетное число")