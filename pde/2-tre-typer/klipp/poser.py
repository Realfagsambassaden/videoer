# Lager poser.json (tider i tavlevideoen) fra kildetider i opptaket.
import json
k=json.load(open('klipp/kart.json')); TEMPO=1.09
def M(T):
    for a,b,c,d,s in k:
        if T<c: return a/TEMPO
        if T<=d: return (a+T-c)/TEMPO
    return k[-1][1]/TEMPO
P=[(228.9,'noytral',0),(248.4,'peker_opp',0),(300.0,'skrive',0),(323.9,'skrive_ferdig',0),(342.0,'peker_tavla',1),
 (361.0,'gruble',0),(375.8,'overrasket',0),(381.6,'peker_tavla',1),(396.3,'gruble',0),(401.2,'peker_tavla',1),
 (480.4,'undrende',0),(509.3,'lattermild',0),(527.8,'undrende',0),(551.6,'mystisk',0),(573.6,'peker_tavla',1),
 (595.4,'gruble',0),(611.9,'skrive',0),(623.3,'peker_tavla',1),(677.0,'skrive',0),(684.3,'tada',0),(695.8,'peker_opp',0),
 (719.6,'skuldre',0),(727.4,'peker_tavla',1),(736.2,'overrasket',0),(788.4,'noytral',0),(794.3,'peker_opp',0),
 (803.0,'peker_tavla',1),(877.6,'peker_tavla',1),(884.8,'peker_opp',0),(889.0,'tada',0),(975.1,'noytral',0),(1024.7,'tada',0)]
E=[(364.0,368.5,'lyspaere'),(595.4,599.5,'spm'),(696.0,700.0,'lyspaere'),(723.8,726.5,'utrop'),(794.3,797.6,'lyspaere')]
P2=[[round(M(t) if i else 0.0,2),n,s] for i,(t,n,s) in enumerate(P)]
json.dump({'poser':P2,'ekstra':[[round(M(a),2),round(M(b),2),n] for a,b,n in E]},open('poser.json','w'),indent=0)
# lydeffekter: (tid, fil)
L=[(M(t),f) for t,f in [(342.0,'pop'),(367.6,'svisj'),(396.3,'svisj'),(401.2,'pop'),(432.48,'pop'),(442.52,'pop'),(511.8,'pop'),(538.2,'pop'),(563.8,'pop'),
 (595.4,'svisj'),(684.34,'pop'),(719.58,'svisj'),(723.76,'pop'),(788.38,'svisj'),(877.58,'svisj'),(975.1,'svisj'),(1019.68,'pop'),(1024.75,'pop')]]
json.dump(L,open('klipp/effekter.json','w'))
print(P2[:5])
