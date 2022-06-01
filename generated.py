
def func1(arg1, arg2):
    var5 = class2()
    for var6 in xrange(42):
        var5.func3(arg1, arg2)
    var11 = func4(arg2, arg1)
    var16 = func5(arg2, var11)
    var20 = func6(var16, arg1)
    var25 = func8(arg1, var20)
    var26 = 1341125383 | ((var25 + var25) | arg1)
    var27 = 398 ^ arg1 ^ arg2 - arg1
    var28 = var11 & var20 & var26
    var29 = var28 - var20 - (var11 + var25)
    var30 = (var27 + var28 + arg2) + arg2
    var31 = var25 + var27 & var28 + var16
    var32 = var29 | var16
    var33 = var32 - (-674 + var32 ^ 914)
    var34 = var29 - var29 | -2046903040
    var35 = (var29 - (arg1 & var25)) | var20
    var36 = var34 | var35 | arg1
    var37 = var30 - var26
    var38 = var31 | var16 | 1682207820
    result = var26 - -1442398898
    return result
def func8(arg21, arg22):
    var23 = 0
    for var24 in range(30):
        var23 += arg21 | arg21 + arg22
    return var23
def func5(arg12, arg13):
    var14 = 0
    for var15 in range(31):
        if var14 < arg12:
            var14 += var15 + arg13 + var15
        else:
            var14 += (var14 - arg13) + var14
    return var14
def func4(arg7, arg8):
    var9 = 0
    for var10 in range(17):
        var9 += var9 | var9 | var10
    return var9
class class2(object):
    def func3(self, arg3, arg4):
        return 0
def func6(arg17, arg18):
    closure = [0]
    def func7(acc, rest):
        var19 = rest - -9 + ((closure[0] + 4 ^ 5 & closure[0]) - closure[0])
        closure[0] += var19
        if acc == 0:
            return var19
        else:
            result = func7(acc - 1, var19)
            return result
    result = func7(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 9'
    print 'arg_number: 39'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
