
def func1(arg1, arg2):
    var7 = func2(arg2, arg1)
    var24 = func3(arg2, var7)
    var44 = func6(var24, arg1)
    var45 = 926482245 & arg1 - arg2
    result = 794684183 ^ arg2
    return result
def func6(arg25, arg26):
    var27 = (-1663497193 | (-442 & 1001364763)) & 682
    var28 = arg25 & (-498 + arg25) & 432
    var29 = 918 | ((-484 - arg25) + var28)
    var30 = var29 - 696 | (-321 + 1816296387)
    var31 = -667 + var28 - var28 ^ var29
    var32 = var27 ^ (var31 & var31)
    var33 = (var31 + arg26 ^ var27) | var32
    var34 = 314 - 159339869
    var35 = (var29 ^ var32 ^ var34) | arg26
    var36 = var35 - var30
    var37 = -97 & ((var31 + var29) & var30)
    var38 = (var36 + var29 + var31) - arg25
    var39 = (var35 ^ var32) ^ arg25 + var29
    var40 = 1679215412 | var28 - var31
    var41 = (var40 + 758662344 & var32) - var30
    var42 = var34 ^ var27 - (var31 ^ var27)
    if var27 < var36:
        var43 = var27 + var30
    else:
        var43 = var36 | var40
    result = (((var33 + var40 ^ var28 + (var40 & (var42 | 84964194))) ^ -603) | var30) | var34 ^ var42
    return result
def func3(arg8, arg9):
    var14 = func4(arg9, arg8)
    var19 = func5(var14, arg9)
    var20 = -874 ^ var14
    var21 = (-162662629 & var19 & arg8 ^ (var14 ^ 689 ^ var14 ^ arg8) - var19 & var20 - (var14 ^ (arg8 & -756))) & var20 ^ (var19 & arg9 & -195606454 ^ var19 - 1281353952)
    var22 = arg8 - var21
    var23 = ((arg8 & var21 ^ (((arg9 - -171227010) & ((arg8 - var14) - var20 + arg9) + var21) | (var19 + -87 | var14)) ^ (var21 - (((-990 - var14) & arg9 ^ arg8) & (-1789051969 | 88))) & var21) ^ var22) | -934
    result = (var19 | var21 + (arg8 ^ (-687 ^ (arg8 + 1135446625) & var20 ^ (var20 ^ var20) + var22)) ^ var20) - arg9
    return result
def func5(arg15, arg16):
    var17 = 0
    for var18 in range(43):
        var17 += arg15 | arg15 | var17
    return var17
def func4(arg10, arg11):
    var12 = 0
    for var13 in xrange(21):
        var12 += (var12 + var12) & -8
    return var12
def func2(arg3, arg4):
    var5 = 0
    for var6 in range(26):
        var5 += var6 | arg3
    return var5
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 7'
    print 'arg_number: 46'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
