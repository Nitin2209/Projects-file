import java.util.ArrayList;
import java.util.Scanner;

class Task {
    String description;
    boolean isDone;

    Task(String description) {
        this.description = description;
        this.isDone = false;
    }

    void markDone() {
        this.isDone = true;
    }
}

public class ToDoList {
    private final ArrayList<Task> tasks = new ArrayList<>();
    private final Scanner scanner = new Scanner(System.in);

    public void addTask() {
        System.out.print("Enter task description: ");
        String description = scanner.nextLine();
        tasks.add(new Task(description));
        System.out.println("Task added successfully!\n");
    }

    public void removeTask() {
        displayTasks();
        System.out.print("Enter task number to remove: ");
        int index = scanner.nextInt() - 1;
        scanner.nextLine();
        if (index >= 0 && index < tasks.size()) {
            tasks.remove(index);
            System.out.println("Task removed successfully!\n");
        } else {
            System.out.println("Invalid task number!\n");
        }
    }

    public void markTaskDone() {
        displayTasks();
        System.out.print("Enter task number to mark as done: ");
        int index = scanner.nextInt() - 1;
        scanner.nextLine();
        if (index >= 0 && index < tasks.size()) {
            tasks.get(index).markDone();
            System.out.println("Task marked as done!\n");
        } else {
            System.out.println("Invalid task number!\n");
        }
    }

    public void displayTasks() {
        if (tasks.isEmpty()) {
            System.out.println("No tasks available!\n");
        } else {
            System.out.println("\nYour To-Do List:");
            for (int i = 0; i < tasks.size(); i++) {
                System.out.println((i + 1) + ". " + tasks.get(i));
            }
            System.out.println();
        }
    }

    public void menu() {
        while (true) {
            System.out.println("To-Do List Menu:");
            System.out.println("1. Add Task");
            System.out.println("2. Remove Task");
            System.out.println("3. Mark Task as Done");
            System.out.println("4. Display Tasks");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1 -> addTask();
                case 2 -> removeTask();
                case 3 -> markTaskDone();
                case 4 -> displayTasks();
                case 5 -> {
                    System.out.println("Goodbye!");
                    return;
                }
                default -> System.out.println("Invalid option!\n");
            }
        }
    }

    public static void main(String[] args) {
        ToDoList toDoList = new ToDoList();
        toDoList.menu();
    }
}
