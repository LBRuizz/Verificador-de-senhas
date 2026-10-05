senha = input("Digite uma senha de no minimo 8 caracteres: ")

pontos = 0

if  len(senha) >= 8:
    print("Senha valida!")
    pontos += 1

else:    
     print("Senha muito curta. Tente novamente.")

if any(char.isupper() for char in senha):
   pontos +=1

if any(char.isdigit() for char in senha):
   pontos +=1

if any(char in "!@#$%^&*()_+-=()" for char in senha):
   pontos +=1

if pontos <= 2:
    print("Força da senha: FRACA.")

elif pontos <= 3:
     print("Força da senha: MÉDIA.")

else:
    print("Força da senha: FORTE.")