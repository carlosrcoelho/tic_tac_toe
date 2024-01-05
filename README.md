This Python code sets up a simple Tic Tac Toe game between a player and a CPU opponent. Here's a summarized breakdown:

### Structure:
- **Player Enum**: Represents X, O, and an empty cell.
- **printGameBoard()**: Prints the Tic Tac Toe board.
- **modifyArray()**: Modifies the game board based on user or CPU input.
- **checkWinner()**: Checks for a winning combination.
- **isBoardFull()**: Checks if the board is full.
- **main()**: Runs the game loop.

### Game Flow:
1. **Initialization**: Sets up the game board, available moves, and turn count.
2. **Game Loop**: Alternates turns between the player and CPU until there's a winner or a tie.
    - Player's turn: Asks for input (1-9) to place 'X' on the board.
    - CPU's turn: Randomly selects an available cell to place 'O' on the board.
    - After each turn, the board is checked for a winner or a tie.
3. **Outcome**:
    - If there's a winner, it prints the winning player.
    - If the board is full without a winner, it declares a tie.

### Improvements:
- Error Handling: Enhance input validation to handle incorrect user inputs.
- CPU Intelligence: Implement more sophisticated CPU moves to make the game more challenging.
- Refactoring: Simplify and optimize the code for better readability and efficiency.
