## Leibniz Pi
## 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 ...) = pi
alt = -1
Total = 0
i = 0
while True:
    i+=1
    alt*=-1
    odd_denom = (i*2)-1
    nTerm = alt * float(1/odd_denom)
    Total += nTerm
    print(Total*4, "\t\t\t", i)