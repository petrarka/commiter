
def func1(arg1, arg2):
    var37 = func2(arg1, arg2)
    var38 = 861767261 + ((149 ^ -58 + arg1) ^ 876075742)
    var39 = -1622784398 ^ arg1 | arg2 + arg1
    var40 = 628 ^ var37
    if var37 < var38:
        var41 = ((-631 & 1328487364 - (var38 ^ var38) | var37 + var37) - -1430584731) | arg2
    else:
        var41 = var38 + (-50 ^ var40 | arg2 + var39)
    result = ((96 - -103 & var40) ^ var38 | var40 ^ var40 | var37) ^ ((var40 & var40) - var38 + -825 | -624404625)
    return result
def func2(arg3, arg4):
    var8 = func3(arg4, arg3)
    var11 = class5()
    for var12 in range(41):
        var13 = var11.func6
        var13(arg3, var8)
    var18 = func7(arg3, arg4)
    var25 = func8(arg3, var18)
    var26 = ((arg3 ^ -596) & var8) & 1440892298
    var27 = 404160163 ^ -687284551
    var28 = var8 & var25
    var29 = var25 & (var27 & arg4 + var26)
    var30 = (var25 ^ var28) | var18
    var31 = var30 | 433
    var32 = var30 & (var29 - var31)
    var33 = (var28 + var25) ^ 994
    var34 = var26 + var33
    var35 = arg3 & var31
    var36 = arg3 | var29
    result = -617538772 & (arg4 | var35) - (var26 & (var28 + arg4 | (847306288 - 556) ^ var33 - var26) | var34 + arg4)
    return result
def func10(arg21, arg22):
    var23 = 544 - arg22 | arg21
    result = ((var23 ^ arg22 + (145 & arg21) + -897 - (var23 + arg21) + arg22 - arg22) ^ var23) - 215 | arg21
    return result
def func7(arg14, arg15):
    var16 = 0
    for var17 in range(10):
        var16 += -5 & arg15 | var16
    return var16
class class5(object):
    def func6(self, arg9, arg10):
        return 0
def func3(arg5, arg6):
    def func4(acc, rest):
        var7 = acc & acc + -4
        if acc == 0:
            return var7
        else:
            result = func4(acc - 1, var7)
            return result
    result = func4(10, 0)
    return result
def func8(arg19, arg20):
    def func9(acc, rest):
        var24 = func10(9, 8)
        if acc == 0:
            return var24
        else:
            result = func9(acc - 1, var24)
            return result
    result = func9(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 42'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
