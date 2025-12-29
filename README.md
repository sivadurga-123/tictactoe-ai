# Task 2: Tic-Tac-Toe AI Game

An advanced implementation of the classic Tic-Tac-Toe game with an unbeatable AI opponent using the Minimax algorithm.

## Project Overview
This project implements an AI-powered Tic-Tac-Toe game where a human player plays against an intelligent computer opponent. The AI uses the Minimax algorithm with optional Alpha-Beta Pruning to determine optimal moves, making it nearly impossible to defeat.

## Tech Stack
- **Backend**: Python, Flask, Flask-CORS
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Algorithm**: Minimax with Alpha-Beta Pruning
- **Architecture**: REST API

## Features
- Interactive web-based game board
- Unbeatable AI opponent using Minimax algorithm
- Move validation and game state management
- Real-time game updates
- Clean, intuitive UI with visual feedback
- Win/Draw detection
- Game reset functionality

## Installation & Setup

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend Setup
1. Open `frontend/index.html` in a web browser
2. Ensure backend server is running on `http://localhost:5000`

## API Endpoints
- **POST /init** - Initialize new game
- **POST /move** - Make a player move
  - Request: `{"position": 0-8}`
  - Response: `{"board": [...], "status": "continue|ai_wins|human_wins|draw"}`
- **POST /ai-move** - Get AI's next move

## Game Rules
- Players alternate placing X (human) and O (AI)
- First player to get 3 in a row (horizontal, vertical, or diagonal) wins
- If all 9 squares are filled with no winner, it's a draw
- AI always plays optimally using Minimax algorithm

## Minimax Algorithm
The AI evaluates all possible future game states using the Minimax algorithm:
- **Maximizing Player**: AI (tries to maximize score)
- **Minimizing Player**: Human (tries to minimize score)
- **Scoring**: AI win = +10, Human win = -10, Draw = 0
- **Alpha-Beta Pruning**: Optimizes by eliminating branches that won't affect final decision

## How to Play
1. Start the game - Human is X, AI is O
2. Click on any empty square to make your move
3. AI automatically makes its move
4. Continue until someone wins or board is full
5. Click "New Game" to play again

## Algorithm Complexity
- **Time Complexity**: O(9!) worst case without pruning
- **Space Complexity**: O(d) where d is depth of tree
- **With Alpha-Beta Pruning**: O(b^(d/2)) - significant improvement

## Future Enhancements
- Difficulty levels (Easy, Medium, Hard)
- Game statistics tracking
- Multiplayer support
- Enhanced UI animations
- Mobile responsive design

## Author
Created as part of CODSOFT AI Internship

## License
MIT License
