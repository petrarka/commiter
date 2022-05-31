
def func10(arg31, arg32):
    var33 = func13()
    var34 = -1166954567 ^ -519939617 + (var33 - -455)
    var35 = arg31 | arg32 & var34
    var36 = arg32 - 1165429082
    var37 = arg32 + (arg31 | arg31 & arg31)
    var38 = arg32 - ((731 ^ -423) + var35)
    var39 = (var37 | var33) - arg32 & var34
    var40 = var35 + (var39 & var33) & var36
    var41 = (1913515336 | var33 | arg31) ^ var33
    var42 = var39 - (var37 ^ var34 ^ var40)
    var43 = var42 + var35 | var33
    var44 = var40 | (var43 - arg32 ^ var37)
    if var38 < var37:
        var45 = var44 + arg31 + var33
    else:
        var45 = -165 | (var40 | var37) ^ var40
    var46 = var40 & var42 & arg32
    var47 = (var40 - var44) & var39
    var48 = var34 | arg32
    var49 = var44 | (arg31 | var35)
    result = var43 | arg31
    return result
def func13():
    func11()
    result = len(xrange(44))
    func12()
    return result
def func12():
    global len
    del len
def func11():
    global len
    len = lambda x : 7
def func1(arg1, arg2):
    if arg2 < arg2:
        var7 = class2()
    else:
        var7 = class4()
    for var8 in (arg1 + arg1 | arg2 ^ arg2 for i in xrange(47)):
        var9 = var7.func3
        var9(arg2, var8)
    var13 = func6(arg2, arg1)
    var17 = func8(arg2, arg1)
    var18 = (-549 | var17 - var13) & var13
    var19 = arg2 | 454
    if var19 < arg1:
        var20 = arg1 ^ var19
    else:
        var20 = var17 | (var19 - var13) ^ var17
    var21 = 313581946 + arg2 - var18 | arg1
    var22 = arg2 ^ var19 & arg2 & var17
    var23 = 188 - (var22 - var17)
    var24 = (var13 | var13) ^ (var21 & var21)
    var25 = var24 + ((var17 + var19) - var13)
    if var13 < var18:
        var26 = (-572205518 + (var24 - 1335312735)) + var23
    else:
        var26 = ((896 ^ var21) ^ var13) | arg2
    var27 = (1672155176 - var21 ^ -653789915) | var25
    if var18 < var13:
        var28 = var23 ^ var22 | var17 & var17
    else:
        var28 = arg2 | -737627072 + var21 ^ var13
    var29 = 1635874162 ^ (var23 & var23)
    var30 = var22 | arg2 | var23 ^ var29
    result = (var23 + arg2) | var19 + arg1 ^ var22 - var18
    return result
class class4(object):
    def func3(self, arg5, arg6):
        return 0
class class2(object):
    def func3(self, arg3, arg4):
        result = arg4 ^ arg3 & arg4
        return result
def func6(arg10, arg11):
    def func7(acc, rest):
        var12 = acc | -8 - 6
        if acc == 0:
            return var12
        else:
            result = func7(acc - 1, var12)
            return result
    result = func7(10, 0)
    return result
def func8(arg14, arg15):
    closure = [0]
    def func9(acc, rest):
        var16 = ((-6 - -6) & ((-7 + -7) | closure[0]) ^ -8) - -7
        closure[0] += var16
        if acc == 0:
            return var16
        else:
            result = func9(acc - 1, var16)
            return result
    result = func9(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 4'
    print 'func_number: 10'
    print 'arg_number: 31'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 14'
    print 'arg_number: 50'
    for i in xrange(25000):
        x = 5
        x = func10(x, i)
        print x,
