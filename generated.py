
def func1(arg1, arg2):
    var7 = func2(arg1, arg2)
    var11 = func3(arg2, var7)
    var16 = func5(arg2, var7)
    var19 = class6()
    for var20 in range(49):
        var19.func7(var16, var7)
    var24 = func8(arg2, var16)
    var25 = ((var11 - var11) ^ arg1) | var7
    var26 = 1951547477 + 163498639
    var27 = var24 | ((arg2 ^ arg1) ^ arg1)
    var28 = var27 + var26 | arg1 | var25
    if var27 < var26:
        var29 = var28 & var27 & var28 + var27
    else:
        var29 = var11 ^ arg2
    var30 = (var16 & var24) - arg2 - arg1
    var31 = (arg2 + var16 ^ var30) + var28
    var32 = var28 - var26 + -1987841112 & var26
    var33 = ((var25 ^ var25) + var7) - var25
    var34 = var31 | -529 & -869 + var16
    var35 = (-487198758 + (var16 | arg1)) + var30
    var36 = (var32 | 770) + var31 | var35
    if var35 < var24:
        var37 = var30 ^ var36 | var36
    else:
        var37 = var25 + var30 | arg1
    var38 = ((var7 - arg2) - -178) ^ var34
    var39 = var34 | (var26 + var35)
    var40 = var31 + (var25 - var27) | var16
    var41 = (var32 | var39) | var38
    result = (980 | (var31 - var11 - arg1) | (var40 | var7) ^ (var39 & (var16 & var11) + var41 | var25)) - var30
    return result
def func8(arg21, arg22):
    var23 = arg22 ^ ((arg22 + (-966238808 - arg22 + 701)) - (567 | 1118733131 - -124 ^ -926 + 1106446864) - arg22 - (-1100524005 | -2000406565 | -955013029) | 876797615)
    result = -385700308 + -213810891 - (92 - arg21) & arg21 & var23 ^ (var23 - -444 | arg22 + arg21) + arg21 | -1417398376
    return result
class class6(object):
    def func7(self, arg17, arg18):
        result = (((arg17 + 788108734) + (-2126028042 ^ arg17 & arg18)) | -222213101) & 1
        return result
def func5(arg12, arg13):
    var14 = 0
    for var15 in xrange(35):
        var14 += var14 & var14 & 4
    return var14
def func2(arg3, arg4):
    var5 = 0
    for var6 in xrange(28):
        var5 += (arg3 ^ var6) ^ var5
    return var5
def func3(arg8, arg9):
    def func4(acc, rest):
        var10 = (acc - -8) | acc
        if acc == 0:
            return var10
        else:
            result = func4(acc - 1, var10)
            return result
    result = func4(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 9'
    print 'arg_number: 42'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
