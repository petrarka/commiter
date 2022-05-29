
def func8(arg41, arg42):
    if arg41 < arg42:
        var47 = class9()
    else:
        var47 = class11()
    for var48 in xrange(33):
        var49 = var47.func10
        var49(var48, arg42)
    var53 = func13(arg42, arg41)
    var54 = (var53 | (arg41 - (var53 - -963277484 ^ ((406674833 - arg42) ^ 2016534019 & var53) | arg41))) | arg41
    var55 = arg41 ^ -325 ^ (var53 | 471) - 655612146
    result = (var53 - arg41 + var53) & -543804089 & var54
    return result
class class11(object):
    def func10(self, arg45, arg46):
        result = 557307193 & (arg45 + arg46) + arg46
        return result
class class9(object):
    def func10(self, arg43, arg44):
        result = (arg43 - arg44) ^ (1 - -1292854797 - arg43) ^ arg43 & arg44
        return result
def func2(arg25, arg26):
    if arg26 < arg25:
        var31 = class3()
    else:
        var31 = class5()
    for var32 in ((5 + arg26) ^ -7 for i in xrange(31)):
        var33 = var31.func4
        var33(var32, arg26)
    var38 = func7(arg26, arg25)
    var39 = -775 - (1083433400 ^ (-602406239 - -599))
    var40 = (arg26 + 656) ^ (334 & arg26 + arg26)
    result = var40 & var40
    return result
def func7(arg34, arg35):
    var36 = 0
    for var37 in xrange(12):
        var36 += (var36 + arg35) & var36
    return var36
class class5(object):
    def func4(self, arg29, arg30):
        result = -529636493 - arg30
        return result
class class3(class5):
    def func4(self, arg27, arg28):
        return 0
def func1(arg1, arg2):
    var3 = (arg2 ^ -1109681705 - 557) + arg1
    var4 = ((1282685807 & var3) | arg1) - var3
    var5 = arg2 - arg2 & arg1 + arg1
    var6 = -490 & var5 ^ 532425717
    if var4 < var3:
        var7 = (arg2 - var5 ^ var5) + var4
    else:
        var7 = var3 | (var3 | var5)
    var8 = (377053875 | var5) - (arg1 - var6)
    var9 = var4 & var3
    var10 = -1156649508 - (47 + var3) & var4
    var11 = var5 & var5
    var12 = (var11 + arg2) - var5 | 772701224
    if var9 < var9:
        var13 = var6 | var10 - var12 | var6
    else:
        var13 = var9 & var10 ^ var12 + var4
    var14 = ((var12 & arg2) | var5) - var11
    var15 = (var3 & arg2) + 92 + var4
    var16 = var14 ^ arg1
    var17 = var5 ^ -267
    var18 = var15 + var4 ^ var10 ^ -504
    var19 = var6 + var14
    var20 = var8 + var11 - var9
    var21 = var3 & var10
    var22 = var4 & (var17 - var6 & var21)
    var23 = var3 + var21
    var24 = ((arg2 + var5) - -2085140641) & var15
    result = (var8 & var9) | (var19 | var19 - (var14 + var20)) ^ 191
    return result
def func13(arg50, arg51):
    def func14(acc, rest):
        var52 = acc & acc & acc
        if acc == 0:
            return var52
        else:
            result = func14(acc - 1, var52)
            return result
    result = func14(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 0'
    print 'func_number: 2'
    print 'arg_number: 25'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 3'
    print 'func_number: 8'
    print 'arg_number: 41'
    for i in xrange(25000):
        x = 5
        x = func2(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 15'
    print 'arg_number: 56'
    for i in xrange(25000):
        x = 5
        x = func8(x, i)
        print x,
