import yfinance


def analisar(codigo, periodo):
    dados = yfinance.Ticker(codigo).history(periodo)
    
    fechamento = dados.Close
    maximo = fechamento.max()
    minimo = fechamento.min()
    atual = fechamento[-1]
    
    resultado = {
        'maximo': f'{maximo:.2f}',
        'minimo': f'{minimo:.2f}',
        'atual': f'{atual:.2f}'
    }
    
    return resultado


def formata_periodo(periodo):
    if 'd' in periodo:
        numerico = int(periodo[0:-1])
        sufixo = 'dias' if numerico > 1 else 'dia'            
        return f'{numerico} {sufixo}'
    elif 'w' in periodo:
        numerico = int(periodo[0:-1])
        sufixo = 'semanas' if numerico > 1 else 'semana'            
        return f'{numerico} {sufixo}'
    elif 'mo' in periodo:
        numerico = int(periodo[0:-2])
        sufixo = 'meses' if numerico > 1 else 'mês'            
        return f'{numerico} {sufixo}'
    elif 'y' in periodo:
        numerico = int(periodo[0:-1])
        sufixo = 'anos' if numerico > 1 else 'ano'            
        return f'{numerico} {sufixo}'
    else:
        return 'período inválido'
