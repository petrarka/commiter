
def func2(arg15, arg16):
    var43 = func3(arg16, arg15)
    result = (arg15 & arg16 ^ arg15 ^ ((arg16 - var43) - (var43 - -83 | (arg15 - -136)) ^ -733)) | (arg16 - arg15)
    return result
def func3(arg17, arg18):
    var19 = 0
    for var42 in func4(arg18, arg17):
        var19 += (var42 + 7) ^ arg18
    return var19
def func5(arg22, arg23):
    var24 = func8()
    var25 = func11()
    var26 = var24 - (arg23 | -401342933) - arg22
    var27 = ((-699 ^ -294) ^ -571110885) - ((var26 & (312 & var24 - var26 ^ -130230664) & -411 & var26 - arg23) | -967) ^ 715
    var28 = (var25 & var25 + var24 | arg22 + var26) & ((-1718725618 & var27) + ((var24 & (771 - -651)) | -501382710 + (-1969027395 & 1570400034)))
    var29 = 304 + 485 ^ ((((var26 - var25) | var24) ^ (((var25 | var28 - (arg22 | var28) & var26 & (var24 + 58 & -468)) | arg23 + -2124064497) & var27 & -1092363703 | var27) - var24) ^ var27 ^ var24) & arg23
    var30 = var29 + var29
    result = 1157222672 & var27
    return result
def func11():
    func9()
    result = len(xrange(37))
    func10()
    return result
def func10():
    global len
    del len
def func9():
    global len
    len = lambda x : 6
def func8():
    func6()
    result = len((((8 - i + -8 & i - -2 | -2) + 8) - -2 for i in xrange(18)))
    func7()
    return result
def func7():
    global len
    del len
def func6():
    global len
    len = lambda x : -1
def func4(arg20, arg21):
    var31 = func5(arg20, -1586339778)
    yield var31
    var32 = arg20 ^ (-766421550 + arg21) | 595
    yield var32
    var33 = arg21 - (arg20 - -309436632 | arg20)
    yield var33
    var34 = var33 & var32
    yield var34
    var35 = arg20 + arg21
    yield var35
    var36 = ((arg21 & arg21) + -1460467127) - var33
    yield var36
    var37 = var35 ^ var35
    yield var37
    var38 = -420779723 - arg20
    yield var38
    var39 = -454085797 + (var34 ^ var35)
    yield var39
    var40 = (arg20 - (var39 | arg20)) ^ var32
    yield var40
    var41 = var39 - ((var40 + var34) ^ var33)
    yield var41
def func1(arg1, arg2):
    var3 = arg1 + -430
    var4 = arg1 | arg1 + arg2 & -814
    var5 = var3 + var4
    var6 = var5 | var4
    var7 = (var6 + -747) | var6 + -345
    var8 = (var3 | arg2) & arg2 | arg1
    var9 = var6 & var8
    var10 = (arg1 & var3 - arg1) ^ var5
    if var6 < arg1:
        var11 = ((var5 | var5) | -229594763) | 585
    else:
        var11 = var6 ^ (var4 ^ var5) + var10
    var12 = var7 - var8 & (var4 & var4)
    var13 = var3 ^ var4 & var6 + var9
    var14 = (-236 + var12 & 736) & var9
    result = var12 | var9
    return result
if __name__ == "__main__":
    print 'prog_size: 0'
    print 'func_number: 2'
    print 'arg_number: 15'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 12'
    print 'arg_number: 44'
    for i in xrange(25000):
        x = 5
        x = func2(x, i)
        print x,
