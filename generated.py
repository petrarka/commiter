
def func1(arg1, arg2):
    def func2(arg3, arg4):
        var26 = var7(arg4, arg2)
        var29 = class12()
        for var30 in xrange(14):
            var29.func13(arg4, arg1)
        var31 = arg3 - (((-1178385614 + -297) | 1825063019 ^ arg2) | arg2 ^ arg3)
        result = -201 - arg3
        return result
    var32 = func2(arg2, arg1)
    var33 = var32 | arg1 - var32 + arg2
    var34 = var33 & arg1
    var35 = (var34 & 397 & -82046727) | arg1
    var36 = -1426613517 & -549522373 | (var34 & 328162364)
    var37 = (413 ^ arg2) | var32
    var38 = 451772472 & var36
    if var38 < arg1:
        var39 = (-373 + (var35 | -1132651809)) ^ var37
    else:
        var39 = var38 & (var35 + var34 ^ var35)
    var40 = var32 + 2113477670
    var41 = (var34 + var38) - var34 & var40
    var42 = var33 - arg1
    var43 = var37 | var38
    var44 = (var35 & var36 ^ var41) ^ var41
    var45 = var36 & var44 + var44 ^ arg2
    var46 = arg2 - (var37 | arg2)
    var47 = arg2 - (var38 + arg2 & var44)
    var48 = (var40 | var44) - var37 + var46
    var49 = var34 & var45
    var50 = ((var48 & var35) | 1630911384) & var38
    if var32 < var34:
        var51 = (arg2 & var47 + var42) - var34
    else:
        var51 = var42 | (var49 & var41) | var42
    var52 = 881 ^ -137675895
    var53 = (var52 + var49 | var35) & var52
    var54 = arg1 - var33
    var55 = var49 & var48 + var50 & var32
    result = (var34 | (var32 - (var48 + ((var49 & ((var32 - (var42 | (var54 & var35))) + var46)) & arg1))) & var44) ^ arg1
    return result
class class12(object):
    def func13(self, arg27, arg28):
        result = (arg27 + arg28 - arg27 + 1988113749 | 0 ^ arg27) + arg27
        return result
def func5(arg8, arg9):
    var10 = func8()
    var11 = func11()
    var12 = arg9 & 964
    var13 = arg9 - var10
    var14 = (arg8 ^ arg9 ^ -606410386) & -1177634805
    var15 = ((var13 - var11) ^ var13) ^ var10
    var16 = 1844148748 & arg9 & (var12 - var14)
    var17 = 145 - var16 | var12
    var18 = var16 - arg8
    var19 = var14 & ((arg9 ^ var13) + var13)
    var20 = var15 | (var12 ^ arg9) | arg8
    var21 = var20 + 797 | var20 | -280256885
    var22 = arg9 & arg9 | (var17 & var11)
    var23 = var14 - var11
    var24 = (arg8 & var19) + var17
    var25 = ((var21 & var19) | var16) - 616
    result = var22 - var12 & arg9 | (2006293261 - (((var14 ^ var22) | var12) - var20) & var18 - arg9) - var14 & var23
    return result
def func11():
    func9()
    result = len(range(22))
    func10()
    return result
def func10():
    global len
    del len
def func9():
    global len
    len = lambda x : -6
def func8():
    func6()
    result = len(xrange(8))
    func7()
    return result
def func7():
    global len
    del len
def func6():
    global len
    len = lambda x : 5
def func4():
    closure = [-9]
    def func3(arg5, arg6):
        closure[0] += func5(arg5, arg6)
        return closure[0]
    func = func3
    return func
var7 = func4()
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 14'
    print 'arg_number: 56'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
