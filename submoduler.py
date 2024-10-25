# 2^iの位が、iが表す集合族を含むかに対応。iは、1の位、2の位、4の位が、a, b, cを含むかに対応。
included_set = 129
ok_list = []

def meet(x, y):
    output = 7
    while(output >= 0):
        if ((included_set & (1<<output)) != 0 and (output & x) == output and (output & y) == output):
            # print(f"meet {bin(included_set)}, {x}, {y}, {output}")
            return output
        else:
            output-=1
    
def join(x, y):
    output = 0
    while(output <= 7):
        if ((included_set & (1<<output)) != 0 and (output & x) == x and (output & y) == y):
            # print(f"join {bin(included_set)}, {x}, {y}, {output}")
            return output
        else:
            output+=1
    
# 分配束を表す数字を選択する
while(included_set <= 255):
    ok = True
    for x in range(8):
        if((included_set & (1<<x)) == 0):
            continue
        for y in range(8):
            if((included_set & (1<<y)) == 0):
                continue
            for z in range(8):
                if((included_set & (1<<z)) == 0):
                    continue
                if(join(x, meet(y, z)) != meet(join(x, y), join(x, z)) or meet(x, join(y, z)) != join(meet(x, y), meet(x, z))):
                    
                    ok = False
    if(ok):
        ok_list.append(included_set)
    included_set+=2

# 重複を削除する
is_unique = [True for _ in range(len(ok_list))]
bit_cor = [[0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]] # correspondence
for i in range(len(ok_list)):
    if(not is_unique[i]):
        continue
    for j in range(len(ok_list)-i-1):
        if(not is_unique[i+1+j]):
            continue
        for k in range(len(bit_cor)):
            included_set_tmp = 0
            for l in range(8):
                # lのbitを入れ替える
                digit = 0
                for m in range(3):
                    digit+=(1 if (l & 1<<m) != 0 else 0) * (1<<bit_cor[k][m])
                if((ok_list[i] & 1<<l) != 0):
                    included_set_tmp+=1<<digit
            if(included_set_tmp == ok_list[i+1+j]):
                is_unique[i+1+j] = False
                break
for i in range(len(ok_list)):
    if(not is_unique[i]):
        continue
    for j in range(8):
        if((ok_list[i] & 1<<j) == 0):
            continue
        elems = []
        if((j & 1) != 0):
            elems.append("a")
        if((j & 2) != 0):
            elems.append("b")
        if((j & 4) != 0):
            elems.append("c")
        print("{", f"{', '.join(elems)}", "} ", end="", sep="")
    print()