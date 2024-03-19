# producer
Golden Raspberry Awards API
Esta aplicação Flask fornece uma API RESTful para explorar os vencedores da categoria Pior Filme do Golden Raspberry Awards. Ela lê dados de um arquivo CSV, armazena-os em um banco de dados SQLite em memória e calcula os produtores com o maior e o menor intervalo entre vitórias consecutivas.

Características
Carga de dados do arquivo CSV para o SQLite em memória ao iniciar a aplicação.
API RESTful para consultar o produtor com o maior intervalo entre dois prêmios consecutivos e o que obteve dois prêmios mais rápido.
Pré-requisitos
Python 3.6+
Flask
Pandas
Como Configurar
Clone este repositório para a sua máquina local.
Crie um ambiente virtual:

python3 -m venv venv

Ative o ambiente virtual:
No Windows: venv\Scripts\activate
No Linux ou macOS: source venv/bin/activate
Instale as dependências necessárias:

pip install Flask pandas

Como Executar
Na raiz do projeto, execute o aplicativo Flask:

python app.py

A aplicação estará disponível em http://localhost:5000/.
Endpoints da API
/load-data: Carrega os dados do arquivo CSV para o banco de dados em memória.
/producers: Retorna o produtor com o maior e o menor intervalo entre prêmios consecutivos.
Testes
Este projeto inclui testes de integração que garantem a funcionalidade dos endpoints e a precisão dos cálculos realizados pela API. Para executar os testes, utilize o seguinte comando:

python -m unittest

Contribuindo
Contribuições para o projeto são bem-vindas. Sinta-se livre para clonar, enviar PRs ou abrir issues.