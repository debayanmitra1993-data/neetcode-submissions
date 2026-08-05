class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        elig = {}

        for task in tasks:
            if task not in counts:
                counts[task] = 0
                elig[task] = 0                      
            counts[task] += 1
        
        count_tasks_complete = 0
        task_order = []
        while count_tasks_complete < len(tasks):
            # get all eligible tasks..
            elig_tasks = [x[0] for x in list(elig.items()) if x[1] == 0]

            # pick the task with highest count...
            highest_task_cnt = 0
            highest_task = None
            for task in elig_tasks:
                if counts[task] > highest_task_cnt:
                    highest_task_cnt = counts[task]
                    highest_task = task 
            
            if highest_task is not None:
                counts[highest_task] -= 1
                task_order.append(highest_task)
                count_tasks_complete += 1
            else:
                task_order.append("NA")
            
            for task in elig.keys():
                if elig[task] > 0:
                    elig[task] -= 1
            
            if highest_task is not None:
                elig[highest_task] = n
        
        print("task_order = ", task_order)
        return len(task_order)