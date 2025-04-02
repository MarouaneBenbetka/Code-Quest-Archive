# Todo List Application

A simple web-based Todo List application built with HTML, CSS, and vanilla JavaScript. This application allows users to add, edit, complete, and delete tasks. All tasks are stored in the browser's localStorage, so they persist even when the page is refreshed.

## Features

-   Add new tasks
-   Mark tasks as complete (click on the task text)
-   Edit existing tasks (click on the pencil icon)
-   Delete tasks (click on the trash icon)
-   Persistent storage using localStorage
-   Responsive design

## Screenshots

### Main Application Interface

![Todo List Application](screenshots/todo-list-main.png)
_The main interface of the Todo List application showing the input field and task list._

### Task List with Items

![Task List with Items](screenshots/task-list-items.png)
_The Todo List with several tasks added._

### Completed Task

![Completed Task](screenshots/completed-task.png)
_A task marked as completed, showing the strikethrough style._

### Editing a Task

![Editing a Task](screenshots/editing-task.png)
_Editing an existing task using the inline edit functionality._

## Prerequisites

-   [Visual Studio Code (VS Code)](https://code.visualstudio.com/)
-   [Live Server Extension](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

## How to Run

1. Clone this repository:

    ```
    git clone https://github.com/MarouaneBenbetka/Code-Quest-Archive.git
    ```

2. Navigate to the project directory:

    ```
    cd web/JS/todo-list-app
    ```

3. Open the Project in VS Code

4. Install Live Server (if not installed)

5. Open `index.html`

6. Run with Live Server
   Right-click on the `index.html` file and select **"Open with Live Server"**.  
   This will open your default web browser and load the page on a local server (usually `http://127.0.0.1:5500`).

## Implementation Details

-   The application is built using vanilla JavaScript without any frameworks.
-   Tasks are stored in the browser's localStorage for persistence.
-   CSS is used for styling and responsive design.
-   The codebase follows modern JavaScript practices.

## Future Improvements

-   Add due dates for tasks
-   Implement task categories or tags
-   Add task priority levels
-   Implement drag-and-drop for reordering tasks
-   Add dark mode toggle
