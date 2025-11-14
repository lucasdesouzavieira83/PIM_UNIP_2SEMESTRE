RESPONSES = {
    'horario': 'As aulas geralmente comecam as 08:00. Verifique o calendario da turma.',
    'prova': 'Verifique o cronograma no diario eletronico. Contate o professor.',
    'nota': 'As notas sao lancadas no final do bimestre pelo professor.'
}

def responder(pergunta: str) -> str:
    p = pergunta.lower()
    for k, resp in RESPONSES.items():
        if k in p:
            return resp
    return 'Desculpe, nao entendi. Tente palavras como \"horario\", \"prova\" ou \"nota\".'
