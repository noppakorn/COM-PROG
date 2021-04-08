def to_gray(img):
    out = []
    for i in img :
        row = []
        for j in i:
            row.append(sum(j)//len(j))
        out.append(row)
    return out
exec(input().strip())