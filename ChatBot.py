import google.generativeai as genai


chave_key = "AIzaSyBeYG1Zy19XqCaMDLE6SxYyyxZMfTennlw"

genai.configure(api_key=chave_key)


modelo = genai.GenerativeModel("gemini-1.5-pro-latest")

print("E ai meu parceiro, Aqui e seu amigo NelBot!")
print("Para sair escreva 'sair'", "\n")

while True:
    pergunta = input("Usuario: ")
    if pergunta == "sair":
        break
    else:
        response = modelo.generate_content(pergunta)
        print("NelBot: ", str(response.text))