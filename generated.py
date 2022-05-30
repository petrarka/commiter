
def func1(arg1, arg2):
    var24 = var5(arg2, arg1)
    var29 = func5(var24, arg1)
    var55 = func6(arg2, var24)
    var63 = func7(var24, arg1)
    var67 = func8(arg1, var63)
    var68 = (arg2 + var24 & var67 + -364 | var67) ^ (var67 | (var63 & (var29 - var29 - arg2 - var63 + 529 + var29) - -1405929555 & var24)) & 54 ^ var29 - arg1
    var69 = 570 & ((var55 ^ var63 | arg2 | var68) ^ 783)
    var70 = ((((arg1 | (((arg1 & -293407634 & (var69 & arg2 + var24 - (var29 + var29 | var29 | (var55 | var68) + arg2) & arg2) & var68) & arg1) - var67)) + var67 - arg2 | var63) + -789) ^ var29) ^ var67
    var71 = var68 + var24
    result = var55 ^ var63
    return result
def func7(arg56, arg57):
    var58 = ((arg57 ^ (arg56 | (arg56 ^ -181)) & arg56 - arg56 - arg56) | 1363759530 + arg57) | arg57 ^ (287 + 171) & arg57 + -820
    var59 = (arg57 - (((arg57 & (39 | -898 + (var58 ^ (arg56 & arg56 | (var58 - arg57 + (arg57 & arg57 - -1586829188 + arg57)))) ^ (arg56 & arg56) | (var58 ^ arg57))) ^ (2004695568 - 764 & 187414845)) ^ 815)) - 21426106
    var60 = var58 & arg57 - -990584063
    var61 = (-151 & arg57) - var60
    var62 = var58 - var61 - (arg57 | -223490372 - var60 | ((-1959143701 ^ 520448410 | var59 - var59) | var59) | (var59 & 743 | arg57 + (var61 & ((-5825296 | arg57) - arg56) | var60 + ((var60 + -1294849535) | arg56))) | 1786682752)
    result = (var58 & (((arg57 + ((var61 + arg57 + -969907055 + -465) - var60)) ^ 313 - var58) & var61)) | arg57 | var59
    return result
def func6(arg30, arg31):
    var32 = arg30 | arg31 - arg30 ^ arg31
    var33 = -1454628114 - (-888749435 & arg31) + var32
    var34 = -920252543 | var33
    var35 = arg30 | arg30 | (-266066153 ^ var33)
    var36 = -969 & var33 + arg30
    var37 = arg30 | (-804460566 + -382 + var34)
    var38 = ((-1021955835 + arg31) + var32) | arg30
    var39 = 236 + ((arg31 ^ arg30) + var33)
    if var39 < var36:
        var40 = (var34 | var38 | var37) + var39
    else:
        var40 = var37 ^ var35
    var41 = var33 & ((arg31 - var37) | var32)
    var42 = var33 - arg31 ^ (var37 | arg31)
    var43 = ((var35 | arg31) - var41) ^ var38
    var44 = (1393227606 | var35 + var39) | var42
    var45 = 180796988 + var37 - arg30
    var46 = var45 ^ (arg31 ^ var44) ^ arg30
    var47 = (var33 - var32 & var38) & var46
    var48 = var45 ^ var46 ^ var36 - var44
    var49 = (var35 + var35) & var46 - var43
    var50 = (var38 + 552) + arg30 & arg30
    var51 = var50 + (var44 - (var47 + arg31))
    var52 = var44 & var36
    var53 = var37 - ((arg30 ^ var45) | var49)
    var54 = var46 - var51 | var47 - var39
    result = var39 + var37
    return result
def func5(arg25, arg26):
    var27 = 0
    for var28 in range(22):
        var27 += var27 & (var28 | arg26)
    return var27
def func4(arg6, arg7):
    var8 = 81413874 & (-868170170 | 705)
    if var8 < var8:
        var9 = ((var8 ^ arg7) ^ 1893433197) & 2005209617
    else:
        var9 = var8 ^ var8 + arg7
    var10 = 629 | arg7 | arg6 - var8
    var11 = ((arg6 | 290022131) | 2014328121) ^ -958945031
    var12 = ((arg6 | -965708545) ^ arg7) - var11
    var13 = (var10 & arg7) & var8
    if arg7 < arg7:
        var14 = arg7 & arg7
    else:
        var14 = -873 ^ var12
    var15 = 1991595393 ^ var11 + -498 ^ arg7
    var16 = var11 & (arg6 - var11) | arg7
    var17 = arg6 + var8 | var10
    var18 = (var8 | var10) + -851
    var19 = var16 | (var10 - var13)
    var20 = var11 + var16 - var10 | var16
    var21 = (1330487039 & var20) - (-714 & var18)
    var22 = var16 & arg6
    var23 = var22 + var13
    result = arg7 + (var11 ^ var17 - ((-582 ^ var11 & ((var21 + var13) - (var12 & var23 & var16) & var8)) - var11))
    return result
def func3():
    closure = [7]
    def func2(arg3, arg4):
        closure[0] += func4(arg3, arg4)
        return closure[0]
    func = func2
    return func
var5 = func3()
def func8(arg64, arg65):
    closure = [0]
    def func9(acc, rest):
        var66 = (acc & (rest ^ -3 - (-1 ^ -4) - acc)) & -3
        closure[0] += var66
        if acc == 0:
            return var66
        else:
            result = func9(acc - 1, var66)
            return result
    result = func9(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 10'
    print 'arg_number: 72'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
