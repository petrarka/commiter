
def func5(arg7, arg8):
    var25 = func6(arg8, arg7)
    var26 = arg8 & arg8 & var25
    result = var26 & 1179228310
    return result
def func6(arg9, arg10):
    var11 = 0
    for var24 in (var11 - var11 | var11 for i in [i + arg9 ^ (arg9 & -1) for i in func7(arg10, 5)]):
        if arg10 < var24:
            var11 += arg10 ^ (var11 - -8)
        else:
            var11 += (var24 + var24) - -6
    return var11
def func7(arg12, arg13):
    var14 = arg12 ^ (arg13 | arg13) & arg13
    yield var14
    var15 = 274 ^ arg12
    yield var15
    var16 = var14 ^ -637 + var14 | -347
    yield var16
    var17 = 929 & var14
    yield var17
    var18 = var17 - var15
    yield var18
    var19 = ((arg13 & arg12) + 898) - var17
    yield var19
    var20 = var17 ^ var19
    yield var20
    var21 = var20 - (var16 + 535)
    yield var21
    var22 = var16 - (var15 + var14) + arg13
    yield var22
    var23 = var17 ^ var18
    yield var23
def func1(arg1, arg2):
    var3 = func4()
    var4 = 978515322 | (arg2 | var3)
    if var4 < arg2:
        var5 = -175 & -1908846237
    else:
        var5 = arg1 ^ var4
    if arg2 < var4:
        var6 = (488 & -1137872929) ^ -398566889
    else:
        var6 = var4 & arg1
    result = var3 + ((arg1 | (-1040534890 - (271 - 526)) | arg1) ^ arg1)
    return result
def func4():
    func2()
    result = len(xrange(33))
    func3()
    return result
def func3():
    global len
    del len
def func2():
    global len
    len = lambda x : 3
if __name__ == "__main__":
    print 'prog_size: 1'
    print 'func_number: 5'
    print 'arg_number: 7'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 8'
    print 'arg_number: 27'
    for i in xrange(25000):
        x = 5
        x = func5(x, i)
        print x,
