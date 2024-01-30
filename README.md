# Obmep

Scrapy crawler dedicado à raspagem de dados sobre premiações concedidas na **Olimpíada Brasileira de Matemática das Escolas Públicas (OBMEP)**, disponíveis em https://www.obmep.org.br/premiados.htm.

Este projeto visa coletar dados referentes aos alunos, professores, escolas e secretarias da educação premiados, proporcionando uma visão abrangente e organizada dos desempenhos na olimpíada. A iniciativa oferece uma valiosa fonte de informações para análises estatísticas, pesquisas educacionais e insights relacionados ao sucesso na OBMEP.

## Instalação

O código fonte está hospedado no GitHub em: https://github.com/brenner-santos/obmep

O scrapy crawler é desenvolvido em [Python](https://docs.python.org/3/) (3.10+).

Com o [Poetry](https://python-poetry.org/) instalado em sua máquina, utilize o comando a seguir em um terminal aberto na raiz do repositório para preparam o ambiente virtual de Python:

```
poetry install --only-root
```

A lista de alterações entre cada versão pode ser encontrada [aqui](CHANGELOG.md).

## Como executar

Para experimentar a execução de um raspador já integrado ao projeto, siga os comandos no diretório raiz do repositório:

1. Ative o ambiente virtual: 
```
poetry shell
``` 
2. Verifique a lista de raspadores disponíveis:
```
scrapy list
```
3. Execute um raspador da lista:
```
scrapy crawl <nome_do_raspador>       // exemplo: scrapy crawl 2005-city
```
4. Os dados coletados na raspagem serão salvos no arquivo `obmep.db`

## Contribuição

Obrigado por se interessar em considerar contribuir com o projeto!

Você encontra como fazê-lo no [CONTRIBUTING.md](./CONTRIBUTING.md)!

Além disso, consulte a [documentação do Obmep](./docs/index.md) para te ajudar. 

## Suporte

Se você estiver tendo problemas, dúvidas ou necessita de ajuda sobre os projetos, me notifique por meio dessa [lista de discussão](https://github.com/brenner-santos/obmep/issues).

## Licença

Código licenciado sob a [Licença MIT](./LICENSE).