"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""
import os

palavra_secreta = "Cachorro-quente"
palavra_secreta_escondida = ""
letras_digitadas = ""
for letra in palavra_secreta:
    if letra.isalpha():
        palavra_secreta_escondida += "*"
    else:
        palavra_secreta_escondida += letra
vidas = 5

print("Bem-vindo ao jogo da palavra secreta!")
print("você tem 5 vidas para adivinhar a palavra secreta")
print("A palavra secreta é:", palavra_secreta_escondida)
print("Boa sorte!")

while vidas > 0:

    print("\nVidas: ", vidas)
    print("Letras digitadas: ", letras_digitadas)
    letra = input("Digite uma letra: ").strip().lower()
    if len(letra) == 1 and letra.isalpha() and letra not in letras_digitadas:
        letras_digitadas += letra + " "
        if letra in palavra_secreta.lower():
            print("Você acertou!")
            print(f"A letra {letra} está na palavra secreta")
            for i in range(len(palavra_secreta)):
                if letra == palavra_secreta[i].lower():
                    palavra_secreta_escondida = palavra_secreta_escondida[:i] + letra.lower() + palavra_secreta_escondida[i + 1:]
            print("Agora a palavra está assim:", palavra_secreta_escondida)
            if palavra_secreta_escondida.lower() == palavra_secreta.lower():
                os.system("clear")
                break
        else:
            print(f"Você errou, a letra {letra} não está na palavra secreta")
            vidas -= 1
    else:
        if letra in letras_digitadas:
            print("Você já digitou essa letra, tente outra")
        else:
            print("Você digitou mais de uma letra ou um número, tente novamente")

if vidas == 0:
    print("\n =( Você perdeu! A palavra secreta era:", palavra_secreta)
else:
    print("\n =) Parabéns! Você acertou a palavra secreta!")
    print("  __________________  ")
    print(" /                  \\ ")
    print("|  ~~~~~~~~~~~~~~~~  |")
    print("|  ~~~~~~~~~~~~~~~~  |")
    print(" \\__________________/ ")
