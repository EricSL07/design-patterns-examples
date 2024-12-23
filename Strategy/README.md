# Strategy
 
 # Propósito
O Strategy é um padrão de projeto comportamental que permite que você defina uma família de algoritmos, coloque-os em classes separadas, e faça os objetos deles intercambiáveis.

# Problema
Um dia você decide criar uma aplicação de navegação para viajantes casuais. A aplicação estava centrada em um mapa bonito que ajudava os usuários a se orientarem rapidamente em uma cidade.

Uma das funcionalidades mais pedidas para a aplicação era o planejamento automático de rotas. Um usuário deveria ser capaz de entrar com um endereço e ver a rota mais rápida no mapa.

A primeira versão da aplicação podia apenas construir rotas sobre rodovias, e isso agradou muito quem viaja de carro. Porém aparentemente, nem todo mundo dirige em suas férias. Então com a próxima atualização você adicionou uma opção de construir rotas de caminhada. Logo após isso você adicionou outra opção para permitir que as pessoas usem o transporte público.

Contudo, isso foi apenas o começo. Mais tarde você planejou adicionar um construtor de rotas para ciclistas. E mais tarde, outra opção para construir rotas até todas as atrações turísticas de uma cidade.

O código do navegador ficou muito inchado
O código do navegador ficou muito inchado.

Embora da perspectiva de negócio a aplicação tenha sido um sucesso, a parte técnica causou a você muitas dores de cabeça. Cada vez que você adicionava um novo algoritmo de roteamento, a classe principal do navegador dobrava de tamanho. Em determinado momento, o monstro se tornou algo muito difícil de se manter.

Qualquer mudança a um dos algoritmos, seja uma simples correção de bug ou um pequeno ajuste no valor das ruas, afetava toda a classe, aumentando a chance de criar um erro no código já existente.

Além disso, o trabalho em equipe se tornou ineficiente. Seus companheiros de equipe, que foram contratados após ao bem sucedido lançamento do produto, se queixavam que gastavam muito tempo resolvendo conflitos de fusão. Implementar novas funcionalidades necessitava mudanças na classe gigantesca, conflitando com os códigos criados por outras pessoas.

# Solução
O padrão Strategy sugere que você pegue uma classe que faz algo específico em diversas maneiras diferentes e extraia todos esses algoritmos para classes separadas chamadas estratégias.

A classe original, chamada contexto, deve ter um campo para armazenar uma referência para um dessas estratégias. O contexto delega o trabalho para um objeto estratégia ao invés de executá-lo por conta própria.

O contexto não é responsável por selecionar um algoritmo apropriado para o trabalho. Ao invés disso, o cliente passa a estratégia desejada para o contexto. Na verdade, o contexto não sabe muito sobre as estratégias. Ele trabalha com todas elas através de uma interface genérica, que somente expõe um único método para acionar o algoritmo encapsulado dentro da estratégia selecionada.

Desta forma o contexto se torna independente das estratégias concretas, então você pode adicionar novos algoritmos ou modificar os existentes sem modificar o código do contexto ou outras estratégias.

Estratégias de planejamento de rotas
Estratégias de planejamento de rotas.

Em nossa aplicação de navegação, cada algoritmo de roteamento pode ser extraído para sua própria classe com um único método construirRota. O método aceita uma origem e um destino e retorna uma coleção de pontos da rota.

Mesmo dando os mesmos argumentos, cada classe de roteamento pode construir uma rota diferente, a classe navegadora principal não se importa qual algoritmo está selecionado uma vez que seu trabalho primário é renderizar um conjunto de pontos num mapa. A classe tem um método para trocar a estratégia ativa de rotas, então seus clientes, bem como os botões na interface de usuário, podem substituir o comportamento de rotas selecionado por um outro.