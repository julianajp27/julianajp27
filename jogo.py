# Jogo Educativo - QuizEco (Verdadeiro, Falso e Múltipla Escolha)
import random

# Função principal do jogo
def jogo_educativo():
    print("\n=== QUIZECO - JOGO EDUCATIVO SOBRE SUSTENTABILIDADE ===\n")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    print(f"\nBem-vindo(a), {nome}! Vamos começar o jogo!\n")

    perguntas = [
        {
            "tipo": "vf",
            "pergunta": "Reciclar papel ajuda a salvar árvores.",
            "resposta": True,
            "curiosidade": "Você sabia que uma tonelada de papel reciclado pode salvar até 20 árvores? Por exemplo, ao reciclar cadernos e folhas usadas, reduzimos a necessidade de cortar novas árvores para produzir papel."
        },
        {
            "tipo": "vf",
            "pergunta": "Energia solar é uma fonte de energia poluente.",
            "resposta": False,
            "curiosidade": "Você sabia que a energia solar é limpa, renovável e abundante? Painéis solares instalados em casas e escolas podem gerar eletricidade sem emitir gases poluentes."
        },
        {
            "tipo": "multipla",
            "pergunta": "Qual destas práticas ajuda a economizar água?",
            "opcoes": ["Deixar a torneira aberta", "Tomar banhos longos", "Usar vassoura para limpar a calçada", "Lavar o carro todos os dias"],
            "resposta": 2,
            "curiosidade": "Você sabia que usar a vassoura em vez da mangueira pode economizar até 280 litros de água por vez?"
        },
        {
            "tipo": "multipla",
            "pergunta": "Qual material pode ser reciclado infinitamente sem perder qualidade?",
            "opcoes": ["Plástico", "Papel", "Vidro", "Isopor"],
            "resposta": 2,
            "curiosidade": "Você sabia que o vidro pode ser reciclado infinitamente? Garrafas e potes usados podem virar novos produtos diversas vezes."
        },
        {
            "tipo": "vf",
            "pergunta": "Os créditos de carbono podem beneficiar empresas sustentáveis.",
            "resposta": True,
            "curiosidade": "Você sabia que empresas sustentáveis podem vender créditos de carbono e lucrar com práticas ecológicas? Por exemplo, uma fábrica que reduz suas emissões pode vender esse crédito a outra que precisa compensar sua poluição."
        },
        {
            "tipo": "vf",
            "pergunta": "Jogar lixo na rua não prejudica o meio ambiente.",
            "resposta": False,
            "curiosidade": "Você sabia que o lixo jogado na rua entope bueiros e causa enchentes nas cidades? Em épocas de chuva, isso aumenta os alagamentos e a proliferação de doenças."
        },
        {
            "tipo": "vf",
            "pergunta": "Desmatamento contribui para o aumento do efeito estufa.",
            "resposta": True,
            "curiosidade": "Você sabia que as florestas absorvem CO₂ e ajudam a regular o clima do planeta? Quando derrubadas, liberam esse gás na atmosfera, agravando o aquecimento global."
        },
        {
            "tipo": "vf",
            "pergunta": "Água é um recurso natural inesgotável.",
            "resposta": False,
            "curiosidade": "Você sabia que menos de 1% da água do planeta está disponível para consumo humano? Por isso, atitudes como fechar a torneira ao escovar os dentes são muito importantes."
        },
        {
            "tipo": "vf",
            "pergunta": "Plantar árvores ajuda a combater a mudança climática.",
            "resposta": True,
            "curiosidade": "Você sabia que uma árvore pode absorver até 150 kg de CO₂ por ano? Projetos de reflorestamento em cidades ajudam a melhorar o ar e reduzir o calor."
        },
        {
            "tipo": "vf",
            "pergunta": "Reutilizar materiais é uma forma de reduzir a geração de resíduos.",
            "resposta": True,
            "curiosidade": "Você sabia que reutilizar materiais reduz a necessidade de extração de novos recursos naturais? Por exemplo, transformar uma caixa de papelão em um organizador evita o descarte desnecessário."
        }
    ]

    pontuacao = 0

    for i, item in enumerate(perguntas):
        print(f"Pergunta {i+1}:")
        if item["tipo"] == "vf":
            print(f"{item['pergunta']} (V/F)")
            resposta = input("Sua resposta: ").strip().upper()
            resposta_bool = resposta == "V"
            if resposta_bool == item["resposta"]:
                print("✅ Resposta correta!\n")
                pontuacao += 1
            else:
                print("❌ Resposta incorreta.\n")
        elif item["tipo"] == "multipla":
            print(item["pergunta"])
            for idx, opcao in enumerate(item["opcoes"]):
                print(f"{idx + 1}) {opcao}")
            try:
                resposta = int(input("Digite o número da alternativa correta: ")) - 1
                if resposta == item["resposta"]:
                    print("✅ Resposta correta!\n")
                    pontuacao += 1
                else:
                    print("❌ Resposta incorreta.\n")
            except:
                print("❌ Entrada inválida.\n")

        # Exibir curiosidade relacionada
        print(f"💡 Curiosidade: {item['curiosidade']}\n")

    print(f"\nJogo finalizado, {nome}!\nSua pontuação: {pontuacao} de {len(perguntas)}")

    if pontuacao == len(perguntas):
        print("Parabéns! Você é um(a) verdadeiro(a) guardião(ã) do planeta! 🌱")
    elif pontuacao >= 6:
        print("Muito bem! Ainda dá pra melhorar! ♻️")
    else:
        print("Vamos estudar mais sobre sustentabilidade! Você consegue! 💪")

# Iniciar o jogo
if __name__ == "__main__":
    jogo_educativo()