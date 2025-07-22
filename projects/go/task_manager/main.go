package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"os"
	"time"
)

type Task struct {
	ID        int       `json:"id"`
	Title     string    `json:"title"`
	Completed bool      `json:"completed"`
	CreatedAt time.Time `json:"created_at"`
}

var taskFile = "tasks.json"

func loadTasks() ([]Task, error) {
	file, err := os.ReadFile(taskFile)
	if err != nil {
		if os.IsNotExist(err) {
			return []Task{}, nil // return empty slice if file doesn't exist
		}
		return nil, err
	}

	var tasks []Task
	if err := json.Unmarshal(file, &tasks); err != nil {
		return nil, err
	}
	return tasks, nil
}

func saveTasks(tasks []Task) error {
	data, err := json.MarshalIndent(tasks, "", "  ")
	if err != nil {
		return err
	}
	return os.WriteFile(taskFile, data, 0644)
}

func listTasks() {
	tasks, err := loadTasks()
	if err != nil {
		fmt.Println("Error loading tasks:", err)
		return
	}
	if len(tasks) == 0 {
		fmt.Println("No tasks found.")
		return
	}
	for _, task := range tasks {
		status := "[ ]"
		if task.Completed {
			status = "[x]"
		}
		fmt.Printf("%s %d: %s (Created: %s)\n", status, task.ID, task.Title, task.CreatedAt.Format("2006-01-02 15:04"))
	}
}

func addTask(title string) {
	tasks, err := loadTasks()
	if err != nil {
		fmt.Println("Error loading tasks:", err)
		return
	}
	newTask := Task{
		ID:        len(tasks) + 1,
		Title:     title,
		Completed: false,
		CreatedAt: time.Now(),
	}
	tasks = append(tasks, newTask)
	if err := saveTasks(tasks); err != nil {
		fmt.Println("Error saving task:", err)
		return
	}
	fmt.Println("Task added!")
}

func main() {
	add := flag.String("add", "", "Add a new task")
	list := flag.Bool("list", false, "List all tasks")

	flag.Parse()

	switch {
	case *add != "":
		addTask(*add)
	case *list:
		listTasks()
	default:
		fmt.Println("Usage:")
		fmt.Println("  -add \"task name\"    Add a new task")
		fmt.Println("  -list                List all tasks")
	}
}
