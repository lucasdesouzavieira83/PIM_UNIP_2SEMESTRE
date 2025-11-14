import socket, pickle

HOST = '127.0.0.1'
PORT = 5000

def send_request(cmd):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(pickle.dumps(cmd))
        data = s.recv(8192)
        return pickle.loads(data)

def menu():
    while True:
        print('\n--- Cliente Sistema Academico ---')
        print('1 - Cadastrar Turma')
        print('2 - Cadastrar Aluno')
        print('3 - Registrar Aula')
        print('4 - Upload Atividade')
        print('5 - Relatorio (texto)')
        print('6 - Gerar Relatorio (PDF)')
        print('7 - Ordenar alunos via C (se compilar)')
        print('8 - Soma via C (se compilar)')
        print('9 - Perguntar ao Chatbot')
        print('0 - Sair')
        op = input('Escolha: ').strip()
        if op == '1':
            tid = input('ID Turma: ').strip()
            nome = input('Nome da Turma: ').strip()
            print(send_request({'op':'cadastrar_turma','args':{'turma_id':tid,'nome':nome}}))
        elif op == '2':
            aid = input('ID Aluno: ').strip()
            nome = input('Nome do Aluno: ').strip()
            tid = input('ID Turma: ').strip()
            print(send_request({'op':'cadastrar_aluno','args':{'aluno_id':aid,'nome':nome,'turma_id':tid}}))
        elif op == '3':
            aid = input('ID Aula: ').strip()
            tid = input('ID Turma: ').strip()
            conteudo = input('Conteudo: ').strip()
            print(send_request({'op':'registrar_aula','args':{'aula_id':aid,'turma_id':tid,'conteudo':conteudo}}))
        elif op == '4':
            aid = input('ID Aluno: ').strip()
            atid = input('ID Atividade: ').strip()
            desc = input('Descricao: ').strip()
            print(send_request({'op':'upload_atividade','args':{'aluno_id':aid,'atividade_id':atid,'descricao':desc}}))
        elif op == '5':
            print(send_request({'op':'relatorio'}))
        elif op == '6':
            print(send_request({'op':'relatorio_pdf'}))
        elif op == '7':
            print('Solicitando ordenacao via C...')
            print(send_request({'op':'ordenar_alunos_c','args':{'alunos_dict':{}}}))
        elif op == '8':
            a = int(input('a: '))
            b = int(input('b: '))
            print(send_request({'op':'soma_c','args':{'a':a,'b':b}}))
        elif op == '9':
            pergunta = input('Digite sua duvida: ').strip()
            print(send_request({'op':'duvida','args':{'pergunta':pergunta}}))
        elif op == '0':
            break
        else:
            print('Opcao invalida')

if __name__ == '__main__':
    menu()
