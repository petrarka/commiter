
def func1(arg1, arg2):
    var48 = func2(arg2, arg1)
    var49 = arg1 & -1028722015 & arg1
    var50 = (arg1 | -828) | arg2 & var49
    var51 = -24 ^ -153700370 + -60698646 + var49
    var52 = var48 + (var49 + var50)
    var53 = arg2 | (arg2 & arg2)
    var54 = (238 + arg2) ^ var48 + -2062126474
    var55 = 681 ^ var50
    var56 = (var55 & var50 & var50) - arg1
    var57 = (var49 ^ var56) + -792554140 - var55
    var58 = arg1 - arg1 | var49 & 115614661
    var59 = (var57 | var56 & arg2) ^ var50
    var60 = var51 ^ var50 | var59
    result = (873 | ((var60 | (((var60 ^ var57) - var57 & var50) & var49 | var59)) + var54 - var50) - -337959369) + var60
    return result
def func2(arg3, arg4):
    var5 = 0
    for var47 in func3(arg3, arg4):
        var5 += (var47 & var5) & 4
    return var5
def func4(arg8, arg9):
    if arg9 < arg9:
        var14 = class5()
    else:
        var14 = class7()
    for var15 in xrange(24):
        var14.func6(arg9, arg9)
    var19 = func9(arg9, arg8)
    var20 = func13()
    var21 = var20 & 706 - var20 & var19
    var22 = var20 + (-381088782 | var20 | var19)
    var23 = var20 | (var22 - 1576606489) & var21
    var24 = var21 & (arg8 ^ var20 + var23)
    if var19 < var22:
        var25 = (arg9 + arg9 ^ -926) + 602
    else:
        var25 = var20 | var23
    var26 = var23 + ((-729 ^ var24) + var24)
    var27 = var24 + (var23 | var22) - arg9
    var28 = var19 & -1306153933 | var22 | var24
    var29 = -755 ^ var22
    if var27 < var19:
        var30 = (var26 | 333722643) + var26 + 1187009583
    else:
        var30 = var27 - var28
    var31 = arg8 - var23
    var32 = arg9 ^ 2065851380 + -666 | var20
    if var21 < var19:
        var33 = var20 - (var20 ^ (var32 & var27))
    else:
        var33 = (var20 | (var27 ^ var19)) & var32
    var34 = var27 ^ var23 ^ var22 - arg8
    var35 = var27 + var20
    result = ((var29 + var27 + (((((var19 ^ var28) + var35 | var19) & var24) + 880) ^ var29 + var29)) - var28) ^ var34
    return result
def func13():
    func11()
    result = len(range(26))
    func12()
    return result
def func12():
    global len
    del len
def func11():
    global len
    len = lambda x : -8
class class7(object):
    def func6(self, arg12, arg13):
        result = arg13 & 1
        return result
class class5(object):
    def func6(self, arg10, arg11):
        return 0
def func3(arg6, arg7):
    var36 = func4(878, arg6)
    yield var36
    var37 = arg7 & -573 | 146
    yield var37
    var38 = (var37 - (arg7 & -882)) | arg6
    yield var38
    var39 = var37 + -718903427
    yield var39
    var40 = 224040075 ^ 21 - var38
    yield var40
    var41 = var40 | 737389195
    yield var41
    var42 = var41 | -806 | -1996716830 & -1201137028
    yield var42
    var43 = -1426612145 - arg6 | var40 & var37
    yield var43
    var44 = (var43 & var40) ^ var38 + var39
    yield var44
    var45 = var37 - var39 | 773737666 | arg7
    yield var45
    var46 = ((var45 + var38) - -231) ^ var40
    yield var46
def func9(arg16, arg17):
    closure = [0]
    def func10(acc, rest):
        var18 = (acc + ((-1 ^ 0) & -1 - rest) - -1) ^ -1
        closure[0] += var18
        if acc == 0:
            return var18
        else:
            result = func10(acc - 1, var18)
            return result
    result = func10(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 14'
    print 'arg_number: 61'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
