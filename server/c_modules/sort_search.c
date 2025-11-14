#include <stdio.h>
#include <string.h>

typedef struct {
    char id[16];
    char nome[64];
} Aluno;

// funcao de teste
int soma(int a, int b) {
    return a + b;
}

// busca sequencial por id
int buscar_aluno(Aluno *alunos, int n, const char* id) {
    for (int i = 0; i < n; ++i) {
        if (strcmp(alunos[i].id, id) == 0) return i;
    }
    return -1;
}

// ordena pelo nome (bubble sort)
void ordenar_alunos(Aluno *alunos, int n) {
    for (int i = 0; i < n-1; ++i) {
        for (int j = 0; j < n-i-1; ++j) {
            if (strcmp(alunos[j].nome, alunos[j+1].nome) > 0) {
                Aluno tmp = alunos[j];
                alunos[j] = alunos[j+1];
                alunos[j+1] = tmp;
            }
        }
    }
}
