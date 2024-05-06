# Tortuguita
Objetivo: aprender como utilizar o ROS e criar um desenho usando o turtlesim.

## Como executar

Abra o seu terminal e clone este repositório:

```gh repo clone Gabrielle-Cartaxo/tortuguita```

Entre na pasta clonada e utilize os seguintes comandos:

------------------------------------------------------------------------------
- Essa primeira parte é para caso você ainda não tenha o rosdep instalado. Caso já tenha, passe para a próxima!

- ```sudo apt install python3-rosdep```

- ```sudo rosdep init```

- ```rosdep update```
------------------------------------------------------------------------------

Compilando o pacote para ser utilizado com o comando ros2 run;

```colcon build```

Configurando o pacote;

```source install/local_setup.bash```

**Agora sim! Vamos botar a tortuguita pra desenhar!**

Nesse mesmo terminal, rode:

```ros2 run turtlesim turlesim_node```

Agora, uma telinha azul com uma tartaruga irá abrir.

Abra um segundo terminal e entre na mesma pasta (tortuguita), e rode:

```ros2 run starMaker star```

E veja a mágica acontecer!!!
Espero que goste <3

## Vídeo

Você pode ver o script em ação nesse vídeo [aqui!](https://youtu.be/hAXkZiF_6PQ?si=5rQdencEZCYKhhIb)
