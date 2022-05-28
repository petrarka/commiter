
def func1(arg1, arg2):
    var14 = var5(arg2, arg1)
    var19 = func8(arg1, arg2)
    var24 = func9(var19, var14)
    var32 = func10(arg2, arg1)
    var33 = var14 & (var19 - var32)
    var34 = var32 ^ arg2 & arg2
    var35 = -903 ^ var24 - var34
    var36 = ((var34 ^ var19) | var32) ^ var32
    var37 = var24 & var35 + var14
    var38 = (var36 ^ arg1 | var19) + var19
    var39 = var38 ^ var36
    var40 = var19 & arg1
    var41 = var35 | -683 + var34 | var33
    var42 = var34 ^ ((var34 + var32) ^ var14)
    var43 = (var42 - var41) - arg1
    var44 = var37 ^ var19
    var45 = var42 + (var42 - var41 ^ arg2)
    var46 = var43 ^ var32
    var47 = var46 & var35 | (var43 - arg2)
    var48 = var34 ^ var38 + var36 & var32
    var49 = (240 ^ var44 - arg2) - var37
    var50 = (var46 ^ var41) ^ var48
    if var50 < var38:
        var51 = var41 | var36
    else:
        var51 = var35 ^ arg2 & (var39 ^ var19)
    var52 = (var40 & var47 | -170) ^ var32
    var53 = var48 + (var43 - -423) | var52
    result = var42 ^ var38 + -625 + var33 | var44
    return result
def func10(arg25, arg26):
    var27 = ((289 & arg25) | arg26) & arg26 - arg25 | 202
    var28 = 266 + (684310019 | 170) | var27
    var29 = (2045283933 - (var27 + (var27 + (arg26 | var27)) ^ ((14 + var28) - 1837721880))) & var28
    if var27 < var28:
        var30 = arg25 & arg25
    else:
        var30 = var28 + var27 ^ (var27 + var29) ^ arg26 & -329
    var31 = (var29 | arg25) - ((var29 + ((var28 ^ -2003573369 + -1176928848 ^ 393 | ((arg25 | ((arg26 & arg26) | (850 + -326141774 + var27 - arg26) - (arg25 ^ arg25)) & 962 - 597) ^ 241 | var29)) ^ var29)) | -1979053010)
    result = (arg25 - ((236534431 + (var27 & arg26 | arg25 & (var31 ^ arg26 & arg26))) + var28 & var27)) ^ var28 - var31
    return result
def func9(arg20, arg21):
    var22 = 0
    for var23 in range(12):
        var22 += (arg20 + arg21) + var23
    return var22
def func8(arg15, arg16):
    var17 = 0
    for var18 in xrange(11):
        var17 += arg15 ^ -4 | arg16
    return var17
def func4(arg6, arg7):
    var13 = var10(arg6, arg7)
    result = arg6 + -658 - ((arg7 + -91 & arg6) ^ arg7)
    return result
def func7(arg11, arg12):
    result = ((796 & arg11) + (arg11 + 701710629 | arg12 + (-1145611521 + arg12) - (-2098303076 | (317 + 1179533851 + arg12)))) | arg12
    return result
def func6():
    closure = [-6]
    def func5(arg8, arg9):
        closure[0] += func7(arg8, arg9)
        return closure[0]
    func = func5
    return func
var10 = func6()
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
    print 'func_number: 11'
    print 'arg_number: 54'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
