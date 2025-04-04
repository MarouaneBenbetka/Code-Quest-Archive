"use strict";
// Task Service class - handles data operations
class TaskService {
    constructor(storage = localStorage, storageKey = "tasks") {
        this.storage = storage;
        this.storageKey = storageKey;
    }
    getTasks() {
        const savedTasks = this.storage.getItem(this.storageKey);
        return savedTasks ? JSON.parse(savedTasks) : [];
    }
    saveTask(task) {
        const tasks = this.getTasks();
        tasks.push(task);
        this.saveTasks(tasks);
    }
    updateTask(taskId, updates) {
        const tasks = this.getTasks();
        const taskIndex = tasks.findIndex((task) => task.id === taskId);
        if (taskIndex !== -1) {
            tasks[taskIndex] = { ...tasks[taskIndex], ...updates };
            this.saveTasks(tasks);
        }
    }
    deleteTask(taskId) {
        const tasks = this.getTasks();
        const filteredTasks = tasks.filter((task) => task.id !== taskId);
        this.saveTasks(filteredTasks);
    }
    toggleTaskCompletion(taskId) {
        const tasks = this.getTasks();
        const taskIndex = tasks.findIndex((task) => task.id === taskId);
        if (taskIndex !== -1) {
            tasks[taskIndex].completed = !tasks[taskIndex].completed;
            this.saveTasks(tasks);
        }
    }
    saveTasks(tasks) {
        this.storage.setItem(this.storageKey, JSON.stringify(tasks));
    }
}
// UI Controller class - handles DOM interactions
class TodoUIController {
    constructor(taskService) {
        this.taskService = taskService;
        this.initializeElements();
        this.setupEventListeners();
        this.renderTasks();
    }
    initializeElements() {
        this.taskInputElement = document.getElementById("taskInput");
        this.addButtonElement = document.getElementById("addButton");
        this.taskListElement = document.getElementById("taskList");
    }
    setupEventListeners() {
        this.addButtonElement.addEventListener("click", this.addTask.bind(this));
        this.taskInputElement.addEventListener("keypress", (e) => {
            if (e.key === "Enter") {
                this.addTask();
            }
        });
    }
    addTask() {
        const taskText = this.taskInputElement.value.trim();
        if (taskText === "") {
            alert("Please enter a task!");
            return;
        }
        const task = {
            id: Date.now(),
            text: taskText,
            completed: false,
        };
        this.taskService.saveTask(task);
        this.createTaskElement(task);
        this.taskInputElement.value = "";
        this.taskInputElement.focus();
    }
    createTaskElement(task) {
        const li = document.createElement("li");
        li.className = "task-item";
        li.dataset.id = task.id.toString();
        if (task.completed) {
            li.classList.add("completed");
        }
        const taskDiv = document.createElement("div");
        taskDiv.className = "task-text";
        taskDiv.textContent = task.text;
        const buttonGroup = document.createElement("div");
        buttonGroup.className = "button-group";
        const editButton = document.createElement("button");
        editButton.className = "edit-button";
        editButton.innerHTML = "✏️";
        editButton.title = "Edit";
        const deleteButton = document.createElement("button");
        deleteButton.className = "delete-button";
        deleteButton.innerHTML = "🗑️";
        deleteButton.title = "Delete";
        buttonGroup.appendChild(editButton);
        buttonGroup.appendChild(deleteButton);
        li.appendChild(taskDiv);
        li.appendChild(buttonGroup);
        this.taskListElement.appendChild(li);
        // Set up event listeners
        taskDiv.addEventListener("click", () => {
            this.toggleComplete(task.id);
        });
        editButton.addEventListener("click", () => {
            this.editTask(task.id);
        });
        deleteButton.addEventListener("click", () => {
            this.deleteTask(task.id);
        });
    }
    toggleComplete(taskId) {
        const taskElement = document.querySelector(`li[data-id="${taskId}"]`);
        taskElement.classList.toggle("completed");
        this.taskService.toggleTaskCompletion(taskId);
    }
    editTask(taskId) {
        const taskElement = document.querySelector(`li[data-id="${taskId}"]`);
        const taskTextDiv = taskElement.querySelector(".task-text");
        const currentText = taskTextDiv.textContent || "";
        const editInput = document.createElement("input");
        editInput.type = "text";
        editInput.value = currentText;
        editInput.className = "edit-input";
        taskTextDiv.textContent = "";
        taskTextDiv.appendChild(editInput);
        editInput.focus();
        editInput.select();
        const saveEdit = () => {
            const newText = editInput.value.trim();
            if (newText) {
                taskTextDiv.textContent = newText;
                this.taskService.updateTask(taskId, { text: newText });
            }
            else {
                taskTextDiv.textContent = currentText;
            }
        };
        editInput.addEventListener("blur", saveEdit);
        editInput.addEventListener("keypress", (e) => {
            if (e.key === "Enter") {
                saveEdit();
            }
        });
    }
    deleteTask(taskId) {
        const taskElement = document.querySelector(`li[data-id="${taskId}"]`);
        taskElement.remove();
        this.taskService.deleteTask(taskId);
    }
    renderTasks() {
        const tasks = this.taskService.getTasks();
        tasks.forEach((task) => {
            this.createTaskElement(task);
        });
    }
}
// App class - main application controller
class TodoApp {
    constructor() {
        this.taskService = new TaskService();
        this.uiController = new TodoUIController(this.taskService);
    }
}
// Initialize the application when DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    new TodoApp();
});
//# sourceMappingURL=script.js.map