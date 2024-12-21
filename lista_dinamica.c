#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LENGTH 100 // Define o tamanho máximo das strings (nome e curso)

// Estrutura para representar um visitante
struct Visitante {
    char nome[MAX_LENGTH];      // Nome do visitante
    char nacionalidade[MAX_LENGTH];     // Curso do visitante
    int idade;                  // Idade do visitante               
    struct Visitante *proximo;  // Ponteiro para o próximo visitante (necessário para a lista circular)
};

// Estrutura para representar a lista circular
struct Lista {
    struct Visitante *inicio;   // Ponteiro para o início (primeiro visitante) da lista
    struct Visitante *fim;      // Ponteiro para o fim (último visitante) da lista
    int tamanho;                // Número de visitantes na lista
};

// Função para inicializar a lista circular
void inicializarLista(struct Lista *lista) {
    lista->inicio = NULL;   // Inicializa o ponteiro de início como NULL (lista vazia)
    lista->fim = NULL;      // Inicializa o ponteiro de fim como NULL (lista vazia)
    lista->tamanho = 0;     // Inicializa o tamanho da lista como 0
}

// Função para criar um novo visitante
struct Visitante *criarVisitante(char nome[], char nacionalidade[], int idade) {
    // Aloca memória para um novo visitante
    struct Visitante *novoVisitante = (struct Visitante *)malloc(sizeof(struct Visitante));

    // Copia os valores fornecidos para os campos da estrutura
    strcpy(novoVisitante->nome, nome);
    strcpy(novoVisitante->nacionalidade, nacionalidade);
    novoVisitante->idade = idade;

    // Inicializa o ponteiro 'proximo' como NULL (será ajustado na inserção)
    novoVisitante->proximo = NULL;

    // Retorna o ponteiro para o novo visitante criado
    return novoVisitante;
}

// Função para inserir um visitante no final da lista circular
void inserirVisitante(struct Lista *lista, char nome[], char nacionalidade[], int idade) {
    // Cria um novo visitante utilizando a função 'criarVisitante'
    struct Visitante *novoVisitante = criarVisitante(nome, nacionalidade, idade);

    // Caso a lista esteja vazia
    if (lista->inicio == NULL) {
        lista->inicio = novoVisitante;   // Define o novo visitante como o primeiro da lista
        lista->fim = novoVisitante;      // Define o novo visitante também como o último
        novoVisitante->proximo = lista->inicio;  // O único visitante aponta para si mesmo (circularidade)
    } else {
        lista->fim->proximo = novoVisitante;     // O visitante atual do fim aponta para o novo visitante
        novoVisitante->proximo = lista->inicio;  // O novo visitante aponta para o início da lista, mantendo a circularidade
        lista->fim = novoVisitante;      // Atualiza o ponteiro de fim para o novo visitante
    }

    // Incrementa o tamanho da lista
    lista->tamanho++;
}

// Função de busca recursiva para encontrar um visitante
struct Visitante *buscarVisitanteRecursivo(struct Visitante *atual, struct Visitante *inicio, char nome[]) {
    
    if (strcmp(atual->nome, nome) == 0) {  // Compara os nomes corretamente
        return atual;
    }
    if (atual->proximo == inicio) {  // Se chegou de volta ao início e não encontrou
        return NULL;
    }
    return buscarVisitanteRecursivo(atual->proximo, inicio, nome);  // Continua a busca
}

// Função para exibir todos os visitantes da lista circular
void exibirVisitantes(struct Lista *lista) {
    // Verifica se a lista está vazia
    if (lista->inicio == NULL) {
        printf("A lista de visitantes está vazia.\n");
        return;
    }

    struct Visitante *temp = lista->inicio;  // Inicializa o ponteiro temporário com o início da lista

    // Percorre a lista circular e exibe as informações de cada visitante
    do {
        printf("Nome: %s, Nacionalidade: %s, Idade: %d\n", temp->nome, temp->nacionalidade, temp->idade);
        temp = temp->proximo;  // Avança para o próximo visitante
    } while (temp != lista->inicio);  // Continua até alcançar o primeiro visitante novamente
}

// Função para remover um visitante da lista circular com base no nome
void removerVisitante(struct Lista *lista, char nome[]) {
    // Verifica se a lista está vazia
    if (lista->inicio == NULL) {
        printf("A lista de visitantes está vazia.\n");
        return;
    }

    struct Visitante *atual = lista->inicio;  // Ponteiro para o visitante atual (começa do início)

    // Usa a função recursiva para buscar o visitante
    struct Visitante *visitanteBuscado = buscarVisitanteRecursivo(atual, lista->inicio, nome);

    // Verifica se o visitante foi encontrado
    if (visitanteBuscado == NULL) {
        printf("Visitante não encontrado.\n");
        return;
    }

    // Caso especial: se o visitante a ser removido for o primeiro (início)
    if (visitanteBuscado == lista->inicio) {
        if (lista->inicio == lista->fim) {  // Caso haja apenas um visitante na lista
            free(visitanteBuscado);         // Libera a memória do único visitante
            lista->inicio = NULL;           // Define o início como NULL (lista vazia)
            lista->fim = NULL;              // Define o fim como NULL (lista vazia)
        } else {
            lista->fim->proximo = visitanteBuscado->proximo;  // O último visitante aponta para o segundo visitante
            lista->inicio = visitanteBuscado->proximo;        // O segundo visitante se torna o novo início
            free(visitanteBuscado);                           // Libera a memória do primeiro visitante
        }
        lista->tamanho--;  // Diminui o tamanho da lista
        return;
    }

    // Se o visitante não for o primeiro, percorremos a lista para encontrar o anterior
    struct Visitante *anterior = atual;
    while (anterior->proximo != visitanteBuscado) {
        anterior = anterior->proximo;  // Atualiza o ponteiro anterior
    }

    // Remove o visitante encontrado
    anterior->proximo = visitanteBuscado->proximo;  // Liga o anterior ao próximo
    if (visitanteBuscado == lista->fim) {           // Se for o último visitante
        lista->fim = anterior;                      // Atualiza o ponteiro de fim
    }
    free(visitanteBuscado);  // Libera a memória do visitante removido
    lista->tamanho--;        // Diminui o tamanho da lista
}

int contarVisitantes(struct Lista *lista) {
    return lista->tamanho;
}

int verificarVisitante(struct Lista *lista, char nome[]) {
    // Verifica se a lista está vazia
    if (lista->inicio == NULL) {
        printf("A lista de visitantes está vazia.\n");
        return 0;  // Visitante não encontrado
    }

    // Usa a função recursiva para buscar o visitante
    struct Visitante *visitanteBuscado = buscarVisitanteRecursivo(lista->inicio, lista->inicio, nome);

    // Se o visitante não foi encontrado, retorna 0
    if (visitanteBuscado == NULL) {
        return 1;  // Visitante não encontrado
    }

    // Se o visitante foi encontrado, retorna 1
    return 2;  // Visitante encontrado
}


int main() {
    struct Lista listaDeVisitantes; // Declaração da lista
    inicializarLista(&listaDeVisitantes); // Inicializa a lista circular

    inserirVisitante(&listaDeVisitantes, "Vitor de Medeiros", "Brasileiro", 21);
    inserirVisitante(&listaDeVisitantes, "Juliano Ratusznei", "Alemão", 35);
    inserirVisitante(&listaDeVisitantes, "Rodinei", "Canadense", 25);
    
    int opcao;
    char nome[MAX_LENGTH];
    char nacionalidade[MAX_LENGTH];
    int idade;
    
    do{
        printf("\nMenu:\n");
        printf("1 - Inserir visitante\n");
        printf("2 - Exibir visitantes\n");
        printf("3 - Remover visitante\n");
        printf("4 - Total de visitantes\n");
        printf("5 - Verificar se está na lista\n");
        printf("0 - Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                printf("Digite o nome do visitante: ");
                scanf("%s", nome);
                printf("Digite a nacionalidade do visitante: ");
                scanf("%s", nacionalidade);
                printf("Digite a idade do visitante: ");
                scanf("%d", &idade);
                inserirVisitante(&listaDeVisitantes, nome, nacionalidade, idade);
                printf("\n\nVisitante inserido com sucesso!\n");
                
                break;
            case 2:
                printf("\nVisitantes:\n");
                exibirVisitantes(&listaDeVisitantes);
                break;
            case 3:
                printf("Digite o nome do visitante a ser removido: ");
                scanf("%s", nome);
                removerVisitante(&listaDeVisitantes, nome);
                printf("Este visitante foi removido com sucesso!\n");
                break;
            case 4:
                printf("Total de visitantes: %d\n", contarVisitantes(&listaDeVisitantes));
                break;
            case 5: {
                // Caso 5: Verificar se o visitante está na lista
                printf("Digite o nome do visitante que deseja verificar: \n");
                scanf("%s", nome);

                // Usa a função verificarVisitante
                int encontrado = verificarVisitante(&listaDeVisitantes, nome);

                if (encontrado == 2) {
                    printf("Visitante %s está na lista.\n", nome);
                } else if (encontrado == 1) {
                    printf("Visitante (%s) não foi encontrado na lista.\n", nome);
                }
                break;
            }
            
            case 0:
                printf("Encerrando o programa.\n");
                break;
            default:
                    printf("Opção inválida. Tente novamente.\n");
                    break;
            
        }
    }while(opcao != 0);
        
    
        
    return 0;
}
