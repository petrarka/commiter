
def func1(arg1, arg2):
    var54 = func2(arg2, arg1)
    var59 = func7(var54, arg2)
    var64 = func8(arg2, arg1)
    var65 = (((var59 ^ ((arg1 ^ -232894030 - -1669848813) - var59)) ^ var59) + var64 | var59 - var64) ^ arg2
    var66 = arg1 & 593369775
    var67 = -1151873165 | 916218187
    var68 = var54 | (var59 - (1320702869 + var65) ^ arg2)
    var69 = var64 | (-1434592933 ^ 190 + (var54 + (((var64 + arg2 & var64 & arg1 + (var54 | var54) + (arg1 & (439 ^ var67 & arg2)) ^ -365) & var64 ^ var59) - var64) | var64 | var64 ^ var54) - arg1)
    result = var67 | var54
    return result
def func8(arg60, arg61):
    var62 = 0
    for var63 in range(8):
        var62 += arg60 + arg61
    return var62
def func7(arg55, arg56):
    var57 = 0
    for var58 in range(45):
        if var58 < arg56:
            var57 += arg55 | -8
        else:
            var57 += (arg56 ^ arg56) + -7
    return var57
def func2(arg3, arg4):
    var10 = func3(arg3, arg4)
    var28 = var13(arg3, arg4)
    var29 = (arg3 & var28) ^ arg3 - arg4
    if var29 < arg3:
        var30 = var10 ^ arg4
    else:
        var30 = arg3 | arg3 + var28
    var31 = (183983863 - arg4 ^ arg4) ^ var29
    var32 = var10 + var28 + arg4 & var29
    var33 = var31 - arg4 + -816195753
    var34 = (var32 & var28) | var33 + var32
    var35 = arg3 ^ (arg4 ^ (-78865552 - var34))
    var36 = var35 & (var28 ^ arg4 ^ var31)
    var37 = 225 + arg3 & arg3 - var31
    var38 = var29 + (var31 ^ var10) | var29
    var39 = var34 ^ (arg3 ^ 106) + var31
    var40 = var33 + var37
    var41 = (var31 - var29) & var39
    var42 = arg3 + var34 - var36 + arg4
    var43 = var39 + var33 & var36 + var10
    var44 = var40 | arg4 + var41 | var41
    var45 = var40 - (var29 ^ var32)
    var46 = var32 + (var32 ^ var40)
    var47 = var36 + var36
    var48 = var38 | -933429609 | var33 | var43
    if var29 < arg3:
        var49 = ((var28 & var37) + var45) | var29
    else:
        var49 = var10 ^ var43 & var36 - var38
    var50 = (var39 - var31 - var31) + var42
    var51 = var39 & (var28 ^ var47)
    var52 = (arg4 - arg3) & -995 | var48
    if var28 < arg4:
        var53 = (var39 - var39 - var41) + 292
    else:
        var53 = var32 - var32 | (var46 | var34)
    result = (var41 - var28 | ((arg4 | var34) | (var28 & var41 ^ var37 | var48)) - (var48 | (var46 + var47))) + var52
    return result
def func6(arg14, arg15):
    var16 = arg15 ^ 168 & 1220211332 | arg15
    var17 = arg14 | var16
    var18 = arg15 + (41770359 + 434 | -319)
    var19 = 1421723960 + (683 ^ var17)
    var20 = var18 - arg14
    var21 = var17 ^ (var20 ^ var18) + var18
    var22 = -249 - arg14 | var21 - var16
    var23 = (arg15 & arg15) ^ var17 - var21
    var24 = arg15 ^ -550 ^ var16 & var19
    if var19 < var22:
        var25 = var17 + 383
    else:
        var25 = ((var20 - var22) & var21) + var17
    var26 = var22 ^ var24
    if var17 < var26:
        var27 = var22 | ((var20 ^ arg14) - var20)
    else:
        var27 = (var16 + (var19 ^ var23)) | var20
    result = var19 & (arg14 + arg15 - var22 - var18 ^ 19 + var26 & arg15 - (var21 + var18) - var21 ^ var20)
    return result
def func5():
    closure = [-9]
    def func4(arg11, arg12):
        closure[0] += func6(arg11, arg12)
        return closure[0]
    func = func4
    return func
var13 = func5()
def func3(arg5, arg6):
    var7 = arg6 | ((arg5 | 144) - arg6)
    var8 = var7 | -81 + arg6 ^ -2043699536 + arg5 ^ var7
    var9 = 942 - var8 & var8 | var7 - (32 & arg5)
    result = var9 ^ (174659460 & var9) | arg5
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 9'
    print 'arg_number: 70'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
