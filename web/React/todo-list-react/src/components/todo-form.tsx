import React, { useState } from "react";
import styles from "../styles//todo-form.module.css";

interface TodoFormProps {
	addTodo: (text: string) => void;
}

const TodoForm: React.FC<TodoFormProps> = ({ addTodo }) => {
	const [text, setText] = useState("");

	const handleSubmit = (e: React.FormEvent): void => {
		e.preventDefault();
		addTodo(text);
		setText("");
	};

	return (
		<form className={styles.todoForm} onSubmit={handleSubmit}>
			<input
				type="text"
				value={text}
				onChange={(e) => setText(e.target.value)}
				placeholder="What needs to be done?"
				className={styles.todoInput}
			/>
			<button
				type="submit"
				className={styles.addButton}
				disabled={!text.trim()}
			>
				<span className={styles.buttonText}>Add Task</span>
				<span className={styles.buttonIcon}>+</span>
			</button>
		</form>
	);
};

export default TodoForm;
