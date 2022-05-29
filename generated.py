
def func1(arg1, arg2):
    var58 = var5(arg1, arg2)
    var63 = func6(var58, arg2)
    if var63 < arg1:
        var68 = class7()
    else:
        var68 = class9()
    for var69 in range(27):
        var70 = var68.func8
        var70(arg1, var63)
    var75 = func11(var63, var58)
    result = var58 | -712
    return result
def func11(arg71, arg72):
    var73 = 0
    for var74 in xrange(1):
        if var73 < var74:
            var73 += arg71 & 0 + 1
        else:
            var73 += -2 & arg71 + var73
    return var73
class class9(object):
    def func8(self, arg66, arg67):
        result = ((arg66 + -2028102166) & 1149264349) | arg66
        return result
class class7(object):
    def func8(self, arg64, arg65):
        result = 813287089 + 0
        return result
def func6(arg59, arg60):
    var61 = 0
    for var62 in xrange(16):
        var61 += (arg59 & arg60) + -4
    return var61
def func4(arg6, arg7):
    var34 = func5(arg7, arg6)
    if arg6 < arg7:
        var35 = arg7 ^ arg7
    else:
        var35 = var34 + ((-1702951545 + arg6) - arg6)
    var36 = (arg6 ^ (arg6 | 79717175)) ^ arg6
    var37 = arg7 ^ 846557134 | -71605721 & -913
    var38 = ((arg6 - var34) | var34) - arg7
    var39 = var36 ^ var37
    var40 = (arg6 ^ arg7) | var36 | var36
    var41 = var40 & (var37 + arg7)
    var42 = var39 | (var41 | var39 | var37)
    var43 = ((var42 & arg6) - var34) | var40
    var44 = var36 ^ (arg6 & arg7 | 594)
    var45 = -1872144820 & (var39 - arg7) & arg7
    var46 = (var45 - var45 + var37) + var44
    var47 = var44 | arg6 ^ var39 & var41
    var48 = (var47 ^ arg7) + -1061835587
    if var43 < var36:
        var49 = (var37 | var46 - var42) ^ var44
    else:
        var49 = arg6 & var39
    var50 = (var34 ^ (var38 & var38)) - var38
    var51 = var48 & var37 ^ var46 ^ var41
    var52 = var39 - var39 - var51
    var53 = (arg6 & var37) + var52 + var52
    var54 = var45 & 771466654
    var55 = var37 + (var48 ^ var50 + 542)
    var56 = (var41 | -647444575) | var54 + var40
    var57 = (var47 + var43 + var51) - -750
    result = var56 - var48 - (var48 | var37)
    return result
def func5(arg8, arg9):
    var10 = (725 ^ arg9) ^ 501 - arg8
    var11 = -704 & -1801556059 - 613 | -1841727203
    var12 = arg8 & arg8
    var13 = -1616061742 - -987 + -565546999 + arg9
    var14 = (var12 + var13) | var11 + var11
    var15 = (arg9 & 169875338) + (894601485 + var13)
    var16 = arg9 + (var13 & (var12 ^ var15))
    var17 = (var10 - var15 ^ var15) | var10
    var18 = ((var13 | var16) | arg8) | arg8
    var19 = arg9 + -163 + var13 & 224
    var20 = var15 ^ (var10 - var15 - var14)
    var21 = 677346191 - var14
    var22 = arg9 | var10 & var21 ^ -129433396
    var23 = (var16 ^ var15 - arg8) + arg8
    var24 = 918 & var20
    var25 = (var15 ^ var21) - var10
    var26 = ((var15 + var18) | 1365649644) + var15
    var27 = var14 + var12
    if var16 < var20:
        var28 = (arg9 | var19 & arg8) - arg8
    else:
        var28 = var21 & var21 + var25 - var17
    var29 = var23 | var12
    var30 = var12 - var17 - var14 | var12
    var31 = var12 & (var20 | var27) & arg9
    var32 = var26 + var13
    if var22 < var18:
        var33 = var32 ^ var18 & var19 + -450
    else:
        var33 = var17 ^ var29
    result = (var14 & var13 | var22 ^ ((var17 & (var22 - var16 & (arg8 - var23)) & var17) - var26) & var16) & var17
    return result
def func3():
    closure = [-5]
    def func2(arg3, arg4):
        closure[0] += func4(arg3, arg4)
        return closure[0]
    func = func2
    return func
var5 = func3()
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 12'
    print 'arg_number: 76'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
