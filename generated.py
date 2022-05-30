
def func5(arg12, arg13):
    var17 = func6(arg12, arg13)
    var22 = func8(var17, arg12)
    var23 = arg13 ^ (-358 & arg13 & var17)
    var24 = -1285042571 + -2027513485 | var22 - 1821645333
    var25 = var22 ^ arg12
    var26 = var24 & arg13
    if var22 < var17:
        var27 = (var25 & var24 - var26) | var17
    else:
        var27 = arg13 & (var23 ^ (var25 | arg13))
    var28 = var26 ^ (var22 - var26) ^ -534433772
    var29 = arg12 & var17 ^ (var24 + arg12)
    var30 = (arg13 + var25) | var24 | var22
    var31 = 280214512 + 578 | (var22 - var23)
    if var30 < var17:
        var32 = var25 + var26 | arg13
    else:
        var32 = -1786690435 & -1109877637
    var33 = 678 | var30 ^ -925 + var30
    var34 = var28 + arg12
    if arg12 < var24:
        var35 = var17 + var34 + var29 - var30
    else:
        var35 = var31 - -825696397 | var26
    var36 = (-205791241 + var17 & var26) + var28
    var37 = var24 | var30 ^ var33 | var23
    var38 = var26 | 1503117183
    var39 = (var29 ^ var22 - var26) | 440
    var40 = ((var34 - var26) - arg12) ^ var23
    var41 = (var30 & -2060047908 - arg12) ^ var36
    result = (arg13 & (arg12 ^ var25) | var31) | var31 & var24
    return result
def func8(arg18, arg19):
    var20 = 0
    for var21 in range(21):
        var20 += (var21 & var21) & -1
    return var20
def func1(arg1, arg2):
    var7 = func2(arg1, arg2)
    var11 = func3(var7, arg2)
    result = 582 - (713 ^ (-413 + -73))
    return result
def func2(arg3, arg4):
    var5 = 0
    for var6 in (0 ^ var5 - arg4 for i in range(15)):
        var5 += arg4 & -3
    return var5
def func3(arg8, arg9):
    closure = [0]
    def func4(acc, rest):
        var10 = ((-8 - (-8 & rest)) | rest) ^ rest
        closure[0] += var10
        if acc == 0:
            return var10
        else:
            result = func4(acc - 1, var10)
            return result
    result = func4(10, 0)
    return result
def func6(arg14, arg15):
    closure = [0]
    def func7(acc, rest):
        var16 = acc + closure[0] | 7
        closure[0] += var16
        if acc == 0:
            return var16
        else:
            result = func7(acc - 1, var16)
            return result
    result = func7(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 3'
    print 'func_number: 5'
    print 'arg_number: 12'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 9'
    print 'arg_number: 42'
    for i in xrange(25000):
        x = 5
        x = func5(x, i)
        print x,
