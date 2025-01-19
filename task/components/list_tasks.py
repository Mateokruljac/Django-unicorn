from django_unicorn.components import UnicornView

from task.models import Todo


class ListTasksView(UnicornView):
    create_task_name = ""
    update_task_name = ""
    tasks = Todo.objects.none()
    update_task_id = 0

    def mount(self):
        self.load_tasks()

    def add_task(self):
        Todo.objects.create(name=self.create_task_name)
        self.load_tasks()  # Automatically re-renders the component
        self.reset_values()

    def delete_task(self,id):
        Todo.objects.get(id=id).delete()
        self.load_tasks()

    def set_update_task_info(self,id):
        task = Todo.objects.get(id=id)
        self.update_task_id = task.id
        self.update_task_name = task.name
        self.load_tasks()

    def update_task(self):
        task = Todo.objects.get(id=self.update_task_id)
        task.name = self.update_task_name
        task.save()
        self.load_tasks()
        self.reset_values()

    def cancel_action(self):
       self.reset_values()


    def reset_values(self):
         self.update_task_id = 0
         self.create_task_name = ""
         self.update_task_name = ""

    def load_tasks(self):
        self.tasks = Todo.objects.all()