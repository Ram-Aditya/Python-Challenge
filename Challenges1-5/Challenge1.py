string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

x = list(string)

for i in range(len(x)):
    if x[i] == ' ' or x[i] == '(' or x[i] == ')':
        continue
    x[i] = chr(((ord(x[i]) - 97) + 2) % 26 + 97)

print(''.join(x))