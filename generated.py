
def func1(arg1, arg2):
    var43 = func2(arg1, arg2)
    var67 = func7(arg2, arg1)
    var68 = 1505804536 + var67
    var69 = var68 ^ 520
    result = (var43 | (1615736801 & var43 | var69) + var43 - arg1 & var69 + 1380246891) & arg1
    return result
def func9(arg46, arg47):
    var48 = arg46 & arg46 ^ arg47
    var49 = (arg46 & var48) + -948 - arg47
    var50 = -1022018527 + arg46
    var51 = ((1949362769 | 919080827) - var48) + var48
    var52 = var49 + var51
    var53 = ((arg46 & var48) - arg47) | var48
    var54 = 203 & var52 ^ var53 ^ var53
    var55 = var53 + (arg47 ^ arg46)
    if var55 < var54:
        var56 = arg47 ^ var48
    else:
        var56 = (var52 - var50 - arg46) | arg46
    var57 = var50 - arg46
    var58 = 736571217 ^ arg47 | arg46 + var52
    var59 = var58 ^ arg46 + var53
    var60 = var53 ^ var52 ^ 892
    if var50 < var55:
        var61 = var57 - (var50 - var60) & 990
    else:
        var61 = var57 + ((var59 + arg46) + var60)
    var62 = var53 - var52 + -352 - var48
    if arg46 < var54:
        var63 = var51 - var62
    else:
        var63 = var52 + var58
    var64 = var57 ^ var55 + var55 ^ var57
    var65 = var59 + (var64 - arg47 & -677)
    result = arg47 - -750
    return result
def func2(arg3, arg4):
    var9 = func3(arg3, arg4)
    var12 = class4()
    for var13 in xrange(29):
        var14 = var12.func5
        var14(arg4, var13)
    var19 = func6(arg3, arg4)
    var20 = (var9 ^ (671 + arg3)) ^ var9
    var21 = -207 ^ (-249 - arg4) - arg3
    var22 = -118 ^ var21
    var23 = var19 ^ var9 | arg4
    var24 = (var9 + -215090657 ^ var22) & arg4
    var25 = arg3 ^ var21 - var9 ^ var24
    var26 = (var23 | 812110403) | var20 & var20
    var27 = (-1616451002 ^ var21) | arg4
    var28 = var20 | var26
    var29 = var22 | (var20 ^ arg3) & 113
    var30 = var29 & 682
    var31 = var30 - var30
    var32 = var24 - var31 + var22 + var25
    var33 = var21 + var20 ^ var23
    var34 = var22 | var28 ^ arg4 | var9
    var35 = ((var28 | var26) ^ var19) & var28
    var36 = arg4 + (var20 ^ var31 + var9)
    var37 = var30 ^ var9 + arg4 | var30
    var38 = var33 - (var21 + var21) ^ var26
    var39 = (39 ^ -1967464080 ^ var20) - var36
    var40 = var38 | var26
    var41 = ((arg4 ^ var31) | var40) + var31
    var42 = var35 & var37 & var30 & var34
    result = var19 ^ ((var41 + (var23 & ((var39 | var33) - var31) - var9 | var28)) & var9 + var34 + -259901180 + var31)
    return result
def func6(arg15, arg16):
    var17 = 0
    for var18 in xrange(50):
        var17 += (7 - arg15) - var18
    return var17
class class4(object):
    def func5(self, arg10, arg11):
        return 0
def func3(arg5, arg6):
    var7 = 0
    for var8 in xrange(36):
        var7 += var7 + (var7 & var7)
    return var7
def func7(arg44, arg45):
    def func8(acc, rest):
        var66 = func9(acc, 1)
        if acc == 0:
            return var66
        else:
            result = func8(acc - 1, var66)
            return result
    result = func8(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 10'
    print 'arg_number: 70'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
