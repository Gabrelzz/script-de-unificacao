import pandas as pd
import glob
import io

def unificar_e_converter_para_csv():

    try:
        arquivos_txt = glob.glob("*.txt")
        conteudo_unificado = ""

        for arquivo in arquivos_txt:
            with open(arquivo, "r", encoding="utf-8") as f:
                conteudo_unificado += f.read()

        ''' Lê o arquivo unificado com tabulação como delimitador '''
        df = pd.read_csv(io.StringIO(conteudo_unificado), sep='\t', encoding="utf-8", header=None)

        ''' Remover colunas vazias '''
        df = df.dropna(axis=1, how='all')
        
        ''' Salva o DataFrame como CSV '''
        df.to_csv("unificado.csv", index=False, header=False, sep=';', encoding="utf-8-sig")
        print("Arquivo CSV criado com sucesso: unificado.csv")
        
    except Exception as e:
        print(f"Erro ao tentar processar o script: {e}")
        
unificar_e_converter_para_csv()
