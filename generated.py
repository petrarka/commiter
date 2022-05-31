
def func1(arg1, arg2):
    var10 = var5(arg1, arg2)
    var14 = func5(arg1, var10)
    var19 = func7(arg2, arg1)
    var24 = func8(var14, var10)
    var29 = func9(var14, var10)
    var30 = arg2 | (-975 | var19) & -395
    var31 = (var30 - var10 ^ -705) + -548
    var32 = (var24 | var24) ^ var14 ^ arg2
    var33 = 292 ^ var31
    var34 = (-1409907062 - var33 | var10) | var24
    var35 = var30 - var30 | (var33 | -841)
    var36 = var10 ^ -44 & var24 ^ var29
    var37 = var10 & (var32 | var35 + 83)
    var38 = var19 | var10 ^ 1868427618 & var32
    if var38 < var36:
        var39 = (-561 + var29 + arg2) ^ var37
    else:
        var39 = var10 ^ var34 ^ (var38 - var32)
    var40 = var33 + (var19 | arg1) | var32
    var41 = -514 - var31 + var37 - var19
    var42 = 442601142 & (var37 - (var37 - -1503000934))
    result = var34 - (var24 + var29) ^ (var19 - (((var41 + (var29 & var41 | arg1) - var38) - arg2) ^ var36)) - var14
    return result
def func9(arg25, arg26):
    var27 = 0
    for var28 in range(37):
        var27 += -3 - arg25 + var27
    return var27
def func8(arg20, arg21):
    var22 = 0
    for var23 in range(41):
        var22 += (arg21 ^ arg21) + 4
    return var22
def func7(arg15, arg16):
    var17 = 0
    for var18 in range(17):
        if var17 < var18:
            var17 += (6 & var18) & arg15
        else:
            var17 += var18 ^ (arg15 | var17)
    return var17
def func4(arg6, arg7):
    var8 = ((((391 ^ arg7) - 968) | arg7) | (arg7 & 1108367326 | -1733031434) + arg6 & (-634 & (arg7 + arg7 ^ 1754320404 & arg6 - -1699638930 & 314))) & ((-690 | -974230051 ^ (1961628172 | arg6) ^ -180695134) + 380877175) ^ arg7
    var9 = (arg7 ^ (-1653376067 - 214 ^ 793)) & (var8 ^ var8) & (var8 ^ 967)
    result = ((1593370471 | var9) | 427831541) & -209 & (var8 - arg7) - (884 + (-634 | arg6)) & (-12787902 ^ -1425629654) & -1224198942
    return result
def func3():
    closure = [-8]
    def func2(arg3, arg4):
        closure[0] += func4(arg3, arg4)
        return closure[0]
    func = func2
    return func
var5 = func3()
def func5(arg11, arg12):
    def func6(acc, rest):
        var13 = 8 + rest
        if acc == 0:
            return var13
        else:
            result = func6(acc - 1, var13)
            return result
    result = func6(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 10'
    print 'arg_number: 43'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
