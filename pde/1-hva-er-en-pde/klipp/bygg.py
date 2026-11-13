# Bygger anim.html fra anim.mal.html med klippekartet (film2_kart.json) og tempoet.
# Kjør fra videomappa: python3 klipp/bygg.py <kart.json> <tempo> <lengde>
import sys, json
k=json.load(open(sys.argv[1])); tempo=float(sys.argv[2]); L=float(sys.argv[3])
s=open('anim.mal.html').read()
s=s.replace('/*KART*/[]',json.dumps([q[:4] for q in k])).replace('/*TEMPO*/1',str(tempo)).replace('/*LENGDE*/300',str(L))
open('anim.html','w').write(s)
