import React, { useState, useEffect } from "react";

import styles from "./styles/app.module.css";
import { Todo } from "./types/todo";
import TodoForm from "./components/todo-form";
import TodoList from "./components/todo-list";

const App: React.FC = () => {
	const [todos, setTodos] = useState<Todo[]>(() => {
		// Load from localStorage on initial render
		const savedTodos = localStorage.getItem("todos");
		return savedTodos ? JSON.parse(savedTodos) : [];
	});

	const [theme, setTheme] = useState<"light" | "dark">(() => {
		const savedTheme = localStorage.getItem("theme");
		return savedTheme === "dark" ? "dark" : "light";
	});

	// Save to localStorage whenever todos change
	useEffect(() => {
		localStorage.setItem("todos", JSON.stringify(todos));
	}, [todos]);

	// Save theme preference
	useEffect(() => {
		localStorage.setItem("theme", theme);
		document.body.className = theme === "dark" ? styles.darkMode : "";
	}, [theme]);

	const addTodo = (text: string): void => {
		if (text.trim()) {
			const newTodo: Todo = {
				id: Date.now(),
				text,
				completed: false,
				createdAt: new Date().toISOString(),
			};
			setTodos([...todos, newTodo]);
		}
	};

	const toggleTodo = (id: number): void => {
		setTodos(
			todos.map((todo) =>
				todo.id === id ? { ...todo, completed: !todo.completed } : todo
			)
		);
	};

	const editTodo = (id: number, newText: string): void => {
		if (newText.trim()) {
			setTodos(
				todos.map((todo) =>
					todo.id === id ? { ...todo, text: newText } : todo
				)
			);
		}
	};

	const deleteTodo = (id: number): void => {
		setTodos(todos.filter((todo) => todo.id !== id));
	};

	const clearCompleted = (): void => {
		setTodos(todos.filter((todo) => !todo.completed));
	};

	const toggleTheme = (): void => {
		setTheme(theme === "light" ? "dark" : "light");
	};

	const completedCount = todos.filter((todo) => todo.completed).length;
	const pendingCount = todos.length - completedCount;

	return (
		<div
			className={`${styles.appContainer} ${
				theme === "dark" ? styles.darkMode : ""
			}`}
		>
			<div className={styles.todoApp}>
				<div className={styles.headerContainer}>
					<h1 className={styles.header}>A2SV Task Manager</h1>
					<button
						className={styles.themeToggle}
						onClick={toggleTheme}
						aria-label={`Switch to ${
							theme === "light" ? "dark" : "light"
						} mode`}
					>
						{theme === "light" ? "🌙" : "☀️"}
					</button>
				</div>

				<TodoForm addTodo={addTodo} />

				<div className={styles.progressContainer}>
					<div className={styles.progressBar}>
						<div
							className={styles.progressFill}
							style={{
								width: todos.length
									? `${
											(completedCount / todos.length) *
											100
									  }%`
									: "0%",
							}}
						></div>
					</div>
					<div className={styles.progressText}>
						{todos.length
							? `${Math.round(
									(completedCount / todos.length) * 100
							  )}% Complete`
							: "No tasks yet"}
					</div>
				</div>

				<TodoList
					todos={todos}
					toggleTodo={toggleTodo}
					editTodo={editTodo}
					deleteTodo={deleteTodo}
				/>

				{todos.length > 0 && (
					<div className={styles.todoStats}>
						<div className={styles.statsCounters}>
							<div className={styles.statItem}>
								<span className={styles.statBadge}>
									{todos.length}
								</span>
								<span>Total</span>
							</div>
							<div className={styles.statItem}>
								<span
									className={`${styles.statBadge} ${styles.pendingBadge}`}
								>
									{pendingCount}
								</span>
								<span>Pending</span>
							</div>
							<div className={styles.statItem}>
								<span
									className={`${styles.statBadge} ${styles.completedBadge}`}
								>
									{completedCount}
								</span>
								<span>Completed</span>
							</div>
						</div>
						{completedCount > 0 && (
							<button
								className={styles.clearButton}
								onClick={clearCompleted}
							>
								Clear Completed
							</button>
						)}
					</div>
				)}
			</div>
		</div>
	);
};

export default App;
