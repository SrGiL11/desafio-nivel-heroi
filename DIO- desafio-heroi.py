# Solicita o nome do herói e a quantidade de experiência (XP)
nome = input("Digite o nome do herói: ")
xp = int(input("Digite a quantidade de experiência do herói: "))

# Verifica o nível do herói com base na XP usando estruturas de decisão
if xp < 1000:
   nivel = "Ferro"
elif 1001 <= xp <= 2000:
   nivel = "Bronze"
elif 2001 <= xp <= 5000:
   nivel = "Prata"
elif 6001 <= xp <= 7000:
   nivel = "Ouro"
elif 7001 <= xp <= 8000:
   nivel = "Platina"
elif 8001 <= xp <= 9000:
   nivel = "Ascendente"
elif 9001 <= xp <= 10000:
   nivel = "Imortal"
else:
   nivel = "Radiante"

# Exibe a mensagem com o nome do herói e seu nível
print("O herói {} está no nível {}.".format(nome, nivel))