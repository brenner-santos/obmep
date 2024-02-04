## v0.2.0 (2024-02-04)

### Feat

- **spiders**: adiciona os raspadores da edição OBMEP 2010 (#16)
- adiociona novos campos e modifica o schema dos itens
- **resources**: adiciona arquivos states.csv e school_types.csv
- **spiders**: adiciona raspadores da edição OBMEP 2009 (#15)
- **spiders**: adicionar raspadores da edição OBMEP 2008
- adiciona os raspadores para a edicao OBMEP 2007
- cria extensao para monitorar as estatisticas das execucoes dos spiders
- adiciona os raspadores da edicao OBMEP 2006
- cria arquivo de listagem das edicoes
- adiciona pipelines de tratamento de dados
- cria atributo created_at nas tabelas
- define o schema das tabelas do banco de dados
- definindo os scrapy itens e aplicando aos raspadores
- adiciona raspadores da edicao OBMEP 2005

### Fix

- busca todas as tabelas da página

### Refactor

- renomeia modulos
- ajusta nomes de classes e códigos de edições
- simplifica os nomes das classes de acordo com codigo da edicao
- renomeia classe dos raspadores e itens

### Perf

- altera o formato de carregamento padrão de SQLite para Json
