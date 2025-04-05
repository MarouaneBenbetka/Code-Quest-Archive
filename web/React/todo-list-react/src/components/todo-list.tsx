import React, { useState } from "react";
import styles from "../styles/todo-list.module.css";
import TodoItem from "./todo-item";
import { Todo as TodoType } from "../types/todo";

interface TodoListProps {
	todos: TodoType[];
	toggleTodo: (id: number) => void;
	editTodo: (id: number, text: string) => void;
	deleteTodo: (id: number) => void;
}

const TodoList: React.FC<TodoListProps> = ({
	todos,
	toggleTodo,
	editTodo,
	deleteTodo,
}) => {
	const [filter, setFilter] = useState<"all" | "active" | "completed">("all");

	const filteredTodos = todos.filter((todo) => {
		if (filter === "active") return !todo.completed;
		if (filter === "completed") return todo.completed;
		return true;
	});

	if (todos.length === 0) {
		return (
			<div className={styles.emptyContainer}>
				<div className={styles.emptyIllustration}>📝</div>
				<p className={styles.emptyMessage}>Your task list is empty</p>
				<p className={styles.emptySubtext}>
					Add a new task to get started!
				</p>
			</div>
		);
	}

	if (filteredTodos.length === 0) {
		return (
			<div>
				<div className={styles.filterControls}>
					<button
						className={`${styles.filterButton} ${
							filter === "all" ? styles.active : ""
						}`}
						onClick={() => setFilter("all")}
					>
						All
					</button>
					<button
						className={`${styles.filterButton} ${
							filter === "active" ? styles.active : ""
						}`}
						onClick={() => setFilter("active")}
					>
						Active
					</button>
					<button
						className={`${styles.filterButton} ${
							filter === "completed" ? styles.active : ""
						}`}
						onClick={() => setFilter("completed")}
					>
						Completed
					</button>
				</div>
				<p className={styles.noMatchesMessage}>
					No {filter} tasks found
				</p>
			</div>
		);
	}

	return (
		<div>
			<div className={styles.filterControls}>
				<button
					className={`${styles.filterButton} ${
						filter === "all" ? styles.active : ""
					}`}
					onClick={() => setFilter("all")}
				>
					All
				</button>
				<button
					className={`${styles.filterButton} ${
						filter === "active" ? styles.active : ""
					}`}
					onClick={() => setFilter("active")}
				>
					Active
				</button>
				<button
					className={`${styles.filterButton} ${
						filter === "completed" ? styles.active : ""
					}`}
					onClick={() => setFilter("completed")}
				>
					Completed
				</button>
			</div>
			<ul className={styles.todoList}>
				{filteredTodos.map((todo) => (
					<TodoItem
						key={todo.id}
						todo={todo}
						toggleTodo={toggleTodo}
						editTodo={editTodo}
						deleteTodo={deleteTodo}
					/>
				))}
			</ul>
		</div>
	);
};

export default TodoList;
