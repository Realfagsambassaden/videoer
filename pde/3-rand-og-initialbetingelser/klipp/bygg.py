# Bygger anim.html fra anim.mal.html med klippekartet. Kjør fra videomappa: python3 klipp/bygg.py <kart.json> <lengde>
import sys, json
k=json.load(open(sys.argv[1])); L=float(sys.argv[2])
s=open('anim.mal.html').read()
s=s.replace('/*KART*/[]',json.dumps([q[:5] for q in k])).replace('/*TEMPO*/1','1').replace('/*LENGDE*/300',str(L))
open('anim.html','w').write(s)
