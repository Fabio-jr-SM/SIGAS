# Documentação

## Guia para Contribuidores - Projeto Integrador Cyber Edux

### Introdução
O projeto integrador é uma parte crucial do curso de Capacitação em Python oferecido pela Cyber Edux. Este guia destina-se a fornecer orientações claras para os desenvolvedores que desejam contribuir para o projeto. A contribuição é uma excelente oportunidade para aplicar os conhecimentos adquiridos durante o curso e desenvolver habilidades práticas em programação.

### Como Contribuir
1. **Familiarize-se com o Projeto**: Leia cuidadosamente o código existente e entenda a estrutura e a lógica do projeto.
2. **Crie um Fork do Repositório**: Faça uma cópia do repositório para sua conta do GitHub.
3. **Desenvolva sua Solução**: Implemente a funcionalidade desejada ou corrija o problema escolhido.
4. **Mantenha a Documentação Atualizada**: Se necessário, atualize a documentação para refletir as alterações feitas.
5. **Envie um Pull Request**: Submeta suas alterações como um Pull Request para revisão. Certifique-se de incluir uma descrição clara das alterações realizadas.

### Diretrizes de Código
- Siga as convenções de codificação Python PEP8.
- Mantenha o código limpo e legível.
- Utilize comentários adequados para explicar trechos de código complexos.
- Evite duplicação de código e siga os princípios do DRY (Don't Repeat Yourself).
- Faça testes unitários para garantir a funcionalidade correta das novas implementações.

### Recursos Adicionais
- Para obter mais informações sobre como contribuir para projetos Django, consulte a documentação oficial do Django: [link](https://docs.djangoproject.com/en/stable/internals/contributing/)
- Para aprender mais sobre boas práticas de contribuição para projetos de código aberto, confira o guia Open Source Guides: [link](https://opensource.guide/how-to-contribute/)
- Para sugestões ou dúvidas sobre o projeto, entre em contato com os mantenedores do repositório.

### Depuração do Projeto

Para garantir o bom funcionamento e desenvolvimento eficiente do projeto, é importante entender como depurar e executar o sistema localmente. Siga os passos abaixo para configurar e executar o projeto:

#### Configuração Inicial

1. **Instalação de Bibliotecas**:
   - Abra o terminal e instale as seguintes bibliotecas utilizando o pip:
     ```
     pip install django-role-permissions python-decouple
     ```

2. **Configurações do Arquivo .env**:
   - Na pasta raiz do projeto, crie um arquivo chamado `.env`.
   - Adicione as seguintes configurações ao arquivo `.env`:
     ```
     EMAIL_HOST_USER=email
     EMAIL_HOST_PASSWORD=password
     EMAIL_USE_TLS=True
     EMAIL_PORT=587  # Caso esteja usando Gmail
     EMAIL_HOST=smtp.gmail.com  # Caso esteja usando Gmail
     ```

#### Executando o Projeto

1. **Inicialização do Servidor de Desenvolvimento**:
   - No terminal, navegue até a pasta raiz do projeto.
   - Execute o seguinte comando para iniciar o servidor de desenvolvimento do Django:
     ```
     python manage.py runserver
     ```
   - O servidor será iniciado e você poderá acessar o projeto em http://localhost:8000/.

2. **Acessando a Interface Administrativa**:
   - Após iniciar o servidor, acesse http://localhost:8000/admin/ para acessar a interface administrativa do Django.
   - Você pode fazer login utilizando as credenciais de superusuário configuradas anteriormente.

#### Depuração e Testes

1. **Depuração de Código**:
   - Utilize ferramentas de depuração do Python, como pdb ou o depurador integrado em IDEs como o VSCode, para identificar e corrigir problemas no código.

2. **Testando Funcionalidades**:
   - Certifique-se de testar todas as funcionalidades do projeto após fazer alterações significativas.
   - Crie testes unitários utilizando o framework de testes do Django para garantir o funcionamento correto das novas implementações.

3. **Logging de Erros**:
   - Utilize a funcionalidade de logging do Django para registrar erros e informações úteis durante a execução do projeto.
   - Analise os logs regularmente para identificar e resolver problemas.

#### Contribuindo com o Projeto

Ao contribuir com o projeto, siga as diretrizes de contribuição fornecidas anteriormente. Certifique-se de testar suas alterações localmente antes de enviar um Pull Request para revisão. Comunique-se com os mantenedores do projeto caso tenha dúvidas ou sugestões.

Agora você está pronto para depurar e desenvolver o Projeto Integrador Cyber Edux! Se tiver alguma dúvida durante o processo, não hesite em entrar em contato com a equipe responsável.

## Modelagem de banco de dados
O projeto utiliza um banco de dados para armazenar informações sobre pessoas, cursos, disciplinas, alunos, professores, inscrições em disciplinas, registros de aulas, registros de faltas, registros de atividades e notas.

### Modelos de Dados

Aqui estão os modelos de dados definidos no projeto:

- **Pessoa**: Armazena informações sobre pessoas, como nome completo, data de nascimento e matrícula. Cada pessoa também está associada a um usuário do sistema.

- **Curso**: Representa um curso oferecido, com nome e duração.

- **Disciplina**: Descreve uma disciplina em um curso, com nome, turno e curso associado.

- **Aluno**: Relaciona uma pessoa como aluno do sistema, com informações como data de ingresso, situação acadêmica e disciplinas cursadas.

- **Professor**: Associa uma pessoa como professor do sistema, com data de admissão, turno e remuneração.

- **InscriçãoDisciplina**: Relaciona uma disciplina a um professor, indicando que o professor está lecionando essa disciplina.

- **RegistroAula**: Registra informações sobre as aulas, como horário, descrição e disciplina associada.

- **RegistroFalta**: Registra a quantidade de faltas de um aluno em uma aula específica.

- **RegistroAtividade**: Descreve as atividades realizadas durante uma aula, vinculada ao registro da aula.

- **Notas**: Armazena as notas dos alunos em atividades específicas.

### Observações

- O projeto utiliza o sistema de autenticação do Django para gerenciar usuários e permissões.
- Os campos de data e hora utilizam a biblioteca `datetime` para fornecer informações precisas.
- A configuração de email é feita através de um arquivo `.env` na pasta raiz do projeto.

Para executar o projeto localmente e interagir com o banco de dados, siga as instruções no [Guia de Desenvolvimento](guia_desenvolvimento.md).

---

<img src="/img/bancoDadosLogico.png">

Agradecemos antecipadamente por sua contribuição para o Projeto Integrador Cyber Edux. Sua participação é fundamental para o sucesso contínuo deste projeto.
