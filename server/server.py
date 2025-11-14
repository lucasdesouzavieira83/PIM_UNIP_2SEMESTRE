import socket, threading, pickle, os
from modules import academic_core as core
from modules import data_manager as dm
from modules import reporting as reporting_mod
from modules import ai_chatbot as ai

HOST = '127.0.0.1'  # se quiser ouvir toda a rede mudar para '0.0.0.0'
PORT = 5000

def handle_client(conn, addr):
    print(f"Conexao de {addr}")
    try:
        while True:
            data = conn.recv(8192)
            if not data:
                break
            try:
                cmd = pickle.loads(data)
            except Exception:
                conn.send(pickle.dumps('Comando invalido'))
                continue
            op = cmd.get('op')
            args = cmd.get('args', {})
            if op == 'cadastrar_turma':
                res = core.cadastrar_turma(**args)
            elif op == 'cadastrar_aluno':
                res = core.cadastrar_aluno(**args)
            elif op == 'registrar_aula':
                res = core.registrar_aula(**args)
            elif op == 'upload_atividade':
                res = core.upload_atividade(**args)
            elif op == 'relatorio':
                res = core.listar_relatorio()
            elif op == 'relatorio_pdf':
                path = reporting_mod.gerar_relatorio_pdf()
                res = f'PDF gerado: {path}'
            elif op == 'ordenar_alunos_c':
                ordered = dm.ordenar_alunos_c(args.get('alunos_dict', {}))
                res = ordered if ordered is not None else 'Modulo C nao disponivel'
            elif op == 'soma_c':
                v = dm.soma_c(args.get('a',0), args.get('b',0))
                res = v if v is not None else 'Modulo C nao disponivel'
            elif op == 'duvida':
                pergunta = args.get('pergunta','')
                res = ai.responder(pergunta)
            else:
                res = 'Operacao desconhecida'
            conn.send(pickle.dumps(res))
    finally:
        conn.close()

def main():
    print(f"Iniciando servidor em {HOST}:{PORT}")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    try:
        while True:
            conn, addr = server.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
    except KeyboardInterrupt:
        print('Servidor encerrado')
    finally:
        server.close()

if __name__ == '__main__':
    main()
