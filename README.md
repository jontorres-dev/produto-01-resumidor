# resumidor

CLI em Python que resume um texto em no máximo 3 frases.

## Requisitos

- Python 3.10 ou superior

## Ambiente virtual

Na raiz do projeto:

```bash
python -m venv .venv
```

Ative o ambiente:

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD)**

```cmd
.venv\Scripts\activate.bat
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

Dependências (nenhuma por enquanto):

```bash
pip install -r requirements.txt
```

## Como rodar

Passe o texto como argumento:

```bash
python main.py "A reunião durou duas horas. O time alinhou o escopo. O prazo ficou para sexta. Detalhes extras foram adiados."
```

Ou envie pelo stdin:

```bash
echo "Primeira frase. Segunda frase. Terceira frase. Quarta frase." | python main.py
```

O resultado é o texto limitado às 3 primeiras frases.
# resumidor
# produto-01-resumidor
