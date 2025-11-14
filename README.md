PIM_SegundoSemestre - Versao Final
==================================

Instrucoes rapidas:
1. Instale MinGW-w64 (x86_64) e adicione C:\mingw64\bin ao PATH.
2. No PowerShell, compile o modulo C (veja build_module.bat):
     cd server\c_modules
     build_module.bat
3. Instale dependencias Python (se houver):
     pip install reportlab
4. Inicie o servidor em uma janela PowerShell:
     cd server
     python server.py
5. Em outra janela, rode o cliente:
     cd client
     python client.py

Estrutura de pastas incluida neste pacote:
- client/client.py
- server/server.py
- server/academic_core.py
- server/database.py
- server/modules/data_manager.py
- server/c_modules/sort_search.c
- server/c_modules/hardware_module.c
- server/c_modules/build_module.bat
- reports/report_generator.py
- ai/chatbot.py

Observacoes:
- A IA aqui e local e simples (respostas por palavra-chave).
- O build_module.bat tenta usar gcc no PATH (MinGW-w64). Se gcc nao for encontrado, instale MinGW-w64.
- Se usar outra maquina na rede, ajuste HOST no client/client.py para o IP do servidor.
