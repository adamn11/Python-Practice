equation = "(1+((2+3)*(4*5)))"
ops = []
val = []

for c in equation:
    if c == "(":
        continue
    elif c == "+":
        ops.append(c)
    elif c == "-":
        ops.append(c)
    elif c == "*":
        ops.append(c)
    elif c =="/":
        ops.append(c)
    elif c == ")":
        sign = ops.pop()
        num = val.pop()

        if sign == "+":
            val.append(val.pop() + num)
        elif sign == "-":
            val.append(val.pop() - num)
        elif sign == "/":
            val.append(val.pop() / num)
        elif sign == "*":
            val.append(val.pop() * num)
    else:
        val.append(int(c))
print(val[0])
