
def func5(arg43, arg44):
    var45 = func8()
    if arg44 < arg43:
        var50 = class9()
    else:
        var50 = class11()
    for var51 in [var45 | ((i ^ arg43 + (var45 + (arg44 & i) + (var45 - var45) & arg43 ^ var45)) - i) & 6 for i in xrange(21)]:
        var50.func10(var51, arg44)
    var56 = func13(var45, arg43)
    result = -1970406398 | (arg44 & (((arg43 ^ -986) ^ ((arg43 - 313 - arg44) ^ arg44 & arg44 | arg43)) ^ arg43) | arg44)
    return result
def func13(arg52, arg53):
    var54 = 0
    for var55 in xrange(1):
        var54 += var54 & -7 ^ arg52
    return var54
class class11(object):
    def func10(self, arg48, arg49):
        return 0
class class9(object):
    def func10(self, arg46, arg47):
        result = (arg46 ^ arg46) | 309557410 & arg46 | 148256454 | 0 ^ 781385178
        return result
def func8():
    func6()
    result = len(range(20))
    func7()
    return result
def func7():
    global len
    del len
def func6():
    global len
    len = lambda x : 3
def func2(arg25, arg26):
    var30 = func3(arg25, arg26)
    var31 = var30 - var30
    var32 = 925 | (var30 & var30)
    if arg25 < var31:
        var33 = var32 ^ (var32 + var30)
    else:
        var33 = arg26 - arg25
    var34 = -1142461293 | -28772827 & -377042172 ^ -728483610
    var35 = arg26 ^ (-577 - var32) ^ var30
    var36 = (var30 ^ (var34 ^ -2100551957)) ^ var31
    var37 = var36 ^ var30 | (var31 + 1603021679)
    var38 = arg25 - -713
    var39 = arg26 + (-1800185892 | var32) - var37
    if var34 < var34:
        var40 = ((-1430987178 - arg25) - var34) ^ var38
    else:
        var40 = (var34 + var32 | var34) - arg26
    var41 = 52 ^ var38 ^ var30 - var34
    var42 = (var36 & arg26) + -712
    result = arg26 ^ var34 - arg25
    return result
def func1(arg1, arg2):
    var3 = -2004431597 | (arg2 & arg2) + 268
    var4 = var3 + 759 - 1859255109 - arg2
    var5 = 13 + var3 ^ 430393947 & var3
    var6 = arg2 ^ arg1 & var3 & arg1
    var7 = var4 & var4 | var5 - var6
    var8 = (118 ^ arg2 + var5) & 1612060202
    if var7 < var5:
        var9 = var3 - var5
    else:
        var9 = var4 | -213141524
    var10 = var5 + var3
    if var10 < var8:
        var11 = var4 + arg2 - arg1 | var6
    else:
        var11 = var4 & var6 ^ var4
    var12 = var10 ^ (arg1 + var5)
    var13 = (var12 - -1848982113) | var10
    var14 = var7 & var13 ^ var5 - var8
    var15 = var10 + (var8 | var14 | arg1)
    if var10 < var14:
        var16 = var3 | (var8 - var7) + var10
    else:
        var16 = var13 + var4
    var17 = -1624178696 ^ (var4 + (-287 & var12))
    if var4 < var13:
        var18 = (var3 & var13 - var7) ^ var12
    else:
        var18 = -1989098437 | var12 & arg1 ^ -1932639113
    var19 = var3 - var4 ^ var15 + -888
    var20 = var4 | var13
    var21 = (var12 - arg1) + var6
    var22 = ((var17 | arg2) ^ var14) - var15
    var23 = var14 - (var6 - -766807768) + var14
    var24 = (var13 - 65762230) - (var5 - arg1)
    result = ((arg2 - 774 | var3) & var15) + var21
    return result
def func3(arg27, arg28):
    def func4(acc, rest):
        var29 = rest - acc & -3
        if acc == 0:
            return var29
        else:
            result = func4(acc - 1, var29)
            return result
    result = func4(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 0'
    print 'func_number: 2'
    print 'arg_number: 25'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 1'
    print 'func_number: 5'
    print 'arg_number: 43'
    for i in xrange(25000):
        x = 5
        x = func2(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 14'
    print 'arg_number: 57'
    for i in xrange(25000):
        x = 5
        x = func5(x, i)
        print x,
