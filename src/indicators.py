def isBinary(expr):
    if(isinstance(expr, tuple) and len(expr) == 3):
        return True
    return False


def isUnary(expr):
    if(isinstance(expr, tuple) and len(expr) == 2 and (type(expr[1]) is tuple)):
        return True
    return False


def isConst(expr):
    if(isinstance(expr, tuple) and len(expr) == 2 and expr[0] == "const"):
        return True
    return False


def isId(expr):
    if(isinstance(expr, tuple) and len(expr) == 2 and expr[0] == "id"):
        return True
    return False


def isValue(expr, n):
    if(isConst(expr)):
        if(expr[1] == n):
            return True
    return False


def isAssigment(stmt):
    if(isinstance(stmt, tuple) and len(stmt) == 3 and stmt[0] == ":="):
        return True
    return False


def isIfStmt(stmt):
    if(isinstance(stmt, tuple) and len(stmt) == 3 and stmt[0] == "IF"):
        return True
    return False


def isPerfectPower(a, b):
    while a % b == 0:
        a = a / b
    if a == 1:
        return True
    return False
