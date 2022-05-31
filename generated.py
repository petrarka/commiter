
def func1(arg1, arg2):
    var7 = func2(arg1, arg2)
    var59 = func3(arg2, arg1)
    var60 = var59 | (var59 | arg1)
    var61 = var59 + arg2
    var62 = var59 | var60
    var63 = (var61 - var59 - 1475475501) + var61
    var64 = 262710460 & var59 | -173 - 493080276
    if arg2 < var62:
        var65 = (var64 + (arg2 + arg2)) - arg1
    else:
        var65 = (arg1 + (var59 & arg2)) & var61
    var66 = arg2 | -792920087 & var59
    var67 = var64 & var63 + var64
    var68 = var66 + var59 & var66 ^ var7
    var69 = var62 | (var60 ^ var60)
    var70 = (var66 & var60 & var67) | var60
    if var66 < var61:
        var71 = -754005322 + var69 | var68
    else:
        var71 = (var63 & var7) & var67 ^ var64
    var72 = var60 - var7 - (var64 - 87)
    if var61 < var69:
        var73 = var63 & arg2 ^ 1255277164
    else:
        var73 = var7 - arg1
    var74 = var61 ^ var67 & 192 & arg1
    result = var67 & ((var69 & (var59 ^ var66) + var69 & ((arg1 - arg1 - (var64 ^ -505) | var74) - arg1)) ^ 388)
    return result
def func3(arg8, arg9):
    var10 = 0
    for var58 in func4(arg9, var10):
        var10 += var10 ^ arg9 - var10
    return var10
def func5(arg13, arg14):
    var22 = var17(arg13, arg14)
    var23 = -654 - (var22 ^ -1342100288) & arg13
    var24 = 480380762 ^ var23 + 399
    var25 = (var24 ^ var24) | arg14 ^ var24
    var26 = (arg13 - -975) | var24
    var27 = (var24 ^ var25) + var26
    var28 = var23 & ((var22 ^ var27) | var22)
    var29 = (var28 ^ -903 + var28) & -952427213
    if var25 < var27:
        var30 = (1210079477 & -422342586 | var29) + var29
    else:
        var30 = -1052547929 + var27
    var31 = var25 + var27
    var32 = var26 & var31 & var26 + 270
    var33 = ((arg13 - var25) ^ var26) + var27
    var34 = (var26 | (var24 - var23)) & var26
    var35 = (var32 & arg13 | var22) - var27
    var36 = var31 + var32 - var33 - var28
    var37 = var31 & var23
    var38 = 198 ^ var25
    var39 = var35 | var34
    var40 = var28 ^ var33 & var39
    var41 = (var38 + var37) + var33 ^ var23
    var42 = var31 - var26
    var43 = var29 ^ var42
    var44 = (var36 & (var43 | var38)) - var33
    var45 = (var43 + (var25 & 1469562732)) - var27
    var46 = arg14 ^ (var36 & var26) & var33
    result = var43 - 502
    return result
def func8(arg18, arg19):
    var20 = arg18 + 494670856
    var21 = -650 + 994
    result = var21 & (var21 ^ var21)
    return result
def func7():
    closure = [-2]
    def func6(arg15, arg16):
        closure[0] += func8(arg15, arg16)
        return closure[0]
    func = func6
    return func
var17 = func7()
def func4(arg11, arg12):
    var47 = func5(arg11, -880)
    yield var47
    var48 = arg11 & arg11
    yield var48
    var49 = arg11 + 272597412
    yield var49
    var50 = var48 ^ -802
    yield var50
    var51 = var49 - -596975392
    yield var51
    var52 = var51 + -430089245
    yield var52
    var53 = (-311665302 ^ arg12) ^ var49 ^ arg12
    yield var53
    var54 = 67 | var48
    yield var54
    var55 = 1112902705 & -383215185
    yield var55
    var56 = var51 | var51 ^ 354 - arg11
    yield var56
    var57 = arg12 | var50 ^ var49
    yield var57
def func2(arg3, arg4):
    var5 = 0
    for var6 in [(arg3 ^ i) + arg4 for i in xrange(20)]:
        var5 += var6 & -7
    return var5
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 9'
    print 'arg_number: 75'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
