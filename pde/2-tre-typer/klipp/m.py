import json,sys
k=json.load(open(sys.argv[1]))
def M(T):
    for a,b,c,d,s in k:
        if c<=T<=d: return a+T-c
    return min((a for a,b,c,d,s in k if c>T),default=None)
print(','.join('0:%.2f'%M(float(t)) for t in sys.argv[2:]))
