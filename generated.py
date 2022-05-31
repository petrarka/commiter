
def func1(arg1, arg2):
    def func2(arg3, arg4):
        var9 = func3(arg4, arg3)
        result = ((arg3 - arg2) + ((arg1 - var9) - 1723023536) & var9) - arg4
        return result
    var10 = func2(arg1, arg2)
    if arg1 < var10:
        var15 = class4()
    else:
        var15 = class6()
    for var16 in xrange(19):
        var15.func5(arg1, var10)
    var21 = func8(var10, arg1)
    var25 = func9(arg1, var21)
    var26 = arg2 ^ 1961130907
    if var10 < var25:
        var27 = var21 + ((var26 & var25) ^ var10)
    else:
        var27 = (var26 + -58234232 & var21) | arg2
    var28 = (-575 | arg1 ^ arg1) ^ arg1
    var29 = arg1 - arg1
    var30 = var21 + (-661 | var29)
    if var29 < var28:
        var31 = (var29 ^ (var30 + var28)) + -145
    else:
        var31 = var29 ^ var28 ^ var10 + var21
    var32 = 1164799589 - var25 & var25 - arg2
    var33 = ((var30 ^ -137238864) & var26) ^ var21
    var34 = var33 | 464 & (904 | 1433282649)
    var35 = (var28 ^ arg1) ^ (var26 + var34)
    var36 = (var26 + 618435388 ^ var21) ^ var21
    var37 = var28 ^ var10
    var38 = var33 | var34 + (arg2 & var30)
    var39 = var21 + -615 & arg1 + var37
    var40 = arg1 | (var35 ^ var30 & -2069469342)
    if arg2 < var32:
        var41 = 240209107 | var34
    else:
        var41 = var36 - var28
    var42 = var25 | var28
    var43 = var21 - (-2020167862 & var29) ^ var36
    result = var10 - ((var40 ^ var28 | ((var29 - var42 - var26) ^ arg1 + 1415860580) | var28 ^ var10) ^ var42) + arg1
    return result
def func8(arg17, arg18):
    var19 = 0
    for var20 in xrange(43):
        var19 += (arg17 + arg17) & arg18
    return var19
class class6(object):
    def func5(self, arg13, arg14):
        return 0
class class4(object):
    def func5(self, arg11, arg12):
        return 0
def func3(arg5, arg6):
    var7 = 0
    for var8 in range(39):
        var7 += (arg5 + arg6) - var8
    return var7
def func9(arg22, arg23):
    def func10(acc, rest):
        var24 = rest | -4
        if acc == 0:
            return var24
        else:
            result = func10(acc - 1, var24)
            return result
    result = func10(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 44'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
