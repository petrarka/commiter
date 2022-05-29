
def func1(arg1, arg2):
    var7 = func2(arg1, arg2)
    var11 = func3(arg2, arg1)
    var36 = var14(arg2, arg1)
    var37 = ((var11 + var7) & (((arg2 | var7) + var11) + var11 - 1906507609 | (var36 + (-544472832 | var11 ^ (-354 ^ (arg1 + ((1568002174 + var7) + -856)))))) ^ 36 - var11 - var36 & arg2 + var11 - var7) ^ var36
    var38 = (((1827023267 - (var7 + (var37 & 181 | (arg1 ^ var36) ^ 839 ^ ((arg1 - var36 - var37) ^ (var7 | arg2))))) - -708 ^ (156 - ((arg2 ^ -353 - arg2 + var37) + var36)) - -2000762605) | var11) | arg2
    var39 = arg2 - var11
    result = (var36 | (((((var36 & 1636133026 ^ var7 & var11 | var39) ^ var7) ^ -662) ^ var7 | var11) + var36)) + arg1
    return result
def func7(arg15, arg16):
    var17 = func10()
    var22 = func11(arg15, var17)
    var23 = -342 ^ arg16 ^ var17
    var24 = ((var17 ^ var22) - 1896560968) & -1670300057
    var25 = ((var22 - var24) - arg16) - var23
    var26 = (var17 - -648552197) | arg16 | arg16
    var27 = var23 | var23
    var28 = var22 + ((var22 + arg15) & arg16)
    var29 = (var17 - var25) | 203 | var24
    var30 = (var25 - var26 ^ var26) - var28
    var31 = var25 | var22
    var32 = (arg15 | var25 & arg15) + arg16
    var33 = ((var23 ^ var24) | var32) | -1639686939
    var34 = 437 | (arg16 + var24)
    var35 = var22 + -16 | var30
    result = var25 ^ (var17 | (var25 | ((var34 & var30 | var24 + var28) - var27) | arg15) + var17 & var34 ^ var23)
    return result
def func11(arg18, arg19):
    var20 = 0
    for var21 in xrange(21):
        var20 += var21 + (arg18 | var20)
    return var20
def func10():
    func8()
    result = len(xrange(40))
    func9()
    return result
def func9():
    global len
    del len
def func8():
    global len
    len = lambda x : -5
def func6():
    closure = [-9]
    def func5(arg12, arg13):
        closure[0] += func7(arg12, arg13)
        return closure[0]
    func = func5
    return func
var14 = func6()
def func2(arg3, arg4):
    var5 = 0
    for var6 in range(25):
        var5 += (var6 | var5) + -7
    return var5
def func3(arg8, arg9):
    closure = [0]
    def func4(acc, rest):
        var10 = (8 ^ (-8 ^ (6 - -8)) - -9 + 8) ^ -9
        closure[0] += var10
        if acc == 0:
            return var10
        else:
            result = func4(acc - 1, var10)
            return result
    result = func4(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 12'
    print 'arg_number: 40'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
