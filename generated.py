
def func1(arg1, arg2):
    def func2(arg3, arg4):
        var24 = func3(arg2, arg4)
        var29 = func4(arg4, arg2)
        var34 = func5(var29, arg2)
        if var24 < arg4:
            var35 = arg3 + (arg3 ^ var29) + arg2
        else:
            var35 = arg2 ^ (var24 & var34 ^ 247)
        var36 = (arg1 - arg2) & 632
        var37 = var36 | ((var29 | arg4) - var24)
        var38 = var36 - arg2 ^ var34 & arg3
        if var29 < arg2:
            var39 = arg4 - 195 ^ arg3
        else:
            var39 = arg3 + var37
        var40 = var36 - arg2
        var41 = var40 + var37 - var29 - var29
        var42 = arg2 | -1028880204 - var41 | var36
        var43 = var37 - var40 + var41 - var29
        var44 = 693 ^ (var37 ^ var37) + var34
        var45 = 413 ^ var37 & var24 ^ -516
        var46 = var38 | (var38 & var38 ^ arg4)
        result = var45 ^ var34
        return result
    var47 = func2(arg2, arg1)
    var52 = func6(var47, arg1)
    var53 = (240 ^ ((arg2 & (((arg1 ^ arg2) & var52) + ((arg2 ^ arg2 + arg2 - arg2) + 717 | arg2) - 341) | var52) ^ var52 | var52 + (768 - -750 ^ 1363225873) ^ var52) - var47 + arg1) + arg1
    var54 = var47 + (666 | (arg2 ^ ((var47 - 57577407) & var53 + -42)) ^ arg1 & 1506511589) + 2087063874 ^ -1323195652 - var53 ^ var52
    var55 = arg1 ^ arg2
    result = var54 - -408 + (683253683 ^ arg1) ^ (var55 ^ arg2 ^ arg2 | var55) ^ ((var47 & var47 ^ var53) ^ var55)
    return result
def func6(arg48, arg49):
    var50 = 0
    for var51 in range(1):
        var50 += (arg48 | var51) + var50
    return var50
def func5(arg30, arg31):
    var32 = 0
    for var33 in xrange(15):
        var32 += (var32 - var33) & var33
    return var32
def func4(arg25, arg26):
    var27 = 0
    for var28 in range(22):
        var27 += var28 & arg26 - arg25
    return var27
def func3(arg5, arg6):
    if arg6 < arg5:
        var7 = (arg6 + -1495314576) & 1003439859 - arg5
    else:
        var7 = (arg6 | 571837033) - arg6 | -674
    var8 = ((arg5 + 213596735) - -514) & 1806930006
    var9 = -423981454 ^ (var8 ^ -365) & arg5
    var10 = -404 ^ arg6
    var11 = var10 ^ var10
    var12 = -1661947976 + (arg5 + var11) - var8
    var13 = var8 - arg5 & arg6 - var10
    var14 = var8 ^ var9
    var15 = var10 & var8
    var16 = (1146905526 ^ var13) | arg5
    var17 = var9 ^ var15 + arg6 | var10
    var18 = var12 + arg5
    if arg6 < var10:
        var19 = var17 ^ var11
    else:
        var19 = var11 + var12
    var20 = var9 ^ var16
    var21 = var12 & var20
    var22 = var17 ^ var8 ^ arg5 + var12
    var23 = var15 - (var22 & 2098783902 ^ var20)
    result = (arg6 + var16 ^ var18 & (arg5 - ((var12 + (-472 ^ var12) ^ var18 & var21) + var17)) + var22) | arg5
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 7'
    print 'arg_number: 56'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
