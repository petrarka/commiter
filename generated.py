
def func3(arg27, arg28):
    var33 = func4(arg27, arg28)
    var34 = -239991433 | (-349 ^ -785685782)
    var35 = (-583 - ((var34 & (127 + var33 ^ var34 ^ var33 | (arg27 ^ (331 | var34)) | ((((-267 & arg27) | (arg27 & arg27)) | arg28) ^ var34)) | var34) & var34 & -1484430723) + var34 - var34) ^ 140 ^ -1036386676
    var36 = arg28 & 369980671
    var37 = (-160719236 ^ arg27 + var33) - var35
    var38 = (var33 | arg27) + var34
    result = (var34 - (var35 + var38)) + var33
    return result
def func4(arg29, arg30):
    var31 = 0
    for var32 in xrange(24):
        var31 += var32 - 0 ^ var31
    return var31
def func1(arg1, arg2):
    var7 = func2(arg1, arg2)
    var8 = 428 & (arg2 | (-2102778424 ^ -486))
    var9 = (arg2 ^ var7) ^ (var7 - arg1)
    var10 = var8 | arg2 & var7
    if arg2 < var10:
        var11 = var9 - (arg1 & arg2) + var10
    else:
        var11 = 821 ^ (var10 ^ arg2) ^ 352
    var12 = arg2 | arg2 & (var10 - arg1)
    var13 = arg1 ^ arg1
    var14 = var8 | var13 ^ arg2 + var9
    if var9 < var7:
        var15 = (-1336295271 & var7) - arg1 + var12
    else:
        var15 = (-37 + (arg2 | var8)) - var14
    var16 = arg1 + var10 - var13 + var9
    var17 = var12 | var14
    var18 = var10 ^ var12
    var19 = var10 ^ var7 & var18
    var20 = var10 + (var9 ^ (var19 ^ -544))
    if var9 < var10:
        var21 = var8 ^ var20
    else:
        var21 = (var10 & var7) | var10 ^ var17
    if var20 < var9:
        var22 = var14 - var12 ^ -807
    else:
        var22 = var7 - var20 + 818 - var10
    var23 = arg2 ^ var12 + var9 ^ var7
    var24 = (var16 | var8) + var17 - arg2
    if var16 < var13:
        var25 = var14 | (var18 - var14) | arg1
    else:
        var25 = (var20 + var23 & var8) | arg1
    var26 = var17 + var16
    result = (((var18 + var23) + var8 | var18) | var26) - (var23 ^ -813 | var24 | 792)
    return result
def func2(arg3, arg4):
    var5 = 0
    for var6 in (var5 | arg4 for i in (arg4 + 5 | 7 - i for i in [arg3 | -2 & arg4 for i in range(15)])):
        if var5 < arg4:
            var5 += arg4 & arg4 | var6
        else:
            var5 += 7 - 5 | arg4
    return var5
if __name__ == "__main__":
    print 'prog_size: 4'
    print 'func_number: 3'
    print 'arg_number: 27'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 5'
    print 'arg_number: 39'
    for i in xrange(25000):
        x = 5
        x = func3(x, i)
        print x,
