import os
import openai
import pysrt
from tqdm import tqdm
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()

# Configurar a chave da API
openai.api_key = os.getenv("OPENAI_API_KEY")

def traduzir_texto(texto, persona_regras):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # ou o modelo que você estiver usando
            messages=[
                {"role": "system", "content": persona_regras},
                {"role": "user", "content": texto}
            ],
            max_tokens=1000,  # Ajuste conforme necessário
            n=1,
            stop=None,
            temperature=0.3,
        )
        traducao = response.choices[0].message['content'].strip()
        return traducao
    except Exception as e:
        print(f"Erro na tradução: {e}")
        return texto  # Retorna o texto original em caso de erro

def dividir_em_blocos(srt, tamanho_bloco=100):
    total_lines = len(srt)
    blocos = []
    for i in range(0, total_lines, tamanho_bloco):
        bloco = srt[i:i+tamanho_bloco]
        blocos.append(bloco)
    return blocos

def salvar_srt_traduzido(blocos_traduzidos, caminho_saida):
    subs = pysrt.SubRipFile()
    contador = 1
    for bloco in blocos_traduzidos:
        for sub in bloco:
            novo_sub = pysrt.SubRipItem()
            novo_sub.index = contador
            novo_sub.start = sub.start
            novo_sub.end = sub.end
            novo_sub.text = sub.text
            subs.append(novo_sub)
            contador += 1
    subs.save(caminho_saida, encoding='utf-8')

def main():
    # Defina o caminho para o arquivo SRT original
    caminho_srt_original = "legendas_original.srt"

    # Defina o caminho para o arquivo SRT traduzido
    caminho_srt_traduzido = "legendas_traduzidas.srt"

    # Defina a persona e as regras para o modelo
    persona_regras = """
Tu és o Poker ESP, um tradutor especializado em inteligência artificial com mais de 10 anos de experiência,
focado em traduções profissionais e precisas no nicho de Poker, especialmente em torneios.
O teu objetivo é corrigir e melhorar traduções de aulas de poker, tornando-as compreensíveis para jogadores de alto nível,
mantendo a terminologia técnica consistente e precisa, e entregando traduções no formato srt sem alterar os timestamps originais.
Instruções: - Pergunte ao usuário qual é o idioma original e qual é o idioma de destino.
Solicite o texto a ser traduzido.
Traduza o segmento de aulas de poker, corrigindo erros de tradução direta e garantindo que o conteúdo seja natural e compreensível para jogadores de poker experientes.
Mantenha a ortografia consistente e a fluidez das frases, adaptando-as para o idioma de destino.Não altere os timestamps.Mantenha o formato original das legendas.
Nota:Não invente ou adicione conteúdo que não existe.
Realize uma tradução por vez, focando-se no idioma especificado pelo usuário.****
Traduz o textto que te é dado, de uma só vez sem perguntar se eu quero que continues
O texto está em EN e vais traduzir para ESP.
QUando te entregar o texto faz tudo do inicio até ao fim

    """

    # Carregar o arquivo SRT
    srt = pysrt.open(caminho_srt_original, encoding='utf-8')

    # Dividir em blocos
    blocos = dividir_em_blocos(srt, tamanho_bloco=100)
    blocos_traduzidos = []

    print(f"Total de blocos a traduzir: {len(blocos)}")

    # Traduzir cada bloco
    for bloco in tqdm(blocos, desc="Traduzindo blocos"):
        # Concatenar todo o texto do bloco
        texto_original = "\n".join([sub.text for sub in bloco])

        # Traduzir usando a função definida
        texto_traduzido = traduzir_texto(texto_original, persona_regras)

        # Criar novos objetos SubRipItem com o texto traduzido
        subs_traduzidos = blocos[:0]  # Cria uma lista vazia com o mesmo tipo
        linhas_traduzidas = texto_traduzido.split('\n')

        # Assegurar que o número de linhas traduzidas coincide com o original
        if len(linhas_traduzidas) != len(bloco):
            print("A quantidade de linhas traduzidas não coincide com o original. Usando tradução parcial.")
            linhas_traduzidas = [linha for linha in linhas_traduzidas[:len(bloco)]]

        bloco_traduzido = []
        for original_sub, traducao in zip(bloco, linhas_traduzidas):
            novo_sub = pysrt.SubRipItem()
            novo_sub.index = original_sub.index
            novo_sub.start = original_sub.start
            novo_sub.end = original_sub.end
            novo_sub.text = traducao
            bloco_traduzido.append(novo_sub)

        blocos_traduzidos.append(bloco_traduzido)

    # Salvar o arquivo SRT traduzido
    salvar_srt_traduzido(blocos_traduzidos, caminho_srt_traduzido)
    print(f"Tradução concluída! Arquivo salvo como {caminho_srt_traduzido}")

if __name__ == "__main__":
    main()
