class STUDYSYSTEM:
 def __init__(self,title,total_lessons):
    self.title=title
    self.total_lessons=total_lessons
    self.completed_lessons=0
 def show_progress(self):
   print("python : " + self.title , "| You completed "+ str(self.completed_lessons) +" out of" +str(self.total_lessons) +"Lessons .")
 def watch_lesson(self):
   self.completed_lessons= self.completed_lessons + 1
   print("Great job ! You watched a new lesson.")
my_cours=STUDYSYSTEM("python" , 20)
my_cours.show_progress()
my_cours.watch_lesson()
my_cours.watch_lesson()
my_cours.watch_lesson()
my_cours.show_progress() 
