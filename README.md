# Magnus the G.O.A.T.

Para el que no conoce al crack: https://en.wikipedia.org/wiki/Magnus_Carlsen

Y Magnus derrotando a jugadores de alto nivel con unas copas encima: https://www.youtube.com/watch?v=K-Kz7bo5tKE

Recuerden instalar pygame! `pip install pygame`.

## Reglas de juego
Para hacer este ejercicio, tienen que saber como se mueven las piezas de ajedrez y como se cuentan los puntos. Esto se encuentra libremente en internet.

En este ajedrez rudimentario no tomamos en cuenta:
- Promoción de fichas (peón a reina)
- En Passant
- Enroque
- Jaques
- Condiciones de terminación: Jaque Mate, empates, etc.

Sin embargo, con el diseño con objetos, ¡Al finalizar el ejercicio puede que se imaginen como implementar esas funciones!

## Especificaciones del programa

El programa cuenta con distintos archivos que tienen distintas partes del programa

### Ajedrez

Este archivo cuenta con todo lo necesario para correr la interfaz gráfica. Usa la librería pygame, y es el archivo que tienen que correr para ver la interfaz. A diferencia de todo el resto del programa, está pensado más con una lógica funcional que con P.O.O.

### Tablero

Define la clase tablero a ser usada en el juego. Cuenta con diversos métodos para obtener y mover piezas. No hace falta que le realicen ninguna modificación

**IMPORTANTE:** Las posiciones `(x,y)` en el tablero no son las tradicionales de los ejes cartesianos. `x` es fila e `y` columna, por lo tanto, `x` sería el eje vertical e `y` el horizontal.

### Lógica

Cuenta con la lógica de máquina de estados necesaria para el desarrollo del juego. Van a tener que modificar algunas cosas para el punto final. Dejo la lógica de los estados a continuación:

![Diagrama de Estados](https://github.com/JZylber/Magnus/blob/8e63be21f0346616ef1d1c6a38d0657e8a460ead/assets/Estados-Ajedrez.png?raw=true)

### Piezas

Declaración y lógica de las piezas de ajedrez. Hay alguna piezas ya hechas, y otras que tiene que completar/arreglar en ciertos puntos de la consigna.

### Jugador

Declaración y constructor incompleto de la clase `Jugador`, a ser completada en el punto de la consigna correspondiente.

### Tests

Están los tests separados en 2 archivos, para que no sea un mega archivo y mas o menos se separen por temas, pero pueden correr todos juntos con `python -m pytest`. Pueden correr tests individuales usando los comandos que se incluyen en cada punto de la consigna. 

## Consigna

### Piezas

Para este ejercicio, pueden asumir que la pieza está en la posición que dice estar, y que las posiciones son válidas (es decir, no caen fuera del tablero).

#### Alfil
Github Copilot sugirió una solución para implementar el movimiento del alfil, que es la que está en el archivo. Sin embargo, esta no anda. Revisando en internet, el siguiente foro de matemática sugiere la siguiente solución a ese problema: https://math.stackexchange.com/questions/1566115/formula-that-describes-the-movement-of-a-bishop-in-chess. Arreglar/Rehacer el método `is_valid_move` del alfil. Recordamos que el alfil se mueve diagonalmente sin saltar piezas.

Para correr **SOLO** los tests del alfil, usar `python -m pytest test_piezas.py::TestBishop` 

#### Torre
¡La torre no sabe moverse! Completar el método `is_valid_move` de la torre para que sepa como hacerlo. Recordamos que la torre se mueve horizontalmente y verticalmente sin saltar piezas. **TIP:** Pueden usar el principio de la solución del alfil para hacer algo parecido. ¡Tal vez convenga partir en movimiento horizontal y vertical por separado!

Para correr **SOLO** los tests de la torre, usar `python -m pytest test_piezas.py::TestRook`

#### Reina
Ahora, con lo que hicimos con la torre y el alfil, completar el método `is_valid_move` de la reina. Recordamos que la reina se mueve horizontalmente, verticalmente y diagonalmente sin saltar piezas.

Para correr **SOLO** los tests de la reina, usar `python -m pytest test_piezas.py::TestQueen`

### Jugadores

#### Puntos

De los jugadores no sólo nos importa el color, si no también los puntos y las piezas que fue capturando. Para eso, completen la clase `Jugador` que:
- Se inicialice con el color (white/black)
- Tenga un método points que devuelva los puntos del jugador, que se calculan en base a  las piezas capturadas del oponente:
  - 1 por peón
  - 3 por alfil o caballo
  - 5 por torre
  - 9 por reina
- Tenga un método `capture_piece` que reciba una pieza y la capture.
- Tenga un método `captured_pieces` que no tome parámetros y devuelva una lista de las piezas capturadas por dicho jugador.

Para correr **SOLO** los tests de los puntos, usar `python -m pytest test_jugador.py::TestPoints`

#### Lógica de Juego

Además, deben hacer que el jugador conozca las piezas capturadas, ya que en este momento los estados no actualizan al jugador cada vez que se come una pieza. Para eso, deben modificar dichos estados (`logica.py`) para que el jugador reciba las piezas que va capturando. Piensen, ¿En qué estado tiene sentido que el jugador capture una pieza? **TIP:** Los jugadores están en los atributos `player` y `oponent` del estado.

Para correr **SOLO** los tests del estado, usar `python -m pytest test_jugador.py::TestPieceCapture`
