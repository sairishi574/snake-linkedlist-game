# app.py
from flask import Flask, render_template, jsonify, request
from snake_linkedlist import LinkedList
import random

app = Flask(__name__)

# Game configuration
cols, rows = 30, 20
snake = LinkedList()
snake.insert_at_beginning(10, 10)
direction = (1, 0)
food = (random.randint(0, cols-1), random.randint(0, rows-1))
score = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/state', methods=['GET'])
def get_state():
    """Return snake, food, and score to front-end"""
    return jsonify({
        "snake": snake.get_positions(),
        "food": food,
        "score": score
    })

@app.route('/move', methods=['POST'])
def move():
    """Update snake based on user direction"""
    global direction, food, score

    data = request.get_json()
    dir_key = data.get("dir")

    # Map keys to movement
    directions = {"up": (0,-1), "down": (0,1), "left": (-1,0), "right": (1,0)}
    new_dir = directions.get(dir_key, direction)

    # Prevent immediate reversal
    if (new_dir[0] != -direction[0] or new_dir[1] != -direction[1]):
        direction = new_dir

    # Move snake
    head_x, head_y = snake.head.x + direction[0], snake.head.y + direction[1]
    snake.insert_at_beginning(head_x, head_y)

    # Check food collision
    if (head_x, head_y) == food:
        food = (random.randint(0, cols-1), random.randint(0, rows-1))
        score += 1
    else:
        snake.delete_at_end()

    # Collision with wall or self
    positions = snake.get_positions()
    if (head_x < 0 or head_y < 0 or head_x >= cols or head_y >= rows or (head_x, head_y) in positions[1:]):
        reset_game()
        return jsonify({"status": "gameover", "score": score})

    return jsonify({"status": "ok", "score": score})

def reset_game():
    """Restart snake when it hits wall/self"""
    global snake, direction, food, score
    snake = LinkedList()
    snake.insert_at_beginning(10, 10)
    direction = (1, 0)
    food = (random.randint(0, cols-1), random.randint(0, rows-1))
    score = 0

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
