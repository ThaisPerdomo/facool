import pandas as pd
import matplotlib.pyplot as plt


print("Criando dataframe de putas...")
objeto_exemplo = [{"nome": "thais", "puta": 1}, {"nome": "lis", "puta": 0}]
df = pd.DataFrame(objeto_exemplo)

fig, ax = plt.subplots()
ax.bar(df.nome, df.puta)
ax.set_title("Putawards 2019\n\n")
ax.annotate("Thais venceu!", xy=(0, 1), xytext=(0, 1.1), arrowprops=dict(facecolor='black', shrink=0.05))
plt.savefig("putas.png")