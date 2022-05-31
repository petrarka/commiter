
def func1(arg1, arg2):
    var19 = func2(arg1, arg2)
    var24 = func4(arg2, var19)
    var25 = arg2 + 467
    var26 = arg1 | (((arg1 + (((arg2 + (var19 ^ ((((((arg2 + (-116055918 + (-552556445 - arg1 & 594) - 1753763840) ^ var19) + var19 & arg1) + -854) & arg2) & var25) + -439)) - var25) + var19) - -314)) - var19) & arg2)
    var27 = (var24 - arg2) & -290
    var28 = var19 | ((175 + 191 - (arg1 - var26 & (arg1 | (var26 | var24)) | var27 ^ (var25 + (((var19 | arg1 + var27) - var27 - var24) + arg2) ^ arg2) - 2072841993)) ^ var24) | var19 & var19 | var27
    var29 = arg1 & 1594221784
    result = var27 - var29
    return result
def func4(arg20, arg21):
    var22 = 0
    for var23 in xrange(29):
        var22 += arg20 & var23
    return var22
def func2(arg3, arg4):
    var5 = 0
    for var18 in [(-3 - arg4) ^ i for i in ((9 | i) + i for i in func3(arg3, var5))]:
        var5 += var18 + arg3 ^ -7
    return var5
def func3(arg6, arg7):
    var8 = (-985 & arg6) | 58
    yield var8
    var9 = -778 - 127
    yield var9
    var10 = var9 & -273851236 & -548
    yield var10
    var11 = var9 - (arg7 | (772 ^ var10))
    yield var11
    var12 = (var8 | (1353487842 - -1812509474)) & 494
    yield var12
    var13 = var10 - (arg7 & -635762605) & var12
    yield var13
    var14 = (var8 | var8) - var8 & var10
    yield var14
    var15 = var14 | var9
    yield var15
    var16 = var15 | (var15 & var13) | arg7
    yield var16
    var17 = var12 ^ var10
    yield var17
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 5'
    print 'arg_number: 30'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
