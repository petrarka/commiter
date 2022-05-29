
def func7(arg18, arg19):
    var20 = func10()
    var21 = var20 & arg19
    if arg19 < arg18:
        var22 = var21 + var21
    else:
        var22 = arg19 + (var20 + 4)
    var23 = (var20 + (arg18 | arg18)) + var21
    var24 = arg19 & (var23 + arg18) | arg19
    var25 = var24 - -1403708319 ^ (376 - arg19)
    if arg19 < var20:
        var26 = ((var21 + var24) - var25) - arg19
    else:
        var26 = var23 & (var24 | arg19) - var25
    var27 = var20 + arg19 | 153164792 - 614
    var28 = var23 & (-1649063881 & arg19) ^ arg19
    var29 = (var21 + -53300315 | var28) ^ -88907353
    var30 = -71 + (var25 | var27) ^ var23
    var31 = var28 & arg18 ^ var24 & var29
    var32 = var29 + arg18
    var33 = var32 | var30
    var34 = var23 | 723700759
    var35 = (var27 ^ -1871144090 ^ var30) + var30
    var36 = var21 & (166644874 ^ (var21 ^ var33))
    var37 = var27 | var32
    var38 = var31 - var32 | arg18 - 1688717471
    var39 = ((-105 | 1640182064) | var37) - var34
    var40 = var37 & 686 ^ var25 & var37
    var41 = var28 & 240512226
    var42 = var29 & var28
    var43 = (var32 + var28) | var24 & arg19
    var44 = (var29 | var43) & var40 + var25
    result = var39 | (var28 - (var31 & var33 & var24 ^ var31) + (var38 - var38) ^ (var36 & var32 ^ var33)) & var21
    return result
def func10():
    func8()
    result = len(xrange(47))
    func9()
    return result
def func9():
    global len
    del len
def func8():
    global len
    len = lambda x : -3
def func1(arg1, arg2):
    if arg1 < arg1:
        var7 = class2()
    else:
        var7 = class4()
    for var8 in (arg1 ^ arg2 & i for i in (arg2 + i - arg2 for i in range(47))):
        var7.func3(arg1, var8)
    var13 = func6(arg1, arg2)
    var14 = ((var13 | (arg1 ^ (arg1 - (arg2 - -906) + 668 + 852 ^ arg1 & (arg1 | arg1)))) ^ 692) - 1555047145
    if arg1 < var13:
        var15 = 933874743 + -819 ^ var14 & var13 | arg2
    else:
        var15 = var13 | 515777675
    var16 = (arg1 - ((arg1 & (-802 - arg2 | 1587124317 - (((((var13 + -1229430893) | var14) + arg2 | arg1 + (var13 - var14)) + (var14 + arg2 - -845 - -1630508461)) & arg1)) + 180 | 236) ^ var14)) - arg2 + -1260664181
    if var16 < arg1:
        var17 = (-1936683449 + (var16 | var14)) - -1282592360
    else:
        var17 = -441 | (var13 & ((var14 - (var13 + 97526856)) | arg2)) | ((-695 - ((var13 & ((var13 ^ arg2 ^ arg2 - (arg2 | ((var14 | var16 - arg2) - arg2))) & -508) & arg2) - 438072601) + arg1) ^ arg1) ^ -1249418587
    result = arg2 & var14
    return result
def func6(arg9, arg10):
    var11 = 0
    for var12 in range(39):
        var11 += var12 & (var11 - arg10)
    return var11
class class4(object):
    def func3(self, arg5, arg6):
        result = (-1 + arg5) & arg5
        return result
class class2(object):
    def func3(self, arg3, arg4):
        return 0
if __name__ == "__main__":
    print 'prog_size: 4'
    print 'func_number: 7'
    print 'arg_number: 18'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 45'
    for i in xrange(25000):
        x = 5
        x = func7(x, i)
        print x,
