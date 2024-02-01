# Contribuindo para o Projeto

Todas as contribuições, relatos, correções de bugs, melhorias na documentação e ideias de funcionalidades são muito bem-vindas.

## Relatos de Bugs e Solicitações de Melhorias

Os relatos de bugs e solicitações de melhorias desempenham um papel crucial para tornar este projeto mais estável e são organizados por meio das [issues no Github](https://github.com/brenner-santos/obmep/issues). Ao relatar um problema ou fazer uma solicitação, por favor, escolha a [categoria apropriada e preencha completamente o formulário](https://github.com/brenner-santos/obmep/issues/new/choose) para garantir que outros colaboradores e a equipe de desenvolvimento compreendam totalmente o escopo do desafio.

A issue ficará visível para a comunidade, permitindo comentários e ideias de outros colaboradores. Juntos, podemos fazer deste projeto algo ainda melhor!

## Encontrar uma Issue para Contribuir

Recomendamos pesquisar a guia [issues do GitHub](https://github.com/brenner-santos/obmep/issues) para encontrar uma issue que lhe interesse.

Ao encontrar um problema interessante, é uma boa ideia atribuir a issue a si mesmo, assim ninguém mais duplica o trabalho. Para fazer isso, deixe um comentário na issue escrito `take` para se atribuir automaticamente.

Se, por qualquer motivo, você não puder continuar trabalhando no problema, por favor, cancele a atribuição para que outras pessoas saibam que ele está disponível novamente. Verifique a lista de issues atribuídas, pois algumas podem não estar mais sendo trabalhadas. Se você deseja assumir uma issue já atribuída, sinta-se à vontade para perguntar gentilmente ao colaborador atual se você pode assumi-la (por favor, aguarde pelo menos uma semana de inatividade antes de considerar o trabalho na questão descontinuado).

Estamos felizes em recebê-lo e apoiá-lo enquanto você se familiariza com a forma como trabalhamos e onde as coisas estão. Dê uma olhada nas próximas seções para saber mais.

## Enviando um Pull Request
### Controle de Versão, Git e GitHub

O projeto está hospedado no [GitHub](https://www.github.com/brenner-santos/obmep/), e para contribuir, será necessário se inscrever para uma [conta gratuita no GitHub](https://github.com/signup/free). Utilizamos o [Git](https://git-scm.com/) para controle de versão, permitindo que várias pessoas trabalhem juntas no projeto.

Além disso, o projeto segue um fluxo de trabalho de bifurcação (forking), onde os colaboradores criam um fork do repositório, realizam alterações e, em seguida, criam um pull request. Portanto, certifique-se de ler e seguir todas as instruções deste guia.

Abaixo estão alguns recursos úteis para aprender mais sobre bifurcação (forking) e pull requests no GitHub:

- Documentação do GitHub sobre [criação de fork de um repositório](https://docs.github.com/pt/get-started/quickstart/fork-a-repo).

- Documentação do GitHub sobre [colaboração com pull requests](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests).

- Documentação do GitHub sobre [trabalho com forks](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/working-with-forks).

### Iniciando com o Git

O GitHub fornece [instruções](https://docs.github.com/en/get-started/quickstart/set-up-git) para instalar o Git, configurar sua chave SSH e realizar as configurações necessárias. Certifique-se de completar essas etapas antes de começar a trabalhar entre seu repositório local e o GitHub.

### Criar um Fork do Projeto

Para contribuir, é necessário ter uma cópia do projeto (fork) em seu perfil. Acesse a [página do projeto](https://github.com/brenner-santos/obmep/) e clique em `Fork`. Desmarque a opção para copiar apenas o ramo principal antes de selecionar `Create Fork`. Clone o seu fork para a sua máquina com os comandos abaixo:

```bash
git clone https://github.com/seu-usuario/obmep.git obmep-seunome
cd obmep-seunome
git remote add upstream https://github.com/brenner-santos/obmep.git
git fetch upstream
```

Isso cria o diretório `obmep-seunome` e conecta seu repositório ao repositório do projeto principal.

### Criando um Ambiente de Desenvolvimento

Os raspadores são desenvolvidos utilizando [Python](https://docs.python.org/3/) (3.10+) e o framework [Scrapy](https://scrapy.org/) gerenciado pelo [Poetry](https://python-poetry.org/).

1. **Instalando o Python e Poetry:**
   O método de instalação dependerá do seu sistema operacional. Consulte [como instalar o Python](https://www.python.org/downloads/) e [como instalar o Poetry](https://python-poetry.org/docs/). Se você optar por usar o Docker na próxima etapa, poderá pular esta etapa.

2. **Criando um ambiente virtual e instalando dependências:**
   Se estiver utilizando o Poetry, execute:

    ```bash
    poetry install
    poetry run pre-commit install
    ```

    Utilizando o Docker:
    No diretório raiz, existe um Dockerfile para construir uma imagem Docker com um ambiente de desenvolvimento completo do projeto. Execute:

    ```bash
    docker build -t obmep-dev .
    docker run -it --rm -v ${PWD}:/home/obmep obmep-dev
    poetry install
    poetry run pre-commit install
    ```

> [!NOTE]
> Ainda mais fácil, você pode integrar o Docker com o **Visual Studio Code**:
>
> Você pode usar o DockerFile para iniciar uma sessão remota com o Visual Studio Code, usando o arquivo .devcontainer.json. Consulte https://code.visualstudio.com/docs/remote/containers para obter detalhes.

### Atualizando o Ambiente de Desenvolvimento

É fundamental atualizar periodicamente sua branch local `main` com as atualizações da branch `main` do projeto e ajustar seu ambiente de desenvolvimento para refletir quaisquer alterações nos diversos pacotes usados durante o desenvolvimento. Execute o seguinte comando:

```bash
git checkout main
git fetch upstream
git merge upstream/main
poetry update
poetry run pre-commit install
```

Se houver conflitos, será necessário resolver esses conflitos. Consulte, por exemplo, a documentação do GitHub sobre [resolvendo um conflito de merge usando linha de comando](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/) para obter uma explicação sobre como fazer isso.

### Criando uma Feacture Branch

Sua branch local `main` deve sempre refletir o estado atual do repositório do projeto principal. Primeiro, certifique-se de que está atualizado com o repositório principal.

```bash
git checkout main
git pull upstream main --ff-only
```

Em seguida, crie um feature branch para fazer suas alterações. Por exemplo:

```bash
git checkout -b nova-funcionalidade-incrivel
```

Isso altera sua branch de trabalho de `main` para o branch `nova-funcionalidade-incrivel`. Mantenha quaisquer alterações neste branch específicas para um único bug ou funcionalidade, para que fique claro o que o branch traz para o projeto. Você pode ter vários branches de funcionalidade e alternar entre eles usando o comando `git checkout`.

### Fazendo um Pull Request

Assim que você terminar suas alterações de código, suas mudanças precisarão seguir as diretrizes de contribuição do projeto para serem aceitas com sucesso.

Se tudo estiver correto, você estará pronto para fazer um pull request. Um pull request é como o código do seu repositório local fica disponível para a comunidade do GitHub revisar e ser mesclado no projeto para aparecer na próxima versão. Para enviar um pull request, siga estas etapas:

1. Acesse o seu repositório no GitHub.

2. Clique no botão `Compare & pull request`.

3. Você pode então clicar em `Commits` e `Files Changed` para garantir que tudo pareça correto pela última vez.

4. Escreva um título descritivo que inclua prefixos com ou sem escopo. O projeto baseia-se na convenção do (Conventional Commits)[https://www.conventionalcommits.org/pt-br/v1.0.0/] para os títulos do Pull Request, seguindo a estrutura `<tipo>[escopo opcional]: <descrição>`. O escopo deve ser o nome do arquivo ou módulo Python afetado. Aqui estão alguns tipos junto com diretrizes gerais para quando usá-los:

   - `build`: alterações que afetam o sistema de compilação ou dependências externas
   - `ci`: alterações em nossos arquivos de configuração de CI e scripts
   - `docs`: adições e atualizações na documentação
   - `feat`: nova funcionalidade ou aprimoramento de uma existente
   - `fix`: correção de bug
   - `perf`: alteração de código que melhora o desempenho
   - `refactor`: alteração de código que não corrige um bug nem adiciona um recurso
   - `style`: alterações que não afetam o significado do código
   - `test`: adicionando testes ausentes ou corrigindo testes existentes

5. Escreva uma descrição das suas alterações na aba `Preview Discussion`, seguindo o [template](./.github/pull_request_template.md).

6. Clique em `Send Pull Request`.

Essa solicitação será enviada para os mantenedores do repositório, e eles irão revisar o código.

### Atualizando seu Pull Request

Com base na revisão que você receber no seu pull request, será provavelmente necessário realizar algumas alterações no código. Além disso, é crucial garantir que as atualizações na branch `main` do projeto estejam refletidas no seu pull request. Certifique-se de seguir a seção [Atualizando o Ambiente de Desenvolvimento](#atualizando-o-ambiente-de-desenvolvimento) para realizar essas atualizações.

Depois de ter atualizado localmente o branch de funcionalidade, você pode agora sincronizar o seu pull request, fazendo push para o branch correspondente no GitHub:

```bash
git push origin nova-funcionalidade-incrivel
```

Qualquer git push automaticamente atualizará o seu pull request com as alterações do seu branch e reiniciará as verificações de Integração Contínua.

## Dicas para um Pull Request de Sucesso

Se você chegou à fase de [fazer um pull request](#Fazendo-um-Pull-Request), um dos mantenedores pode avaliar suas alterações. No entanto, é importante observar que apenas um grupo reduzido de pessoas é responsável por revisar todas as contribuições, o que pode resultar em possíveis gargalos.

Para aumentar as chances de revisão e aceitação do seu pull request, considere as seguintes dicas:

- **Referencie uma issue aberta** para mudanças não triviais, proporcionando contexto e esclarecendo o propósito do PR.

- **Mantenha seus pull requests o mais simples possível**, priorizando a clareza e facilitando o processo de revisão.

- **Certifique-se de que a integração contínua (CI) está em um estado verde**, indicando que todas as verificações automatizadas foram concluídas com sucesso.

- **[Atualize continuamente seu pull request](#atualizando-seu-pull-request)**, seja em resposta a solicitações de revisão ou regularmente a cada poucos dias