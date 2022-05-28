
def func1(arg1, arg2):
    if arg2 < arg2:
        var7 = class2()
    else:
        var7 = class4()
    for var8 in xrange(3):
        var7.func3(var8, arg1)
    var12 = func6(arg1, arg2)
    def func8(arg13, arg14):
        var15 = (348 & arg13 + (arg1 - (arg1 ^ arg14) + -695)) - arg13 - (var12 & ((arg13 & var12) & -946) + arg14 + (513 | arg14))
        result = (arg1 - arg2) ^ arg13 & (arg2 ^ ((arg13 - -990) & (var15 | var12)))
        return result
    var16 = func8(arg1, var12)
    var21 = func9(var16, arg1)
    if var12 < arg2:
        var26 = class10()
    else:
        var26 = class12()
    for var27 in range(3):
        var26.func11(arg2, arg2)
    var28 = 378 & var16
    if var16 < arg1:
        var29 = var21 - var28 ^ var21 & 1146395363
    else:
        var29 = var28 & arg1 + (var12 + arg1)
    var30 = arg1 + var21
    var31 = var16 + (937266454 + var21) ^ arg1
    var32 = ((var28 + var12) + var28) - var21
    var33 = arg2 - ((arg1 & var30) ^ var32)
    var34 = var33 & arg1
    var35 = -1714276084 + -413999109 - var31
    var36 = var28 ^ -172
    var37 = 964 & var12 | var30 - var21
    var38 = ((arg1 ^ var37) ^ var16) ^ var33
    var39 = var34 ^ var35
    var40 = var38 + (var36 - var21) | var30
    var41 = arg1 & var36 ^ var37
    var42 = (var41 & arg2) ^ var38 & var28
    var43 = var34 & var37
    var44 = var38 & (var41 + (var28 & arg2))
    var45 = (var32 + var40) - (var33 ^ var30)
    result = var34 & var42
    return result
class class12(object):
    def func11(self, arg24, arg25):
        return 0
class class10(class12):
    def func11(self, arg22, arg23):
        result = arg22 | arg22 & (arg23 & -1630902234)
        return result
def func9(arg17, arg18):
    var19 = 0
    for var20 in range(43):
        var19 += var20 | var19
    return var19
class class4(object):
    def func3(self, arg5, arg6):
        result = (-1 | 1443508217 & -1 | (0 + 2012396091)) + 949107612 - 1570040195
        return result
class class2(object):
    def func3(self, arg3, arg4):
        return 0
def func6(arg9, arg10):
    closure = [0]
    def func7(acc, rest):
        var11 = -5 + -4 + (-4 + closure[0]) | (closure[0] ^ -5) - rest
        closure[0] += var11
        if acc == 0:
            return var11
        else:
            result = func7(acc - 1, var11)
            return result
    result = func7(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 14'
    print 'arg_number: 46'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
