# Helena-IA

Assistente virtual de estudos para programadores, construída com **Python + Flask** e integrada ao **Google Gemini (google-generativeai)**.

> **Importante (segurança):** este repositório contém uma **chave de API exposta no código**. Remova/rotacione essa chave imediatamente e use variáveis de ambiente (veja a seção **Segurança**).

## Visão geral

O projeto sobe uma aplicação Flask com uma interface web (templates HTML) e uma API (Blueprint) para enviar perguntas de texto e também perguntas acompanhadas de arquivos (código, PDF e documentos Office).

Rotas principais (frontend):
- `GET /` → `templates/chat.html`
- `GET /code` → `templates/code.html`
- `GET /pdf` → `templates/pdf.html`
- `GET /office/<type>` → páginas em `templates/office/`

Rotas de API (Blueprint `question_bp`, prefixo `/question`):
- `POST /question/text` → pergunta apenas em texto
- `POST /question/codeFile` → pergunta + upload de arquivo de código
- `POST /question/pdfFile` → pergunta + upload de PDF
- `POST /question/office/<type>` → pergunta + upload de arquivo Office (`word`, `excel`, `powerpoint`)

## Tags

`python` `flask` `gemini` `google-generativeai` `ai-assistant` `chatbot` `pdf` `docx` `pptx` `xlsx` `upload` `jinja2`

## Estrutura do projeto (alto nível)

- `app.py` — inicializa o Flask e registra o Blueprint `question_bp`.
- `question.py` — endpoints da API para perguntas e upload de arquivos.
- `Class/Genai.py` — classe `GenerativeAI` que integra com o Gemini e faz leitura de arquivos (PDF, DOCX, XLSX, PPTX e texto).
- `templates/` — páginas HTML (chat, code, pdf, office).
- `static/` — assets estáticos (CSS etc.).

> Observação: há pastas `venv/` e `__pycache__/` versionadas no repositório. Em geral, é recomendado removê-las do Git e colocar no `.gitignore`.

## Requisitos

- Python 3.12 (recomendado, pois o repositório contém `venv/lib/python3.12/...`)
- Dependências em `requirements.txt` (inclui `Flask` e `google-generativeai`)

## Como rodar (dev)

1) Clone o repositório e entre na pasta:

```bash
git clone https://github.com/mr-body/Helena-IA.git
cd Helena-IA
```

2) Crie e ative um ambiente virtual:

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3) Instale as dependências:

```bash
pip install -r requirements.txt
```

4) Configure a chave de API (recomendado):

- Crie a variável de ambiente `GEMINI_API_KEY`.

```bash
# Linux/Mac
export GEMINI_API_KEY="sua_chave_aqui"

# Windows (PowerShell)
$env:GEMINI_API_KEY="sua_chave_aqui"
```

5) Rode o servidor:

```bash
python app.py
```

A aplicação sobe em modo debug (conforme `app.run(debug=True)`).

## Segurança (faça isso antes de publicar)

- **Rotacione a chave do Gemini imediatamente** (a chave aparece hardcoded em `question.py`).
- Troque a criação do cliente para usar variável de ambiente, por exemplo:
  - `GenerativeAI(os.getenv("GEMINI_API_KEY"))`
- Adicione no `.gitignore`:
  - `.venv/` (ou `venv/`)
  - `__pycache__/`
  - `static/upload/` (arquivos enviados pelo usuário)
  - `.env`

## API – exemplos de uso

### Pergunta em texto

`POST /question/text` com JSON:

```json
{ "text": "Explique o que é Flask" }
```

Resposta:

```json
{ "response": "..." }
```

### Pergunta + arquivo (código/PDF/Office)

Os endpoints recebem `multipart/form-data` com:
- campo `text`: a pergunta
- campo `file`: arquivo

Exemplo (cURL) para código:

```bash
curl -X POST http://127.0.0.1:5000/question/codeFile \
  -F "text=Analise este arquivo" \
  -F "file=@meu_codigo.py"
```

## Limitações / melhorias sugeridas

- Evitar commitar `venv/` e `__pycache__/`.
- Melhorar o tratamento de uploads (validação de extensão/tamanho, nomes seguros, etc.).
- `question.py` cria um `Flask(__name__)` separado (além do app principal) apenas para acessar `static_folder`; dá para simplificar usando `current_app`.
- Em `Class/Genai.py`, existem funções de upload para o Gemini que parecem não ser usadas no fluxo atual (dá para limpar/refatorar).

## Licença

Não definida. Se quiser, adicione um arquivo `LICENSE` (MIT, Apache-2.0, GPL etc.).
