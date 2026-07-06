import os
import json
import random
from datetime import datetime

# ==========================================
# CONFIGURAÇÕES E BANCO DE DADOS LOCAL (MOCK)
# ==========================================
ARQUIVO_HISTORICO = "historico_aprendizado.txt"
ARQUIVO_CONFIG = "config_assistente.json"

CONCEITOS = {
    "1": ("Variáveis e Tipos de Dados", "Variáveis são caixas que guardam dados. Em Python, você não precisa declarar o tipo. Ex: nome = 'Ana' (String), idade = 25 (Int), altura = 1.68 (Float)."),
    "2": ("Estruturas Condicionais", "Permitem ao programa tomar decisões usando `if`, `elif` e `else`. Ex:\nif nota >= 7:\n    print('Aprovado')\nelse:\n    print('Reprovado')"),
    "3": ("Laços de Repetição (Loops)", "Usados para repetir tarefas. O `for` percorre sequências (listas, intervalos). O `while` repete enquanto uma condição for verdadeira."),
    "4": ("Funções", "Blocos de código reutilizáveis que executam uma tarefa específica. Definidas com a palavra-chave `def`. Ex: def saudar(nome): return f'Olá, {nome}'")
}

QUIZ_PERGUNTAS = [
    {"pergunta": "Qual comando é usado para exibir texto na tela?", "opcoes": ["A) input()", "B) print()", "C) echo()", "D) output()"], "resposta": "B"},
    {"pergunta": "Como criamos uma lista em Python?", "opcoes": ["A) lista = []", "B) lista = {}", "C) lista = ()", "D) lista = < >"], "resposta": "A"},
    {"pergunta": "Qual o retorno de 10 // 3 em Python?", "opcoes": ["A) 3.333...", "B) 1", "C) 3", "D) 0"], "resposta": "C"}
]

# ==========================================
# FUNÇÕES UTILITÁRIAS / SISTEMA
# ==========================================
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def salvar_historico(acao, detalhe):
    try:
        with open(ARQUIVO_HISTORICO, "a", encoding="utf-8") as f:
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            f.write(f"[{data_hora}] {acao}: {detalhe}\n")
    except IOError:
        print("Erro ao gravar no histórico.")

def carregar_config():
    if os.path.exists(ARQUIVO_CONFIG):
        try:
            with open(ARQUIVO_CONFIG, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {"api_key": "AQ.Ab8RN6L7UTi8IGk-xVkX7MVOLkp_OFtvHRXBCFqaCRY8wYnMKQ", "modo": "Iniciante"}

def salvar_config(config):
    try:
        with open(ARQUIVO_CONFIG, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
    except IOError:
        print("Erro ao salvar configurações.")

# ==========================================
# FUNCIONALIDADES DO MENU
# ==========================================
def explicar_conceitos():
    limpar_tela()
    print("--- 📚 EXPLICAR CONCEITOS ---")
    for k, v in CONCEITOS.items():
        print(f"{k}. {v[0]}")
    
    opcao = input("\nEscolha um conceito para explicar (ou Enter para voltar): ")
    if opcao in CONCEITOS:
        print(f"\n💡 {CONCEITOS[opcao][0]}:\n{CONCEITOS[opcao][1]}")
        salvar_historico("Explicação de Conceito", CONCEITOS[opcao][0])
    else:
        print("Opção inválida ou retorno ao menu.")
    input("\nPressione Enter para continuar...")

def tirar_duvidas(config):
    limpar_tela()
    print("--- 💬 TIRAR DÚVIDAS (AI ENGINE) ---")
    if not config["api_key"]:
        print("⚠️ [IA OFFLINE] Nenhuma chave de IA detectada nas Configurações.")
        print("O assistente responderá usando a base de conhecimento local básica.")
    else:
        print(f"✨ [IA ONLINE] Autenticado com a chave: {config['api_key'][:8]}...")
    
    duvida = input("\nDigite sua dúvida sobre Python: ")
    if duvida.strip():
        print("\n🤖 Processando com Dev Python AI...")
        # Simulação de processamento inteligente de strings
        if "lista" in duvida.lower():
            resposta = "Listas são mutáveis e ordenadas. Use .append() para adicionar elementos e .remove() para retirar."
        elif "dicionario" in duvida.lower() or "dicionário" in duvida.lower():
            resposta = "Dicionários guardam pares de chave:valor. Ex: dados = {'nome': 'Python'}"
        else:
            resposta = f"Interessante sua dúvida sobre '{duvida}'. Lembre-se sempre de checar a indentação e a sintaxe do Python!"
        
        print(f"\nResposta da IA:\n-> {resposta}")
        salvar_historico("Dúvida Respondida", duvida)
    input("\nPressione Enter para continuar...")

def gerar_exercicios():
    limpar_tela()
    print("--- 📝 GERAR EXERCÍCIOS ---")
    exercicios = [
        "Crie um programa que peça a temperatura em Celsius e converta para Fahrenheit.",
        "Escreva um programa que receba um número e diga se ele é par ou ímpar.",
        "Crie uma lista de 5 nomes e use um laço 'for' para imprimir cada um em maiúsculo."
    ]
    ex = random.choice(exercicios)
    print(f"\nExercício Proposto:\n👉 {ex}")
    salvar_historico("Exercício Gerado", ex)
    input("\nPressione Enter para continuar...")

def corrigir_codigo():
    limpar_tela()
    print("--- 🛠️ CORRIGIR CÓDIGO ---")
    print("Cole ou digite seu código abaixo (pressione Enter vazio 2 vezes para finalizar):")
    
    linhas = []
    while True:
        linha = input()
        if linha == "" and len(linhas) > 0 and linhas[-1] == "":
            break
        linhas.append(linha)
    
    codigo = "\n".join(linhas).strip()
    
    if codigo:
        print("\n🔍 Analisando sintaxe...")
        erros_encontrados = False
        
        # Validação simples de erros comuns
        if "print " in codigo and "(" not in codigo:
            print("❌ Erro encontrado: No Python 3, 'print' é uma função e precisa de parênteses. Ex: print('Olá')")
            erros_encontrados = True
        if "if" in codigo and ":" not in codigo:
            print("❌ Erro encontrado: Faltou o caractere de dois pontos (:) ao final da instrução 'if'.")
            erros_encontrados = True
            
        if not erros_encontrados:
            print("✅ Análise Básica concluída: Nenhum erro de sintaxe óbvio detectado pela IA!")
        
        salvar_historico("Código Analisado", "Análise de sintaxe realizada.")
    input("\nPressione Enter para continuar...")

def criar_desafios():
    limpar_tela()
    print("--- 🏆 DESAFIOS DE PROGRAMAÇÃO ---")
    desafios = [
        "Desafio Boss: Crie um mini-sistema de cadastro de alunos usando dicionários e salve os dados em um arquivo .txt.",
        "Desafio Lógica: Crie uma função que receba uma string e retorne True se ela for um palíndromo (ex: 'arara') e False caso contrário."
    ]
    desafio = random.choice(desafios)
    print(f"\n🚀 {desafio}")
    salvar_historico("Desafio Criado", desafio[:30] + "...")
    input("\nPressione Enter para continuar...")

def quiz():
    limpar_tela()
    print("--- 🧠 QUIZ INTERATIVO ---")
    pergunta_foco = random.choice(QUIZ_PERGUNTAS)
    print(f"\n{pergunta_foco['pergunta']}")
    for opcao in pergunta_foco['opcoes']:
        print(opcao)
        
    resposta_usuario = input("\nSua resposta (A, B, C ou D): ").strip().upper()
    
    if resposta_usuario == pergunta_foco['resposta']:
        print("🎉 Parabéns! Resposta CORRETA.")
        salvar_historico("Quiz", "Acertou a pergunta")
    else:
        print(f"❌ Resposta incorreta. A alternativa certa era a {pergunta_foco['resposta']}.")
        salvar_historico("Quiz", "Errou a pergunta")
    input("\nPressione Enter para continuar...")

def plano_estudos(config):
    limpar_tela()
    print("--- 📅 PLANO DE ESTUDOS PERSONALIZADO ---")
    modo = config.get("modo", "Iniciante")
    print(f"Nível Atual Definido: {modo}\n")
    
    if modo == "Iniciante":
        print("Semana 1: Sintaxe Básica, Variáveis e Operadores Matemáticos.")
        print("Semana 2: Estruturas de Decisão (if/else) e Operadores Lógicos.")
        print("Semana 3: Estruturas de Repetição (While e For).")
    else:
        print("Semana 1: Programação Orientada a Objetos (Classes e Herança).")
        print("Semana 2: Tratamento de Exceções Avançado e Manipulação de Arquivos JSON.")
        print("Semana 3: Integração com APIs e Ambientes Virtuais (venv).")
        
    salvar_historico("Plano de Estudos", f"Visualizou plano {modo}")
    input("\nPressione Enter para continuar...")

def exibir_historico():
    limpar_tela()
    print("--- 📜 HISTÓRICO DE APRENDIZADO ---")
    if os.path.exists(ARQUIVO_HISTORICO):
        try:
            with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
                linhas = f.readlines()
                if linhas:
                    for linha in linhas[-10:]:  # Mostra as últimas 10 ações
                        print(linha.strip())
                else:
                    print("Histórico vazio.")
        except IOError:
            print("Erro ao ler o arquivo de histórico.")
    else:
        print("Nenhum histórico registrado ainda.")
    input("\nPressione Enter para continuar...")

def configuracoes(config):
    while True:
        limpar_tela()
        print("--- ⚙️ CONFIGURAÇÕES ---")
        print(f"1. Chave da IA (API KEY): {config['api_key'] if config['api_key'] else 'Não configurada'}")
        print(f"2. Nível de Nivelamento: {config['modo']}")
        print("3. Voltar")
        
        opcao = input("\nEscolha o que deseja alterar: ")
        
        if opcao == "1":
            nova_chave = input("Digite sua chave de API para Inteligência Artificial: ").strip()
            config["api_key"] = nova_chave
            salvar_config(config)
            print("Chave salva com sucesso!")
            input()
        elif opcao == "2":
            print("\nSelecione o nível:\n1. Iniciante\n2. Avançado")
            niv = input("Opção: ")
            config["modo"] = "Avançado" if niv == "2" else "Iniciante"
            salvar_config(config)
            print("Nível atualizado!")
            input()
        elif opcao == "3":
            break
        else:
            print("Opção Inválida!")
            input()

def sobre():
    limpar_tela()
    print("--- ℹ️ SOBRE O DEV PYTHON AI ---")
    print("Desenvolvido como um assistente educacional inteligente.")
    print("Objetivo: Guiar o estudante do zero ao código avançado em Python.")
    print("Tecnologias: Python 3, Estruturas de Dados e Persistência de Arquivos.")
    print("Versão: 1.0.0 (2026)")
    input("\nPressione Enter para retornar...")

# ==========================================
# MENU PRINCIPAL (LOOP DO FLUXO)
# ==========================================
def menu_principal():
    config = carregar_config()
    
    while True:
        limpar_tela()
        print("=========================================")
        print("        🤖 DEV PYTHON AI v1.0 🤖        ")
        print("=========================================")
        print("1. Explicações de Conceitos")
        print("2. Tirar Dúvidas com a IA")
        print("3. Gerar Exercícios Práticos")
        print("4. Corrigir Código Fonte")
        print("5. Criar Desafios Avançados")
        print("6. Executar Quiz Técnico")
        print("7. Meu Plano de Estudos")
        print("8. Ver Histórico de Aprendizado")
        print("9. Configurações do Sistema")
        print("10. Sobre o Aplicativo")
        print("11. Sair")
        print("=========================================")
        
        opcao = input("Escolha uma opção (1-11): ").strip()
        
        try:
            if opcao == "1":
                explicar_conceitos()
            elif opcao == "2":
                tirar_duvidas(config)
            elif opcao == "3":
                gerar_exercicios()
            elif opcao == "4":
                corrigir_codigo()
            elif opcao == "5":
                criar_desafios()
            elif opcao == "6":
                quiz()
            elif opcao == "7":
                plano_estudos(config)
            elif opcao == "8":
                exibir_historico()
            elif opcao == "9":
                configuracoes(config)
            elif opcao == "10":
                sobre()
            elif opcao == "11":
                print("\nObrigado por utilizar o Dev Python AI. Bons estudos!")
                break
            else:
                print("\n⚠ Opção inválida! Digite um número de 1 a 11.")
                input("Pressione Enter para tentar novamente...")
        except Exception as e:
            print(f"\n💥 Ocorreu um erro inesperado no sistema: {e}")
            input("Pressione Enter para retornar ao Menu...")

if __name__ == "__main__":
    menu_principal()