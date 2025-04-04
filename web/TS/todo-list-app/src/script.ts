interface Task {
	id: number;
	text: string;
	completed: boolean;
}

// Task Service class - handles data operations
class TaskService {
	private storage: Storage;
	private storageKey: string;

	constructor(storage: Storage = localStorage, storageKey: string = "tasks") {
		this.storage = storage;
		this.storageKey = storageKey;
	}

	public getTasks(): Task[] {
		const savedTasks = this.storage.getItem(this.storageKey);
		return savedTasks ? JSON.parse(savedTasks) : [];
	}

	public saveTask(task: Task): void {
		const tasks = this.getTasks();
		tasks.push(task);
		this.saveTasks(tasks);
	}

	public updateTask(taskId: number, updates: Partial<Task>): void {
		const tasks = this.getTasks();
		const taskIndex = tasks.findIndex((task) => task.id === taskId);

		if (taskIndex !== -1) {
			tasks[taskIndex] = { ...tasks[taskIndex], ...updates };
			this.saveTasks(tasks);
		}
	}

	public deleteTask(taskId: number): void {
		const tasks = this.getTasks();
		const filteredTasks = tasks.filter((task) => task.id !== taskId);
		this.saveTasks(filteredTasks);
	}

	public toggleTaskCompletion(taskId: number): void {
		const tasks = this.getTasks();
		const taskIndex = tasks.findIndex((task) => task.id === taskId);

		if (taskIndex !== -1) {
			tasks[taskIndex].completed = !tasks[taskIndex].completed;
			this.saveTasks(tasks);
		}
	}

	private saveTasks(tasks: Task[]): void {
		this.storage.setItem(this.storageKey, JSON.stringify(tasks));
	}
}

// UI Controller class - handles DOM interactions
class TodoUIController {
	private taskService: TaskService;
	private taskInputElement!: HTMLInputElement;
	private addButtonElement!: HTMLButtonElement;
	private taskListElement!: HTMLUListElement;

	constructor(taskService: TaskService) {
		this.taskService = taskService;
		this.initializeElements();
		this.setupEventListeners();
		this.renderTasks();
	}

	private initializeElements(): void {
		this.taskInputElement = document.getElementById(
			"taskInput"
		) as HTMLInputElement;
		this.addButtonElement = document.getElementById(
			"addButton"
		) as HTMLButtonElement;
		this.taskListElement = document.getElementById(
			"taskList"
		) as HTMLUListElement;
	}

	private setupEventListeners(): void {
		this.addButtonElement.addEventListener(
			"click",
			this.addTask.bind(this)
		);
		this.taskInputElement.addEventListener(
			"keypress",
			(e: KeyboardEvent) => {
				if (e.key === "Enter") {
					this.addTask();
				}
			}
		);
	}

	private addTask(): void {
		const taskText = this.taskInputElement.value.trim();

		if (taskText === "") {
			alert("Please enter a task!");
			return;
		}

		const task: Task = {
			id: Date.now(),
			text: taskText,
			completed: false,
		};

		this.taskService.saveTask(task);
		this.createTaskElement(task);
		this.taskInputElement.value = "";
		this.taskInputElement.focus();
	}

	private createTaskElement(task: Task): void {
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

	private toggleComplete(taskId: number): void {
		const taskElement = document.querySelector(
			`li[data-id="${taskId}"]`
		) as HTMLLIElement;
		taskElement.classList.toggle("completed");
		this.taskService.toggleTaskCompletion(taskId);
	}

	private editTask(taskId: number): void {
		const taskElement = document.querySelector(
			`li[data-id="${taskId}"]`
		) as HTMLLIElement;
		const taskTextDiv = taskElement.querySelector(
			".task-text"
		) as HTMLDivElement;
		const currentText = taskTextDiv.textContent || "";

		const editInput = document.createElement("input");
		editInput.type = "text";
		editInput.value = currentText;
		editInput.className = "edit-input";

		taskTextDiv.textContent = "";
		taskTextDiv.appendChild(editInput);

		editInput.focus();
		editInput.select();

		const saveEdit = (): void => {
			const newText = editInput.value.trim();
			if (newText) {
				taskTextDiv.textContent = newText;
				this.taskService.updateTask(taskId, { text: newText });
			} else {
				taskTextDiv.textContent = currentText;
			}
		};

		editInput.addEventListener("blur", saveEdit);
		editInput.addEventListener("keypress", (e: KeyboardEvent) => {
			if (e.key === "Enter") {
				saveEdit();
			}
		});
	}

	private deleteTask(taskId: number): void {
		const taskElement = document.querySelector(
			`li[data-id="${taskId}"]`
		) as HTMLLIElement;
		taskElement.remove();
		this.taskService.deleteTask(taskId);
	}

	private renderTasks(): void {
		const tasks = this.taskService.getTasks();
		tasks.forEach((task) => {
			this.createTaskElement(task);
		});
	}
}

// App class - main application controller
class TodoApp {
	private taskService: TaskService;
	private uiController: TodoUIController;

	constructor() {
		this.taskService = new TaskService();
		this.uiController = new TodoUIController(this.taskService);
	}
}

// Initialize the application when DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
	new TodoApp();
});
