
def func1(arg1, arg2):
    var5 = class2()
    for var6 in range(42):
        var7 = var5.func3
        var7(arg2, arg2)
    var11 = func4(arg1, arg2)
    var12 = func8()
    var18 = func9(arg2, arg1)
    var25 = var21(var12, var18)
    var26 = arg2 ^ (235 ^ (var25 & var12))
    var27 = var11 & var11 ^ (var11 - arg2)
    if var18 < var25:
        var28 = var26 - var25 + arg2 & -345
    else:
        var28 = (var12 + var25) - arg2 + var18
    var29 = var12 | var12 & arg2 | var18
    var30 = -241 + 405
    var31 = var11 ^ arg1
    var32 = (var29 | var27) ^ var12 - -820267515
    var33 = arg2 + var29
    var34 = var26 + (var31 & var32) | var11
    var35 = var12 - -687
    var36 = (var31 - var18) - var34 | var31
    var37 = var36 + (arg2 | var30)
    var38 = (var27 ^ 280 & var26) - arg2
    var39 = var31 | arg1
    var40 = var12 - var34 - arg2 & -2082277636
    var41 = var29 ^ (var31 ^ var36)
    if var18 < var39:
        var42 = var11 - (var37 ^ var36 | var31)
    else:
        var42 = var31 | arg1
    var43 = (var34 & var41 - var41) | var12
    var44 = var39 - (var25 + var30 + 268)
    var45 = var36 + 258 | (var37 - var29)
    var46 = var29 ^ var34
    var47 = (arg1 & var30 & var44) & arg1
    var48 = var29 + var18
    var49 = var48 | var30 & var41
    result = ((var39 | -895493725) | var35 | var12) & var32
    return result
def func12(arg22, arg23):
    var24 = -1780888036 + (683 & -694 ^ (1467880794 & -2125020211)) | ((-168 & arg23 + ((arg23 & (arg22 - 1573229631 | arg22 & -1442981583 & 180)) - 1547162360) ^ 327 - 1725354305 & arg23 | arg23) & -1560222245) | arg23 - -1202017162 & arg22
    result = ((arg22 & -939 + (var24 | -2010414264 & -795) - arg22 ^ var24) - -203 - arg23) + -2137294326
    return result
def func11():
    closure = [-3]
    def func10(arg19, arg20):
        closure[0] += func12(arg19, arg20)
        return closure[0]
    func = func10
    return func
var21 = func11()
def func9(arg13, arg14):
    var15 = arg13 | (arg14 & arg14 ^ (-690 + arg14) | -700) | arg13
    var16 = 174 & -744
    var17 = 984844190 & arg14
    result = -5 & -772231310 & (arg14 & arg14 & ((191 & (var17 + arg14)) & (1307664852 + 360942427)) & arg14) | arg14 + var17
    return result
def func8():
    func6()
    result = len(range(1))
    func7()
    return result
def func7():
    global len
    del len
def func6():
    global len
    len = lambda x : 1
class class2(object):
    def func3(self, arg3, arg4):
        result = arg4 ^ (arg3 + -918731737)
        return result
def func4(arg8, arg9):
    def func5(acc, rest):
        var10 = 0 + -8 & -10
        if acc == 0:
            return var10
        else:
            result = func5(acc - 1, var10)
            return result
    result = func5(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 13'
    print 'arg_number: 50'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
