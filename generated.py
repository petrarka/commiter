
def func1(arg1, arg2):
    var48 = var5(arg1, arg2)
    var49 = (-1141711968 - ((arg1 + (-1640707759 - arg1 ^ ((var48 - (arg2 + -709645145 + (((arg1 + (arg1 - arg1)) + arg1) + arg1 & var48))) | var48))) + arg1 | var48 | arg2 + (arg2 - 136852688) ^ arg2 + 392)) & -531206467
    var50 = 81 | arg1
    var51 = arg2 + arg2
    result = var48 | var49
    return result
def func4(arg6, arg7):
    var24 = func5(arg7, arg6)
    var25 = (-523 & (var24 | arg7)) ^ 660
    var26 = ((var25 + arg6) + arg7) + arg6
    var27 = var24 | arg6
    var28 = (arg7 & (var27 & var27)) + arg7
    var29 = (-254 ^ var27 & var26) - var28
    var30 = (var25 | (arg6 | var28)) - var25
    var31 = var24 | var26
    var32 = 883565794 - ((arg6 & var31) & arg7)
    var33 = var25 | var28 | var28 + arg7
    var34 = (arg7 ^ var29) | var26 & var26
    var35 = -712607786 ^ var31 - var33 - var29
    var36 = var32 - (var30 ^ arg6)
    if var35 < arg6:
        var37 = var30 & var29
    else:
        var37 = ((var35 + var27) ^ var32) + var35
    var38 = 1261686641 ^ (var26 + var26 ^ arg7)
    var39 = var31 | 146413356 ^ var33 + var27
    if var27 < var25:
        var40 = ((var24 - arg7) ^ var24) ^ var39
    else:
        var40 = var38 ^ var30
    var41 = arg7 - (var33 | var31)
    if var39 < var28:
        var42 = var34 - var26
    else:
        var42 = var34 & arg6 + var35 | var27
    var43 = var32 + var35 - (var24 & var34)
    var44 = (arg6 + (var27 | var34)) & var31
    var45 = -278 - var44
    var46 = (var26 ^ var30) ^ var24 & var28
    var47 = (var28 + (var30 ^ -1958014772)) & var36
    result = var26 - var30 + var46 - var35 & var41 + var31
    return result
def func5(arg8, arg9):
    var10 = 0
    for var23 in (i ^ (i - (var10 + (var10 + 2)) & (var10 & arg8 | arg8 + -8) + -7 - arg8) & var10 for i in [arg8 | (7 - 4) for i in func6(var10, -4)]):
        var10 += arg9 & var10 | var10
    return var10
def func6(arg11, arg12):
    var13 = arg11 + arg12
    yield var13
    var14 = arg12 & -100725950
    yield var14
    var15 = var13 + arg11
    yield var15
    var16 = var14 | 1444974353 ^ var14
    yield var16
    var17 = var13 ^ (200 + 506)
    yield var17
    var18 = -487 - (var13 ^ 435) - var14
    yield var18
    var19 = (var13 | (var13 | var15)) & -88
    yield var19
    var20 = (var13 ^ arg11) - 117888259 + var17
    yield var20
    var21 = var13 & (-1532921720 + var20) | 724
    yield var21
    var22 = (var13 & var15 & var21) - arg11
    yield var22
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
    print 'func_number: 7'
    print 'arg_number: 52'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
