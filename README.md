# Doc2Mark 📄➡️📝
🇧🇷 [Leia em português](./README.pt-br.md)

A powerful Python API for converting various document formats (PDF, DOCX, TXT, etc.) to clean Markdown. Built with Flask and Docling library using a clean architecture approach.


[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)


![image](https://github.com/user-attachments/assets/03fea66f-0e06-48e4-8e04-e6261e216b4c)

### ✨ Features

- **Multi-format Support**: Convert PDF, DOCX, TXT and other document formats to clean Markdown
- **RESTful API**: Simple HTTP interface for document conversion
- **Clean Architecture**: Well-organized code with separation of concerns (controllers, views, validators)
- **Robust Error Handling**: Friendly, informative error messages
- **Docker Support**: Easy deployment with containerization
- **Input Validation**: Ensures proper file formats and parameters

### 🏗️ Architecture

The project follows clean architecture principles with clear separation of concerns:

```
src/
├── controllers/      # Business logic implementation
├── errors/           # Centralized error handling
├── main/             # Flask server and routing configuration
├── validators/       # Input validation using Cerberus
└── views/            # HTTP interface adapters
```

### 🔧 Requirements

- Python 3.12+
- Flask
- Docling
- Other dependencies in `requirements.txt`
- Docker (optional)

### 🚀 Installation

#### Standard Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/doc2mark.git
cd doc2mark

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
```

#### Docker Installation

```bash
# Build and run with Docker
docker build -t doc2mark .
docker run -p 3000:3000 doc2mark
```

Or using Docker Compose:

```bash
docker-compose up --build
```

### 📝 Usage

#### API Endpoint

**Convert Document to Markdown**

- **URL**: `/convert_document`
- **Method**: `POST`
- **Content-Type**: `multipart/form-data`
- **Request Body**:
  - `source`: The document file to convert

#### Example Request

Using cURL:

```bash
curl -X POST \
  -F "source=@/path/to/your/document.pdf" \
  http://localhost:3000/convert_document
```

Using Python requests:

```python
import requests

url = "http://localhost:3000/convert_document"
files = {"source": open("document.pdf", "rb")}

response = requests.post(url, files=files)
print(response.json())
```

#### Example Response

```json
{
  "data": {
    "type": "Markdown Document",
    "filename": "document.pdf",
    "markdown": "# Document Title\n\n## Section 1\n\nContent of the document..."
  }
}
```

### ⚙️ Configuration

Environment variables can be set in a `.env` file:

```
PORT=3000
DEBUG=True
```

### 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src
```

### 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 📚 Additional Documentation

For more detailed information about the API and its components, check the [wiki](https://github.com/yourusername/doc2mark/wiki) section.

---

<a name="português"></a>
## Português

Uma poderosa API em Python para converter vários formatos de documentos (PDF, DOCX, TXT, etc.) para Markdown limpo. Construída com Flask e a biblioteca Docling usando uma abordagem de arquitetura limpa.

[![Versão Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Licença](https://img.shields.io/badge/licença-MIT-green.svg)](LICENSE)

### ✨ Funcionalidades

- **Suporte Multi-formato**: Converte PDF, DOCX, TXT e outros formatos de documentos para Markdown limpo
- **API RESTful**: Interface HTTP simples para conversão de documentos
- **Arquitetura Limpa**: Código bem organizado com separação de responsabilidades (controllers, views, validators)
- **Tratamento Robusto de Erros**: Mensagens de erro amigáveis e informativas
- **Suporte Docker**: Implantação fácil com containerização
- **Validação de Entrada**: Garante formatos de arquivo e parâmetros adequados

### 🏗️ Arquitetura

O projeto segue princípios de arquitetura limpa com clara separação de responsabilidades:

```
src/
├── controllers/      # Implementação da lógica de negócios
├── errors/           # Tratamento centralizado de erros
├── main/             # Servidor Flask e configuração de rotas
├── validators/       # Validação de entrada usando Cerberus
└── views/            # Adaptadores de interface HTTP
```

### 🔧 Requisitos

- Python 3.12+
- Flask
- Docling
- Outras dependências em `requirements.txt`
- Docker (opcional)

### 🚀 Instalação

#### Instalação Padrão

```bash
# Clone o repositório
git clone https://github.com/seuusuario/doc2mark.git
cd doc2mark

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python run.py
```

#### Instalação com Docker

```bash
# Construa e execute com Docker
docker build -t doc2mark .
docker run -p 3000:3000 doc2mark
```

Ou usando Docker Compose:

```bash
docker-compose up --build
```

### 📝 Uso

#### Endpoint da API

**Converter Documento para Markdown**

- **URL**: `/convert_document`
- **Método**: `POST`
- **Content-Type**: `multipart/form-data`
- **Corpo da Requisição**:
  - `source`: O arquivo de documento a ser convertido

#### Exemplo de Requisição

Usando cURL:

```bash
curl -X POST \
  -F "source=@/caminho/para/seu/documento.pdf" \
  http://localhost:3000/convert_document
```

Usando Python requests:

```python
import requests

url = "http://localhost:3000/convert_document"
files = {"source": open("documento.pdf", "rb")}

resposta = requests.post(url, files=files)
print(resposta.json())
```

#### Exemplo de Resposta

```json
{
  "data": {
    "type": "Markdown Document",
    "filename": "documento.pdf",
    "markdown": "# Título do Documento\n\n## Seção 1\n\nConteúdo do documento..."
  }
}
```

### ⚙️ Configuração

Variáveis de ambiente podem ser definidas em um arquivo `.env`:

```
PORT=3000
DEBUG=True
```

### 🧪 Testes

```bash
# Execute todos os testes
pytest

# Execute com relatório de cobertura
pytest --cov=src
```
