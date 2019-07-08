## Projeto Integrador2

## Sistema do Robô

Para executar o arquivo mainSR.py você deve passar 4 parametros sendo eles, o nome do robô, a posição no eixo x, a poisção do eixo y e a orientação do Robô
```
python3 mainSR.py "speter" 1 1 "N"
```
Além disso deve ser alterado no arquivo Comunica_SS o parametro Host para o ip do Robô e no arquivo Recebe_SS também deve alterar o parametro Host para o ip do Sistema Supervisório

## Sistema Supervisório

Para executar o arquivo mainSS.py você deve passar 1 parametros sendo ele o ip do Sistema Auditor.
```
python3 mainSR.py "192.168.1.142"
```
Além disso deve ser alterado no arquivo Comunica_SR o parametro Host para o ip do Sistema Supervisório e no arquivo Recebe_SR também deve alterar o parametro Host para o ip do Robô

## Equipe
  * [Daniel Cabral Correa](https://github.com/Danehko)
  - [Adonis Andreas Marinos](https://github.com/adonismarinos)
