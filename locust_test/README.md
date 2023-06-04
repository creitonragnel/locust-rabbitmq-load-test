## Performance Test com Locust e RabbitMQ

Esse repositório contém uma classe RabbitMQClient que gerencia conexões e publicações no RabbitMQ, um cenário de teste com o propósito de publicar mensagens no RabbitMQ e duas suites, sendo uma suite com controlador de rampa de teste e um smoke test.

Nesse projeto, utilizo RabbitMQ em um container Docker. As instruções podem ser encontradas em: 
* https://medium.com/xp-inc/rabbitmq-com-docker-conhecendo-o-admin-cc81f3f6ac3b

## Instalação

Para instalação utilize os comandos prepare e install contidos no Makefile
```shell
make prepare
```
```shell
make install
```

E finalize instalando a lib do pika
```shell
pip install pika
```

## Execução
Para execução, utilizo Makefile para automatizar as execuções. Utilizo o Poetry para gerenciamento de dependências e Locust para execução e gerenciamento do teste.

#### Executar smoke test
```shell
make run-smoke-test
```

#### Executar test com rampup
```shell
make run-test
```

## Documentação
* Python: https://docs.python.org/3/
* Locust: https://docs.locust.io/en/0.12.2/index.html
* RabbitMQ com Python: https://www.rabbitmq.com/tutorials/tutorial-one-python.html
* Pika: https://pika.readthedocs.io/en/stable/