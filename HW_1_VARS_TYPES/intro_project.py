# hw_1
def print_var_type(var):
    print("var value = " + str(var) + " " + str(type(var)))


varString = "blabla"
print_var_type(varString)

varInt = 12
print_var_type(varInt)

varFloat = 12.5
print_var_type(varFloat)

varList = [1, 2, 3, 4, 5]
print_var_type(varList)

varTuple = tuple(varList)
print_var_type(varTuple)

varSet = set(varList)
print_var_type(varSet)

varFrozenSet = frozenset(varList)
print_var_type(varFrozenSet)

varDict = {1: "One", 2: "Two"}
print_var_type(varDict)

varBytes = varString.encode('utf-8')
print_var_type(varBytes)

for bytes in varBytes:
    print(bytes, end=" ")
print('\r')

varStringAnother = "BLABLA"
varSumString = varString + varStringAnother

print(varSumString)
print(varString, varInt)
print(varString + str(varInt))
