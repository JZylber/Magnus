# Magnus the G.O.A.T.

Para el que no conoce al crack: https://en.wikipedia.org/wiki/Magnus_Carlsen

Y Magnus derrotando a jugadores de alto nivel con unas copas encima: https://www.youtube.com/watch?v=K-Kz7bo5tKE

Recuerden instalar pygame! `pip install pygame`.

## Reglas de juego
Para hacer este ejercicio, tienen que saber como se mueven las piezas de ajedrez y como se cuentan los puntos. Esto se encuentra libremente en internet.

En este ajedrez rudimentario no tomamos en cuenta:
- Promoción de fichas (peón a reina)
- Jaques
- Condiciones de terminación: Jaque Mate, empates, etc.
- En Passant

Sin embargo, con el diseño con objetos, ¡Al finalizar el ejercicio puede que se imaginen como implementar esas funciones!

## Piezas

Para este ejercicio, pueden asumir que la pieza está en la posición que dice estar, y que las posiciones son válidas (es decir, no caen fuera del tablero).

### Torre
¡La torre no sabe moverse! Completar el método `is_valid_move` de la torre para que sepa como hacerlo. Recordamos que la torre se mueve horizontalmente y verticalmente sin saltar piezas.

Para correr **SOLO** los tests de la torre, usar `python -m pytest test_ajedrez.py::TestPieces::TestRook`

### Alfil
Github Copilot sugirió una solución para implementar el movimiento del alfil, que es la que está en el archivo. Sin embargo, esta no anda. Revisando en internet, el siguiente foro de matemática sugiere la siguiente solución a ese problema: https://math.stackexchange.com/questions/1566115/formula-that-describes-the-movement-of-a-bishop-in-chess. Arreglar/Rehacer el método `is_valid_move` del alfil. Recordamos que el alfil se mueve diagonalmente sin saltar piezas.

Para correr **SOLO** los tests del alfil, usar `python -m pytest test_ajedrez.py::TestPieces::TestBishop` 

### Reina
Ahora, con lo que hicimos con la torre y el alfil, completar el método `is_valid_move` de la reina. Recordamos que la reina se mueve horizontalmente y verticalmente sin saltar piezas.

Para correr **SOLO** los tests de la reina, usar `python -m pytest test_ajedrez.py::TestPieces::TestQueen`

## Jugadores

De los jugadores no sólo nos importa el color, si no también los puntos y las piezas que fue capturando. Para eso, completen la clase `Jugador` que:
- Se inicialice con el color (white/black)
- Tenga un método points que devuelva los puntos del jugador, que se calculan en base a  las piezas capturadas del oponente:
  - 1 por peón
  - 3 por alfil o caballo
  - 5 por torre
  - 9 por reina
- Tenga un método `capture_piece` que reciba una pieza y la capture.
- Tenga un método `captured_pieces` que no tome parámetros y devuelva una lista de las piezas capturadas por dicho jugador.

Además, deben hacer que el jugador conozca las piezas capturadas. Para eso, deben modificar los estados (`logica.py`) para que el jugador reciba las piezas que va capturando. Piensen, ¿En qué estado tiene sentido que el jugador capture una pieza?