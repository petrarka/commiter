
def func1(arg1, arg2):
    def func2(arg3, arg4):
        def func3(arg5, arg6):
            if arg2 < arg4:
                var11 = class4()
            else:
                var11 = class6()
            for var12 in range(17):
                var13 = var11.func5
                var13(arg6, var12)
            var14 = func10()
            var15 = arg4 ^ (arg6 - arg4)
            var16 = -422 & (arg1 ^ arg5 - ((arg4 - var14) & var14))
            result = arg4 + ((var16 | arg2) | arg2)
            return result
        var17 = func3(arg1, arg4)
        var18 = arg1 ^ var17
        var19 = arg2 - arg2
        var20 = arg2 | -194865147 + arg2 & var18
        var21 = -52048625 | 2111499613 | arg3
        var22 = (arg3 - arg2 - var20) & arg1
        var23 = arg4 - var18 | arg3 & var17
        var24 = var23 + arg3
        var25 = arg1 - arg3
        var26 = var24 + var23
        if arg2 < var17:
            var27 = var22 | (var26 - 67 | -1172210739)
        else:
            var27 = (arg4 - var26) ^ (var24 + var23)
        var28 = var25 & -307 + var26
        result = arg4 + var17 | var17
        return result
    var29 = func2(arg1, arg2)
    var35 = func11(arg1, arg2)
    var36 = arg2 | -186 - arg1 & -226
    var37 = arg2 - (var29 | arg2)
    var38 = 71 ^ 472732683 & var36 ^ var37
    var39 = var35 - -1708602477
    var40 = var35 & arg2 | arg1 + var36
    var41 = var40 | -1759355374 + arg1 & arg1
    var42 = (-675 & var37 & var38) - var35
    var43 = (var37 & var42) - 1858573962 ^ var42
    var44 = (var36 + (var29 & var42)) - var29
    var45 = ((var39 & var39) - var42) ^ var42
    var46 = ((-280670441 + var45) - var45) ^ var45
    var47 = (arg2 & (1196726153 & var46)) | var29
    if arg2 < var44:
        var48 = (var45 - var35 + var45) | var42
    else:
        var48 = var29 + (arg2 | arg1 | var35)
    var49 = var35 - var29
    result = ((var35 | (var44 + var43)) | ((arg2 + (410 - var29)) + (var44 + var44 + (var46 + var42)) - var36)) + var42
    return result
def func11(arg30, arg31):
    var32 = (313 & (-1311560222 + arg31 - (arg31 ^ (1527120257 ^ (((770 & ((arg31 + ((-362 ^ arg31) ^ 917 - arg30 - (arg31 + -1458740142)) & 877) ^ -779848455)) ^ arg30) ^ arg31))) | arg30)) | (arg30 | arg30 + 1088709493) & arg31
    var33 = arg30 | ((((arg31 + -1704200506) | arg31 & (-1601694049 | var32) & (arg30 - arg30)) + arg31) - (555 | (((297024188 ^ arg30 + arg30 ^ var32 & var32) + arg30 | -91) & arg31) + 93699245) - arg30) - var32 - -113
    var34 = -377 ^ (arg31 - (-1935191307 + (-167 + (645 + 40) & (var33 - (var33 + (arg30 + ((var33 - arg31) & -713244340)) + (arg30 & arg30))) - ((((var33 - var33 & ((arg30 - 888) - 701281539)) | var32) - arg31) ^ -499))))
    result = var34 - -1606954518 ^ (1509137578 & var33) & var33
    return result
def func10():
    func8()
    result = len(range(42))
    func9()
    return result
def func9():
    global len
    del len
def func8():
    global len
    len = lambda x : -7
class class6(object):
    def func5(self, arg9, arg10):
        result = arg10 & arg9
        return result
class class4(class6):
    def func5(self, arg7, arg8):
        result = (arg8 | arg8) & arg7
        return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 12'
    print 'arg_number: 50'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
