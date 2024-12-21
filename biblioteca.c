#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LENGTH 100 


// criar struct ==> sobre o que vai ser armazenado (Livro + array de livros))
struct Livro {
  char titulo[MAX_LENGTH];
  char autor[MAX_LENGTH];
  int ano;
  struct Livro *proximo;
};

struct Estudante {
  char nome[MAX_LENGTH];
  char curso[MAX_LENGTH];
  int RGM;
  int nivel;
  struct Livro emprestimo;  // Adicionado o membro livro 
  struct Estudante *proximo;
};

/*
 add herança de struct --> referenciar livro ao estudante
 */

struct Fila_Emprestimo {
  struct Estudante *estudantes; 
  int inicio, fim, tamanho;
  int capacidade;
};


struct ListaLigadaEstudante {
  struct Estudante *elemento;
  int tamanho;
};

struct ListaLigadaLivro {
  struct Livro *elemento;
  int tamanho;
};

void inicializarEstudante(struct ListaLigadaEstudante *lista) {
  lista->elemento = NULL;
  lista->tamanho = 0;
};

void inicializarLivro(struct ListaLigadaLivro *lista) {
  lista->elemento = NULL;
  lista->tamanho = 0;
};

int inicializarFila(struct Fila_Emprestimo *fila) {
  fila->inicio = 0;
  fila->fim = -1;
  fila->tamanho = 0;
  fila->capacidade = 1;  // Capacidade inicial
  fila->estudantes = (struct Estudante *)malloc(fila->capacidade * sizeof(struct Estudante));
  if (fila->estudantes == NULL) {
    printf("Erro de alocação de memória.\n");
    return -1;
  }
  return 0;
}

void inserir_final_Estudante(struct ListaLigadaEstudante *lista, const char *nome, const char *curso, int RGM, int nivel) {

  struct Estudante *novo = (struct Estudante *)malloc(sizeof(struct Estudante));

  if (novo == NULL) {
    printf("Erro na alocação de memória.\n");
    return;
  }
  strcpy(novo->nome, nome);
  strcpy(novo->curso, curso);
  novo->RGM = RGM;
  novo->nivel = nivel;
  novo->proximo = NULL;
  
  if (lista->elemento == NULL) {
    lista->elemento = novo;

  } else {
    struct Estudante *atual = lista->elemento;
    while (atual->proximo != NULL) {
      atual = atual->proximo;
    }

    atual->proximo = novo;
  }

  lista->tamanho++;
}

void exibirEstudante(struct ListaLigadaEstudante *lista) {
  printf("\nLista de Estudantes:\n");
  struct Estudante *atual = lista->elemento;
  while (atual != NULL) {
    printf("Nome: %s", atual->nome);
    printf(" | Curso: %s", atual->curso);
    printf(" | RGM: %d", atual->RGM);
    printf(" | Nivel: %s", atual->nivel == 0 ? "Usuário" : "Administrador\n");
    printf(" | Livro Emprestado: %s", atual->emprestimo.titulo);
    printf(" | Autor: %s", atual->emprestimo.autor);
    printf(" | Ano de lançamento: %d\n\n", atual->emprestimo.ano);
    atual = atual->proximo;
  }
}

int buscarIntEstudantePorRGM(struct ListaLigadaEstudante *lista, int rgm) {
    struct Estudante *atual = lista->elemento;
    int posicao = 0;

    while (atual != NULL && atual->RGM != rgm) {
        atual = atual->proximo;
        posicao++;
    }

    if (atual != NULL) {
        printf("\nEstudante com RGM %d encontrado na posição %d\n", atual->RGM, posicao);
        return atual->RGM;
    } else {
        printf("\nPoxa!!!  ≡(▔﹏▔)≡ \nEstudante com RGM %d não encontrado\n", rgm);
        return -1;
    }
}

int buscarEstudante(struct ListaLigadaEstudante *lista, const char *nome) {
  struct Estudante *atual = lista->elemento;
  int posicao = 0;

  while (atual != NULL && strcmp(atual->nome, nome) != 0) {
    atual = atual->proximo;
    posicao++;
  }
  if (atual != NULL) {
    printf("\nUsuário %s encontrado na posição %d\n", atual->nome, posicao);
    return posicao;
  } else {
    return -1;
  }
}

struct Estudante *buscarEstudantePorRGM(struct ListaLigadaEstudante *lista, int rgmEstudante) {
    struct Estudante *atual = lista->elemento;
    int posicao = 0;

    while (atual != NULL) {
        if (atual->RGM == rgmEstudante) {
            printf("\nEstudante com RGM %d encontrado na posição %d\n", atual->RGM, posicao);
            return atual;
        }
        posicao++;
        atual = atual->proximo;
    }

    printf("\nPoxa!!!  ≡(▔﹏▔)≡ \nEstudante com RGM %d não encontrado\n", rgmEstudante);
    return NULL; // Retorna NULL se o estudante não for encontrado
}


struct Estudante *buscarEstudantePorNome(struct ListaLigadaEstudante *lista, const char *nomeEstudante) {
    struct Estudante *atual = lista->elemento;
    int posicao = 0;
    while (atual != NULL) {
      
      if (strcmp(atual->nome, nomeEstudante) == 0) {
          printf("\nEstudante %s encontrado na posição %d\n", atual->nome, posicao);
          return atual;
        }
      posicao++;
      atual = atual->proximo;
    }
    printf("\nPoxa!!!  ≡(▔﹏▔)≡ \nEstudante %s não encontrado\n", nomeEstudante);
    return NULL; // Retorna NULL se o estudante não for encontrado
}


struct ListaLigadaEstudante *remover_estudante(struct ListaLigadaEstudante *lista, int RGM) {
  struct Estudante *atual = lista->elemento;
  struct Estudante *anterior = NULL;
  // Verifica se a lista está vazia
  if (atual == NULL) {
    printf("\nA lista está vazia.\n");
    return lista;
  }
  // Verifica se o primeiro livro da lista é o que queremos remover
  if (atual->RGM == RGM) {
    lista->elemento = atual->proximo; // Remove o primeiro livro
    printf("\nAluno %s removido.\n", atual->nome);
    free(atual); // Libera a memória do livro removido
    return lista;
  }
  // Percorre a lista para encontrar o livro a ser removido
  while (atual != NULL && atual->RGM != RGM) {
    anterior = atual;
    atual = atual->proximo;
  }
  // Se o livro foi encontrado, remove-o da lista
  if (atual != NULL) {
    anterior->proximo = atual->proximo; // Conecta o livro anterior ao próximo
    printf("\nAluno %s removido.\n", atual->nome);
    free(atual); // Libera a memória do livro removido
  } else {
    printf("\nEstudante %s, não encontrado na lista.\n", atual->nome);
  }
  return lista;
}

void selectionSort_Estudante(struct ListaLigadaEstudante *lista) {
  struct Estudante *atual, *menor, *proximo;
  char temp_nome[MAX_LENGTH], temp_curso[MAX_LENGTH];
  int tem_RGM, tem_nivel;

  atual = lista->elemento;
  while (atual != NULL) {
    menor = atual;
    proximo = atual->proximo;

    while (proximo != NULL) {
      if (strcmp(proximo->nome, menor->nome) < 0) {
        menor = proximo;
      }
      proximo = proximo->proximo;
    }

    // Troca os elementos
    strcpy(temp_nome, atual->nome);
    strcpy(temp_curso, atual->curso);
    tem_RGM = atual->RGM;
    tem_nivel = atual->nivel;
    strcpy(atual->nome, menor->nome);
    strcpy(atual->curso, menor->curso);
    atual->RGM = menor->RGM;
    atual->nivel = menor->nivel;
    strcpy(menor->nome, temp_nome);
    strcpy(menor->curso, temp_curso);
    menor->RGM = tem_RGM;
    menor->nivel = tem_nivel;

    atual = atual->proximo;
  }
}

void liberarListaEstudante(struct ListaLigadaEstudante *lista) {
  struct Estudante *atual = lista->elemento;
  while (atual != NULL) {
    struct Estudante *proximo = atual->proximo;
    free(atual);
    atual = proximo;
  }

  lista->elemento = NULL;
  lista->tamanho = 0;
}

void inserirLivroPorNome(struct Estudante *estudante, struct Livro *novoLivro) {
    // Copia os dados do novo livro para o campo emprestimo do estudante
    strcpy(estudante->emprestimo.titulo, novoLivro->titulo);
    strcpy(estudante->emprestimo.autor, novoLivro->autor);
    estudante->emprestimo.ano = novoLivro->ano;
    estudante->emprestimo.proximo = NULL;
}

void inserir_final_Livro(struct ListaLigadaLivro *lista, const char *titulo, const char *autor, int ano) {

  struct Livro *novo = (struct Livro *)malloc(sizeof(struct Livro));

  if (novo == NULL) {
    printf("Erro na alocação de memória.\n");
    return;
  }
  strcpy(novo->titulo, titulo);
  strcpy(novo->autor, autor);
  novo->ano = ano;
  novo->proximo = NULL;

  if (lista->elemento == NULL) {
    lista->elemento = novo;

  } else {
    struct Livro *atual = lista->elemento;
    while (atual->proximo != NULL) {
      atual = atual->proximo;
    }
    atual->proximo = novo;
  }
  lista->tamanho++;
}



void exibirLivro(struct ListaLigadaLivro *lista) {
  printf("\nLista de Livro:\n");
  struct Livro *atual = lista->elemento;
  while (atual != NULL) {
    printf(" | Livro Emprestado: %s", atual->titulo);
    printf(" | Autor: %s", atual->autor);
    printf(" | Ano de lançamento: %d\n\n", atual->ano);
    atual = atual->proximo;
  }
}


struct Livro *buscarLivroPorTitulo(struct ListaLigadaLivro *lista, const char *titulo) {
  struct Livro *atual = lista->elemento;
  int posicao = 0;

  while (atual != NULL && strcmp(atual->titulo, titulo) != 0) {
    atual = atual->proximo;
    posicao++;
  }
  if (atual != NULL) {
    printf("\nLivro, %s, encontrado na %d° posição\n", atual->titulo, posicao);
    return atual;
  } else {
    printf("\nPoxa!!!  ≡(▔﹏▔)≡ \n\nEstudante %s não encontrado", titulo);
    return NULL;
  }
}

struct ListaLigadaLivro *remover_livro(struct ListaLigadaLivro *lista,
                                       const char *titulo) {
  struct Livro *atual = lista->elemento;
  struct Livro *anterior = NULL;

  // Verifica se a lista está vazia
  if (atual == NULL) {
    printf("A lista está vazia.\n");
    return lista;
  }

  // Verifica se o primeiro livro da lista é o que queremos remover
  if (strcmp(atual->titulo, titulo) == 0) {
    lista->elemento = atual->proximo; // Remove o primeiro livro
    free(atual);                      // Libera a memória do livro removido
    printf("\nLivro \"%s\" removido.\n", titulo);
    return lista;
  }

  // Percorre a lista para encontrar o livro a ser removido
  while (atual != NULL && strcmp(atual->titulo, titulo) != 0) {
    anterior = atual;
    atual = atual->proximo;
  }

  // Se o livro foi encontrado, remove-o da lista
  if (atual != NULL) {
    anterior->proximo = atual->proximo; // Conecta o livro anterior ao próximo
    free(atual);                        // Libera a memória do livro removido
    printf("\nLivro \"%s\" removido.\n", titulo);
  } else {
    printf("\nLivro \"%s\" não encontrado na lista.\n", titulo);
  }

  return lista;
}


void liberarListaLivro(struct ListaLigadaLivro *lista) {
  struct Livro *atual = lista->elemento;
  while (atual != NULL) {
    struct Livro *proximo = atual->proximo;
    free(atual);
    atual = proximo;
  }

  lista->elemento = NULL;
  lista->tamanho = 0;
}


void selectionSort_Livro(struct ListaLigadaLivro *lista) {
  struct Livro *atual, *menor, *proximo;
  char temp_titulo[MAX_LENGTH], temp_autor[MAX_LENGTH];
  int tem_ano;

  atual = lista->elemento;
  while (atual != NULL) {
    menor = atual;
    proximo = atual->proximo;

    while (proximo != NULL) {
      if (strcmp(proximo->titulo, menor->titulo) < 0) {
        menor = proximo;
      }
      proximo = proximo->proximo;
    }

    // Troca os elementos
    strcpy(temp_titulo, atual->titulo);
    strcpy(temp_autor, atual->autor);
    tem_ano = atual->ano;
    strcpy(atual->titulo, menor->titulo);
    strcpy(atual->autor, menor->autor);
    atual->ano = menor->ano;
    strcpy(menor->titulo, temp_titulo);
    strcpy(menor->autor, temp_autor);
    menor->ano = tem_ano;

    atual = atual->proximo;
  }
}

int estaVazia(struct Fila_Emprestimo *fila) {
  return fila->tamanho == 0;
}

int redimensionarFila(struct Fila_Emprestimo *fila) {
  // Dobrar a capacidade
  int novaCapacidade = fila->capacidade * 2; 
  struct Estudante *novoArray = (struct Estudante *)realloc(fila->estudantes, 
    novaCapacidade * sizeof(struct Estudante));
  if (novoArray == NULL) {
    printf("Erro de realocação de memória.\n");
    return -1;
  }
  fila->estudantes = novoArray;
  fila->capacidade = novaCapacidade;
  return 0; // Redimensionamento bem-sucedido
}

void enqueue(struct Fila_Emprestimo *fila, struct Estudante *estudante) {
    if (fila->tamanho == fila->capacidade) {
        if (redimensionarFila(fila) == -1) {
            return; // Saia da função se houver erro de redimensionamento
        }
    }
    if (fila->tamanho == 0) {
        strcpy(fila->estudantes[fila->inicio].nome, estudante->nome);
        strcpy(fila->estudantes[fila->inicio].curso, estudante->curso);
        fila->estudantes[fila->inicio].RGM = estudante->RGM;
        fila->estudantes[fila->inicio].nivel = estudante->nivel;

        fila->fim = (fila->fim + 1) % fila->capacidade;
        fila->tamanho++;
    }
    // Copia as informações do estudante para a fila
    strcpy(fila->estudantes[fila->fim].nome, estudante->nome);
    strcpy(fila->estudantes[fila->fim].curso, estudante->curso);
    fila->estudantes[fila->fim].RGM = estudante->RGM;
    fila->estudantes[fila->fim].nivel = estudante->nivel;

    fila->fim = (fila->fim + 1) % fila->capacidade;
    fila->tamanho++;
}




int dequeue(struct Fila_Emprestimo *fila) {
  if (estaVazia(fila)) {
    printf("Erro: Fila vazia.\n");
    return -1;
  }
  int valor = fila->estudantes[fila->inicio].RGM;
  fila->inicio = (fila->inicio + 1) % fila->capacidade;
  fila->tamanho--;
  return valor;
}

int peek(struct Fila_Emprestimo *fila) {
  if (estaVazia(fila)) {
    printf("Erro: Fila vazia.\n");
    return -1;
  }
  struct Estudante *estudante = &fila->estudantes[fila->inicio];
  if (estudante == NULL) {
    printf("Erro: Ponteiro de estudante inválido.\n");
    return -1;
  }
  int valor = estudante->RGM;
  printf("O primeiro da fila é: %s\n", estudante->nome);
  return valor;
}

void liberarFila(struct Fila_Emprestimo *fila) {
  free(fila->estudantes);
  fila->tamanho = 0;
  fila->capacidade = 0;
  fila->inicio = 0;
  fila->fim = -1;
}



  int main() {
      struct ListaLigadaEstudante lista_estudantes;
      inicializarEstudante(&lista_estudantes);

      struct ListaLigadaLivro lista_livros;
      inicializarLivro(&lista_livros);

      struct Fila_Emprestimo fila;
      inicializarFila(&fila);

      int option, opcao;
      char nome[MAX_LENGTH], curso[MAX_LENGTH];
      int RGM, ano;
      char titulo[MAX_LENGTH], autor[MAX_LENGTH];
      bool executando = true;

      while (executando) {
          printf("\n==== Mundo dos Livros ====\n");
          printf("0. SAIR\n");
          printf("1. ENTRAR\n");
          printf("2. CADASTRAR\n");
          printf("Escolha uma opção: ");
          scanf("%d", &option);

          switch (option) {
              case 0:
                  executando = false;
                  break;
              case 1: {
                  printf("\n==== Mundo dos Livros ====\n");
                  printf("Nome: ");
                  getchar();
                  fgets(nome, MAX_LENGTH, stdin);
                  printf("RGM: ");
                  scanf("%d", &RGM);
                  int nivel = buscarEstudante(&lista_estudantes, nome); // Esta função deve retornar o nível do estudante ou -1 se não encontrado

                  if (nivel == 0) {
                      do {
                          printf("\nMenu:\n");
                          printf("1. Inserir Estudante\n");
                          printf("2. Inserir Livro\n");
                          printf("3. Exibir Estudantes\n");
                          printf("4. Exibir Livros\n");
                          printf("5. Buscar Estudante\n");
                          printf("6. Buscar Livro\n");
                          printf("7. Remover Estudante\n");
                          printf("8. Remover Livro\n");
                          printf("9. Ordenar Estudante\n");
                          printf("10. Ordenar Livro\n");
                          printf("11. Enqueue (Adicionar Estudante na Fila)\n");
                          printf("12. Dequeue (Remover Estudante da Fila)\n");
                          printf("13. Peek (Verificar primeiro da Fila)\n");
                          printf("14. Liberar Fila\n");
                          printf("0. Sair\n");
                          printf("Escolha uma opção: ");
                          scanf("%d", &opcao);

                          switch (opcao) {
                              case 0:
                                  printf("\nLogoff realizado\n");
                                  break;
                              case 1: {
                                  printf("Nome: ");
                                  getchar();
                                  fgets(nome, MAX_LENGTH, stdin);
                                  printf("Curso: ");
                                  fgets(curso, MAX_LENGTH, stdin);
                                  printf("RGM: ");
                                  scanf("%d", &RGM);
                                  printf("0. Administrador  1. Usuário\nSelecione: ");
                                  scanf("%d", &nivel);
                                  inserir_final_Estudante(&lista_estudantes, nome, curso, RGM, nivel);
                                  break;
                              }
                              case 2: {
                                  printf("Título: ");
                                  getchar();
                                  fgets(titulo, MAX_LENGTH, stdin);
                                  printf("Autor: ");
                                  fgets(autor, MAX_LENGTH, stdin);
                                  printf("Ano de lançamento: ");
                                  scanf("%d", &ano);
                                  inserir_final_Livro(&lista_livros, titulo, autor, ano);
                                  break;
                              }
                              case 3:
                                  exibirEstudante(&lista_estudantes);
                                  break;
                              case 4:
                                  exibirLivro(&lista_livros);
                                  break;
                              case 5: {
                                  printf("Digite o nome do estudante a ser buscado: ");
                                  getchar();
                                  fgets(nome, MAX_LENGTH, stdin);
                                  buscarEstudantePorNome(&lista_estudantes, nome);
                                  break;
                              }
                              case 6: {
                                  printf("Digite o título do livro a ser buscado: ");
                                  getchar();
                                  fgets(titulo, MAX_LENGTH, stdin);
                                  buscarLivroPorTitulo(&lista_livros, titulo);
                                  break;
                              }
                              case 7: {
                                  printf("Digite o RGM do estudante a ser removido: ");
                                  scanf("%d", &RGM);
                                  remover_estudante(&lista_estudantes, RGM);
                                  break;
                              }
                              case 8: {
                                  printf("Digite o título do livro a ser removido: ");
                                  getchar();
                                  fgets(titulo, MAX_LENGTH, stdin);
                                  remover_livro(&lista_livros, titulo);
                                  break;
                              }
                              case 9:
                                  selectionSort_Estudante(&lista_estudantes);
                                  printf("Estudantes ordenados por nome.\n");
                                  break;
                              case 10:
                                  selectionSort_Livro(&lista_livros);
                                  printf("Livros ordenados por título.\n");
                                  break;
                              case 11: {
                                  char nomeEstudante[MAX_LENGTH], tituloLivro[MAX_LENGTH];
                                  printf("Digite o nome do estudante para fazer o empréstimo: ");
                                  getchar();
                                  fgets(nomeEstudante, MAX_LENGTH, stdin);
                                  printf("Digite o título do livro a ser emprestado: ");
                                  fgets(tituloLivro, MAX_LENGTH, stdin);
                                  struct Livro* livro = buscarLivroPorTitulo(&lista_livros, tituloLivro);
                                  if (livro == NULL) {
                                      printf("Livro com o título '%s' não encontrado.\n", tituloLivro);
                                      break;
                                  }

                                  struct Estudante* estudante = buscarEstudantePorNome(&lista_estudantes, nomeEstudante);
                                  if (estudante == NULL) {
                                      printf("Estudante com o nome '%s' não encontrado.\n", nomeEstudante);
                                      break;
                                  }
                                  inserirLivroPorNome(estudante, livro);
                                  enqueue(&fila, estudante);
                                  printf("\nLivro emprestado com sucesso.\n");
                                  break;
                              }
                              case 12:
                                  dequeue(&fila);
                                  break;
                              case 13:
                                  peek(&fila);
                                  break;
                              case 14:
                                  liberarFila(&fila);
                                  printf("Fila liberada.\n");
                                  break;
                              default:
                                  printf("Opção inválida. Tente novamente.\n");
                                  break;
                          }

                      } while (opcao != 0);

                  } else if (nivel == 1) {
                      // Código do menu para usuários...
                      do {
                          printf("\nMenu:\n");
                          printf("1. Exibir Livros\n");
                          printf("2. Buscar Livro\n");
                          printf("3. Entrar na fila de Empréstimo\n");
                          printf("4. Fazer Emprestimo\n");
                          printf("5. Ordenar Livros\n");
                          printf("6. Verificar primeiro da fila\n");
                          printf("0. Sair\n");
                          printf("Escolha uma opção: ");
                          scanf("%d", &opcao);

                          switch (opcao) {
                              case 0:
                                  printf("\nLogoff realizado\n");
                                  break;
                              case 1:
                                  exibirLivro(&lista_livros);
                                  break;
                              case 2: {
                                  printf("Digite o título do livro a ser buscado: ");
                                  getchar();
                                  fgets(titulo, MAX_LENGTH, stdin);
                                  buscarLivroPorTitulo(&lista_livros, titulo);
                                  break;
                              }
                              case 3: {
                                  char nomeEstudante[MAX_LENGTH];
                                  printf("Digite seu nome completo: ");
                                  getchar();
                                  fgets(nomeEstudante, MAX_LENGTH, stdin);
                                  struct Estudante* estudante = buscarEstudantePorNome(&lista_estudantes, nomeEstudante);
                                  if (estudante == NULL) {
                                      printf("Estudante com o nome '%s' não encontrado.\n", nomeEstudante);
                                      break;
                                  }
                                  enqueue(&fila, estudante);
                                  printf("\nVocê entrou na fila de empréstimo, aguarde seu momento de empréstimo.\n");
                                  break;
                              }
                              case 4: {
                                  int confirmacao = 0;
                                  char nomeEstudante[MAX_LENGTH], tituloLivro[MAX_LENGTH];

                                  while (confirmacao != 1) {
                                      int RGM, primeiro_fila;
                                      printf("Digite seu RGM:");
                                      scanf("%d", &RGM);
                                      primeiro_fila = peek(&fila);

                                      if (RGM == primeiro_fila) {
                                          printf("Você está no primeiro da fila\n");
                                          confirmacao = 1;
                                      } else {
                                          printf("Você não está no primeiro da fila\n");
                                          confirmacao = 0;
                                          break;
                                      }
                                  }
                                  if (confirmacao == 1) {
                                      printf("Digite o título do livro a ser emprestado: ");
                                      getchar();
                                      fgets(tituloLivro, MAX_LENGTH, stdin);
                                      struct Livro* livro = buscarLivroPorTitulo(&lista_livros, tituloLivro);
                                      if (livro == NULL) {
                                          printf("Livro com o título '%s' não encontrado.\n", tituloLivro);
                                          confirmacao = 0;
                                          dequeue(&fila);
                                          break;
                                      } else {
                                          printf("Digite seu nome: ");
                                          getchar();
                                          fgets(nomeEstudante, MAX_LENGTH, stdin);
                                          struct Estudante* estudante = buscarEstudantePorRGM(&lista_estudantes, RGM);
                                          if (estudante == NULL) {
                                              printf("\nEstudante não encontrado.\n");
                                              confirmacao = 0;
                                              break;
                                          }
                                          inserirLivroPorNome(estudante, livro);
                                          dequeue(&fila);
                                          printf("\nLivro emprestado com sucesso.\n");
                                          break;
                                      }
                                  }
                              }
                              case 5:
                                  selectionSort_Livro(&lista_livros);
                                  printf("Livros ordenados por título.\n");
                                  break;
                              case 6:
                                  peek(&fila);
                                  break;
                              default:
                                  printf("Opção inválida. Tente novamente.\n");
                                  break;
                          }
                      } while (opcao != 0);
                  } else {
                      printf("Usuário não encontrado.\n");
                  }
                  break;
              }
              case 2: {
                  printf("Nome: ");
                  getchar();
                  fgets(nome, MAX_LENGTH, stdin);
                  printf("Curso: ");
                  fgets(curso, MAX_LENGTH, stdin);
                  printf("RGM: ");
                  scanf("%d", &RGM);
                  printf("0. Usuário  1. Administrador\nSelecione: ");
                  int nivel;
                  scanf("%d", &nivel);
                  inserir_final_Estudante(&lista_estudantes, nome, curso, RGM, nivel);
                  break;
              }
              default:
                  printf("Opção inválida. Tente novamente.\n");
                  continue;
          }
      }

      liberarListaEstudante(&lista_estudantes);
      liberarListaLivro(&lista_livros);

      return 0;
  }
