# Doc2Mark 📄➡️📝
EN [Read in English](./README.md)

Uma poderosa API em Python para converter vários formatos de documentos (PDF, DOCX, TXT, etc.) para Markdown limpo. Construída com Flask e a biblioteca Docling usando uma abordagem de arquitetura limpa.

[![Versão Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

![image](https://github.com/user-attachments/assets/03fea66f-0e06-48e4-8e04-e6261e216b4c)

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

### 🤝 Contribuindo

1. Faça um fork do repositório
2. Crie sua branch de recurso (`git checkout -b recurso/funcionalidade-incrivel`)
3. Faça commit de suas alterações (`git commit -m 'Adiciona funcionalidade incrível'`)
4. Faça push para a branch (`git push origin recurso/funcionalidade-incrivel`)
5. Abra um Pull Request

### 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

### 📚 Documentação Adicional

Para informações mais detalhadas sobre a API e seus componentes, consulte a seção [wiki](https://github.com/seuusuario/doc2mark/wiki).
