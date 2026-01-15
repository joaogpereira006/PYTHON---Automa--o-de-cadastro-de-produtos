# Automação de Cadastro de Produtos com Python 🤖

Projeto prático desenvolvido para automatizar o fluxo de leitura e inserção de dados em um sistema ERP web, eliminando o trabalho manual e reduzindo erros de digitação.

## 📝 Sobre o Projeto
Este projeto foi realizado como um exercício prático durante uma live da **Hashtag Treinamentos**. A automação simula o comportamento humano para realizar o login em uma plataforma, percorrer uma base de dados e cadastrar centenas de produtos de forma autônoma.

## 🛠️ Tecnologias e Bibliotecas
* **Python**: Linguagem principal.
* **Pandas**: Utilizado para a manipulação de dados e leitura do arquivo `.csv`.
* **PyAutoGUI**: Responsável pela automação da interface gráfica (cliques, digitação e navegação).
* **Time**: Utilizado para gerenciar pausas estratégicas, garantindo que o código acompanhe o tempo de carregamento do navegador.

## 🚀 Funcionalidades
1.  **Acesso ao Sistema:** Abre o navegador Chrome e acessa a URL específica.
2.  **Autenticação:** Realiza o login automático com usuário e senha na plataforma.
3.  **Processamento de Dados:** Lê uma base de dados externa (CSV) contendo informações como Código, Marca, Tipo, Categoria e Preço.
4.  **Loop de Cadastro:** Preenche automaticamente cada campo do formulário para cada linha da planilha.
5.  **Envio de Dados:** Confirma o cadastro e reinicia o processo para o próximo item.

## ⚠️ Observação Técnica
Este script utiliza coordenadas de tela baseadas na resolução do meu monitor. Para rodar em outras máquinas, é necessário ajustar os pontos de clique ou utilizar o modo de busca por imagem do PyAutoGUI.


https://github.com/user-attachments/assets/e16b0717-ba90-443b-87e6-13f407c3b254



























