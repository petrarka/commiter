
def func1(arg1, arg2):
    var20 = var5(arg2, arg1)
    if arg1 < var20:
        var25 = class5()
    else:
        var25 = class7()
    for var26 in xrange(39):
        var25.func6(arg1, arg1)
    def func9(arg27, arg28):
        var29 = (arg2 & 68804275 & arg28) - var20
        var30 = var20 - arg1
        var31 = arg27 | ((176862573 + 197584460) ^ arg27)
        var32 = var30 - var29 | 210175135
        var33 = arg28 | -457
        var34 = var31 & arg28
        var35 = (var30 - var30) & var33 | arg1
        var36 = ((var20 ^ arg27) & var33) - var20
        var37 = (var29 - (505 ^ 1260464800)) & var29
        var38 = arg1 + var33 | arg1 | arg2
        if var38 < var20:
            var39 = 1548083271 ^ (-837 + arg2) - -1075392528
        else:
            var39 = var20 + var38
        result = arg1 + ((arg28 | (var30 | arg1 & arg1 | var20 & 1275963978 | var35) & var35 ^ arg2) - var29) ^ var38
        return result
    var40 = func9(var20, arg1)
    def func10(arg41, arg42):
        var43 = (arg41 - arg1) + (arg1 - -903)
        var44 = ((-527 | var40) - var20) | arg41
        var45 = (arg41 | arg41) | var40 & var40
        var46 = (var43 | arg41) & arg41 - arg1
        var47 = 635378553 - var46 & var20 + -817
        var48 = var40 - arg1
        var49 = arg2 + (-1999285707 | var47) ^ var40
        var50 = arg1 & arg42 ^ arg1
        var51 = 337 | arg1 - (var43 + arg41)
        var52 = arg1 - var48 ^ var47 & -521744625
        var53 = var45 & (var47 ^ var43)
        var54 = arg1 | arg41
        var55 = (arg42 - var48) - arg41
        var56 = var44 | var46
        var57 = var44 | var20
        var58 = var45 & var57
        result = -803 & arg1
        return result
    var59 = func10(arg2, arg1)
    var60 = func13()
    if var20 < var59:
        var61 = 826 | var60 & var59 ^ var40
    else:
        var61 = (var40 ^ arg2 ^ arg2) + -1200258118
    var62 = var20 + (arg1 + -539 | arg2)
    var63 = var20 + arg1 | (var20 + var20)
    var64 = arg2 + 461438035 | arg2 + arg1
    var65 = var40 - var59 + arg2 & var59
    var66 = var65 & var62
    var67 = (var66 | var62) + arg2 & arg1
    var68 = var20 & (var67 & (var62 - var20))
    var69 = (var59 + (arg2 | var63)) | var68
    var70 = var69 | var64 & var20 | 153985996
    var71 = (var63 ^ 2100501146 & arg1) & arg1
    var72 = var63 & (var65 ^ arg1)
    var73 = (-590416408 | arg1 - var59) | arg2
    var74 = -87 ^ (var59 - var68 | var59)
    var75 = (var62 - var40 + var71) + var59
    var76 = var20 & var71 | (var40 - var62)
    var77 = (var66 ^ arg1 | var67) & -343
    var78 = var66 & (var20 & var68) | var74
    var79 = ((var75 ^ 701395294) - var74) + var69
    var80 = var78 + var59 & var71 ^ var66
    var81 = var70 & var68 + var76 & var74
    var82 = var73 - var63 | var66
    result = ((var73 & var71) + var72) & (var79 | (var64 - ((var40 | var74) - (var77 + var66)) - var80 ^ var75)) + var62
    return result
def func13():
    func11()
    result = len(xrange(7))
    func12()
    return result
def func12():
    global len
    del len
def func11():
    global len
    len = lambda x : 3
class class7(object):
    def func6(self, arg23, arg24):
        result = arg23 | 0 + (871661414 - 1562704498 - arg24 - arg23 & 1)
        return result
class class5(class7):
    def func6(self, arg21, arg22):
        result = arg21 + arg22 + -665217910
        return result
def func4(arg6, arg7):
    var8 = arg7 & arg6
    var9 = 281 | 402 - (var8 + var8)
    var10 = (784 & var9) | -872
    var11 = var8 & arg7
    var12 = (-893 - arg6) | var8 - var8
    if arg6 < var12:
        var13 = var9 | var11
    else:
        var13 = arg6 | (var8 | -622 + var9)
    var14 = (372 ^ var11) - (var9 ^ var12)
    var15 = var11 | var12
    if var10 < var11:
        var16 = (15 & var9 - var9) & var10
    else:
        var16 = (var14 - var8) & (287965313 & var15)
    var17 = var9 - (var15 - var12) + var12
    var18 = var14 + var8 - arg6 & var9
    var19 = arg6 | arg6
    result = (var15 ^ var15 + var10 - var17) - var10
    return result
def func3():
    closure = [5]
    def func2(arg3, arg4):
        closure[0] += func4(arg3, arg4)
        return closure[0]
    func = func2
    return func
var5 = func3()
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 14'
    print 'arg_number: 83'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
