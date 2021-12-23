try:
    a = 12
    s = "hello"
    print(a+s)
except :
    print("unsupported operand type(s) for +: 'int' and 'str'")
finally:
    print(str(a)+s)