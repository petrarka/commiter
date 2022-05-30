
def func1(arg1, arg2):
    var3 = func4()
    var51 = func5(arg2, var3)
    var52 = var51 & arg1
    var53 = arg2 + var51
    var54 = (arg1 & arg1 | var3) | var52
    var55 = (var51 + -144273064) | (var53 | -142)
    var56 = -70699631 + arg2
    var57 = ((var55 - var51) + var56) - 369163727
    if var56 < arg2:
        var58 = var53 & 787061483 + var53 ^ var3
    else:
        var58 = var52 & (-1122007903 + arg1 + var55)
    var59 = ((var52 ^ arg2) & var56) & arg2
    var60 = (var56 & var57) & var55 | var52
    var61 = ((var59 - var53) & var52) - var59
    var62 = (95 - var59) - (var60 & var3)
    var63 = var62 ^ -820365391 | var3 ^ var53
    var64 = var56 - var53 + var53 ^ 389
    var65 = (var61 ^ arg1) | var64 & var59
    var66 = var51 + arg2 & (var53 & -718)
    result = (815 - (732 - var56) - var52) - (var60 & var59) | var51
    return result
def func7(arg6, arg7):
    var11 = func8(arg7, arg6)
    def func10(arg12, arg13):
        var14 = (arg13 + var11 ^ -128211748) & arg7
        var15 = arg7 - (var14 ^ (arg6 & 633))
        var16 = var14 - arg13
        var17 = var14 + var11 + var11 | var15
        if arg7 < var16:
            var18 = -541 & 1355674120
        else:
            var18 = (-480173216 | arg7) - -990234656
        if var14 < var15:
            var19 = ((var14 + arg12) + arg12) + -228
        else:
            var19 = (var16 | var17 | var14) - arg7
        var20 = -2052523000 & ((543166724 + arg6) | arg13)
        var21 = -141 | arg13
        var22 = ((-730 + var15) + -292) + var11
        var23 = ((var11 & arg7) ^ arg13) + var21
        var24 = var11 & var23 & 1207954634
        var25 = ((var11 | var23) ^ 1096472545) + var23
        result = (arg12 | 586 + ((var23 | var23 - (((arg7 & arg6) ^ var11) | var22) | var24) ^ var23) + var17) ^ var16
        return result
    var26 = func10(var11, arg7)
    var31 = func11(var26, arg7)
    var32 = arg7 & 299405234
    var33 = var11 | 61033028
    var34 = ((var26 ^ arg6) - 987) + var33
    var35 = arg6 + var34 ^ var34 + arg7
    var36 = var32 ^ (arg7 - var31)
    var37 = (var33 & arg7) - var26 - arg7
    var38 = (var26 | var11) + var11 | var11
    var39 = (-247877586 + var34 | var33) + -602
    var40 = (var39 ^ -625) & var36
    if var11 < var38:
        var41 = (var37 ^ (var35 - var34)) ^ 2139223030
    else:
        var41 = var33 & var26 ^ var11
    var42 = var40 - var39
    if var36 < var40:
        var43 = var36 & var34 + arg6 - var40
    else:
        var43 = var35 | var38
    var44 = ((var31 ^ var34) - var39) - arg7
    var45 = var34 + var31
    if var36 < var36:
        var46 = var26 | (arg7 | var33)
    else:
        var46 = arg7 + (arg7 ^ var42) | var32
    var47 = var35 - (331 - (var32 & -316))
    var48 = var31 & var39
    var49 = ((var38 + var42) & var40) - arg7
    result = var38 - var32 - var39
    return result
def func11(arg27, arg28):
    var29 = 0
    for var30 in range(11):
        var29 += (var29 | arg27) ^ arg27
    return var29
def func4():
    func2()
    result = len(xrange(41))
    func3()
    return result
def func3():
    global len
    del len
def func2():
    global len
    len = lambda x : -5
def func8(arg8, arg9):
    def func9(acc, rest):
        var10 = -6 ^ acc + 3
        if acc == 0:
            return var10
        else:
            result = func9(acc - 1, var10)
            return result
    result = func9(10, 0)
    return result
def func5(arg4, arg5):
    def func6(acc, rest):
        var50 = func7(6, -7)
        if acc == 0:
            return var50
        else:
            result = func6(acc - 1, var50)
            return result
    result = func6(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 12'
    print 'arg_number: 67'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
