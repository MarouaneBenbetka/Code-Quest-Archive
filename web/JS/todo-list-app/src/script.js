document.addEventListener("DOMContentLoaded", function () {
	const taskInput = document.getElementById("taskInput");
	const addButton = document.getElementById("addButton");
	const taskList = document.getElementById("taskList");

	loadTasks();

	// Add task event
	addButton.addEventListener("click", addTask);
	taskInput.addEventListener("keypress", function (e) {
		if (e.key === "Enter") {
			addTask();
		}
	});

	function addTask() {
		const taskText = taskInput.value.trim();

		if (taskText === "") {
			alert("Please enter a task!");
			return;
		}

		const task = {
			id: Date.now(),
			text: taskText,
			completed: false,
		};

		createTaskElement(task);

		taskInput.value = "";

		saveTasks();

		taskInput.focus();
	}

	function createTaskElement(task) {
		const li = document.createElement("li");
		li.className = "task-item";
		li.dataset.id = task.id;

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

		taskList.appendChild(li);

		taskDiv.addEventListener("click", function () {
			toggleComplete(task.id);
		});

		editButton.addEventListener("click", function () {
			editTask(task.id);
		});

		deleteButton.addEventListener("click", function () {
			deleteTask(task.id);
		});
	}

	function toggleComplete(taskId) {
		const taskElement = document.querySelector(`li[data-id="${taskId}"]`);
		taskElement.classList.toggle("completed");
		saveTasks();
	}

	function editTask(taskId) {
		const taskElement = document.querySelector(`li[data-id="${taskId}"]`);
		const taskTextDiv = taskElement.querySelector(".task-text");
		const currentText = taskTextDiv.textContent;

		const editInput = document.createElement("input");
		editInput.type = "text";
		editInput.value = currentText;
		editInput.className = "edit-input";

		taskTextDiv.textContent = "";
		taskTextDiv.appendChild(editInput);

		editInput.focus();
		editInput.select();

		editInput.addEventListener("blur", saveEdit);
		editInput.addEventListener("keypress", function (e) {
			if (e.key === "Enter") {
				saveEdit();
			}
		});

		function saveEdit() {
			const newText = editInput.value.trim();
			if (newText) {
				taskTextDiv.textContent = newText;
				saveTasks();
			} else {
				taskTextDiv.textContent = currentText;
			}
		}
	}

	function deleteTask(taskId) {
		const taskElement = document.querySelector(`li[data-id="${taskId}"]`);
		taskElement.remove();
		saveTasks();
	}

	function saveTasks() {
		const tasks = [];
		document.querySelectorAll(".task-item").forEach(function (taskElement) {
			tasks.push({
				id: Number(taskElement.dataset.id),
				text: taskElement.querySelector(".task-text").textContent,
				completed: taskElement.classList.contains("completed"),
			});
		});

		localStorage.setItem("tasks", JSON.stringify(tasks));
	}

	function loadTasks() {
		const savedTasks = localStorage.getItem("tasks");
		if (savedTasks) {
			const tasks = JSON.parse(savedTasks);
			tasks.forEach(function (task) {
				createTaskElement(task);
			});
		}
	}
});
