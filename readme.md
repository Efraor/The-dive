Juego Gato vs Ratón con Minimax

    ¿Qué creé?
    Este es un pequeño juego de consola en python que simula una persecución entre el raton y el gato sobre un tablero 5x5. Ambos personajes se mueven en direcciones octogonales(8 direcciones), y a partir del turno 3, utilizan el algorimo Minimax para tomar decisiones estratégicas:El ratón intenta escapar y el gato intenta atraparlo.
    El juego se detiene si el gato atrapa al ratón o si pasan 10 turnos y el ratón no fue atrapado

    ¿Qué funcionó?
    El tablero se genera y muestra correctamente en cada turno.
    Se implementaron correctamente los movimientos aleatorios y el control de límites del tablero.
    integración del algoritmo Minimax funciona: el gato y el ratón toman decisiones más "inteligentes" después del turno 3.
    El sistema de evaluación por distancia Manhattan ayudó a definir la lógica de persecución y evasión.

    ¿Qué fue un desastre?
    Al principio fue difícil balancear la lógica del turno y la profundidad del algoritmo Minimax: un valor muy bajo lo hacía inútil, y uno muy alto ralentizaba todo.
    Manejar los estados del juego al mismo tiempo que se actualizaba el tablero fue algo confuso al comienzo.
    
    Mi mejor “¡ajá!” 
|   El mayor momento de claridad fue entender cómo aplicar Minimax desde ambos puntos de vista: el gato como el jugador maximizador y el ratón como minimizador.
    Eso me permitió implementar turnos separados con decisiones estratégicas y que ambos jugadores realmente "pensaran" antes de moverse.

