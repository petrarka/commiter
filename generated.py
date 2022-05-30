
def func1(arg1, arg2):
    var47 = func2(arg1, arg2)
    def func10(arg48, arg49):
        var50 = (arg49 & (1812870815 & (var47 & -545 & 149) ^ 415052385)) | -672124492 - 811 | (arg2 + arg49)
        var51 = (var50 | var50) | arg48
        var52 = arg1 ^ (var51 - arg49 ^ arg48 + (var50 & (-245 ^ var47) ^ (var47 | ((arg49 - arg2 | arg2) | var47 | var51)) & arg1 + 448218684 & -963) & (var50 & arg48) | arg2 & arg49 + arg49) | var51
        result = arg49 & arg1
        return result
    var53 = func10(var47, arg1)
    var54 = (((arg2 - 26) + var53 + var47) & (((arg1 & arg1) ^ arg1 & ((((-1463983775 + -708) - var47) + (823 & (var47 ^ arg1))) - 180389277)) ^ -145559923 + ((arg2 + arg2) + arg2))) & arg2
    var55 = arg1 + 138378175
    result = (arg1 + (var47 | arg1 | ((var55 - var53) ^ (arg1 | (var54 | var53 + var55 ^ 771 + arg1))))) + var55
    return result
def func2(arg3, arg4):
    var5 = func5()
    var13 = func6(var5, arg4)
    var35 = func9(var5, var13)
    var36 = -693806794 | var35 - arg4 & arg3
    var37 = var35 & (var35 ^ var36 | 1235427943)
    if var36 < var13:
        var38 = 854719710 ^ var37
    else:
        var38 = arg3 | var36 & var5
    if arg4 < arg4:
        var39 = var36 & var36
    else:
        var39 = arg3 | arg3
    var40 = arg4 - arg4
    var41 = var36 - var36 - -621
    var42 = var41 & (var37 | var13 ^ var13)
    var43 = 221 + var42 | var35 + var36
    var44 = (var36 - var37 + var43) + var42
    var45 = var44 + var43
    var46 = var41 | ((var42 & var5) + var44)
    result = var45 & ((var42 & (arg3 | var35)) & (var35 + var41 ^ arg3))
    return result
def func9(arg14, arg15):
    var16 = 2021372724 & arg15
    var17 = arg15 | ((arg15 | var16) & 61359262)
    var18 = var16 | var17 & 1105144938 - var16
    var19 = 2089729796 & (arg15 - var16) & 436
    if arg14 < arg14:
        var20 = ((316 & arg14) - var16) & var16
    else:
        var20 = (-444 | -1194845662 - var16) ^ 498
    var21 = var17 ^ 886
    var22 = var18 | -84 - (var16 ^ var17)
    if var18 < arg15:
        var23 = (var21 - var21) & (var16 & arg15)
    else:
        var23 = -120 | (var21 & var16)
    var24 = arg15 | -1599422177 & var21
    var25 = ((var19 + var17) - -426) ^ var16
    var26 = (var19 - 1109037785) - var18
    var27 = (arg14 | var21 + arg14) ^ var25
    var28 = arg15 & var24 | var22 | var18
    var29 = arg15 | var28
    var30 = (var18 - var25 | var21) + arg14
    var31 = var21 & var27 | var27 | arg14
    var32 = var22 & var18
    var33 = var31 & var19
    var34 = var29 + -2078101039
    result = var32 & var18
    return result
def func8(arg8, arg9):
    var10 = arg9 ^ -1227479776
    var11 = var10 + ((759 & (arg8 + 2136592163 ^ var10)) - (var10 | arg8) + -400356921 ^ ((arg9 ^ (-914 | arg8 | 276 | var10)) | 650223618))
    result = var11 + arg8
    return result
def func5():
    func3()
    result = len(range(42))
    func4()
    return result
def func4():
    global len
    del len
def func3():
    global len
    len = lambda x : 4
def func6(arg6, arg7):
    def func7(acc, rest):
        var12 = func8(5, 0)
        if acc == 0:
            return var12
        else:
            result = func7(acc - 1, var12)
            return result
    result = func7(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 56'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
