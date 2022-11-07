import math


def euclidean(a:int,b:int):
    r = [a,b]
    s = [1,0]
    t = [0,1]
    q = math.floor(a/b)
    while(True):
        print("q_{i-1}:"+str(q))
        r.append(r[len(r)-2] - q*r[len(r)-1])
        print("r_i:"+str(r[len(r)-1]))
        s.append(s[len(s)-2] - q*s[len(s)-1])
        print("s_i:"+str(s[len(s)-1]))
        t.append(t[len(t)-2] - q*t[len(t)-1])
        print("t_i:"+str(t[len(t)-1]))
        if(r[len(r)-1] == 0):
            return (r, s, t)
        else:
            q = math.floor(r[len(r)-2]/r[len(r)-1])



a = 240
b = 46

tmp = euclidean(a,b)
print(tmp[1][len(tmp[1])-1])
print(tmp[2][len(tmp[2])-1])

#print(euclidean(a,b))
gcd = tmp[0][len(tmp[0])-2]
print(gcd)