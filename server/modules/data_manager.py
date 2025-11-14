import os, platform
from ctypes import CDLL, Structure, c_char, c_int, c_char_p, POINTER

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
C_DLL = os.path.join(BASE, 'c_modules', 'sort_search.dll')
C_SO = os.path.join(BASE, 'c_modules', 'sort_search.so')

lib = None
if platform.system() == 'Windows' and os.path.exists(C_DLL):
    lib = CDLL(C_DLL)
elif platform.system() in ('Linux','Darwin') and os.path.exists(C_SO):
    lib = CDLL(C_SO)

class AlunoC(Structure):
    _fields_ = [('id', c_char * 16), ('nome', c_char * 64)]

def carregar_alunos_para_c(alunos_dict):
    arr = (AlunoC * len(alunos_dict))()
    for i, (aid, data) in enumerate(alunos_dict.items()):
        arr[i].id = aid.encode('utf-8')[:15]
        arr[i].nome = data.get('nome','').encode('utf-8')[:63]
    return arr, len(alunos_dict)

def ordenar_alunos_c(alunos_dict):
    if not lib:
        return None
    arr, n = carregar_alunos_para_c(alunos_dict)
    lib.ordenar_alunos.argtypes = [POINTER(AlunoC), c_int]
    lib.ordenar_alunos.restype = None
    lib.ordenar_alunos(arr, n)
    ordered = []
    for i in range(n):
        aid = arr[i].id.decode('utf-8').rstrip('\\x00')
        ordered.append((aid, arr[i].nome.decode('utf-8').rstrip('\\x00')))
    return ordered

def soma_c(a, b):
    if not lib:
        return None
    lib.soma.argtypes = [c_int, c_int]
    lib.soma.restype = c_int
    return lib.soma(a, b)
