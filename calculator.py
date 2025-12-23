print("знаки: +, -, *, /")
try:
    num1 = int(input("number 1:"))
    num2 = int(input("number 2:"))
    val = input("знак:")
    def v1():
        num_3 = num1 + num2
        print(num_3)
    def v2():
        num_3 = num1 - num2
        print(num_3)
    def v3():
        num_3 = num1 * num2
        print(num_3)
    def v4():
        num_3 = num1 / num2
        print(num_3)
    if val == "+":
        v1()
    elif val == "-":
        v2()
    elif val == "*":
        v3()
    elif val == "/":
        v4()
    else:
        print("???")
except:
    print("Где этому можно обучиться?")