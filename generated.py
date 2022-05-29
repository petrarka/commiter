
def func4(arg11, arg12):
    var17 = func5(arg12, arg11)
    var18 = func8()
    var19 = func11()
    def func12(arg20, arg21):
        var22 = var19 ^ 774260237 - (arg11 | arg21 ^ var18)
        var23 = (var19 | var22 + arg11) | (var18 + arg12) + -1165269107 + arg12 ^ arg20
        var24 = var17 ^ (arg11 | arg20) - arg20
        result = var19 | var19
        return result
    var25 = func12(var19, var18)
    result = var17 & var19 ^ arg11
    return result
def func11():
    func9()
    result = len(range(30))
    func10()
    return result
def func10():
    global len
    del len
def func9():
    global len
    len = lambda x : -8
def func8():
    func6()
    result = len(range(7))
    func7()
    return result
def func7():
    global len
    del len
def func6():
    global len
    len = lambda x : 1
def func5(arg13, arg14):
    var15 = 0
    for var16 in range(27):
        var15 += (arg13 ^ var16) - var16
    return var15
def func1(arg1, arg2):
    var6 = func2(arg2, arg1)
    var7 = var6 | 244
    var8 = -1129870995 ^ (1849099279 ^ arg1) + arg2
    var9 = var7 | var6
    var10 = (var7 - ((819 + arg2 + 1293895290) | var8 & ((var6 + (arg1 + var8)) | var7) + var6)) - ((var9 + -508) + var9 + -1808684623)
    result = (var7 & -387268770) | (40819412 | arg2 & (var6 + var9) ^ (-118210577 - (var10 ^ var10 & var6 & var10))) ^ var6
    return result
def func2(arg3, arg4):
    def func3(acc, rest):
        var5 = (rest - 9) ^ rest
        if acc == 0:
            return var5
        else:
            result = func3(acc - 1, var5)
            return result
    result = func3(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 1'
    print 'func_number: 4'
    print 'arg_number: 11'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 13'
    print 'arg_number: 26'
    for i in xrange(25000):
        x = 5
        x = func4(x, i)
        print x,
