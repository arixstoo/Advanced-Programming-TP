#include <cstdio>
#include <cstring>
#include <cstdlib>

struct Task {
    int id;
    char description[100];
    int priority;
    char status[20];
    Task* next;

    Task(int id, const char* desc, int pri, const char* stat) : id(id), priority(pri), next(nullptr) {
        strncpy(description, desc, sizeof(description));
        strncpy(status, stat, sizeof(status));
    }
};

class TaskManager {
private:
    Task* head;

    bool isValidPriority(int priority) {
        return priority >= 1 && priority <= 5;
    }

    bool isValidStatus(const char* status) {
        return strcmp(status, "Pending") == 0 || strcmp(status, "In Progress") == 0 || strcmp(status, "Completed") == 0;
    }

    void print(const char* str) {
        printf("%s", str);
    }

    void printInt(int value) {
        printf("%d", value);
    }

public:
    TaskManager() : head(nullptr) {}

    ~TaskManager() {
        Task* current = head;
        while (current) {
            Task* temp = current;
            current = current->next;
            delete temp;
        }
    }

    void addTask(int id, const char* description, int priority, const char* status) {
        if (!isValidPriority(priority) || !isValidStatus(status)) return;

        Task* newTask = new Task(id, description, priority, status);

        if (!head || head->priority < priority) {
            newTask->next = head;
            head = newTask;
            print("Task added successfully.\n");
            return;
        }

        Task* current = head;
        while (current->next && current->next->priority >= priority) {
            current = current->next;
        }
        newTask->next = current->next;
        current->next = newTask;
        print("Task added successfully.\n");
    }

    void displayTasks() {
        print("\nDisplaying all tasks:\n");

        const char* statuses[3] = {"Pending", "In Progress", "Completed"};

        for (int i = 0; i < 3; ++i) {
            print(statuses[i]);
            print(" Tasks:\n");

            Task* current = head;
            bool found = false;
            while (current) {
                if (strcmp(current->status, statuses[i]) == 0) {
                    found = true;
                    print("ID: ");
                    printInt(current->id);
                    print("\nDescription: ");
                    print(current->description);
                    print("\nPriority: ");
                    printInt(current->priority);
                    print("\nStatus: ");
                    print(current->status);
                    print("\n-------------------------\n");
                }
                current = current->next;
            }

            if (!found) {
                print("No tasks in this category.\n");
            }
        }
    }

    void updateTaskStatus(int id, const char* newStatus) {
        if (!isValidStatus(newStatus)) return;

        Task* current = head;
        while (current) {
            if (current->id == id) {
                strncpy(current->status, newStatus, sizeof(current->status));
                print("Task status updated successfully.\n");
                return;
            }
            current = current->next;
        }
        print("Task not found.\n");
    }

    void deleteTask(int id) {
        Task* current = head;
        Task* prev = nullptr;

        while (current) {
            if (current->id == id) {
                if (prev) prev->next = current->next;
                else head = current->next;
                delete current;
                print("Task deleted successfully.\n");
                return;
            }
            prev = current;
            current = current->next;
        }
        print("Task not found.\n");
    }

    void searchByPriority(int priority) {
        if (!isValidPriority(priority)) return;

        print("\nSearching for tasks with priority ");
        printInt(priority);
        print(":\n");

        Task* current = head;
        bool found = false;
        while (current) {
            if (current->priority == priority) {
                found = true;
                print("ID: ");
                printInt(current->id);
                print("\nDescription: ");
                print(current->description);
                print("\nPriority: ");
                printInt(current->priority);
                print("\nStatus: ");
                print(current->status);
                print("\n-------------------------\n");
            }
            current = current->next;
        }

        if (!found) {
            print("No tasks found with this priority.\n");
        }
    }
};

int main() {
    TaskManager manager;

    manager.addTask(1, "Complete project report", 3, "Pending");
    manager.addTask(2, "Prepare for meeting", 5, "In Progress");
    manager.addTask(3, "Submit assignment", 2, "Completed");

    manager.displayTasks();

    printf("\nUpdating task status:\n");
    manager.updateTaskStatus(1, "Completed");

    printf("\nDisplaying all tasks after update:\n");
    manager.displayTasks();

    printf("\nSearching for tasks with priority 5:\n");
    manager.searchByPriority(5);

    printf("\nDeleting a task:\n");
    manager.deleteTask(2);

    printf("\nDisplaying all tasks after deletion:\n");
    manager.displayTasks();

    return 0;
}
