
def func5(arg24, arg25):
    if arg25 < arg24:
        var30 = class6()
    else:
        var30 = class8()
    for var31 in xrange(34):
        var32 = var30.func7
        var32(arg25, arg24)
    var35 = class10()
    for var36 in func12(arg24, arg25):
        var49 = var35.func11
        var49(arg25, var36)
    var54 = func13(arg24, arg25)
    var55 = 1992322410 ^ 801493503
    var56 = (arg24 ^ var55 | -348) + var55
    var57 = (var54 | var54 | var56) ^ -52894286
    var58 = var54 ^ arg24
    var59 = var57 ^ (var58 + -153)
    var60 = (var59 | -836 ^ var55) ^ -193
    var61 = var58 + (var55 & arg24) - var57
    var62 = 162 & (var61 + arg25 ^ var57)
    if var61 < var57:
        var63 = (var60 - arg25 - arg25) ^ var55
    else:
        var63 = var62 & (var58 & var61 & arg24)
    var64 = arg25 | -908
    var65 = var61 ^ var62
    var66 = (var54 & 189 | var61) ^ arg25
    var67 = var62 - (var59 - var57) & var62
    if var55 < var56:
        var68 = (var56 - var58 + 569433737) + var56
    else:
        var68 = ((var65 + var60) + var59) + var59
    var69 = var62 + (var54 & var55)
    result = var65 & arg24
    return result
def func13(arg50, arg51):
    var52 = 0
    for var53 in xrange(5):
        var52 += -2 & var52
    return var52
def func12(arg37, arg38):
    var39 = ((arg37 ^ -260849903) & -69) - arg37
    yield var39
    var40 = 338 & var39 - (881922272 + arg37)
    yield var40
    var41 = 407314430 - 186289094 ^ (-1210994149 - var40)
    yield var41
    var42 = -216533769 - var40 + var40
    yield var42
    var43 = var41 ^ var40 ^ arg38 | arg38
    yield var43
    var44 = arg38 | var42 | (var39 | arg37)
    yield var44
    var45 = (var43 & var44 + arg37) ^ var44
    yield var45
    var46 = (-1601570340 + var43) & -526397555 & var45
    yield var46
    var47 = (var43 & var46) | var42 & arg37
    yield var47
    var48 = var41 | var39
    yield var48
class class10(object):
    def func11(self, arg33, arg34):
        return 0
class class8(object):
    def func7(self, arg28, arg29):
        return 0
class class6(class8):
    def func7(self, arg26, arg27):
        result = (arg27 - (0 - arg27) & (arg27 | -1)) & arg27 | arg26
        return result
def func1(arg1, arg2):
    var3 = func4()
    var4 = arg1 + (-881 - arg2) - -199438332
    if var3 < arg2:
        var5 = ((arg1 | -2103314649) & arg2) - arg1
    else:
        var5 = arg2 | 430076876
    if var3 < var4:
        var6 = var3 ^ ((arg2 | arg1) + -105)
    else:
        var6 = arg2 | ((147553322 | -823) - arg2)
    var7 = 241 - (arg2 - (-1920219824 & 1552470193))
    var8 = (var7 & var7 + arg1) & var3
    var9 = var8 + (926862610 | var3) | var4
    var10 = 857 | var7 ^ var8 ^ -1742662157
    var11 = 1012189986 - var9
    var12 = (var9 + var8) ^ -646 + var9
    var13 = ((var12 + var4) ^ var4) + var11
    var14 = (var7 - arg1) ^ (var8 - -1586111371)
    var15 = (-480333303 - var3 + 167509075) ^ var13
    var16 = var4 | var10
    var17 = var16 | var10 | var16
    var18 = (var11 - var9) | arg1 ^ var9
    var19 = var15 & (var10 | var3 & var7)
    var20 = var8 + (var3 | var16) | var14
    var21 = (var14 - var15 | var15) & var19
    var22 = var14 | var20 | (var13 & var11)
    var23 = var12 | var15 ^ var18 & var12
    result = (1879176746 | (var3 | ((arg2 ^ var18) ^ var7)) & (var12 | arg1)) ^ (var13 & 928 & (var13 | var9))
    return result
def func4():
    func2()
    result = len(xrange(7))
    func3()
    return result
def func3():
    global len
    del len
def func2():
    global len
    len = lambda x : 5
if __name__ == "__main__":
    print 'prog_size: 1'
    print 'func_number: 5'
    print 'arg_number: 24'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 14'
    print 'arg_number: 70'
    for i in xrange(25000):
        x = 5
        x = func5(x, i)
        print x,
