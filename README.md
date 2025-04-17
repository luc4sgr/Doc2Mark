<p align="center">
  <img src="https://github.com/user-attachments/assets/7d9b9968-2a13-4a0f-88d9-2fc8caeaade3" alt="Convert Doc to Markdown API" />
</p>

Uma API desenvolvida em **Python** para converter documentos (como PDF, DOCX, TXT, etc) em Markdown utilizando a biblioteca **Docling**. A aplicação é construída com **Flask** e organizada em arquitetura limpa, separando responsabilidades em camadas como controller, view, validador e tratamento de erro.

---

## 🚀 Funcionalidades

- **Conversão de documentos para Markdown**: Suporta múltiplos formatos e retorna o conteúdo convertido.
- **Upload de arquivos**: Aceita envio via `multipart/form-data`.
- **Validação de entrada**: Garante que o campo `source` seja um arquivo válido.
- **Tratamento de erros centralizado** com mensagens amigáveis via camada `error_handler`.

---

## 📁 Estrutura do Projeto

```plaintext
src/
├── controllers/      # Lógica de negócios (use case)
├── errors/           # Tratamento de exceções
├── main/             # Rotas e servidor Flask
├── validators/       # Validação de entrada com Cerberus
├── views/            # Camada de interface HTTP (adapters)
run.py                # Ponto de entrada da aplicação
requirements.txt      # Dependências do projeto
Dockerfile            # Configuração do container Docker
docker-compose.yml    # Gerenciamento simplificado de container
📦 Requisitos
Python 3.12 ou superior

Docker (opcional para containerizar)

Bibliotecas do requirements.txt

⚙️ Instalação
bash
Copiar
Editar
# 1. Clone o repositório
git clone <URL_DO_REPOSITORIO>
cd convert_mk_docling

# 2. Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate     # Linux/macOS
# ou no Windows:
.venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt
🐳 Com Docker
bash
Copiar
Editar
# Build da imagem
docker build -t seu_usuario/convert-markdown-api .

# Rodar localmente
docker run -p 3000:3000 seu_usuario/convert-markdown-api
Ou usando Docker Compose:

bash
Copiar
Editar
docker-compose up --build
▶️ Uso
1. Inicie o servidor
bash
Copiar
Editar
python run.py
2. Faça uma requisição POST para /convert_document
Tipo: multipart/form-data

Campo: source com o arquivo a ser convertido

Exemplo via Postman:
Método: POST

URL: http://localhost:3000/convert_document

Body (form-data):
source → arquivo .pdf, .docx, etc

3. Resposta:
json
Copiar
Editar
{
  "data": {
    "type": "Markdown Document",
    "filename": "arquivo.pdf",
    "markdown": "### Document Content\n..."
  }
}
✅ Testes
bash
Copiar
Editar
pytest
📄 Licença
Este projeto está licenciado sob a MIT License.

javascript
Copiar
Editar

Se quiser, posso gerar esse `.md` como um download ou como conteúdo Docker Hub também. Deseja?# Doc2Mark
