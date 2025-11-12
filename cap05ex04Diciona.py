dic = {'lapis': 8, 'caderno': 12, 'borracha': 3, 'mouse': 59, 'fone': 154}

for k,v in dic.items():
    dic[k] = round(v * 1.1,2)

print(dic)


'''dic = {chave: valor*1.1 for chave, valor in dic.items()}'''