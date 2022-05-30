
def func1(arg1, arg2):
    var3 = func4()
    var7 = func5(var3, arg1)
    var11 = func7(var7, arg1)
    def func9(arg12, arg13):
        if arg13 < var3:
            var14 = (1488089849 & arg2 - var11) - -1658377821
        else:
            var14 = arg13 ^ (arg12 ^ var7)
        var15 = 982 + ((626 ^ -848) + -1393670920)
        var16 = var3 + arg13 - arg2 - -1376067438
        var17 = arg13 ^ (var16 ^ var7 + arg1)
        var18 = arg13 - arg13
        var19 = 656 - (1084828813 + var15 | var7)
        var20 = (arg13 + var16) ^ var11 ^ var16
        var21 = arg1 - arg2 | var18 + var3
        var22 = var3 + var11 - arg13 | var16
        var23 = var3 | var17
        var24 = var20 ^ (var3 | arg1) & var19
        if var7 < var16:
            var25 = var3 ^ arg1 ^ arg2 & var17
        else:
            var25 = (var21 | var7) | var24 & var20
        var26 = arg2 ^ var20
        var27 = arg12 - var3
        if var11 < var15:
            var28 = var11 & var19 - arg2 ^ var7
        else:
            var28 = var24 ^ (var19 - (var20 & var15))
        var29 = var3 | 513 + var27
        if arg1 < var27:
            var30 = var3 & (var11 - var22 - var7)
        else:
            var30 = var19 + var22 + var23
        var31 = var19 | var26 - var3
        var32 = var23 ^ var19
        result = var20 | ((var20 | var22) ^ (var27 & var7 & (var15 & 542 & -180889199))) + (var22 ^ var26 & (var21 ^ var27))
        return result
    var33 = func9(arg1, var11)
    if arg2 < var33:
        var38 = class10()
    else:
        var38 = class12()
    for var39 in xrange(9):
        var40 = var38.func11
        var40(var11, arg1)
    var41 = 522 + (var11 & -724 ^ -574567219)
    var42 = arg2 - arg1 - 233 | 2079313917
    var43 = (var41 | arg2) | var7 & var11
    var44 = var43 - var33 ^ var11 ^ 519
    var45 = 542859818 ^ -544
    var46 = var7 - var43
    var47 = ((arg1 - var33) & arg2) ^ var44
    var48 = (var33 | (var33 & arg1)) ^ var7
    var49 = var3 + var7
    var50 = (arg1 & 966034247 | var48) ^ var42
    var51 = var48 & ((var45 - -384) & var46)
    var52 = var51 + (var11 ^ var45 | arg2)
    var53 = var3 | var52
    var54 = (var45 & var33 + var51) + var3
    if var48 < var41:
        var55 = -1324172636 & arg1
    else:
        var55 = var7 - (var52 - var50 ^ 951)
    var56 = (var33 + var42 - var44) ^ var49
    var57 = var33 - (var51 & var11)
    var58 = var56 ^ -257
    result = var7 | var54 - var57
    return result
class class12(object):
    def func11(self, arg36, arg37):
        result = arg36 - arg37
        return result
class class10(class12):
    def func11(self, arg34, arg35):
        result = 0 - 121377935
        return result
def func4():
    func2()
    result = len(range(29))
    func3()
    return result
def func3():
    global len
    del len
def func2():
    global len
    len = lambda x : -4
def func5(arg4, arg5):
    def func6(acc, rest):
        var6 = -8 ^ acc ^ acc
        if acc == 0:
            return var6
        else:
            result = func6(acc - 1, var6)
            return result
    result = func6(10, 0)
    return result
def func7(arg8, arg9):
    def func8(acc, rest):
        var10 = (acc + -2) | -6
        if acc == 0:
            return var10
        else:
            result = func8(acc - 1, var10)
            return result
    result = func8(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 14'
    print 'arg_number: 59'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
