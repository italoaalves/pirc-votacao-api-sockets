# Projeto da disciplina de Protocolos de Interconexão de Redes de Computadores
Aplicação cliente/servidor usando API de Sockets e um protocolo de aplicação.
## Proposta
Optamos por desenvolver uma aplicação de votações utilizando um protocolo de aplicação próprio inpirado no http.
## Especificação do projeto
O projeto constará do desenvolvimento de um aplicativo distribuído em uma arquitetura cliente/servidor, implementado com base na API de Sockets, o qual deverá usar um protocolo de aplicação para realizar a comunicação, de forma padronizada, entre os módulos do sistema.

O aplicativo será composto de 2 módulos principais: cliente e servidor. Toda a comunicação entre os módulos cliente e servidor deverá ser feita usando um protocolo de aplicação padrão, já existente, ou um novo, que venha a ser projetado especificamente para a aplicação. O protocolo de transporte deverá ser escolhido de acordo com a necessidade do sistema distribuído.

O módulo servidor deverá ser capaz de atender, de forma simultânea, a diversas instâncias de clientes que solicitem os seus serviços. Desta forma, pense nos dados que podem causar condições de corrida se acessados simultaneamente (dados compartilhados) e use estruturas vistas na disciplina Sistemas Operacionais, tais como semáforos.

