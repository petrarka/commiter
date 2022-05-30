
def func3(arg11, arg12):
    var42 = var15(arg12, arg11)
    var43 = 225 & (arg12 - arg11) | 291841531
    var44 = var43 | (var43 & arg12 & -1771107336)
    var45 = arg11 & (arg12 - var44)
    var46 = arg12 | (arg11 ^ arg11)
    if var42 < arg11:
        var47 = ((var45 - var44) - -757) & var43
    else:
        var47 = var46 ^ var42 & (-163 ^ -2041006149)
    var48 = var44 & var45 & (var45 | -867579655)
    var49 = var43 & arg11 ^ var44 | var45
    var50 = ((var43 | var42) + 1484931347) | -418
    var51 = -1567154552 - 198 - arg12 | var45
    if var45 < arg11:
        var52 = (var50 - 320) - (var50 + var44)
    else:
        var52 = ((arg11 + var49) ^ arg12) & var44
    var53 = var51 ^ arg12 - var45 & var46
    if var43 < var45:
        var54 = (var51 - var50) + arg12 & -1775698320
    else:
        var54 = ((var44 & var53) & var43) - var42
    var55 = (var49 ^ var42) - arg12
    result = ((arg12 | var46) - (var45 - var51)) + (var43 & (var46 ^ var51))
    return result
def func6(arg16, arg17):
    var36 = var20(arg16, arg17)
    var41 = func10(arg16, var36)
    result = var36 | -1210819472
    return result
def func10(arg37, arg38):
    var39 = 0
    for var40 in xrange(4):
        var39 += arg37 & var40 | arg37
    return var39
def func9(arg21, arg22):
    var23 = -1121243775 | arg22 ^ -910481328 + arg22
    var24 = (arg21 & 861980036 ^ arg22) | -1571053729
    var25 = 1757590120 + var24
    var26 = (arg22 | arg21 ^ -219) - 145302899
    var27 = (arg21 & -538801065) & var25
    var28 = (var26 - var23) & arg22 + var24
    var29 = var25 | 752696916
    var30 = var29 | var24
    var31 = 1612937391 ^ var24 - var24
    var32 = var24 - 45973352 | 524 - -915
    var33 = var27 + (arg22 ^ (var27 - arg22))
    var34 = (var33 | var33 - var26) | var24
    var35 = var29 | var28
    result = ((var32 & (var29 ^ var28 ^ (-554331022 & var34) | arg22 - var32) & var29 ^ var24) | var29) + arg22 - arg22
    return result
def func8():
    closure = [6]
    def func7(arg18, arg19):
        closure[0] += func9(arg18, arg19)
        return closure[0]
    func = func7
    return func
var20 = func8()
def func5():
    closure = [-7]
    def func4(arg13, arg14):
        closure[0] += func6(arg13, arg14)
        return closure[0]
    func = func4
    return func
var15 = func5()
def func1(arg1, arg2):
    var7 = func2(arg2, arg1)
    var8 = arg2 | (1432026267 + arg2) & 344419084 | 719 + var7 - ((arg1 ^ ((1711281146 - (arg2 | -424130289) | (arg1 & 729616236 | ((arg2 & arg1 ^ 1294769433 ^ arg2 - arg2) ^ arg1 | -879186885))) ^ 1282675626)) ^ arg1) - -476151107
    var9 = arg1 ^ -566754893
    var10 = var7 ^ arg1 + var8
    result = -602578634 | arg2
    return result
def func2(arg3, arg4):
    var5 = 0
    for var6 in [-8 - i - (var5 + (var5 | 6)) for i in range(45)]:
        var5 += -10 - var5 ^ arg4
    return var5
if __name__ == "__main__":
    print 'prog_size: 2'
    print 'func_number: 3'
    print 'arg_number: 11'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 56'
    for i in xrange(25000):
        x = 5
        x = func3(x, i)
        print x,
