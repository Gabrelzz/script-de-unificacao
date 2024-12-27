import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        confidence = result['confidence']
        return encoding, confidence

file_path = 'arquivo.txt'
encoding, confidence = detect_encoding(file_path)
print(f'Codificação detectada: {encoding} com confiança de {confidence:.2f}')
