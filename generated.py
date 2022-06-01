
def func1(arg1, arg2):
    var7 = func2(arg2, arg1)
    var34 = var10(var7, arg2)
    var35 = func8()
    var40 = func9(var34, var7)
    def func10(arg41, arg42):
        result = (arg1 ^ (-1368120775 ^ arg2) + var7 | (arg42 | var40 & var40)) | var34 - var7
        return result
    var43 = func10(var7, var40)
    var44 = arg2 - var40 & 1241095828 ^ var35
    var45 = var7 - (var7 | arg1 | arg1)
    var46 = arg2 | 659
    var47 = (var7 | var7) | var40 - var7
    var48 = -223 & var40 | arg1 | -719185871
    var49 = (arg1 ^ var44) | var44
    var50 = var44 | var45
    if var47 < var35:
        var51 = 122 - var50
    else:
        var51 = var45 & arg1
    var52 = var49 & arg2 + arg2
    var53 = var50 ^ var7
    var54 = (arg2 | var43 + var52) + -376
    var55 = var50 + ((var34 | var35) - var53)
    if var48 < var43:
        var56 = var48 - 175
    else:
        var56 = arg2 | var34
    var57 = var50 - (var43 + var40) - var50
    var58 = (arg2 ^ var49) ^ var45
    if var43 < var50:
        var59 = (var47 & var54) & var40
    else:
        var59 = var53 - var34 | var46
    if var43 < var54:
        var60 = var52 + (var43 & arg1 & arg1)
    else:
        var60 = var47 + var47
    var61 = arg2 - arg2
    var62 = var40 & var50 | var46 & var44
    var63 = var55 - var40 | (var57 - var55)
    var64 = var46 | var40 ^ var50 | var44
    var65 = (-1186468622 + var43 | var63) & var34
    var66 = arg2 | var61
    result = ((arg1 | arg2) - var50 ^ var50) & ((var53 & var54 + var58 & 800) ^ var62)
    return result
def func9(arg36, arg37):
    var38 = 0
    for var39 in range(21):
        if arg37 < var39:
            var38 += var39 | var39 | 7
        else:
            var38 += var39 ^ arg37 + var38
    return var38
def func8():
    func6()
    result = len(xrange(37))
    func7()
    return result
def func7():
    global len
    del len
def func6():
    global len
    len = lambda x : -4
def func5(arg11, arg12):
    var13 = ((arg12 - arg12) | -351) - -804
    var14 = -838 + arg12 & 293 + arg12
    var15 = 189 - 667
    var16 = arg11 | 441
    var17 = var14 + 942
    var18 = var17 & var16 ^ -1209334352 & var15
    var19 = var16 - var13 + var16 + arg11
    var20 = var17 + (var13 ^ var14)
    var21 = 2131043403 - (var15 - var20) ^ var13
    var22 = var20 | var18
    if var14 < var16:
        var23 = ((var22 | 1836770414) - -319) ^ var21
    else:
        var23 = (var13 | var17) + (var20 & arg12)
    if var13 < var16:
        var24 = var15 ^ var21 + var13 - arg12
    else:
        var24 = (var18 - var13 + var21) + var13
    var25 = var17 & arg12 - arg12 - var15
    var26 = var19 + (var17 & arg11 | var16)
    var27 = (var21 - var26 ^ var18) ^ var20
    var28 = var13 & arg11
    var29 = var20 + ((var14 | var21) - -1545745122)
    var30 = -455 ^ var18 - var25 & -725
    var31 = (-253 ^ var25) - var25 - var28
    var32 = var26 ^ (553839743 ^ var17 ^ var20)
    var33 = var29 + var13 & var32 - var29
    result = var28 - var27 & var19 ^ (var18 ^ var33) ^ var14 - var22 - arg12
    return result
def func4():
    closure = [-5]
    def func3(arg8, arg9):
        closure[0] += func5(arg8, arg9)
        return closure[0]
    func = func3
    return func
var10 = func4()
def func2(arg3, arg4):
    var5 = 0
    for var6 in xrange(8):
        var5 += arg3 ^ (arg4 ^ 1)
    return var5
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 67'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
