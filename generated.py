
def func1(arg1, arg2):
    var19 = func2(arg1, arg2)
    def func4(arg20, arg21):
        var22 = (arg1 | -420) & (arg2 + 535)
        var23 = arg2 ^ 1467507236
        var24 = arg1 + (arg1 ^ arg21) & -105
        var25 = -693067909 & arg2
        var26 = arg21 & -110 - arg1
        var27 = arg2 - var23 - var22 + arg2
        if var27 < var23:
            var28 = (var22 ^ (var24 - 667)) & var19
        else:
            var28 = (var24 & var23 ^ var25) | var24
        if var19 < arg2:
            var29 = (arg20 ^ 39) ^ 479 & arg20
        else:
            var29 = ((1499247022 & var24) ^ arg21) | var25
        if var24 < arg2:
            var30 = var27 | -680
        else:
            var30 = var26 ^ var19 ^ var23 - var27
        var31 = -763 & arg20
        var32 = arg20 - -370 + var22
        var33 = (var32 - (var22 - var31)) | var25
        var34 = var31 + arg1
        result = arg20 + ((var22 ^ (arg20 | var33 ^ var26)) & (var26 - arg21) - (var19 & -1166263961) - var22 + var32 | var19)
        return result
    var35 = func4(var19, arg1)
    var36 = func7()
    var41 = func8(arg1, arg2)
    var42 = var36 & (-735859363 ^ var19) ^ arg1
    if arg2 < var36:
        var43 = (var19 & var35) - (var35 ^ var41)
    else:
        var43 = var41 ^ 1157284724
    var44 = var42 + var19 & arg2 ^ 1369559522
    var45 = var19 + (297 - -1170024864)
    var46 = arg1 - arg2 ^ (var19 + var44)
    var47 = var42 - (var46 - var41)
    var48 = var36 ^ var44
    if var44 < var46:
        var49 = var36 | var41
    else:
        var49 = var19 + (var44 ^ var41 - var46)
    var50 = arg1 + var19 ^ var35 | var45
    var51 = 913 - (var42 + (var45 - var46))
    var52 = var36 ^ 697507081
    if var41 < arg2:
        var53 = var50 - var35
    else:
        var53 = var19 | -410227388 ^ arg1
    var54 = var47 - (var44 - (836 ^ 1372919350))
    var55 = -545646991 | var35
    var56 = var36 ^ var35 - var36 ^ var55
    var57 = ((var45 & var46) + var46) ^ var19
    var58 = ((var54 ^ var36) | -363421688) ^ var19
    var59 = (var35 ^ var57) | var19 & var45
    result = var46 + var55 & var48 | (-1221481799 + var50) + var35 - var45
    return result
def func8(arg37, arg38):
    var39 = 0
    for var40 in range(29):
        var39 += arg37 ^ var39 | arg38
    return var39
def func7():
    func5()
    result = len(range(15))
    func6()
    return result
def func6():
    global len
    del len
def func5():
    global len
    len = lambda x : 6
def func2(arg3, arg4):
    var5 = 0
    for var18 in func3(var5, arg4):
        var5 += (var18 ^ var5) + -10
    return var5
def func3(arg6, arg7):
    var8 = arg6 | (-1962413901 ^ (arg7 - 169218828))
    yield var8
    var9 = (-948 - 411) & var8 | var8
    yield var9
    var10 = arg7 | ((arg7 - var8) | arg7)
    yield var10
    var11 = arg6 | var10 - -1629231796 ^ -715045770
    yield var11
    var12 = -692613418 + arg6 ^ arg7 ^ arg7
    yield var12
    var13 = (var8 & var12 & arg7) ^ var11
    yield var13
    var14 = (arg6 + var13 ^ arg7) + 1262361812
    yield var14
    var15 = var12 + (var10 + var9) | var12
    yield var15
    var16 = -2036897825 | arg7
    yield var16
    var17 = ((var9 ^ var10) ^ -392766996) + var16
    yield var17
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 9'
    print 'arg_number: 60'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
