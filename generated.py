
def func1(arg1, arg2):
    var50 = var5(arg1, arg2)
    var58 = var53(var50, arg2)
    var63 = func12(arg2, arg1)
    var64 = (var50 - var63 | var63) & var63
    var65 = (var64 & var50 ^ var58) | arg2
    var66 = var58 - 100158466 - var50 + arg2
    var67 = var63 ^ -975
    var68 = var67 | (993 ^ (var63 - var50))
    if arg1 < arg1:
        var69 = -181 + var64
    else:
        var69 = var66 ^ var63 & var63 & arg2
    var70 = (var66 - arg1) ^ -713 ^ var63
    var71 = ((var63 | var66) ^ var64) - -1443634032
    var72 = var64 - var70
    var73 = (var65 ^ var71 + var71) - -990
    if var63 < var58:
        var74 = var70 + (var65 + var66)
    else:
        var74 = ((-75 & var65) | var67) ^ var72
    if var73 < var64:
        var75 = (-2124909474 - arg1 + var73) - var67
    else:
        var75 = var66 - (var58 - arg1)
    result = var58 ^ var71
    return result
def func12(arg59, arg60):
    var61 = 0
    for var62 in xrange(23):
        var61 += arg60 - var62 ^ arg59
    return var61
def func11(arg54, arg55):
    var56 = ((-1460823003 - (-418 & arg55) + arg55) & 206 | arg54 - 1891648531 - -357 & (arg54 ^ (arg55 ^ arg55))) - (arg55 + (616 ^ (arg55 + -853))) + -252
    var57 = 133 - arg54 & -1902828533 | (arg54 | (arg54 | arg55))
    result = var56 + 160
    return result
def func10():
    closure = [6]
    def func9(arg51, arg52):
        closure[0] += func11(arg51, arg52)
        return closure[0]
    func = func9
    return func
var53 = func10()
def func4(arg6, arg7):
    var12 = func5(arg7, arg6)
    var30 = var15(var12, arg7)
    var31 = (438 - 367 ^ -842284011) & arg7
    var32 = var30 - var12 ^ (var30 & 75)
    var33 = (arg7 & var12) ^ (var12 ^ arg6)
    var34 = var31 | var12
    var35 = var34 - ((arg7 - arg6) & 710)
    var36 = (var35 | 1816789286) | var31
    var37 = var12 | var32
    var38 = var35 + var31
    var39 = var33 ^ -288
    var40 = -533 + var31
    var41 = ((var35 | var34) & var40) & 620
    var42 = var41 & (var36 | 1254090314 & var39)
    var43 = var32 ^ var34 & var38 & var31
    var44 = ((var41 + arg7) - var34) + var31
    var45 = var42 | (var34 + arg7 - var30)
    var46 = var45 - var39
    var47 = (var46 - var45) - var35
    if var33 < var31:
        var48 = var32 | var32 & -852 & var33
    else:
        var48 = ((var45 & var46) + var38) + var12
    var49 = var39 | var33
    result = (((var33 - (var47 & var43) ^ var45 | var30) + var42 & var34) ^ var12 ^ var12 | var31 + arg6) | var37
    return result
def func8(arg16, arg17):
    var18 = 334 | (arg16 - -1750692594) & arg16
    var19 = (295 | 1095440353 + 57) | arg16
    var20 = (arg16 ^ var19) + -344 & arg17
    var21 = 537 & (arg17 + arg16) & var18
    var22 = var20 - var21 | -827
    var23 = var22 - var22 & var21 ^ 1992390989
    var24 = ((726 + var21) & arg16) ^ -463229302
    var25 = 79512786 ^ var22
    var26 = (var24 ^ var22 + var21) ^ var25
    var27 = (var25 | var18 + var18) - var23
    if var20 < var21:
        var28 = (598 & (var19 ^ var18)) + var21
    else:
        var28 = var26 | arg17 & var25 | var26
    var29 = var27 | -1631873747 & var20 ^ var20
    result = var24 - arg16
    return result
def func7():
    closure = [-2]
    def func6(arg13, arg14):
        closure[0] += func8(arg13, arg14)
        return closure[0]
    func = func6
    return func
var15 = func7()
def func5(arg8, arg9):
    var10 = 0
    for var11 in xrange(43):
        var10 += (var11 | arg9) - arg9
    return var10
def func3():
    closure = [-4]
    def func2(arg3, arg4):
        closure[0] += func4(arg3, arg4)
        return closure[0]
    func = func2
    return func
var5 = func3()
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 13'
    print 'arg_number: 76'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
