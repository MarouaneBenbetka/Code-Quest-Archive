import React, { useState } from "react";
import styles from "../styles/todo-item.module.css";
import { Todo } from "../types/todo";

interface TodoItemProps {
	todo: Todo;
	toggleTodo: (id: number) => void;
	editTodo: (id: number, text: string) => void;
	deleteTodo: (id: number) => void;
}

const TodoItem: React.FC<TodoItemProps> = ({
	todo,
	toggleTodo,
	editTodo,
	deleteTodo,
}) => {
	const [isEditing, setIsEditing] = useState(false);
	const [editText, setEditText] = useState(todo.text);
	const [isDeleting, setIsDeleting] = useState(false);

	const handleEdit = (): void => {
		setIsEditing(true);
		setEditText(todo.text);
	};

	const handleSave = (): void => {
		editTodo(todo.id, editText);
		setIsEditing(false);
	};

	const handleCancel = (): void => {
		setIsEditing(false);
		setEditText(todo.text);
	};

	const handleDeleteConfirm = (): void => {
		deleteTodo(todo.id);
		setIsDeleting(false);
	};

	const handleKeyDown = (e: React.KeyboardEvent): void => {
		if (e.key === "Enter") {
			handleSave();
		} else if (e.key === "Escape") {
			handleCancel();
		}
	};

	// Format creation date
	const formatDate = (dateString: string): string => {
		const date = new Date(dateString);
		return new Intl.DateTimeFormat("en-US", {
			month: "short",
			day: "numeric",
			hour: "2-digit",
			minute: "2-digit",
		}).format(date);
	};

	return (
		<li
			className={`${styles.todoItem} ${
				todo.completed ? styles.completed : ""
			}`}
		>
			{isEditing ? (
				<div className={styles.editContainer}>
					<input
						type="text"
						value={editText}
						onChange={(e) => setEditText(e.target.value)}
						onKeyDown={handleKeyDown}
						className={styles.editInput}
						autoFocus
					/>
					<div className={styles.editActions}>
						<button
							onClick={handleSave}
							className={styles.saveButton}
							disabled={!editText.trim()}
						>
							Save
						</button>
						<button
							onClick={handleCancel}
							className={styles.cancelButton}
						>
							Cancel
						</button>
					</div>
				</div>
			) : isDeleting ? (
				<div className={styles.deleteConfirm}>
					<p>Are you sure you want to delete this task?</p>
					<div className={styles.deleteActions}>
						<button
							onClick={handleDeleteConfirm}
							className={styles.confirmButton}
						>
							Yes, Delete
						</button>
						<button
							onClick={() => setIsDeleting(false)}
							className={styles.cancelButton}
						>
							Cancel
						</button>
					</div>
				</div>
			) : (
				<div className={styles.todoContent}>
					<div className={styles.todoMain}>
						<label className={styles.checkboxContainer}>
							<input
								type="checkbox"
								checked={todo.completed}
								onChange={() => toggleTodo(todo.id)}
								className={styles.checkbox}
							/>
							<span className={styles.checkmark}></span>
						</label>
						<div className={styles.todoDetails}>
							<span className={styles.todoText}>{todo.text}</span>
							{todo.createdAt && (
								<span className={styles.todoDate}>
									Created: {formatDate(todo.createdAt)}
								</span>
							)}
						</div>
					</div>
					<div className={styles.todoActions}>
						<button
							onClick={handleEdit}
							className={styles.editButton}
							aria-label="Edit task"
						>
							✏️
						</button>
						<button
							onClick={() => setIsDeleting(true)}
							className={styles.deleteButton}
							aria-label="Delete task"
						>
							🗑️
						</button>
					</div>
				</div>
			)}
		</li>
	);
};

export default TodoItem;
