
def func8(arg19, arg20):
    var23 = func9(arg19, arg20)
    var24 = func12()
    if var23 < var23:
        var25 = arg19 + var24
    else:
        var25 = -669 | arg20
    if var24 < var24:
        var26 = -52 ^ var23
    else:
        var26 = arg20 + arg19
    var27 = (var23 - arg20) ^ arg20 & arg20
    var28 = (497491936 | -961) | var23 + var23
    var29 = 26 - var24 | var24 - arg20
    var30 = (var27 | var27 & arg20) & arg19
    var31 = var27 & arg20 - arg20
    var32 = 1274185827 ^ var28 & var29 - var28
    var33 = var28 & (var29 ^ arg19) & var24
    var34 = var33 - var33
    var35 = (var23 & var34 ^ arg19) & arg19
    result = (var28 + var32 - var27 ^ var30 | var23 + -1195342332) & var34
    return result
def func12():
    func10()
    result = len(range(2))
    func11()
    return result
def func11():
    global len
    del len
def func10():
    global len
    len = lambda x : -4
def func9(arg21, arg22):
    result = (arg21 - ((((-370 - arg22 & arg21 ^ arg22) + arg21 ^ 1416806035 - 1279821189) | arg21 + -913) ^ arg21)) - 242
    return result
def func2(arg3, arg4):
    var8 = func3(arg3, arg4)
    def func5(arg9, arg10):
        var11 = (arg10 ^ 560771114 | arg10 ^ arg4) & var8 + -279
        result = (arg9 & (936376216 & var8) ^ (var11 | var8 | ((219 ^ arg3) + arg3 & -1576469717) + arg10) ^ arg3) + -549
        return result
    var12 = func5(arg3, var8)
    var16 = func6(var8, arg4)
    var17 = (var8 ^ var16) + var16
    var18 = 1944871203 & -151 + var17
    result = -449 & var12
    return result
def func1(arg1, arg2):
    result = (arg2 + arg1 ^ ((arg1 | arg2) ^ arg1 + arg2 - arg1)) + 332 | 1025087363
    return result
def func3(arg5, arg6):
    closure = [0]
    def func4(acc, rest):
        var7 = (rest - (rest ^ rest + 6 & closure[0])) + -2
        closure[0] += var7
        if acc == 0:
            return var7
        else:
            result = func4(acc - 1, var7)
            return result
    result = func4(10, 0)
    return result
def func6(arg13, arg14):
    closure = [0]
    def func7(acc, rest):
        var15 = (((2 | rest - -5) - 4) - 4) & 4 - -5
        closure[0] += var15
        if acc == 0:
            return var15
        else:
            result = func7(acc - 1, var15)
            return result
    result = func7(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 0'
    print 'func_number: 2'
    print 'arg_number: 3'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 3'
    print 'func_number: 8'
    print 'arg_number: 19'
    for i in xrange(25000):
        x = 5
        x = func2(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 13'
    print 'arg_number: 36'
    for i in xrange(25000):
        x = 5
        x = func8(x, i)
        print x,
