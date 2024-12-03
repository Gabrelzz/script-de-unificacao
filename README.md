# Script de Unificação
 
Olá, seja bem vindo ao meu script de unificação.

Explicação da funcionalidade do script:

Este script ele lê todos os arquivos ".txt" que possui na mesma pasta que está o script, ele unifica todos os arquivos .txt pelo demilitador "tabulação" e
em seguida ele pega todos os arquivos unificados e coloca todas as informações em um único arquivo csv com o nome de: "unificado.txt".

# Recomendações

Utilizar o pyinstaller para caso queira fazer a criação de um executável.
Baixar e extrair o UPX caso queira um script mais leve (Sem UPX 35.000KB | Com UPX 25.000KB)
(Baixe o UPX por aqui "https://upx.github.io/", descompacte ele e utilize o diretório desta pasta que está descompactada no comando a ser utilizado para a criação do executável)

comando utilizado para a criação do executável:
"pyinstaller --onefile --icon=icone-unificar.ico --noconsole --upx-dir "diretorio/da/pasta/que/esta/instalado/o/upx" .\unificar.py"
