class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        didntgetcount = 0

        while didntgetcount < len(students):

            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                didntgetcount = 0
            else:
                stu_going_back = students.pop(0)
                students.append(stu_going_back)
                didntgetcount += 1
        
        return didntgetcount






        