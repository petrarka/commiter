
def func1(arg1, arg2):
    var6 = func2(arg2, arg1)
    def func4(arg7, arg8):
        var9 = (-569 ^ -2100231212 & arg1) & var6
        var10 = (arg7 - var9 ^ var6) | -675
        var11 = arg7 - (var10 + arg7)
        var12 = var10 | var11
        var13 = (var10 | arg2 - var9) + -53
        var14 = var6 - arg1 - var12 | arg1
        var15 = var10 ^ arg2
        var16 = (arg8 + (arg1 - 289)) & -65
        var17 = (var16 - -695 + arg2) + var15
        var18 = var14 + arg2
        var19 = var14 - (704 ^ var9 ^ arg1)
        var20 = arg1 - 778 | -1927275925 | var6
        var21 = (var19 | var20) - var16 & arg7
        var22 = var14 & (var11 ^ var17)
        var23 = var22 + var10
        var24 = -758 | (var19 + var21) - arg7
        var25 = (var13 ^ var17) + var23
        var26 = ((var25 + var21) & arg2) + arg8
        var27 = (var20 & var23 & var14) - var18
        var28 = var16 + arg7
        var29 = var14 - -24181161 - 537 | var22
        var30 = var13 & var9 | (var29 | 147443795)
        var31 = var27 ^ (var28 + var24) - arg1
        var32 = -108189536 | var17 ^ 146544204 | arg7
        var33 = ((var22 - var23) + var19) | var26
        result = (((var10 + (var25 & var15 + -119755670)) + (var20 - var28) ^ arg7 & var22 ^ var31) + var16 & var14) + var6
        return result
    var34 = func4(arg2, arg1)
    def func5(arg35, arg36):
        var37 = var34 + arg1
        var38 = var37 & arg1
        var39 = arg35 | arg36
        var40 = ((var38 ^ var38) & (arg1 - 2131971558 | arg35 + (var38 | arg35))) & -1278294101 ^ var6 & (var37 + (-2065226148 & (var38 - arg36))) & var34
        var41 = 41665081 - var6
        result = ((((arg2 + (arg1 + var37 ^ arg35 | arg35)) - var40 | var38) ^ arg35 & var34) & 1420017031) + arg36 & -117
        return result
    var42 = func5(arg1, var6)
    var46 = func6(arg1, var6)
    def func8(arg47, arg48):
        var49 = arg48 | arg1 ^ arg1 + arg48
        if arg2 < var42:
            var50 = -616034249 & arg48 ^ var34 ^ arg47
        else:
            var50 = (var34 & var42 + var6) + var42
        var51 = arg2 - var42
        var52 = (arg48 | arg48 ^ arg47) & var6
        var53 = var46 & var52
        var54 = var52 | var53 | var52 + arg2
        var55 = 105 | var6 & var46 - var51
        var56 = arg48 - var49
        var57 = (var49 ^ arg47 - var42) ^ var56
        var58 = var54 | (var56 - var57) | arg1
        var59 = (var51 + var46) - (var42 ^ var6)
        var60 = arg1 ^ (var56 - var34) + -1437282471
        var61 = 1341871963 | var51 | arg1
        var62 = arg47 ^ var46 - var54 + var52
        var63 = arg47 - 677 & var53
        var64 = var53 + (var49 + arg47)
        var65 = (-38 & (var51 & arg2)) + var42
        result = arg48 ^ ((-157 - var57 ^ (((var64 - var59) ^ arg48 | arg2) - arg48)) & (var6 + var57) & arg2 | var52)
        return result
    var66 = func8(var46, arg2)
    result = var6 + -983 - ((((-210 - -689 | (var66 - 927) - arg1 - var66) | var66 - var46) - var66) & var42)
    return result
def func2(arg3, arg4):
    closure = [0]
    def func3(acc, rest):
        var5 = acc + rest
        closure[0] += var5
        if acc == 0:
            return var5
        else:
            result = func3(acc - 1, var5)
            return result
    result = func3(10, 0)
    return result
def func6(arg43, arg44):
    def func7(acc, rest):
        var45 = (acc - -9) + -9
        if acc == 0:
            return var45
        else:
            result = func7(acc - 1, var45)
            return result
    result = func7(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 9'
    print 'arg_number: 67'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
