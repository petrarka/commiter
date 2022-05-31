
def func1(arg1, arg2):
    var16 = var5(arg1, arg2)
    var17 = func8()
    var43 = var20(arg1, var16)
    if var17 < arg1:
        var48 = class12()
    else:
        var48 = class14()
    for var49 in xrange(17):
        var50 = var48.func13
        var50(var17, var17)
    if arg2 < var43:
        var51 = var43 & 121
    else:
        var51 = 639 | var43
    var52 = var43 ^ (arg1 + var17 + arg1)
    var53 = (584 + arg1) & var52 - var52
    var54 = var53 - var52 | -361270756
    var55 = var43 & var43
    if var54 < var54:
        var56 = var43 + ((var53 | var16) + arg1)
    else:
        var56 = ((arg2 - var17) | var16) | var54
    var57 = -1077508890 & (-1042427617 ^ var16)
    var58 = arg2 | arg1
    var59 = var58 | var55
    var60 = 699 & 391 ^ (-798805306 | var52)
    var61 = (var58 + var55) & var60 ^ var52
    if var60 < var57:
        var62 = var52 | -1372283866
    else:
        var62 = var17 + (var52 + arg2)
    var63 = 313 + var17
    var64 = var17 | var16 & (var59 ^ var61)
    var65 = var59 + var16 | var59 & var61
    var66 = var59 | var55
    var67 = (var60 + var63) - (var16 + arg1)
    var68 = var17 + arg1 | var53 - var59
    var69 = (var65 | var67 & var54) - var59
    var70 = (var58 & var63) | var52 & var60
    var71 = var54 - (-114 + var59) | var57
    var72 = var60 & var64
    result = var55 ^ var52
    return result
class class14(object):
    def func13(self, arg46, arg47):
        return 0
class class12(object):
    def func13(self, arg44, arg45):
        return 0
def func11(arg21, arg22):
    var23 = -1447555444 & 636 - (arg21 & arg22)
    var24 = -1189637573 - arg22
    var25 = (arg21 - -232 ^ var23) + 587322405
    var26 = var24 & -2109245987 + (var25 + var23)
    var27 = var23 | var23 & arg21 - var24
    var28 = var27 ^ -310 & var26 + var24
    var29 = (arg22 ^ 1149875656) + var24
    var30 = (var29 - var25) | var29
    var31 = arg21 - var30
    var32 = ((311 & var23) & var26) & var31
    var33 = var28 | var31 & var24 | var24
    var34 = (var28 - var24) & (var31 | var29)
    var35 = arg22 - var24 & var31
    var36 = (var34 + var35) ^ var24
    var37 = var28 - var30
    var38 = (var25 | var23 - var27) | var31
    var39 = var26 | var33 & var32 + var33
    var40 = var36 + var29
    var41 = (var29 & var35) - arg21 - var37
    if var39 < arg22:
        var42 = var39 + arg21
    else:
        var42 = (var31 & var25) - (var33 + var24)
    result = ((var35 ^ var41 - (((var32 - var35 & var24 + var25) - var31) + var30) & var31) - var30 & var24) - var36
    return result
def func10():
    closure = [4]
    def func9(arg18, arg19):
        closure[0] += func11(arg18, arg19)
        return closure[0]
    func = func9
    return func
var20 = func10()
def func8():
    func6()
    result = len(range(14))
    func7()
    return result
def func7():
    global len
    del len
def func6():
    global len
    len = lambda x : 4
def func4(arg6, arg7):
    var12 = func5(arg6, arg7)
    if arg7 < var12:
        var13 = (var12 + arg7 ^ 155 + ((var12 ^ arg7 + 775) - arg6 | -864 | var12) & 635) | arg7
    else:
        var13 = -342413609 ^ (627 & arg7) | var12
    var14 = -493723072 + arg6
    var15 = 369894185 + arg7 - (arg7 ^ 2135016420) & arg6 - var14
    result = (var12 + arg7) ^ (var14 | ((arg6 - arg6 + -720) & arg7 & arg7 - (var14 & arg7)) - -1212654197) + var14
    return result
def func5(arg8, arg9):
    var10 = 0
    for var11 in range(7):
        var10 += var11 ^ arg9
    return var10
def func3():
    closure = [1]
    def func2(arg3, arg4):
        closure[0] += func4(arg3, arg4)
        return closure[0]
    func = func2
    return func
var5 = func3()
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 16'
    print 'arg_number: 73'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
