
def func1(arg1, arg2):
    var9 = var5(arg1, arg2)
    var10 = func7()
    var17 = func8(arg2, var9)
    var27 = func9(arg1, var9)
    var48 = func12(var9, var27)
    var49 = var17 + var10 + -1506863990 ^ (arg2 & -1297264408)
    var50 = var48 & (var9 | (1133205456 - var17)) - -2040278649
    result = (var49 | arg2 - var48) & 389
    return result
def func12(arg28, arg29):
    var30 = 137 - arg29 ^ (arg29 + -852)
    var31 = (arg29 | arg28 & 1486214627) - arg28
    var32 = var30 + (-645 - var30 | -658802210)
    var33 = var30 & var31
    var34 = ((var32 + var30) - var31) & var30
    if var30 < var30:
        var35 = arg29 ^ (arg29 & var33 ^ arg29)
    else:
        var35 = (arg29 ^ arg29 ^ arg29) - arg28
    var36 = var32 ^ (-1768647680 - arg28 & -1408591955)
    var37 = (var31 + (var32 + -103)) - var30
    var38 = var33 ^ var31 & -1000 + arg28
    var39 = -722453167 & -2129935908 - var38 | var38
    if var32 < var33:
        var40 = var34 ^ var39 - -756
    else:
        var40 = var32 | arg29 - var39 + 2117174819
    var41 = arg29 - arg29
    var42 = var30 ^ (var41 - -1768556468) ^ arg29
    var43 = var31 & var36 + var34 ^ var36
    var44 = arg28 | 321 & var43
    var45 = var30 - var33
    if var31 < var38:
        var46 = var45 + (var45 ^ arg29) - 652
    else:
        var46 = (var41 + var36 - var38) | var36
    var47 = -60 | var33 | var38 - var42
    result = arg28 | var43
    return result
def func11(arg20, arg21):
    var22 = -462095485 ^ 1168956377 ^ -1144321174
    var23 = (-58812630 ^ (((var22 & arg20) ^ arg21) + (((((((arg20 | (25420763 & 938879384)) + arg21) ^ arg20 & 217 + 47953931) & (arg20 - -430) - (-1639909440 + arg20) + arg20) - -177201449 - -471190761) - -829) | 223431588))) & arg20 - -695
    var24 = var23 - (arg21 | ((((-449 | (var23 & var22 + arg21) ^ (43 & arg20) & var23) - -289) | (arg20 | arg20)) - (var22 - ((var22 | var23 & (((arg21 ^ var23) & arg20) - var22)) | 1206541558)) | 1662997514 & arg20))
    var25 = (((arg21 - 579) - var24) & var22) ^ -94088596 + var22
    result = arg21 + var23
    return result
def func8(arg11, arg12):
    if arg12 < arg11:
        var13 = -205650743 & 1403844570
    else:
        var13 = arg11 | 514
    var14 = (((449 - arg11) - arg11) | arg11) & arg12
    var15 = (168 ^ ((arg12 ^ -48 + arg11 - arg11) & ((arg12 ^ (var14 - (521474214 ^ -1440863728)) ^ arg12 + (233449693 + (arg12 | arg11) - (-278 ^ 874) ^ arg12 - arg11 ^ var14) & -207994401) - arg11)) - -338) - -273
    var16 = var14 ^ 841151151
    result = (-666 | (arg11 - var16 & (arg11 ^ (-511 + ((arg12 ^ arg11 - -621648643) | var15))))) ^ arg12
    return result
def func7():
    func5()
    result = len(xrange(33))
    func6()
    return result
def func6():
    global len
    del len
def func5():
    global len
    len = lambda x : 8
def func4(arg6, arg7):
    if arg6 < arg6:
        var8 = arg7 | -232 & arg6
    else:
        var8 = arg7 | arg6
    result = arg6 & 56 | 340 ^ (2123708813 ^ 514)
    return result
def func3():
    closure = [5]
    def func2(arg3, arg4):
        closure[0] += func4(arg3, arg4)
        return closure[0]
    func = func2
    return func
var5 = func3()
def func9(arg18, arg19):
    def func10(acc, rest):
        var26 = func11(acc, 2)
        if acc == 0:
            return var26
        else:
            result = func10(acc - 1, var26)
            return result
    result = func10(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 13'
    print 'arg_number: 51'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
