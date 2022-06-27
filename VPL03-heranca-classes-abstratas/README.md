# VPL03 | Herança e Classes Abstratas
Escreva um programa em Python que possua cinco classes: Animal, Mamifero, Ave, Cachorro, Gato e Canarinho. Defina uma hierarquia de herança entre essas classes.

A implementação deve atender às seguintes regras:

 1. Não existem instâncias de Animal, Mamifero e Ave, somente dos seus sub-tipos
 2. Todos os animais possuem um tamanho de passo e quando se movem, retornam a mensagem: "ANIMAL: DESLOCOU " tamanhoPasso
 3. As aves quando se movem, retornam a mensagem: "ANIMAL: DESLOCOU "+tamanhoPasso+" VOANDO"
 4. Todos os animais produzem algum tipo de som com um volume, mas cada um do seu jeito:
 5. Gato (miar): "MAMIFERO: PRODUZ SOM: "+volumeSom+ " SOM: MIAU"
 6. Cachorro (latir): "MAMIFERO: PRODUZ SOM: "+volumeSom+ " SOM: AU"
 7. Canarinho (cantar): "AVE: PRODUZ SOM: PIU"
 8. Somente as aves voam (que é a mesma coisa que mover para uma ave)
 9. Somente os canarinhos cantam 
 10. Cachorros tem tamanhoPasso = 3 e volumeSom = 3
 11. Gatos tem tamanhoPasso = 2 e volumeSom = 2
 12. Aves tem tamanhoPasso e alturaVoo parametrizáveis no construtor

#### Observação:

Ordem de parâmetros dos construtores:

 - Ave(int tamanhoPasso, int alturaVoo)
 - Mamifero(int volumeSom, int tamanhoPasso)
 - Canarinho(int tamanhoPasso, int alturaVoo)

[DIagrama de Classes](assets/Modelo_Ex_05.png)