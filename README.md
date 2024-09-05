Estudo de python através da criação de uma simples API backend.

Possui virtualização com as configurações utilizadas para a criação e execução da aplicação.

Dentro de um CMD (shell) no diretório do projeto, foram utilizados os seguintes comandos:

Criação do Ambiente Virtual:
- Comando: "python -m venv venv"
- Possui o nome de venv

Ativação do Ambiente Virtual no Windows:
- Comando: "venv\Scripts\activate.bat"
- É esperado que apareça "(venv)" ao lado do diretório no CMD.

Ativação do Ambiente Virtual no Linux/Mac:
- Comando: "source venv/bin/activate"
- É esperado que apareça "(venv)" ao lado do diretório no CMD.

Desativação do Ambiente Virtual no Windows/Linux/Mac:
- Comando: "deactivate"
- É esperado que seja removido o "(venv)" ao lado do diretório no shell.

É utilizado o pip (gerenciador de módulos e pacotes) para instalação de pacotes.

É utilizado o pacote "requests" para a aplicação poder realizar requests:
- Comando: "pip install requests"
- - Para remover: "pip uninstall requests"
- - Se atentar que são instalados outros pacotes para que o requests funcione. eles também precisam ser desinstalados.

É utilizado o pacote "fast api" para criação de endpoints na aplicação:
- Comando: "pip install fastapi"
- - Para remover: "pip uninstall fastapi"
- - Se atentar que são instalados outros pacotes para que o requests funcione. eles também precisam ser desinstalados.

É utilizado o pacote "uvicorn" para o servidor:
- Comando: "pip install uvicorn"
- É utilizado internamente pelo FastAPI

Para listar todos os pacotes instalados:
- Comando: "pip freeze"

Foi criado um arquivo com todos os requerimnentos de libs para executar a aplicação:
- Comando: "pip freeze > requirements.txt"