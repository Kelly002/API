# Minha primeira API

Neste projeto vamos aprender como desenvolver uma primeira API, utilizando o Software Livre Flask.

## Começando

Seguindo esse passo a passo você irá conseguir colocar uma aplicação para rodar em sua máquina local, com uma url.

### Pré-requqisitos

Para começar, você precisa baixar o aplicativo Flask direto pelo terminal da sua máquina:

```
pip install flask
```

Vamos precisar também de um editor de textos, no meu caso, eu estou usando o Visual Studio Code.

### Executando

Criaremos uma pasta na máquina, onde será colocado os códigos que vamos utilizar.

Dentro do editor de texto abriremos um novo arquivo e chamaremos de "main.py", que é nome normalmente dado aos arquivos principais desse tipo de aplicação, e salvamos esse arquivo dentro da pasta que criamos.

Dentro desse arquivo, importamos a biblioteca do Flask: 

```
from flask import Flask
```

Vamos instancia-lo, dando uma nome para a nossa aplicação

```
app = Flask("meu app")
```

Em seguida, construimos a route, por onde as informações irão trafegar: 

```
@app.route('/')
```

Na sequência, criamos a função, que será executada. Nesse caso, nossa função faz apenas um printe:  
### Minha primeira aplicação

Que será impressa utilizando a função return

```
return "Minha primeira aplicação"
```

Encerramos a aplicação com :

```
app.run()
```

## Deploy

Pra fazer rodar essa aplicação, vamos até o terminal e navegamos até a pasta que contém o arquivo que foi salvo.

Para rodar essa aplicação, basta digitar no terminal a versão do python que você está usando, junto com o nome que salvamos o arquivo com sua extensão.

```
python main.py
```

Ao rodar esse pedaço de código,  vai ser gerado um endereço http, que copiaremos e abriremos em um novo brouse, onde poderemos ver o resultado da nossa aplicação:
   

```
Give an example
```
O código completo da aplicação será disponibilizado dentro deste projeto.

## Construido com:

* [Flask](https://flask.palletsprojects.com/en/2.3.x/) - Documentação
* [Visual Studio Code](https://code.visualstudio.com/) - Editor de textos

## Autores

* **Kelly Lopes** - 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
