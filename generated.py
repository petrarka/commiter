
def func1(arg1, arg2):
    var7 = func2(arg1, arg2)
    var12 = func3(arg2, arg1)
    var16 = func4(var7, var12)
    var22 = var19(arg1, var16)
    var27 = func8(var22, var7)
    var28 = arg2 | arg2
    result = var16 & var16
    return result
def func8(arg23, arg24):
    var25 = 0
    for var26 in range(30):
        var25 += 3 ^ var25
    return var25
def func7(arg20, arg21):
    result = 297 ^ arg20 + (-1006046457 + 1702158799)
    return result
def func6():
    closure = [-8]
    def func5(arg17, arg18):
        closure[0] += func7(arg17, arg18)
        return closure[0]
    func = func5
    return func
var19 = func6()
def func4(arg13, arg14):
    if arg14 < arg14:
        var15 = (arg14 + -68361058 + 1378791538) | 1107158710
    else:
        var15 = ((370 & 1161655429) + -980) | ((arg13 & ((372 ^ arg14 & arg13) | ((-316 & (((-651 | -1849169272 + ((arg14 & arg13) & -50410375) & arg13 & arg13) | arg14) & -204980968)) & 866 - -167129150) | arg14) & -749) - 656)
    result = (31 ^ arg13) & (arg13 & -1684071490 | arg13 ^ arg13 & arg13)
    return result
def func3(arg8, arg9):
    var10 = 0
    for var11 in xrange(44):
        var10 += var10 ^ var11
    return var10
def func2(arg3, arg4):
    var5 = 0
    for var6 in range(12):
        var5 += var6 | (arg4 | arg3)
    return var5
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 9'
    print 'arg_number: 29'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
