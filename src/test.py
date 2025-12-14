from dao import *
from models import *

r1 = Restricao(1, "Vegetariano")
RestricaoDAO.add(r1)
a1 = Aluno("12345", "Gilbert", "abc", [ r1 ])
AlunoDAO.add(a1)

for a in AlunoDAO.get_all():
    print(a)
    for r in a.get_restricoes():
        print(r)
    print("---")
