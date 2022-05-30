
def func8(arg45, arg46):
    var51 = func9(arg46, arg45)
    var55 = func10(arg45, arg46)
    var56 = var51 & var55
    result = var55 | (((var56 & arg45 & (441 | var55) ^ arg45 ^ var51 | var55 + var51) ^ -2076377753) ^ -415) & 526
    return result
def func9(arg47, arg48):
    var49 = 0
    for var50 in range(33):
        var49 += (3 | var49) - 0
    return var49
def func1(arg1, arg2):
    if arg1 < arg2:
        var7 = class2()
    else:
        var7 = class4()
    for var8 in [(arg2 - -2) | arg2 for i in func6(0, arg2)]:
        var7.func3(var8, var8)
    var43 = 708508641 - arg2 + (309305472 ^ 74) ^ arg2
    var44 = (-1305325447 & (((-76486598 | arg1) ^ arg2) | (var43 & arg2)) | -2042804630) | (var43 & arg1 + arg2)
    result = ((-985 ^ -880) + var43) - var43 | var44 | arg1 ^ var44 + (var43 - 1517351761)
    return result
def func7(arg11, arg12):
    var13 = (-636819383 ^ arg11 & -2040737139) | 138087855
    var14 = (arg11 ^ var13) | arg11 | -663
    var15 = var13 & arg11
    if arg11 < var14:
        var16 = -525084119 + -1877015718 & var15 ^ arg11
    else:
        var16 = 1550596031 + var13
    var17 = var13 + var13
    var18 = (-1980193711 & var13 + var15) + var15
    var19 = (278012996 + -1679108965) + var18
    var20 = ((var17 - var18) + 231) + -1177089170
    var21 = var15 + arg12 + var13 ^ var15
    if var14 < var14:
        var22 = var17 & var15
    else:
        var22 = arg11 + arg12
    var23 = 615 | var17 + var21 + var19
    var24 = arg12 + var17
    if var21 < var13:
        var25 = var17 ^ arg12
    else:
        var25 = (-71 & arg11) - (155730385 & var21)
    var26 = -507 | var14 ^ var17 & var13
    var27 = var17 | var20
    var28 = (var17 + var18) - 2140392079
    var29 = ((var13 & var20) & arg12) | -298
    var30 = (var24 - var21 - var15) | arg12
    if arg11 < var18:
        var31 = var17 ^ var18
    else:
        var31 = var28 | (var29 & var15) | var24
    result = var20 & arg11 | var29
    return result
def func6(arg9, arg10):
    var32 = func7(arg10, -2079432000)
    yield var32
    var33 = arg9 - 2037835327 + 56
    yield var33
    var34 = var33 - -948 | arg9 | var33
    yield var34
    var35 = var34 & arg9
    yield var35
    var36 = arg10 - arg10 + var34
    yield var36
    var37 = 2094795444 ^ var36
    yield var37
    var38 = var33 & arg10
    yield var38
    var39 = ((-734330947 & -68) + var38) ^ var33
    yield var39
    var40 = var38 + -162463059 - arg9 ^ var34
    yield var40
    var41 = arg10 & var33 - var34 - var34
    yield var41
    var42 = var34 & (var33 ^ arg9) + -127661641
    yield var42
class class4(object):
    def func3(self, arg5, arg6):
        return 0
class class2(class4):
    def func3(self, arg3, arg4):
        result = 264541207 | -1
        return result
def func10(arg52, arg53):
    def func11(acc, rest):
        var54 = (-9 | -9) & -8
        if acc == 0:
            return var54
        else:
            result = func11(acc - 1, var54)
            return result
    result = func11(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 3'
    print 'func_number: 8'
    print 'arg_number: 45'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 12'
    print 'arg_number: 57'
    for i in xrange(25000):
        x = 5
        x = func8(x, i)
        print x,
