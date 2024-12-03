# Script de Unificação
 
Olá, seja bem vindo ao meu script de unificação.

Para poder utilizá-lo da melhor forma segue o passo a passo.

- Crie uma pasta.
- Coloque o executável do script nesta pasta.
- Coloque todos os arquivos .txt que você deseja unificar.
- Execute o script.
- Pronto! seus arquivos .txt estão transformados em um único arquivo ".csv".

# Explicação

Estou utilizando a biblioteca pandas, glob e io.

pandas -> para criação do DataFrame

glob -> ler todos os arquivos ".txt"

io -> para não precisar criar um arquivo ".txt"

Este script ele unifica vários arquivos ".txt" que estiver presente no mesmo local que o arquivo do script, ele unifica guarda a informação e transforma em um único arquivo ".csv".

Ele está configurado para ler o arquivos ".txt" com delimitador "tabulação" e na codificação "utf-8", excluir algumas colunas vazias que estavam sendo criadas e salvar o DataFrame como ".csv" com separação por ponto e vírgula e utilizando a codificação "utf-8-sig" para melhor adaptação ao Excel.

# Recomendações

Utilizar o pyinstaller para caso queira fazer a criação de um executável.

Baixar e extrair o UPX caso queira um script mais leve (Sem UPX 35.000KB | Com UPX 25.000KB)

(Baixe o UPX por aqui "https://upx.github.io/", descompacte ele e utilize o diretório desta pasta que está descompactada no comando a ser utilizado para a criação do executável)

comando utilizado para a criação do executável:

"pyinstaller --onefile --icon=icone-unificar.ico --noconsole --upx-dir "diretorio/da/pasta/que/esta/instalado/o/upx" .\unificar.py"
