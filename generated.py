
def func1(arg1, arg2):
    var15 = var5(arg1, arg2)
    var20 = func6(arg1, var15)
    def func7(arg21, arg22):
        var23 = (arg21 | arg2) & -328 + arg2 - var20
        var24 = arg1 - (arg21 ^ arg1)
        var25 = ((arg2 - (-1628239478 & arg2 | 1532963054) & var24) ^ var20) + (arg1 & ((1805282674 - (((var23 + (var15 ^ var24)) + var15) - -882)) & -2131286379) & (arg2 + 816)) | var20
        var26 = var24 & var24
        result = (((-1362013970 + (-222 + arg22 + 508) ^ arg1 & arg21) - (var15 ^ -1871228095 & var20) + var26) ^ var25) + arg22
        return result
    var27 = func7(var20, arg1)
    if arg2 < var27:
        var32 = class8()
    else:
        var32 = class10()
    for var33 in range(13):
        var34 = var32.func9
        var34(arg2, var27)
    var35 = 1306428031 ^ arg1 & (-804 & var15)
    var36 = arg2 & var35
    var37 = -906 & var15
    var38 = arg2 + (var20 & var36) & arg2
    if var20 < arg1:
        var39 = var38 & arg1
    else:
        var39 = (var35 | var20 | 643) & var37
    var40 = ((var35 ^ 641) + var15) | var27
    var41 = var38 - arg2
    var42 = (var36 - var35 & var35) | var15
    var43 = ((arg1 ^ var36) + arg1) | var36
    if arg2 < var38:
        var44 = var37 ^ var40
    else:
        var44 = var40 | var36 + var20 ^ var38
    var45 = ((150 ^ var20) - var40) - var38
    var46 = (var42 & var41) ^ var27 & var40
    var47 = var35 + -971 & (var46 - var45)
    var48 = var37 + 87
    var49 = arg2 - var42 | -2036640699 ^ var48
    var50 = var35 + (var37 ^ var43) + var43
    var51 = -564026518 & (var50 + var40) - var41
    var52 = var20 & (var37 - var51 - var36)
    var53 = var52 ^ var48
    var54 = arg1 - (var35 - var15 ^ var27)
    result = arg2 & var43 ^ ((-1223384185 + var36) - var43)
    return result
class class10(object):
    def func9(self, arg30, arg31):
        return 0
class class8(class10):
    def func9(self, arg28, arg29):
        result = (1 ^ ((2039966550 + -1) - 1356326317)) + 0
        return result
def func6(arg16, arg17):
    var18 = 0
    for var19 in xrange(27):
        var18 += arg16 ^ arg16
    return var18
def func4(arg6, arg7):
    var12 = func5(arg7, arg6)
    var13 = (arg7 ^ arg7) ^ 174461903 ^ (1465063229 | 428) + (919110286 - -1459987384) & arg7
    var14 = (((-1036194828 - (arg7 ^ ((arg6 & (((59 - var12 | var13) + arg7) | var12)) | (arg6 | (((-602897398 ^ 400) & -278) ^ (var13 - var13)))) + var13) - arg7) & var13) ^ var13) + arg7 - arg6
    result = (arg7 + var13) + var14 & arg6
    return result
def func5(arg8, arg9):
    var10 = 0
    for var11 in range(28):
        var10 += var10 ^ var10 & arg8
    return var10
def func3():
    closure = [-10]
    def func2(arg3, arg4):
        closure[0] += func4(arg3, arg4)
        return closure[0]
    func = func2
    return func
var5 = func3()
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 12'
    print 'arg_number: 55'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
