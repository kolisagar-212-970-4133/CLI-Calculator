
def calcy(operate,a,b):
    match operate:
        case "add":
            return a+b
        case "sub":
            return a-b
        case "mul":
            return a*b
        case "div":
            return a/b
        case "mod":
            return a%b
        case "pow":
            return a**b
        case _:
            return "Invalid operation"