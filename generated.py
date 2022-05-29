
def func9(arg11, arg12):
    def func10(arg13, arg14):
        if arg12 < arg13:
            var19 = class11()
        else:
            var19 = class13()
        for var20 in xrange(28):
            var19.func12(arg12, arg12)
        var24 = func15(arg11, arg12)
        var25 = arg12 - arg12 ^ arg12 ^ arg13
        if var24 < var25:
            var26 = arg11 + (arg12 | arg14) - arg14
        else:
            var26 = arg14 ^ -141 | arg11
        if arg13 < var24:
            var27 = arg13 + 514 + -833 + arg13
        else:
            var27 = (var25 - arg13) ^ -330 | arg12
        var28 = arg13 - arg13 ^ var24 - var25
        var29 = 524 - 819
        var30 = (var24 ^ -127) + arg13
        var31 = arg11 - 174 ^ arg13 + var28
        var32 = var30 - arg13
        var33 = var28 + var30 ^ arg11 ^ arg13
        var34 = var24 & var33 + arg11 & var25
        var35 = var29 ^ var29 - arg11 + arg11
        var36 = var28 - (var32 ^ -639 + var30)
        var37 = arg12 - var31 - var36 - var25
        if var36 < arg13:
            var38 = var33 + (var25 - arg11) ^ var35
        else:
            var38 = var29 | var35 - arg14 ^ var24
        var39 = var28 & var29
        var40 = var36 + (var29 & (var35 ^ var37))
        var41 = var40 - var32
        if var36 < var28:
            var42 = var35 + var32 & arg12
        else:
            var42 = var37 ^ arg12
        var43 = var34 & arg13
        var44 = var25 - arg12 + arg14
        var45 = -190 + var43 ^ arg12 ^ arg14
        result = arg13 + arg12
        return result
    var46 = func10(arg11, arg12)
    var47 = -1127052315 - (725 ^ arg11) ^ arg11
    var48 = arg11 | 779 | -223 | var47
    var49 = (-2105978104 ^ 5) + 1195994557 | var46
    var50 = -460 | var46
    var51 = var47 | var47
    var52 = 54 & 657 ^ var46 ^ var46
    var53 = var52 | (var46 ^ (var47 & arg12))
    if var49 < var49:
        var54 = arg12 - var53
    else:
        var54 = var51 & var50 & var50 - var52
    var55 = (569062533 + var50 + var48) & var50
    var56 = (var51 - var47 ^ var46) - 755301198
    var57 = (var49 ^ arg11 - var48) + arg12
    var58 = -1130800561 - (var47 + var48) & -478
    var59 = 973 | var51 - var55 | -480231341
    if arg12 < var53:
        var60 = var53 & -1226896364 - (var59 - var48)
    else:
        var60 = var56 | (-826 & var49)
    var61 = var56 & ((var48 - var47) | -597)
    result = var56 ^ var50
    return result
class class13(object):
    def func12(self, arg17, arg18):
        result = (arg17 | arg17 + arg18) - (arg18 - arg17 + -2062297570) & -606886192
        return result
class class11(object):
    def func12(self, arg15, arg16):
        result = (arg15 & 1758629 + (1 ^ 0)) ^ arg16 | 527273600 & arg16
        return result
def func1(arg1, arg2):
    if arg2 < arg1:
        var7 = class2()
    else:
        var7 = class4()
    for var8 in xrange(20):
        var7.func3(var8, var8)
    var9 = func8()
    var10 = 907025610 & (var9 ^ arg1) | (arg2 ^ arg2 - (1308758360 & 1342397128) ^ var9 + arg1) ^ -433048206
    result = var9 & var10
    return result
def func8():
    func6()
    result = len(range(41))
    func7()
    return result
def func7():
    global len
    del len
def func6():
    global len
    len = lambda x : -4
class class4(object):
    def func3(self, arg5, arg6):
        result = 0 & -1
        return result
class class2(object):
    def func3(self, arg3, arg4):
        return 0
def func15(arg21, arg22):
    def func16(acc, rest):
        var23 = 0 & (6 + 0)
        if acc == 0:
            return var23
        else:
            result = func16(acc - 1, var23)
            return result
    result = func16(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 2'
    print 'func_number: 9'
    print 'arg_number: 11'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 17'
    print 'arg_number: 62'
    for i in xrange(25000):
        x = 5
        x = func9(x, i)
        print x,
