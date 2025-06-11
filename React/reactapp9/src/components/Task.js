import './Task.css';

import React, { useState, useEffect } from "react"; // add useEffect

function Task() {
  const [tasks, setTasks] = useState(() => {
    const saved = localStorage.getItem("todo-tasks");
    return saved ? JSON.parse(saved) : [];
  });

  const [newTask, setNewTask] = useState("");

  useEffect(() => {
    localStorage.setItem("todo-tasks", JSON.stringify(tasks));
  }, [tasks]);


  const Task = () => {
    if (newTask.trim() === "") return;
    setTasks([...tasks, { text: newTask, done: false }]);
    setNewTask("");
  };

  const toggleTask = (index) => {
    const updated = tasks.map((task, i) =>
      i === index ? { ...task, done: !task.done } : task
    );
    setTasks(updated);
  };

  const deleteTask = (index) => {
    const updated = tasks.filter((_, i) => i !== index);
    setTasks(updated);
  };

  return (
    <div className='container'>
      <h2 className='heading'>To-Do List 📝</h2>
      <input
        className='input'
        value={newTask}
        onChange={(e) => setNewTask(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && Task()}
        placeholder="Enter a new task..."
      />
      <button className='button1' onClick={Task}>Add Task</button>
      <ul className='ul'>
        {tasks.map((task, index) => (
          <li className='li'
            key={index}
            style={{
              
              textDecoration: task.done ? "line-through" : "none",
              backgroundColor: task.done ? "#d1f2eb" : "#e3e3e3",
            }}
            onClick={() => toggleTask(index)}
          >
            {task.text}
            <button
              className='deleteButton'
              onClick={(e) => {
                e.stopPropagation();
                deleteTask(index);
              }}
            >
              X
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}



export default Task;
