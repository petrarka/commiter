
def func1(arg1, arg2):
    var70 = func2(arg1, arg2)
    if arg2 < arg1:
        var71 = arg2 ^ arg2
    else:
        var71 = (arg1 + -598 | arg1) ^ (910 | var70)
    var72 = arg1 - -379667479
    if arg1 < arg2:
        var73 = arg2 + var70
    else:
        var73 = ((arg1 ^ var72 | -802) + -975) - var72
    var74 = (458 | (arg1 - (var72 & (var72 | -669967894)) ^ var70) | arg1 ^ ((((-701454 | ((arg2 + (arg1 + var72) ^ var70 & -1605524011) + (var70 ^ arg1))) | var70 & -1135757877 | arg1 - var72) ^ var70) & var72)) & arg1
    var75 = (var74 + var72) ^ (2034288081 & var70 - 918748341)
    result = ((arg2 | (arg2 + arg2) | var75 & -91) + -670) + var72
    return result
def func2(arg3, arg4):
    var5 = 0
    for var69 in func3(arg3, var5):
        var5 += arg4 - -9 + var5
    return var5
def func4(arg8, arg9):
    var15 = var12(arg9, arg8)
    def func8(arg16, arg17):
        if var15 < arg17:
            var18 = arg16 & 2028763697 | arg16 | arg16
        else:
            var18 = ((arg8 - arg8) - -348797589) - arg8
        var19 = arg9 & 783
        var20 = arg16 & arg16
        var21 = var20 | var20 - arg8 & 1442002197
        var22 = (var20 + -59) + -1076590618 ^ var15
        var23 = var21 ^ (var19 + var15)
        if var15 < arg17:
            var24 = ((var19 - var20) ^ var22) + 938
        else:
            var24 = (var23 ^ var20) & arg9
        var25 = var19 + var22
        var26 = (arg8 ^ -104 + var15) | var21
        var27 = var22 - var22 ^ var25 & var21
        var28 = var15 ^ arg8 + (arg17 & arg8)
        var29 = var22 - var19 & var20 - var28
        var30 = 688025458 + 428 | arg17 & -442
        var31 = var29 + arg9
        var32 = var15 + arg9
        var33 = ((var31 - var25) - var28) & var15
        var34 = var22 + var20 & -444 | var15
        result = arg8 | var22
        return result
    var35 = func8(var15, arg9)
    var36 = func11()
    var37 = arg9 ^ ((1179897344 ^ arg9) & var35)
    var38 = arg8 | (931 | var35) - 867
    var39 = var36 & var38 + 754 + -948234747
    var40 = (var15 + (arg9 & var35)) | var36
    if var15 < arg8:
        var41 = var35 ^ -1673643448
    else:
        var41 = var15 ^ arg8 & var36 + arg9
    var42 = (var39 | (var36 | var35)) & var36
    var43 = ((var36 | arg9) + -824) & var39
    var44 = var39 & (arg8 - var39 & var35)
    var45 = (arg9 & var15) + var37 ^ var43
    if var40 < var42:
        var46 = (var45 | var44) & var43 | var40
    else:
        var46 = var44 ^ var45 + var35 | 91
    var47 = var35 + var45 | var36 ^ var40
    var48 = arg8 & (var35 ^ var38)
    var49 = var44 + var45 - var44
    var50 = var37 | var49 - var49 | var44
    var51 = var36 | var15 ^ var37
    var52 = var35 ^ (var43 & var44 & var40)
    var53 = arg8 + var45 | var42 | var44
    var54 = var36 ^ var36
    var55 = (var40 + var44 & arg8) - var44
    var56 = var54 | arg9
    var57 = var35 - var42
    result = var38 - ((var49 & var51) ^ var57)
    return result
def func11():
    func9()
    result = len(xrange(26))
    func10()
    return result
def func10():
    global len
    del len
def func9():
    global len
    len = lambda x : -3
def func7(arg13, arg14):
    result = arg13 & (1894954424 - (arg13 | 925))
    return result
def func6():
    closure = [8]
    def func5(arg10, arg11):
        closure[0] += func7(arg10, arg11)
        return closure[0]
    func = func5
    return func
var12 = func6()
def func3(arg6, arg7):
    var58 = func4(1396312938, -613)
    yield var58
    var59 = ((605 - arg7) - 46) + 203259349
    yield var59
    var60 = -26 + var59 ^ -711 + -62
    yield var60
    var61 = 201 - var60 - var59 ^ 824069215
    yield var61
    var62 = var60 & 45
    yield var62
    var63 = (-1219387077 | arg7) ^ (arg6 ^ var59)
    yield var63
    var64 = var59 | (1827543072 + var61 & arg7)
    yield var64
    var65 = (var60 | var60 | var59) + var64
    yield var65
    var66 = var59 | -63935540
    yield var66
    var67 = (var60 & var63) | 353013007 ^ 469
    yield var67
    var68 = arg6 & var67
    yield var68
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 12'
    print 'arg_number: 76'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
