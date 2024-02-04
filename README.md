# Obmep

Scrapy crawler dedicado à raspagem de dados sobre premiações concedidas na **Olimpíada Brasileira de Matemática das Escolas Públicas (OBMEP)**, disponíveis em https://www.obmep.org.br/premiados.htm.

Este projeto visa coletar dados referentes aos alunos, professores, escolas e secretarias da educação premiados, proporcionando uma visão abrangente e organizada dos desempenhos na olimpíada. A iniciativa oferece uma valiosa fonte de informações para análises estatísticas, pesquisas educacionais e insights relacionados ao sucesso na OBMEP.

## Instalação

O código fonte está hospedado no GitHub em: https://github.com/brenner-santos/obmep

Os raspadores são desenvolvido em [Python](https://docs.python.org/3/) (3.10+).

Com o [Poetry](https://python-poetry.org/) instalado em sua máquina, utilize o comando a seguir em um terminal aberto na raiz do repositório para preparam o ambiente virtual de Python:

```bash
poetry install --only main
```

A lista de alterações entre cada versão pode ser encontrada [aqui](CHANGELOG.md).

## Como executar

Para experimentar a execução de um raspador já integrado ao projeto, siga os comandos no diretório raiz do repositório:

1. Ative o ambiente virtual: 

```bash
poetry shell
``` 

2. Verifique a lista de raspadores disponíveis:

```bash
scrapy list
```

3. Execute um raspador da lista:

```bash
scrapy crawl <nome_do_raspador>       # exemplo: scrapy crawl obmep2005-city
```

4. Os dados coletados na raspagem serão salvos por padrão na pasta `data` no formato `.json`. No arquivo `obmep.db` você pode ter informações estatísticas das execuções dos raspadores.

### Dicas de execução

Os nomes dos raspadores seguem a estrutura `<codigo da edicao>-<tabela>`. 

O `<codigo da edicao>` refere-se ao código identificador único de uma edição específica da OBMEP. Você pode encontrar a lista desses códigos no arquivo [editions.csv](./obmep/resources/editions.csv).

A `<tabela>` indica a categoria de premiados da OBMEP. Existem quatro categorias disponíveis:

- `city`: Tabela referente as secretarias de educação premiadas.
- `school`: Tabela referente as escolas premiadas.
- `student`: Tabela referente aos estudantes premiados.
- `teacher`: Tabela referente aos professores premiados.

É possível combinar comandos que o Scrapy oferece para facilitar o coleta de dados.

- Coleta completa de uma edição

    Para coletar todos os dados de uma edição específica, execute o seguinte comando, substituindo `<codigo da edicao>` pelo código da edição (por exemplo, `obmep2005`):

    ```bash
    scrapy list | grep '^<codigo da edicao>' | xargs -n 1 scrapy crawl
    ```

- Coleta completa de uma tabela
    
    Para coletar todas as premiações de uma tabela específica, execute o seguinte comando, substituindo `<tabela>` pelo nome da tabela (por exemplo, `city`):

    ```bash
    scrapy list | grep '<tabela>$' | xargs -n 1 scrapy crawl
    ```

Além dos comandos acima, o Scrapy oferece outros recursos para configurar o comando de raspagem. Para mais informações acesse [a documentação](https://docs.scrapy.org/en/latest/topics/commands.html#crawl).

## Contribuição

Todas as contribuições, relatos e correções de bugs, melhorias na documentação, melhorias e ideias de funcionalidades são bem-vindas.

Uma visão geral detalhada sobre como contribuir pode ser encontrada em [CONTRIBUTING.md](./CONTRIBUTING.md).

Como colaboradores e mantenedores deste projeto, espera-se que você cumpra o código de conduta. Mais informações podem ser encontradas em: [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

## Suporte

Se você estiver tendo problemas, dúvidas ou necessita de ajuda sobre os projetos, me notifique por meio dessa [lista de discussão](https://github.com/brenner-santos/obmep/issues).

## Licença

Código licenciado sob a [Licença MIT](./LICENSE).