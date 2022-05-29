
def func1(arg1, arg2):
    var30 = func9()
    var60 = var33(var30, arg2)
    if var60 < var30:
        var65 = class13()
    else:
        var65 = class15()
    for var66 in xrange(32):
        var65.func14(var60, arg2)
    var67 = 609 & 1760261027 ^ arg1 + (var30 + var60 - ((var30 | -856172437 | -225 | 176) & arg2))
    if arg1 < var30:
        var68 = var67 - ((-999 ^ ((arg2 & ((arg1 & ((var67 & var67 + -338571199 | var67) ^ (-616 | -1535746293 | (var30 + var30) & var60 & -556))) ^ arg2)) + arg2) | -761) | var67 ^ var60)
    else:
        var68 = arg1 | -258775161
    var69 = (arg1 | var67) ^ var30
    var70 = arg1 - (1797409575 - ((((arg1 & var69 & (834 & var60) & var60) ^ arg1 ^ arg2) | (var30 + var69) & arg2) | var69 + (var67 ^ arg2) + arg1)) ^ ((var60 | (arg1 + arg1)) + var30) & 48337906 - arg2
    var71 = arg2 | arg2 + (var70 ^ (((arg2 | (var67 - arg2) - var67) + var30 + arg1) - var70) & arg2 | arg1) - arg1
    result = -896 + var60
    return result
class class15(object):
    def func14(self, arg63, arg64):
        return 0
class class13(object):
    def func14(self, arg61, arg62):
        return 0
def func12(arg34, arg35):
    var36 = ((-15 ^ arg34) & arg35) - arg34
    var37 = (arg34 ^ arg35) + arg35
    var38 = (var36 & var36) + (arg34 ^ var37)
    var39 = var38 - 436 + -1885657419 & var38
    var40 = -84 - (var36 ^ arg35) ^ var38
    var41 = arg35 ^ (arg35 & var37 + var38)
    var42 = var37 + arg35 - arg34 + var37
    var43 = var38 + (-1542652707 & var37) - var41
    var44 = var41 & (var43 | var43) + var36
    var45 = var42 - (498 & var41)
    var46 = (var38 + var39) | -1791906018 ^ var44
    var47 = arg35 - ((var40 ^ var44) - var43)
    var48 = ((var42 ^ var36) | var45) - arg34
    var49 = var48 + arg35
    var50 = var49 | arg34
    var51 = var43 & var50
    if var44 < var40:
        var52 = (var41 - -195260777) + var36 - var49
    else:
        var52 = ((var51 - var37) & var48) | var42
    var53 = var47 | var37 - var39
    var54 = ((arg35 - var40) | arg34) | -854
    var55 = arg34 & var42
    if var39 < var44:
        var56 = -562 + var40 & -477 ^ var45
    else:
        var56 = var44 & (var47 & var45) | -1904630869
    var57 = var38 - var47
    var58 = var45 | var48 - -1599251531
    var59 = ((var46 ^ var39) | var46) - var38
    result = var53 ^ var48 ^ var46 & var57
    return result
def func11():
    closure = [0]
    def func10(arg31, arg32):
        closure[0] += func12(arg31, arg32)
        return closure[0]
    func = func10
    return func
var33 = func11()
def func9():
    func2()
    result = len(func4(7, -3))
    func3()
    return result
def func5(arg5, arg6):
    var7 = func8()
    var8 = (-343416841 + arg5) - 755
    var9 = arg6 - -1714679730 - arg6 ^ var7
    var10 = (244622724 & (-561 | var9)) + arg6
    if var10 < var8:
        var11 = var7 + (var8 - 1785196779 ^ var10)
    else:
        var11 = ((var7 ^ arg6) ^ var9) ^ var7
    var12 = var10 | -36167031
    var13 = arg5 | 147
    var14 = (var7 - var13) - var8
    var15 = arg5 & var8 | arg5
    var16 = var9 - (var8 ^ var12) ^ var8
    var17 = var15 ^ var7 + -385 | var9
    var18 = 2140264317 - (arg5 & arg5 ^ var16)
    result = ((arg6 & (var12 & var13) + var14 - -234) ^ var7) | ((var7 + (-715 | arg5 - var15) + var12) | arg6)
    return result
def func8():
    func6()
    result = len(range(34))
    func7()
    return result
def func7():
    global len
    del len
def func6():
    global len
    len = lambda x : 8
def func4(arg3, arg4):
    var19 = func5(arg4, arg3)
    yield var19
    var20 = arg3 & arg4 | arg3 + arg4
    yield var20
    var21 = arg3 + arg4
    yield var21
    var22 = -823348909 + arg3 - (-1879355056 + -342)
    yield var22
    var23 = (1346635695 - (arg3 & 508882677)) + var20
    yield var23
    var24 = (var20 ^ 948 - 170834569) ^ arg4
    yield var24
    var25 = var21 - var20 & -849 | 712
    yield var25
    var26 = var23 + var22
    yield var26
    var27 = ((var26 - var22) | arg4) + var26
    yield var27
    var28 = var25 ^ ((1982640469 + -538) & var25)
    yield var28
    var29 = (arg3 - var28) + arg4
    yield var29
def func3():
    global len
    del len
def func2():
    global len
    len = lambda x : 0
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 17'
    print 'arg_number: 72'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
