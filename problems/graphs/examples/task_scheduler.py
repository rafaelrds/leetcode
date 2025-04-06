# TODO solve it in optimal way

# Phase 1
# scheduler = TaskScheduler()
# coffee_task = Task("Brew some coffee")
# print(f"coffee task: {coffee_task}")
# scheduler.add_task(coffee_task)
# next_task = scheduler.get_next_task() # Should be coffee_task
# print(f"next task: {next_task}")
# scheduler.complete_task(next_task)
# print(f"completed next task: {next_task}")


# Phase 2
# scheduler = TaskScheduler()
# coffee_task = Task("Brew some coffee")
# scheduler.add_task(coffee_task)
# toast_task = Task("Make a toast")
# scheduler.add_task(toast_task)
# brainstorm_task = Task("Brainstorm project ideas", [coffee_task, toast_task])
# scheduler.add_task(brainstorm_task)

# print(scheduler.get_all_tasks())

# next_task = scheduler.get_next_task() # Should be coffee_task or toast_task
# print(f"first task: {next_task}")
# scheduler.complete_task(next_task)
# print(f"first task update: {next_task}")
# next_task = scheduler.get_next_task() # Should be coffee_task or toast_task
# print(f"second task: {next_task}")
# print(f"brainstorm task state: {brainstorm_task}")
# scheduler.complete_task(next_task)
# print(f"second task update: {next_task}")
# next_task = scheduler.get_next_task() # Should be brainstorm_task
# print(f"third task: {next_task}")
# scheduler.complete_task(next_task)
# print(f"third task update: {next_task}")

# Phase 3
# scheduler = TaskScheduler()
# yoga_task = Task("Do morning yoga")
# scheduler.add_task(yoga_task)
# coffee_task = Task("Brew some coffee", [yoga_task])
# scheduler.add_task(coffee_task)
# toast_task = Task("Make a toast", [yoga_task])
# scheduler.add_task(toast_task)
# brainstorm_task = Task("Brainstorm project ideas", [coffee_task, toast_task])
# scheduler.add_task(brainstorm_task)

# Should be [yoga_task, coffee_task, toast_task, brainstorm_task] or [yoga_task, toast_task, coffee_task, brainstorm_task]
# plan = scheduler.get_completion_plan_for(brainstorm_task)
# print(f"completion plan: {plan}")
