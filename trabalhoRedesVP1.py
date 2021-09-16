import csv

#parametros recebidos:
userPath = 'tabelaDeRotas.csv' # colocar as informações dentro deste arquivo
userIp = '128.45.67.36' #IP informado pelo usuario (exemplo da aula do dia 31/8)

# aqui converte os IPs para binário
def toBinary(ip):
    return '.'.join([bin(int(x)+256)[3:]
     for x in ip.split('.')])

# retorna os bit, comparados de acordo com o CIDR 
def compareTo(userIp, csvIp, mask):
    count = 0
    userIp = compareTo(userIp).replace('.', ' ')
    csvIp = compareTo(csvIp).replace('.', ' ')
    for bit in range(0, mask):
        if userIp[bit] == csvIp[bit]:
            count = count + 1
    return count


# verifica o total de bits 1 na máscara
def maskCounter(mask):
    count = 0 #necessario iniciar com 0
    mask = compareTo(mask)
    for bit in range(0, len(mask)):
        if mask[bit] == '1':
            count = count + 1
    return count

#aqui realiza a leitura do arquivo tabelaDeRotas.csv
def readCsv():
    with open(userPath) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        lineCount = 0
        for row in csvReader:
            print(f'Prefixo : {row[0]}, '
                  f'Máscara : {row[1]}, '
                  f'Next Port Hop: {row[2]}'
                  )
            lineCount = lineCount + 1


# pega o IP para comparar
def operation(userIp): 
    print(f' *Realizando a comparação dos IPs* ')
    with open(userPath) as csvFile: #pega o caminho
        csvReader = csv.reader(csvFile, delimiter=',')
        lineCount = 0
        matchPrefix = 0
        for row in csvReader:
            prefix = row[0]
            mask = maskCounter(row[1])
            if binaryCompare(userIp, prefix, mask) == mask:
                print(f'Deu match com o prefixo {row[0]} / {mask}')
                if mask > matchPrefix:
                    matchPrefix = mask
            lineCount += 1
    return matchPrefix


print('\nEndereço IPv4 recebido: ', userIp)
print('Caminho para o arquivo CSV recebido pelo usuário: ', userPath, '\n') 
print('IP destino convertido em binário: ', toBinary(userIp), '\n')
print('* Exibindo dados do arquivo .csv *')
readCsv()
print(
  f'\nA interface de rede com o Prefixo: /{operation(userIp)} deu match!')