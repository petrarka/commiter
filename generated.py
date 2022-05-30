
def func1(arg1, arg2):
    var7 = func2(arg2, arg1)
    var11 = func3(arg1, arg2)
    var33 = var14(arg2, arg1)
    def func9(arg34, arg35):
        var36 = arg35 ^ -739 & var11
        if arg2 < arg35:
            var37 = (arg34 ^ arg35) | var11
        else:
            var37 = var11 ^ (var36 ^ var11) ^ var11
        var38 = ((arg34 & var36) ^ arg34) & var7
        var39 = -44 + 1990825898 - var36 ^ var33
        var40 = var7 + -179 + -740
        var41 = arg34 & (var33 ^ var38 ^ -1800880735)
        var42 = arg2 + var36 | var39 + var39
        if arg34 < var41:
            var43 = var42 - var33 - arg35
        else:
            var43 = ((arg34 + var33) ^ var11) | var41
        var44 = arg34 ^ arg2 | (var7 + var36)
        var45 = var36 ^ var38
        var46 = (var45 - var41) & var42
        var47 = (var46 - (arg2 & var11)) & var11
        var48 = 310 ^ var11 - arg34 | arg1
        var49 = (var41 - arg2) ^ (var33 | var33)
        var50 = (var42 - var36) & var41 | arg2
        result = var7 ^ var45 ^ var45 ^ var7 - var42
        return result
    var51 = func9(arg1, var33)
    var52 = arg2 & var51
    var53 = var11 | (var7 - arg2)
    var54 = 236 | arg2
    result = -1450542843 & ((arg2 - (var53 & (var11 & (-172 - var33))) + var52 ^ var53 + -1548531835 ^ var54 ^ var11) ^ -179662714)
    return result
def func7(arg15, arg16):
    var21 = func8(arg15, arg16)
    var22 = arg15 & ((arg16 & var21) | 746)
    var23 = -91434746 - (1254150429 | var21 + var21)
    var24 = -964 + 798
    var25 = arg16 & -2064071750 ^ var23
    var26 = arg15 | var24
    var27 = var24 - (arg16 | arg16) + var24
    var28 = var24 | (var21 + arg15 | 55)
    var29 = arg15 ^ var27 & var27 | var21
    var30 = (var22 & (arg15 & arg16)) & var27
    var31 = var27 + (var22 ^ var24 | -2033098544)
    var32 = (var24 & var29 ^ var22) & var30
    result = var25 ^ (((var27 - ((var27 ^ var32 ^ var24) ^ arg16) ^ (var23 | (var23 - var22))) - var31) ^ -1641903743 + var21)
    return result
def func8(arg17, arg18):
    var19 = 0
    for var20 in xrange(6):
        var19 += (arg18 ^ arg17) + -2
    return var19
def func6():
    closure = [-5]
    def func5(arg12, arg13):
        closure[0] += func7(arg12, arg13)
        return closure[0]
    func = func5
    return func
var14 = func6()
def func2(arg3, arg4):
    var5 = 0
    for var6 in xrange(16):
        var5 += var6 + (arg4 + arg4)
    return var5
def func3(arg8, arg9):
    def func4(acc, rest):
        var10 = acc & -1 + 5
        if acc == 0:
            return var10
        else:
            result = func4(acc - 1, var10)
            return result
    result = func4(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 10'
    print 'arg_number: 55'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
