
def func2(arg22, arg23):
    var49 = var26(arg22, arg23)
    var54 = func8(var49, arg23)
    var58 = func9(var49, arg23)
    var59 = arg22 | ((var54 + 611 | var58 ^ (1574978646 & arg22 - var58)) & 371606266) ^ var54
    var60 = -945904534 | 305
    var61 = ((var58 ^ var54 | arg23) | var54 - var49) & 188305748 & ((((var59 ^ ((1945780785 & (var59 - 913703162) - var54 - var59 ^ var58) - var54) | var59) - var49) - arg22 ^ var59 & 196547067 & arg22) - (var59 & arg22))
    result = var61 ^ var59
    return result
def func8(arg50, arg51):
    var52 = 0
    for var53 in xrange(20):
        var52 += arg51 - arg51 & var52
    return var52
def func5(arg27, arg28):
    var47 = func6(arg28, arg27)
    var48 = -59 - -669
    result = arg27 | arg28
    return result
def func6(arg29, arg30):
    def func7(arg31, arg32):
        var33 = arg29 & (((-99788617 | arg30) & arg32 - arg32) - arg32)
        var34 = (arg32 - (arg32 | (arg29 + (arg32 + ((arg31 | arg29) ^ -1128687204 - -25)))) & var33) ^ -890
        var35 = var33 + arg30
        result = -948109279 ^ arg31
        return result
    var36 = func7(arg30, arg29)
    var37 = (arg29 ^ var36) | var36 & var36
    var38 = var37 | (arg30 - (var36 - 1634264734))
    var39 = (var37 | arg29 ^ var38) - 644309601
    var40 = 205140026 - (arg29 | (arg29 - var39))
    var41 = (arg29 ^ var37) + var37 + var38
    var42 = -1965448491 | arg30
    var43 = var41 - var38
    var44 = var37 | (1817553884 | -1728002326 - var38)
    var45 = (var38 ^ var36 | var41) ^ arg29
    if var43 < var41:
        var46 = var36 ^ -608920875 - 1640521463 - var45
    else:
        var46 = var45 - (var42 - (var36 ^ var37))
    result = var45 + 886
    return result
def func4():
    closure = [-8]
    def func3(arg24, arg25):
        closure[0] += func5(arg24, arg25)
        return closure[0]
    func = func3
    return func
var26 = func4()
def func1(arg1, arg2):
    var3 = 363 ^ -32 + arg2 ^ -1434727444
    var4 = arg1 + var3
    var5 = var4 + arg2
    var6 = (1136061229 | 1081649746) | var4
    var7 = var5 ^ arg2 + (var3 | arg2)
    var8 = arg2 & 1477402104 & var5 ^ var6
    var9 = (var6 ^ -427853147) | -1840960193 + var3
    var10 = (-461 - var6 - arg2) & var5
    var11 = var3 & 243369637
    var12 = var4 | var4
    var13 = var12 ^ (var11 ^ var5) - var3
    var14 = (arg2 | var5) ^ -367
    var15 = var13 | (var14 - var8)
    var16 = var6 - var6 & var15 | var13
    var17 = var10 ^ var14
    var18 = -352 ^ (var13 & var12 | arg2)
    var19 = var16 + var18 & var5 + var5
    var20 = (arg2 | var5) | (var3 & var17)
    var21 = (-375035661 + (var16 - var5)) ^ arg1
    result = (var3 & (var7 - var8 ^ var21)) ^ var19
    return result
def func9(arg55, arg56):
    def func10(acc, rest):
        var57 = 1 + acc
        if acc == 0:
            return var57
        else:
            result = func10(acc - 1, var57)
            return result
    result = func10(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 0'
    print 'func_number: 2'
    print 'arg_number: 22'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 62'
    for i in xrange(25000):
        x = 5
        x = func2(x, i)
        print x,
