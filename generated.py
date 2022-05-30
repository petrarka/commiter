
def func1(arg1, arg2):
    var7 = func2(arg1, arg2)
    var12 = func3(arg1, arg2)
    var13 = func6()
    var29 = func7(arg2, arg1)
    var30 = var12 + var29
    var31 = var29 ^ arg2
    var32 = (-525 - var13) + var12 + arg2
    var33 = ((var31 + var32) | arg1) + (((-59 + var31) & var30) & arg2)
    var34 = ((var12 & -527 | var33) | var32 ^ (var31 | ((((((-1451724510 + var12 ^ var32) | (-645 - 684)) - (arg1 - (var33 & var7) - -430)) - var7) - var13) + var31)) | (arg2 + var32 | (var30 ^ var32))) - 1430069300
    result = var7 + ((var32 | 271 | var29 ^ var31) - var33) | -885 - var34 - var30 ^ var33 + -879
    return result
def func7(arg14, arg15):
    var16 = arg14 & (arg15 | arg14) | -937
    var17 = 846671123 + (-1890625650 ^ 21)
    if var17 < arg14:
        var18 = arg15 ^ -136 ^ arg14 + var17
    else:
        var18 = var17 - var16 ^ arg15 ^ var16
    var19 = var16 + var16
    var20 = (var16 + var16) ^ (var19 + 897)
    var21 = var17 & 774463985 | 972
    var22 = var21 + (arg15 ^ 1947261209 & 1478879841)
    if arg15 < var21:
        var23 = -991 - var20
    else:
        var23 = var16 | var20 - arg14
    if var21 < arg15:
        var24 = -780819532 | (var20 ^ -1464099650) + var19
    else:
        var24 = (var22 | var22 & var16) + var17
    var25 = (arg15 ^ var21 & var20) + arg14
    var26 = arg15 - (var25 ^ var22 & 2039829752)
    var27 = (var21 | var26) - var19 & var22
    var28 = var19 & var19
    result = 1437183668 - (649 | var28) ^ var16
    return result
def func6():
    func4()
    result = len(xrange(34))
    func5()
    return result
def func5():
    global len
    del len
def func4():
    global len
    len = lambda x : 9
def func3(arg8, arg9):
    var10 = 0
    for var11 in range(18):
        var10 += arg9 | (var10 | arg9)
    return var10
def func2(arg3, arg4):
    var5 = 0
    for var6 in [arg4 | i - 9 + (-10 + arg3) for i in xrange(45)]:
        var5 += var5 | arg3
    return var5
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 8'
    print 'arg_number: 35'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
