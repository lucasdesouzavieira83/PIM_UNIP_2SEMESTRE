from modules.database import load_db, save_db

def _get_db():
    return load_db()

def cadastrar_turma(turma_id: str, nome: str):
    db = _get_db()
    if turma_id in db['turmas']:
        return f"Turma {turma_id} ja existe"
    db['turmas'][turma_id] = {"nome": nome, "alunos": [], "aulas": []}
    save_db(db)
    return f"Turma {nome} cadastrada."

def cadastrar_aluno(aluno_id: str, nome: str, turma_id: str):
    db = _get_db()
    if aluno_id in db['alunos']:
        return f"Aluno {aluno_id} ja existe"
    if turma_id not in db['turmas']:
        return f"Turma {turma_id} nao existe"
    db['alunos'][aluno_id] = {"nome": nome, "turma": turma_id, "atividades": []}
    db['turmas'][turma_id]['alunos'].append(aluno_id)
    save_db(db)
    return f"Aluno {nome} cadastrado na turma {turma_id}."

def registrar_aula(aula_id: str, turma_id: str, conteudo: str):
    db = _get_db()
    if turma_id not in db['turmas']:
        return f"Turma {turma_id} nao existe"
    db['aulas'][aula_id] = {"turma": turma_id, "conteudo": conteudo}
    db['turmas'][turma_id]['aulas'].append(aula_id)
    save_db(db)
    return f"Aula {aula_id} registrada para turma {turma_id}."

def upload_atividade(aluno_id: str, atividade_id: str, descricao: str):
    db = _get_db()
    if aluno_id not in db['alunos']:
        return f"Aluno {aluno_id} nao existe"
    db['atividades'][atividade_id] = {"aluno": aluno_id, "descricao": descricao}
    db['alunos'][aluno_id]['atividades'].append(atividade_id)
    save_db(db)
    return f"Atividade {atividade_id} salva para {aluno_id}."

def listar_relatorio():
    db = _get_db()
    lines = []
    for tid, turma in db['turmas'].items():
        lines.append(f"Turma {tid} - {turma['nome']}")
        for aid in turma['alunos']:
            aluno = db['alunos'].get(aid, {})
            lines.append(f"  Aluno {aid}: {aluno.get('nome','-')} - Atividades: {len(aluno.get('atividades',[]))}")
    return "\\n".join(lines)
