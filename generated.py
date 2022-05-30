
def func1(arg1, arg2):
    def func2(arg3, arg4):
        var9 = func3(arg3, arg2)
        var30 = var12(var9, arg1)
        var52 = var33(arg3, var30)
        var53 = var52 ^ var30 - arg3
        var54 = arg2 ^ var52 & (((-125832787 & var53 - arg4 & (-1378917733 - (((arg2 ^ arg2 ^ var52 | (arg2 | var52)) | arg4) | var53 - var30 - var52 ^ arg3 | arg2 ^ -1123070204 - 295)) | -875) | arg3) - arg3)
        var55 = 1498512682 ^ (var52 | -957 + var52 + var52 ^ (var30 & 935 | var54)) - arg2
        result = var30 & var52
        return result
    var56 = func2(arg1, arg2)
    def func10(arg57, arg58):
        if var56 < var56:
            var59 = ((30355946 & arg1 - 1905111264 & (506 + arg1)) + -662721372 - arg1) ^ 856 | arg57 - -284
        else:
            var59 = var56 + arg57
        var60 = (arg2 | 943) | -1478178233 ^ arg1
        var61 = -975 | (-546 | 294544516) - arg57
        result = arg58 ^ var56 ^ -899
        return result
    var62 = func10(arg2, var56)
    var63 = arg1 + (arg2 ^ var62 - var62)
    var64 = -2032683865 + var63 & var56
    var65 = var62 ^ var56 - var63 + 331102675
    if arg1 < arg2:
        var66 = var56 + (-1874343408 - var65 - -549)
    else:
        var66 = var62 | var62
    var67 = (arg2 & arg2 - var65) & arg2
    if var64 < arg1:
        var68 = (arg1 & 502112676) ^ var62
    else:
        var68 = arg1 ^ -1472557587
    if arg2 < var64:
        var69 = var64 - -866 | (var67 - -892)
    else:
        var69 = (1509462271 & var62) & var67 & var56
    var70 = var64 - var67
    var71 = var62 | var65
    var72 = (arg1 + var70 | arg2) + 167
    var73 = (var70 | var63 & var65) ^ -1103209404
    var74 = (-1079923404 & var73 ^ var65) | var70
    result = (-443834550 - var56) ^ 779816374 + arg2
    return result
def func9(arg34, arg35):
    var36 = -402 + ((arg34 ^ 1695555616) & arg35)
    var37 = arg35 & var36
    var38 = arg34 | arg34
    var39 = -164 & var36
    var40 = arg35 + arg34 | 1992027390
    var41 = var40 - 230 + (arg34 & var38)
    var42 = var40 & var40 + var39
    var43 = arg34 - var41
    var44 = var40 ^ (var40 ^ var42)
    var45 = var42 | var41
    var46 = arg34 | arg35 ^ (var37 ^ var36)
    if var46 < arg35:
        var47 = -1437186461 | var36 ^ var42
    else:
        var47 = (var44 | var41 - var46) | arg35
    var48 = arg34 - (arg34 & var45 + var45)
    var49 = arg34 - (var39 ^ var45)
    var50 = var37 | (var40 + (var39 & arg34))
    var51 = var50 & var36 & var45 - var43
    result = arg35 & var49 + ((var41 ^ (var38 - ((var45 | (var42 + var38 & var39) | var50) | -588017126 + var37))) - var45)
    return result
def func8():
    closure = [-4]
    def func7(arg31, arg32):
        closure[0] += func9(arg31, arg32)
        return closure[0]
    func = func7
    return func
var33 = func8()
def func6(arg13, arg14):
    var15 = -447 - -1112017097
    var16 = ((var15 & arg14) - -739705159) & 1357942386
    var17 = (-460 - arg13 + var16) ^ var15
    var18 = var16 ^ 233
    var19 = var17 & arg14
    var20 = var15 ^ arg14
    var21 = arg14 - var17
    var22 = arg14 | (-522 ^ var21 | var21)
    var23 = -665 & var20 | var20 - var18
    var24 = var21 ^ -1031775628 | var20 | arg13
    var25 = arg13 + var24 | var18
    var26 = var16 ^ 532
    var27 = arg14 ^ -817822339 - var21 - -1517996448
    var28 = (var25 & var25 - var16) + var18
    var29 = var17 - var26 - (var27 + -883)
    result = (var15 ^ (var17 ^ (var16 | -1396667011)) + (var19 ^ -423843566 ^ var23) + var28 & var21 ^ var22 + var17) - var29
    return result
def func5():
    closure = [0]
    def func4(arg10, arg11):
        closure[0] += func6(arg10, arg11)
        return closure[0]
    func = func4
    return func
var12 = func5()
def func3(arg5, arg6):
    var7 = 0
    for var8 in range(45):
        var7 += arg6 ^ (arg6 ^ 4)
    return var7
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 75'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
