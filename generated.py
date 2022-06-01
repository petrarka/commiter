
def func1(arg1, arg2):
    var3 = func4()
    def func5(arg4, arg5):
        var6 = var3 - (((((arg4 | arg5) & arg1 + 1089422189 - arg2 - (2112369784 | arg5 ^ (arg5 - arg5))) ^ 414) | arg5) | (-1970387751 | var3 - arg2 | -588914769 | arg2 ^ arg5) - arg2) ^ arg5 | 644 + arg1
        var7 = var3 & var6 - 2003734576 | (var6 ^ (-612 + (var6 + arg1 ^ (((arg4 - (arg4 + (arg2 ^ (arg4 + arg1)) | var6 | var3)) & arg2) | var3) ^ 693) & 214 + arg1) - arg5) & var6 & arg2
        var8 = (((var7 | arg5 | var3 | arg4 | var6) ^ (1663721529 + 1639494540) + (464 - (arg2 + arg5 | (arg1 | arg2 + (-197 - (var3 + (1951013740 + var7))))))) - (arg1 | arg5 | var6 + var7) ^ arg4) & arg1
        result = arg5 ^ arg2 & arg4 + arg4 | -255376518 & (var6 & var6 ^ var6) & arg2
        return result
    var9 = func5(var3, arg1)
    var13 = func6(var9, arg1)
    var18 = func8(var13, var9)
    var22 = func9(var18, arg1)
    var23 = var22 - var18
    var24 = arg1 ^ 1104238271 - var3 - -374902331
    var25 = -1753401622 - (var13 + var3) + arg2
    var26 = 2041060836 & -731788673
    var27 = (var24 ^ (797772296 ^ var25)) + var24
    var28 = ((-148 ^ var24) | var9) ^ arg2
    var29 = var28 + var22
    var30 = var23 + var28 + var25
    var31 = (var22 - var27 + arg1) ^ var29
    var32 = var28 + (var24 - var27) & arg1
    var33 = ((var3 & arg1) + var13) | var23
    var34 = var33 ^ var18
    var35 = arg1 + (var18 | (var25 ^ var31))
    var36 = (var32 - var32) + var27
    result = var36 | var23 | var29 - var3 | (var25 - (var36 | ((-1841926648 + 694308894) - var33) | var22)) + var28 | -1023508918
    return result
def func9(arg19, arg20):
    var21 = (arg19 | (1542062699 + 91 & (arg20 | -152 & 447 - ((2033262790 | -1769139105) | arg20 ^ -204187007 - arg19 & (1499756905 - 1359659961 & -1981827298 ^ -1345756781 - arg19))) ^ 138620316 ^ -49692369 - -108627854) ^ arg20 + -969452411) - arg20
    result = (var21 + var21) + (-175 | 1446783649 & 94896469)
    return result
def func8(arg14, arg15):
    var16 = 0
    for var17 in xrange(33):
        if var16 < var16:
            var16 += arg15 & arg15 & 6
        else:
            var16 += -7 | -1
    return var16
def func4():
    func2()
    result = len(xrange(31))
    func3()
    return result
def func3():
    global len
    del len
def func2():
    global len
    len = lambda x : -7
def func6(arg10, arg11):
    def func7(acc, rest):
        var12 = 0 | (-2 ^ 3)
        if acc == 0:
            return var12
        else:
            result = func7(acc - 1, var12)
            return result
    result = func7(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 10'
    print 'arg_number: 37'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
