
def func1(arg1, arg2):
    var6 = func2(arg2, arg1)
    var9 = class4()
    for var10 in xrange(19):
        var9.func5(arg1, arg2)
    if arg2 < arg2:
        var15 = class6()
    else:
        var15 = class8()
    for var16 in xrange(30):
        var15.func7(arg1, var6)
    var22 = var19(arg2, arg1)
    if var22 < arg1:
        var27 = class13()
    else:
        var27 = class15()
    for var28 in range(25):
        var27.func14(var6, arg2)
    var29 = arg2 + 44
    if var6 < arg2:
        var30 = var22 & arg2 & (var22 - var6)
    else:
        var30 = (var6 | -586) | var29
    var31 = arg1 ^ var6
    var32 = -1123008269 | var31
    var33 = 271 - var29 + var32 - var29
    var34 = var32 - arg1
    var35 = -497 - 485 & var29 - 650307140
    var36 = (var31 - var32) & 317460600
    var37 = 527 & (25 + (var32 | arg2))
    var38 = var6 ^ arg1
    var39 = var38 | var34 + var6 & arg2
    var40 = arg2 & var29
    if var34 < var29:
        var41 = ((var33 & var34) + arg2) + var34
    else:
        var41 = ((var29 + arg1) - arg1) + var32
    if var32 < var39:
        var42 = var39 | ((var32 | arg1) | var31)
    else:
        var42 = (var39 ^ var29 - var29) + var32
    var43 = arg1 | var33
    result = (var22 ^ arg1) ^ -529 ^ var39 - var31 | var34
    return result
class class15(object):
    def func14(self, arg25, arg26):
        result = (-977510364 & (0 | 1 & 0 & arg25) | 2076625753) - 2006554418
        return result
class class13(class15):
    def func14(self, arg23, arg24):
        return 0
def func12(arg20, arg21):
    result = (arg21 + -275) - arg20
    return result
def func11():
    closure = [-9]
    def func10(arg17, arg18):
        closure[0] += func12(arg17, arg18)
        return closure[0]
    func = func10
    return func
var19 = func11()
class class8(object):
    def func7(self, arg13, arg14):
        result = -157683706 | -1520180736 + arg14 ^ 0 & (1 - 1)
        return result
class class6(object):
    def func7(self, arg11, arg12):
        return 0
class class4(object):
    def func5(self, arg7, arg8):
        result = 780210096 | 2020738579 - -1 + arg8
        return result
def func2(arg3, arg4):
    closure = [0]
    def func3(acc, rest):
        var5 = 5 - (-1 & acc) - -10
        closure[0] += var5
        if acc == 0:
            return var5
        else:
            result = func3(acc - 1, var5)
            return result
    result = func3(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 17'
    print 'arg_number: 44'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
