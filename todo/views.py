from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import Task
from .forms import TaskForm
from .services.task_factory import TaskFactory


def index(request):

    tasks = Task.objects.all().order_by(
        "-created_at"
    )

    if request.method == "POST":

        title = request.POST.get(
            "title", ""
        ).strip()

        if title:
            TaskFactory.create_task(
                title
            )

        return redirect(
            "index"
        )

    context = {
        "tasks": tasks,
        "form": TaskForm()
    }

    return render(
        request,
        "todo/index.html",
        context
    )


def update_task(request, pk):

    task = get_object_or_404(
        Task,
        id=pk
    )

    if request.method == "POST":

        form = TaskForm(
            request.POST,
            instance=task
        )

        if form.is_valid():
            form.save()

            return redirect(
                "index"
            )

    else:

        form = TaskForm(
            instance=task
        )

    return render(
        request,
        "todo/update.html",
        {
            "form": form,
            "task": task
        }
    )


def delete_task(request, pk):

    task = get_object_or_404(
        Task,
        id=pk
    )

    task.delete()

    return redirect(
        "index"
    )


def complete_task(request, pk):

    task = get_object_or_404(
        Task,
        id=pk
    )

    task.completed = (
        not task.completed
    )

    task.save()

    return redirect(
        "index"
    )
