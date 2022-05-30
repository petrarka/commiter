
def func1(arg1, arg2):
    var51 = var5(arg1, arg2)
    var58 = func12(arg1, var51)
    var59 = arg1 + var58 ^ -919126483 - arg1
    var60 = -10 + var59
    var61 = (var59 - 811 & arg1) + var51
    var62 = -446 + var61
    var63 = var61 | (1951375587 - var60) | arg1
    var64 = (var51 - var61) & arg2 | 1924420474
    var65 = var64 - (var60 ^ -565611502 + var60)
    var66 = (var58 & var58) ^ -423033020 + var62
    var67 = (-669 | var51) | arg1 | arg2
    var68 = var59 & var61 ^ var51 ^ var58
    var69 = var66 - var60 - var61
    var70 = ((var64 | var59) | 1974629652) - var67
    var71 = 879759405 - var68
    var72 = (var63 - arg1 & var61) ^ var60
    var73 = var58 + (arg2 | var59)
    var74 = (arg1 + var71 ^ var72) + var63
    result = 843 ^ (var70 | (var62 | var71))
    return result
def func12(arg52, arg53):
    var54 = (-744 ^ ((arg53 ^ ((arg52 & 554938760) + (-969108037 | -502)) | -1412675374) | arg52 | arg52)) & (((arg52 & 616028666 & arg52 & 1036440465) | 1082972914) ^ 1282777174) | arg53
    var55 = arg53 - var54 | -664
    var56 = 1585030032 ^ (arg52 + arg52)
    var57 = var55 & var56 ^ ((var54 & (2131967658 & var54) + var55) ^ var55) ^ (var56 | arg53 & var55 & -112)
    result = var56 & ((var56 & arg52 + arg52) | (arg52 - var56) - (var55 | arg52) + (arg53 | var56)) + var54
    return result
def func4(arg6, arg7):
    if arg6 < arg6:
        var12 = class5()
    else:
        var12 = class7()
    for var13 in xrange(13):
        var14 = var12.func6
        var14(arg7, var13)
    var21 = func9(arg6, arg7)
    var25 = func10(arg6, var21)
    var26 = var21 | -165
    var27 = var26 | arg6
    var28 = arg6 & var27
    if var25 < arg7:
        var29 = arg6 & var25
    else:
        var29 = var25 + (var27 | arg6)
    var30 = (var27 ^ 1930172598) | var26 & var28
    var31 = -865698437 + var21
    var32 = var31 | (var31 - var26) & 1106168790
    var33 = (var30 & var28) - var30 | var30
    var34 = (1859534703 & (var21 + var30)) - 470
    var35 = var32 | -483524101 - var21 | 527032172
    var36 = (arg6 ^ var35 - var27) + arg6
    var37 = arg6 & var21
    var38 = (var27 - var30 ^ arg6) ^ var33
    var39 = (var28 + (542 ^ -442)) & var32
    if var25 < var26:
        var40 = var32 & var35 - var21
    else:
        var40 = var31 + var34 & var39
    var41 = var38 ^ (var28 + var33) ^ var30
    var42 = var21 - var41 - (var39 - arg6)
    var43 = var28 + var37 & var31 ^ var39
    var44 = (-132 - var42) | var30
    var45 = -536 + var30 + var35 - var31
    var46 = var36 | var27
    var47 = var32 ^ (var30 + var21 & -1755329398)
    var48 = (var35 - arg6) | var36 & var30
    var49 = (var36 & (var28 | var31)) - arg6
    var50 = var28 | var39
    result = var27 + var39
    return result
def func9(arg15, arg16):
    var17 = arg15 | arg15 | (607 | -419) - arg16 + 1883060334 ^ (-798 | 1126609486) & arg16
    var18 = var17 | (304 - -1468597970)
    var19 = arg16 - 664 | var17
    var20 = ((var18 & arg16) + ((arg16 | -289149152 - var18 & (var17 | -560753144) & 502974906) & var17)) | arg15 - (var18 ^ (arg15 | (arg15 | (arg16 + (-506 | arg16)) | -1723002235) - arg15 | var18 - arg16) & var19 + arg15)
    result = var18 + ((-1439740920 & var20 ^ arg16 & var18 ^ var18 - -443924840) & ((((arg16 ^ -287) ^ var19) + -420) ^ var19))
    return result
class class7(object):
    def func6(self, arg10, arg11):
        result = arg10 + -410064882
        return result
class class5(object):
    def func6(self, arg8, arg9):
        return 0
def func3():
    closure = [-6]
    def func2(arg3, arg4):
        closure[0] += func4(arg3, arg4)
        return closure[0]
    func = func2
    return func
var5 = func3()
def func10(arg22, arg23):
    def func11(acc, rest):
        var24 = rest + rest + -3
        if acc == 0:
            return var24
        else:
            result = func11(acc - 1, var24)
            return result
    result = func11(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 13'
    print 'arg_number: 75'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
