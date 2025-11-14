from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
from modules.database import load_db

REPORTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'reports_output'))
os.makedirs(REPORTS_DIR, exist_ok=True)

def gerar_relatorio_pdf(filename='relatorio_turmas.pdf'):
    db = load_db()
    path = os.path.join(REPORTS_DIR, filename)
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4
    y = height - 40
    c.setFont('Helvetica-Bold', 14)
    c.drawString(40, y, 'Relatorio de Turmas')
    y -= 30
    c.setFont('Helvetica', 10)
    for tid, turma in db['turmas'].items():
        c.drawString(40, y, f"Turma {tid}: {turma.get('nome','')}")
        y -= 14
        for aid in turma.get('alunos', []):
            aluno = db['alunos'].get(aid, {})
            c.drawString(60, y, f"Aluno {aid}: {aluno.get('nome','')} - Atividades: {len(aluno.get('atividades',[]))}")
            y -= 12
            if y < 60:
                c.showPage()
                y = height - 40
    c.save()
    return path
