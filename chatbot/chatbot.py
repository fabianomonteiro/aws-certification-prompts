import os
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar a chave da API da OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("A chave da API da OpenAI não foi encontrada no arquivo .env.")

# Inicializar o modelo de chat
chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7, model_name="gpt-4")

def ler_prompt(caminho_do_arquivo):
    try:
        with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"Arquivo {caminho_do_arquivo} não encontrado.")
        return ""

certificacoes = {
    "Foundational": {
        "1": {"nome": "AWS Certified Cloud Practitioner", "disponivel": True},
        "2": {"nome": "AWS Certified AI Practitioner", "disponivel": True},
    },
    "Associate": {
        "3": {"nome": "AWS Certified SysOps Administrator", "disponivel": True},
        "4": {"nome": "AWS Certified Solutions Architect", "disponivel": True},
        "5": {"nome": "AWS Certified Developer", "disponivel": True},
        "6": {"nome": "AWS Certified Machine Learning Engineer", "disponivel": True},
        "7": {"nome": "AWS Certified Data Engineer", "disponivel": True},
    },
    "Professional": {
        "8": {"nome": "AWS Certified Solutions Architect – Professional", "disponivel": True},
        "9": {"nome": "AWS Certified DevOps Engineer – Professional", "disponivel": True},
    },
    "Specialty": {
        "10": {"nome": "AWS Certified Machine Learning – Specialty", "disponivel": True},
        "11": {"nome": "AWS Certified Security – Specialty", "disponivel": False},
        "12": {"nome": "AWS Certified Advanced Networking – Specialty", "disponivel": False},
        "13": {"nome": "AWS Certified Database – Specialty", "disponivel": False},
        "14": {"nome": "AWS Certified Data Analytics – Specialty", "disponivel": False},
        "15": {"nome": "AWS Certified SAP on AWS – Specialty", "disponivel": False},
    }
}

def listar_certificacoes():
    mensagem = "Por favor, escolha uma das seguintes certificações para iniciar o simulado:\n\n"
    for nivel, certs in certificacoes.items():
        mensagem += f"**{nivel}**\n\n"
        for numero, info in certs.items():
            disponibilidade = "" if info["disponivel"] else " *(Em desenvolvimento)*"
            mensagem += f"{numero}. {info['nome']}{disponibilidade}\n"
        mensagem += "\n"
    mensagem += "*Nota: As certificações marcadas como \"(Em desenvolvimento)\" ainda não estão disponíveis para seleção.*"
    return mensagem

def exibir_mensagem_inicial(chain):
    mensagem = chain.run()
    print("Bot:", mensagem)

def obter_selecao_usuario():
    return input("\nVocê: ").strip()

def validar_selecao(selecao):
    todos_numeros = [num for nivel in certificacoes.values() for num in nivel]
    return selecao in todos_numeros

def obter_cert_info(selecao):
    for nivel, certs in certificacoes.items():
        if selecao in certs:
            return certs[selecao]
    return None

def executar_simulado(cert_info, selecao):
    print(f"\nBot: Ótima escolha! Iniciando o simulado para {cert_info['nome']}.\n")
    
    caminho_simulado = f"prompts/simulado_{selecao}.txt"
    prompt_simulado = ler_prompt(caminho_simulado)
    
    if prompt_simulado:
        simulado_chain = LLMChain(
            llm=chat, 
            prompt=PromptTemplate(template=prompt_simulado, input_variables=[])
        )
        simulado_chain.run()
    else:
        print("Bot: Houve um problema ao iniciar o simulado. Por favor, tente novamente mais tarde.")

def perguntar_continuar():
    resposta = input("\nDeseja fazer outro simulado? (Sim/Não): ").strip().lower()
    return resposta == "sim"

def iniciar_chatbot():
    # Ler o prompt inicial
    prompt_inicial = ler_prompt("prompts/inicial.txt")
    
    # Criar a cadeia de prompts
    chain = LLMChain(
        llm=chat, 
        prompt=PromptTemplate(template=prompt_inicial, input_variables=[])
    )
    
    # Exibir a mensagem inicial
    exibir_mensagem_inicial(chain)
    
    while True:
        # Listar certificações
        certificacoes_msg = listar_certificacoes()
        print("\nBot:", certificacoes_msg)
        
        # Solicitar seleção do usuário
        selecao = obter_selecao_usuario()
        
        # Validar a seleção
        if not validar_selecao(selecao):
            print("\nBot: Entrada inválida. Por favor, insira um número válido da lista acima.")
            continue
        
        # Obter informações da certificação selecionada
        cert_info = obter_cert_info(selecao)
        
        if not cert_info:
            print("\nBot: Entrada inválida. Por favor, insira um número válido da lista acima.")
            continue
        
        if not cert_info["disponivel"]:
            print("\nBot: Desculpe, a certificação que você selecionou está em desenvolvimento e não está disponível no momento. Por favor, escolha outra opção da lista.")
            continue
        
        # Executar o simulado
        executar_simulado(cert_info, selecao)
        
        # Perguntar se o usuário deseja continuar
        if not perguntar_continuar():
            print("\nBot: Obrigado por utilizar o Simulador de Exames de Certificação AWS. Boa sorte nos seus estudos!")
            break

if __name__ == "__main__":
    iniciar_chatbot()
