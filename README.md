## Performante test com Locust e RabbitMQ
Neste repositório contém a classe RabbitMQClient responsável por gerenciar as conexões e as indexações no RabbitMQ, um cenário de teste e duas suites, sendo uma configurada para rampup e outra suite para smoke test, ambas com com comandos configurados no Makefile.

## Dependências
Para execução do projeto precisamos de:
* RabbitMQ: Precisamos de uma RabbitMQ configurado, no meu caso utilizo um container docker para subir o RabbitMQ
	* https://medium.com/xp-inc/rabbitmq-com-docker-conhecendo-o-admin-cc81f3f6ac3b
* Python: https://python.org.br/instalacao-linux/
* Locust: https://docs.locust.io/en/0.12.2/index.html
* Poetry: https://pypi.org/project/poetry/
* Pika: https://pypi.org/project/pika/
* Makefile: https://www.gnu.org/software/make/manual/make.html

### Instalação
Para realizar a preparação do projeto e instação das dependencias execute os comandos abaixo:
```shell
make prepare
```
```shell
make install
```
```shell
pip install pika
```

### Execução
Para executar o teste de performance execute os seguintes comandos:

#### Smoke Test
```shell
make run-smoke-test
```

#### Rampup Test
```shell
make run-test
```