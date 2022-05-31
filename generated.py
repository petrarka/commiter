
def func3(arg8, arg9):
    var13 = func4(arg9, arg8)
    var18 = func5(arg8, var13)
    var22 = func6(var18, arg8)
    var23 = func10()
    var24 = (-273549430 - var22) & 1943119653 ^ var22
    var25 = -356 & var13 - 1591723794 & var24
    var26 = 336 & var25 - var23 + -743633475
    if var26 < arg8:
        var27 = ((var26 - -919140729) - arg9) & var22
    else:
        var27 = var26 - var24 - var26 ^ var25
    var28 = (663 & var24) ^ arg9 + arg8
    var29 = var13 & (var23 - var13 | -368193842)
    var30 = arg9 ^ var26
    var31 = ((var18 & arg9) - var24) & var22
    var32 = (arg9 | var13) & var23 - arg9
    var33 = var25 | var25 - var22 ^ var23
    var34 = var31 | var18 - var32 - var30
    var35 = -302 | var32 & (var34 | arg8)
    var36 = var25 ^ var31 & var31 ^ var23
    var37 = (var35 ^ -337208170 - var35) & arg8
    var38 = (var13 ^ var31 | var25) ^ var23
    var39 = var26 + (var33 - var33)
    var40 = var34 + var13
    var41 = (var13 + var31) + (var37 | var25)
    var42 = var29 | var40 + var31
    var43 = var41 ^ var35
    var44 = var29 + var41
    var45 = (var33 | (var13 ^ var24)) ^ var38
    var46 = var22 + (var39 | var23 ^ var18)
    result = (arg9 | var23) & ((var23 + var43 ^ 212) ^ 1619830469 & ((99 - var29) - var18) | var41 & var28) & var37
    return result
def func10():
    func8()
    result = len(range(49))
    func9()
    return result
def func9():
    global len
    del len
def func8():
    global len
    len = lambda x : 8
def func5(arg14, arg15):
    var16 = 0
    for var17 in xrange(17):
        var16 += var17 - (arg15 + arg14)
    return var16
def func4(arg10, arg11):
    var12 = arg11 - -796 + ((306021326 & arg10) + 791400693) ^ 1769494549 + 557 - arg11
    result = var12 | var12
    return result
def func1(arg1, arg2):
    var7 = func2(arg1, arg2)
    result = var7 + (arg1 & arg2) + ((((1721269796 - arg2) ^ arg1 ^ arg2) | arg1) + ((869 | arg2) & -548) + -256)
    return result
def func2(arg3, arg4):
    var5 = 0
    for var6 in xrange(48):
        if var6 < var5:
            var5 += var6 | arg3
        else:
            var5 += arg4 + var6
    return var5
def func6(arg19, arg20):
    def func7(acc, rest):
        var21 = acc ^ -10
        if acc == 0:
            return var21
        else:
            result = func7(acc - 1, var21)
            return result
    result = func7(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 1'
    print 'func_number: 3'
    print 'arg_number: 8'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 47'
    for i in xrange(25000):
        x = 5
        x = func3(x, i)
        print x,
