
def func1(arg1, arg2):
    var13 = var5(arg2, arg1)
    var40 = var16(arg1, var13)
    if arg2 < arg1:
        var45 = class8()
    else:
        var45 = class10()
    for var46 in xrange(13):
        var45.func9(arg1, var46)
    var49 = class12()
    for var50 in xrange(33):
        var51 = var49.func13
        var51(var50, var13)
    var52 = func16()
    var53 = arg2 - arg2 & arg1 - 1043027596
    var54 = (var53 - arg1 & arg1) ^ var53
    var55 = var13 & var52
    var56 = ((var13 - var40) + arg1) & var53
    var57 = var52 | var13 & var40 ^ var53
    var58 = arg2 + -1167647942 & var55 | var55
    var59 = (arg1 | var54 | var57) + 2097943545
    var60 = (var13 | var53 ^ var54) - var54
    var61 = (217188387 | var40 + 713070158) + var59
    var62 = var13 ^ var53
    var63 = var55 & (var56 | -927)
    result = var63 ^ var58 ^ (var55 | var58 & var53) - var52 | arg2 + var56
    return result
def func16():
    func14()
    result = len(range(36))
    func15()
    return result
def func15():
    global len
    del len
def func14():
    global len
    len = lambda x : -1
class class12(object):
    def func13(self, arg47, arg48):
        return 0
class class10(object):
    def func9(self, arg43, arg44):
        result = -711962062 ^ 1
        return result
class class8(class10):
    def func9(self, arg41, arg42):
        return 0
def func7(arg17, arg18):
    var19 = (arg18 ^ -237 & 847) | -314824816
    var20 = (arg17 & 487) + arg18
    var21 = var20 + arg17 | var20
    if var21 < var21:
        var22 = -299289100 ^ arg17
    else:
        var22 = arg17 ^ (var19 - var21 - var20)
    var23 = -1179936555 ^ var21 & arg18 + -190807255
    var24 = var19 | var20
    var25 = arg17 ^ arg17 ^ var20 + arg18
    if var24 < var21:
        var26 = ((-251258098 ^ arg18) & var23) + arg17
    else:
        var26 = (arg17 ^ var19) & (var19 ^ 25082927)
    var27 = var19 + (arg17 & var24 & -597409884)
    var28 = arg17 & (var20 | var24) ^ arg17
    var29 = (var19 | var20) | var27 & 370
    var30 = (var20 & var20) ^ 647 + var24
    var31 = -588566043 | var29
    var32 = ((var30 - arg18) ^ var24) - 965
    var33 = var30 + var30 + var19
    var34 = var19 + var30 ^ var23 - 687378498
    var35 = (var32 ^ var19) | 807801583 | var31
    var36 = (var19 & arg17) | var32
    var37 = var19 ^ var23 - var27 - var25
    var38 = var29 - var20
    var39 = (var27 + var30 & arg18) + var34
    result = (var38 + (var23 - var21 - var39)) + (var24 | var37)
    return result
def func6():
    closure = [-4]
    def func5(arg14, arg15):
        closure[0] += func7(arg14, arg15)
        return closure[0]
    func = func5
    return func
var16 = func6()
def func4(arg6, arg7):
    if arg7 < arg6:
        var8 = arg6 - -97 + -879
    else:
        var8 = -1412178702 - (arg6 + (((arg7 ^ arg6) | arg7 + ((arg6 - arg6 & 140 | 752 | arg7) & arg7 - arg6 ^ (405 ^ arg7 & 880))) | (arg6 ^ (arg7 - arg7)))) - arg7
    var9 = -750 & arg6
    var10 = -1098598294 - arg6
    var11 = (var10 | -765 ^ ((arg7 ^ arg7 & (var10 ^ var9 + -1969545556 - arg6)) - var9 ^ (-1015849106 & -1901308121 + arg6) & (1208647420 ^ arg6 + 578) + (var10 ^ arg6 ^ var9 | (-1108113671 - var9)) + 15)) | -829925784
    var12 = var10 ^ var11
    result = var12 | (var12 & -1808460730 | arg7 | var11)
    return result
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
    print 'func_number: 17'
    print 'arg_number: 64'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
