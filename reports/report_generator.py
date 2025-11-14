# script utilitario para gerar relatorios via terminal
from modules.reporting import gerar_relatorio_pdf
if __name__ == '__main__':
    path = gerar_relatorio_pdf()
    print('Relatorio gerado em:', path)
