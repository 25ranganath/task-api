
1. Create the Virtual Envionment
2. Activate the Virtual Enviornment
3. Install the packages 

```pip install -r requirement.txt ```

4. Run the app.py 
5. Tets the API

## 📖 API Endpoints

| Method | Endpoint | Description | Payload (if applicable) |
| --- | --- | --- | --- |
| **GET** | `/create_db` | Creates the `taskdb` database | *None* |
| **GET** | `/create_table` | Creates the `tasks` table | *None* |
| **POST** | `/tasks` | Creates a new task | `{ "task_name": "Task title", "task_detail": "Details about the task" }` |
| **GET** | `/tasks` | Retrieves all tasks | *None* |
| **GET** | `/tasks/<taskid>` | Retrieves a task by `taskid` | *None* |
| **PUT** | `/tasks/<taskid>` | Updates a task by `taskid` | `{ "task_name": "Updated title", "task_detail": "Updated details" }` |
| **DELETE** | `/tasks/<taskid>` | Deletes a task by `taskid` | *None* |

---

- **Request Method**
- **URL**
- **Headers** (if needed)
- **Body** (if applicable — with raw JSON)

---

## 📬 Postman API Requests

---

### 📗 1️⃣ Create Database

- **Method:** `GET`
- **URL:** `http://localhost:5000/create_db`
- **Body:** None

---

### 📘 2️⃣ Create Table

- **Method:** `GET`
- **URL:** `http://localhost:5000/create_table`
- **Body:** None

---

### 📙 3️⃣ Create a New Task

- **Method:** `POST`
- **URL:** `http://localhost:5000/tasks`
- **Headers:**
    - `Content-Type: application/json`
- **Body:** (raw, JSON)

```json
{
  "task_name": "Write Flask API",
  "task_detail": "Build a simple CRUD API using Flask and MySQL"
}

```

---

### 📒 4️⃣ Get All Tasks

- **Method:** `GET`
- **URL:** `http://localhost:5000/tasks`
- **Body:** None

---

### 📕 5️⃣ Get a Task by `taskid`

- **Method:** `GET`
- **URL:** `http://localhost:5000/tasks/1`
- *(replace `1` with the actual `taskid` you want to fetch)*
- **Body:** None

---

### 📘 6️⃣ Update a Task by `taskid`

- **Method:** `PUT`
- **URL:** `http://localhost:5000/tasks/1`
- *(replace `1` with the `taskid` you want to update)*
- **Headers:**
    - `Content-Type: application/json`
- **Body:** (raw, JSON)

```json
{
  "task_name": "Update Flask API",
  "task_detail": "Refactor CRUD API and improve error handling"
}

```

---

### 📙 7️⃣ Delete a Task by `taskid`

- **Method:** `DELETE`
- **URL:** `http://localhost:5000/tasks/1`
- *(replace `1` with the `taskid` you want to delete)*
- **Body:** None
