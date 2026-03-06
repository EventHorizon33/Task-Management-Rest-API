from flask import Blueprint, jsonify, request
from models import tasks, Task

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify([task.to_dict() for task in tasks]), 200


@tasks_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.json

    if not data or not data.get('title'):
        return jsonify({"error": "Title is required"}), 400

    task = Task(
        title=data['title'],
        description=data.get('description', '')
    )
    tasks.append(task)
    return jsonify(task.to_dict()), 201


@tasks_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t.id == task_id), None)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    data = request.json
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.done = data.get('done', task.done)

    return jsonify(task.to_dict()), 200


@tasks_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((t for t in tasks if t.id == task_id), None)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    tasks.remove(task)
    return '', 204