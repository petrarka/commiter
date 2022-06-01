
def func1(arg1, arg2):
    def func2(arg3, arg4):
        var21 = func3(arg1, arg2)
        var22 = (arg4 - (arg1 ^ arg1 ^ (-573 + 798))) ^ arg2
        var23 = (arg2 - (arg4 - arg1 & arg3) | arg2 + var22 & (arg2 | arg3 | -95 | arg1 & var21 - (arg1 ^ arg3) ^ arg4 - ((arg1 & -564839839) - var22) + var22 - arg3) - -150678498 | arg2) - -1366928865
        var24 = arg2 + arg4
        var25 = -1161008622 ^ ((872644062 ^ var23 - -84) ^ arg2) ^ arg4
        var26 = arg4 | var24 & var24
        result = (arg4 ^ 140) | (var25 | var26 - (1322675091 + var24 ^ ((var21 - var26 | arg4) & arg4)) ^ arg4 ^ arg1)
        return result
    var27 = func2(arg1, arg2)
    var31 = func5(arg2, var27)
    var32 = -1652277145 ^ arg1
    var33 = arg1 | 309
    var34 = (arg1 + var33) + (var32 + arg1)
    var35 = var27 + var33
    var36 = var27 + 2136292560 ^ var32
    var37 = var35 & (var31 ^ var27)
    var38 = var34 | var32 + -1785512075 + var35
    if var33 < var32:
        var39 = -595 & var27 | var38
    else:
        var39 = var33 & 12 | var32 & var35
    var40 = var38 - arg2
    var41 = arg1 ^ var38
    if arg2 < var34:
        var42 = arg1 - (var36 | var38 ^ var38)
    else:
        var42 = var34 - var33 & (var34 ^ var34)
    var43 = var33 ^ (var35 ^ var38) - 184
    var44 = -863 + var33 + (var34 ^ var37)
    var45 = (var43 - -361067065 - var43) + var44
    var46 = var41 | var35 | var27
    var47 = var33 - 1571007148 + var45 | var35
    var48 = var46 - (var32 ^ var37 | var35)
    var49 = var41 ^ var31 | var36 & var38
    var50 = var43 - (-457580622 ^ var36) & var41
    result = var50 | (var27 | var37) | (var40 | var36)
    return result
def func3(arg5, arg6):
    var7 = 0
    for var20 in [var7 + (6 & 9) for i in func4(4, arg5)]:
        var7 += var20 - var20
    return var7
def func4(arg8, arg9):
    var10 = -402864908 ^ (arg9 | arg8 + -275)
    yield var10
    var11 = ((arg8 | var10) + 637) - arg9
    yield var11
    var12 = (-247599128 ^ 1144712550) ^ var11 ^ arg9
    yield var12
    var13 = arg8 + var10
    yield var13
    var14 = (arg8 & var12) & var10 - -1891504675
    yield var14
    var15 = var14 | var10
    yield var15
    var16 = (var12 & (var15 ^ var14)) & -1388591517
    yield var16
    var17 = var13 & (-1160400637 + var16 + var15)
    yield var17
    var18 = var14 | var13 + var12 - var11
    yield var18
    var19 = arg9 & arg9
    yield var19
def func5(arg28, arg29):
    def func6(acc, rest):
        var30 = (acc & 0) - acc
        if acc == 0:
            return var30
        else:
            result = func6(acc - 1, var30)
            return result
    result = func6(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 7'
    print 'arg_number: 51'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
