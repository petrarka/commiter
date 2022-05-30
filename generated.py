
def func1(arg1, arg2):
    var60 = func2(arg1, arg2)
    var61 = (arg2 | 2064314834) + 52107520
    var62 = 303 | arg1 + (arg2 & arg2 | -2050363874 ^ arg2 + (((((var60 + arg1) & arg1 | arg2) - (arg2 ^ -892 ^ arg1)) | arg1) & arg2)) - arg2 | var60 | var61 | 866 ^ var60 | arg2 - 493553078
    var63 = (arg1 & arg1 ^ var62) - var62 ^ (987 ^ (arg1 ^ (arg1 - arg2) & arg2) ^ (1322031045 & var61 & var60 + ((var61 & arg1 - (var62 | ((arg1 ^ var61 & var60) & arg1 + var62) & -988077373)) | var60)))
    var64 = (-283927201 & arg1 - var61) ^ (var62 & var63)
    result = -57 - var60 | 1993694273
    return result
def func4(arg5, arg6):
    var11 = func5(arg5, arg6)
    var46 = func6(var11, arg6)
    var47 = func12()
    var48 = var11 - var46
    var49 = ((arg5 ^ var46) ^ var47) ^ var46
    var50 = (var11 + arg6) & arg6 ^ 656
    var51 = 72 - (-1067076762 + (930 - arg5))
    var52 = var46 ^ ((var49 + var49) & var11)
    if var50 < arg6:
        var53 = var47 | (var51 - (arg5 ^ arg5))
    else:
        var53 = var11 ^ (var47 ^ 838272917) - 1424596873
    var54 = var46 - (var49 | arg6) - var52
    var55 = var46 ^ var46
    var56 = (arg5 & -655352978 ^ var50) & var49
    var57 = -978 | (var46 ^ var51) & -254627873
    var58 = (var50 | -536219161 - -884) ^ var54
    result = (363700916 - var57 | var57) ^ var58 ^ arg5
    return result
def func12():
    func10()
    result = len(xrange(45))
    func11()
    return result
def func11():
    global len
    del len
def func10():
    global len
    len = lambda x : 0
def func6(arg12, arg13):
    var22 = var16(arg13, arg12)
    var23 = 474 & arg12
    var24 = arg12 - 116186718 & -1615511862 + -1566168377
    var25 = var23 + var22
    if var24 < arg13:
        var26 = -222 & (var25 + arg12) & arg12
    else:
        var26 = (-857 + var25) - (1706122263 - var24)
    var27 = (var22 | var25 - arg12) + arg13
    var28 = var22 | var24 ^ arg12 - var23
    var29 = arg12 & var25 ^ var25 ^ var24
    var30 = ((var23 - arg12) | var25) - var23
    var31 = var22 ^ (var28 + var28 + var28)
    var32 = (var28 - var25) | var24
    var33 = 870645597 + 195692682 ^ var29
    var34 = (arg12 - var33) - var24
    var35 = arg12 - var29 ^ var24 ^ var32
    var36 = var34 - var31
    var37 = (var23 | 111585941) - var27
    if arg12 < var23:
        var38 = -684 | var22 + -843276768 & arg13
    else:
        var38 = var36 & arg13 | arg12 | var27
    var39 = arg13 + var35 | (var22 | var31)
    var40 = (arg13 | var36) | -806
    var41 = var35 & (-391 & var39) | var35
    var42 = (var36 | arg13 | var27) ^ 41
    var43 = ((var22 - var30) | var33) & var25
    if arg12 < var36:
        var44 = var43 + (var23 ^ var31)
    else:
        var44 = var30 & var23
    var45 = var37 - arg12
    result = (var32 + var32 ^ (var37 ^ (var35 + (var32 & (var23 - var42))) & var22 | var35) | var29 & var31) - var39
    return result
def func9(arg17, arg18):
    var19 = arg18 + (1864786586 ^ arg18 + arg18 + arg17 ^ -849463013 ^ (((arg17 + (-1500169970 & 345 | (arg18 & (413 + (((421 ^ 720) ^ arg17) & -2052146403)))) & arg17) & 559 | arg18) & arg18) | -60 | arg18 & arg18)
    var20 = 698 ^ (-478244624 - -423989315 | var19 - arg18 + var19 | ((arg18 & 896) | ((-634 - arg18 | arg17 & arg17 - -357) ^ arg18)) + 1801251782 + arg17 & -362520895) - arg17 ^ var19 | arg18 + -26795680 ^ arg17
    var21 = (var20 - (2070690683 ^ var20 + arg18)) + (588 | var19 + arg18) | -782539547 + arg18
    result = (var21 | -539) + arg18 + arg17 - var19 - (var19 - var20) | var20 | var19
    return result
def func8():
    closure = [-9]
    def func7(arg14, arg15):
        closure[0] += func9(arg14, arg15)
        return closure[0]
    func = func7
    return func
var16 = func8()
def func5(arg7, arg8):
    var9 = 0
    for var10 in xrange(31):
        var9 += arg7 + var9
    return var9
def func2(arg3, arg4):
    def func3(acc, rest):
        var59 = func4(-4, 4)
        if acc == 0:
            return var59
        else:
            result = func3(acc - 1, var59)
            return result
    result = func3(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 13'
    print 'arg_number: 65'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
