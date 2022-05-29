
def func1(arg1, arg2):
    var6 = func2(arg2, arg1)
    var35 = func4(var6, arg2)
    var36 = func10()
    var37 = arg2 - 981 | ((111391675 - -121300091 ^ 1000205874 - var6 - var6 - var36 & var36 | (arg1 + (arg1 ^ arg1)) + var35) + ((arg2 & (arg2 | (var36 & var36))) | arg1)) - (247074825 ^ var35) | 1430005301 + arg1
    var38 = var6 - 406657098
    var39 = var35 & (var35 ^ (arg1 | arg2))
    var40 = (var6 + var36) - var37
    result = (((-865 & (601 ^ -851017533)) | (var39 & (arg2 - var6))) | var36) | (((var39 - var35) + var6) | var37 | arg2)
    return result
def func10():
    func8()
    result = len(range(39))
    func9()
    return result
def func9():
    global len
    del len
def func8():
    global len
    len = lambda x : 4
def func4(arg7, arg8):
    var9 = 0
    for var34 in func5(arg7, var9):
        if var34 < var34:
            var9 += arg8 & var34 | var9
        else:
            var9 += var34 + var34
    return var9
def func6(arg12, arg13):
    var18 = func7(arg13, arg12)
    var19 = arg13 & ((((arg12 & ((arg13 - arg12 | arg13 | var18) - arg13 | -1337974342) & (((arg13 | (-162 & 669)) - 666249791 & arg13 + arg13 & var18 ^ arg12 & 734) | var18)) ^ arg13) + -496 + var18) - var18)
    var20 = (var18 + 1918637246 & arg13 | arg13 ^ 1007958120) | (var18 & arg12 + (arg13 - (1278912539 ^ (((var18 + arg12) ^ (var18 ^ arg12) - 1780063268) + -190112519 - -899) ^ (var19 & 1155202133)))) + 471860460 ^ var19
    var21 = 333473154 - var20 ^ var18 + var18 + (-685 + 420) ^ var19 & arg13 | arg13 - arg13 - 12
    if var19 < var21:
        var22 = (-191 + var18 ^ var21) | -599114374 - var21 | var20
    else:
        var22 = (((-202671807 ^ arg13 + (var20 ^ var20)) + arg13 + var18 + var21 ^ var19) & (var18 - (var19 | arg12) ^ (var18 + arg13 - -1860613417 & var21) ^ (-318787183 ^ var18) ^ arg13 & var19 - 637)) ^ 67 ^ arg12
    result = ((var20 - ((var18 & arg12) & arg12)) + (var19 - var21)) | ((var19 + 2095577880) - (var19 + var21))
    return result
def func7(arg14, arg15):
    var16 = 0
    for var17 in xrange(30):
        var16 += arg15 & arg14
    return var16
def func5(arg10, arg11):
    var23 = func6(1996892274, -390)
    yield var23
    var24 = 130 | arg10 - -97 + arg10
    yield var24
    var25 = -2067422698 | -888651739 - 1693536266
    yield var25
    var26 = var24 ^ var25
    yield var26
    var27 = 817 & (var25 + -867) + arg10
    yield var27
    var28 = -758 | var25 ^ var26 ^ -1430987440
    yield var28
    var29 = (var24 & var24 + 984) - arg10
    yield var29
    var30 = arg10 & -24 + var27 & arg11
    yield var30
    var31 = (var28 - arg11 & var25) ^ var25
    yield var31
    var32 = (var26 & 940 ^ 349) - var29
    yield var32
    var33 = var30 - var31 | var26 - var24
    yield var33
def func2(arg3, arg4):
    def func3(acc, rest):
        var5 = (rest - 2) & 2
        if acc == 0:
            return var5
        else:
            result = func3(acc - 1, var5)
            return result
    result = func3(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 41'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
