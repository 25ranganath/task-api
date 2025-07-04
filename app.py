from flask import Flask, request, jsonify
from db_config import get_db_connection

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Mom and Dad!"

# ---------- API to Create Database and Table ---------- #

# Create taskdb database
@app.route('/create_db', methods=['GET'])
def create_database():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS taskdb")
    cursor.execute("USE taskdb")
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Database created successfully!"})

# Create tasks table
@app.route('/create_table', methods=['GET'])
def create_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS tasks (
        taskid INT AUTO_INCREMENT PRIMARY KEY,
        task_name VARCHAR(255) NOT NULL,
        task_detail TEXT
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Table created successfully!"})


# Create Task API
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task_name = data.get('task_name')
    task_detail = data.get('task_detail')

    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO tasks (task_name, task_detail) VALUES (%s, %s)"
    cursor.execute(query, (task_name, task_detail))
    connection.commit()
    task_id = cursor.lastrowid
    cursor.close()
    connection.close()

    return jsonify({"message": "Task created successfully!", "task_id": task_id}), 201

# API to get all tasks API
@app.route('/tasks', methods=['GET'])
def get_tasks():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    connection.close()

    return jsonify(tasks)


# API to get a specific task by ID
@app.route('/tasks/<int:taskid>', methods=['GET'])
def get_task(taskid):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks WHERE taskid = %s", (taskid,))
    task = cursor.fetchone()
    cursor.close()
    connection.close()

    if task:
        return jsonify(task)
    else:
        return jsonify({"message": "Task not found"}), 404

# API to update a specific task by ID
@app.route('/tasks/<int:taskid>', methods=['PUT'])
def update_task(taskid):
    data = request.get_json()
    task_name = data.get('task_name')
    task_detail = data.get('task_detail')

    connection = get_db_connection()
    cursor = connection.cursor()
    query = "UPDATE tasks SET task_name = %s, task_detail = %s WHERE taskid = %s"
    cursor.execute(query, (task_name, task_detail, taskid))
    connection.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    connection.close()

    if rows_affected:
        return jsonify({"message": "Task updated successfully!"})
    else:
        return jsonify({"message": "Task not found"}), 404

# API to delete a specific task by ID
@app.route('/tasks/<int:taskid>', methods=['DELETE'])
def delete_task(taskid):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "DELETE FROM tasks WHERE taskid = %s"
    cursor.execute(query, (taskid,))
    connection.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    connection.close()

    if rows_affected:
        return jsonify({"message": "Task deleted successfully!"})
    else:
        return jsonify({"message": "Task not found"}), 404

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
