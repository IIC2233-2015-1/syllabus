class Student:

    def __init__(self, name, username, assistance):
        self.name = name
        self.username = username
        self.assistance = assistance


class ConsoleApp:

    def __init__(self, spykiller):
        self.spykiller = spykiller

    def run(self):
        while True:
            self.clear()
            print("Select an option:")
            print("\t1) Register me.")
            print("\t2) Mark a classmate as unassistent.")

            selected = input()
            self.clear()
            
            if selected == "1":
                print(self.spykiller.register_me())

            elif selected == "2":
                victim = self.select_victim()
                if victim:
                    print(self.spykiller.mark_unassistent(victim))
                else:
                    print("No victim available.")

            print("=" * 10)
            if input("Exit? (Y/N):").lower() == "Y".lower():
                break

    def select_victim(self):
        '''
        Retorna el Student según su username. 
        Si no es encontrado, retorna el último.
        Si está vacía, retorna None
        '''
        print("Downloading student list...")
        
        self.clear()
        students = self.spykiller.download_list()
        usernames = []

        if len(students) == 0:
            return None

        print("-" * 10)
        for student in students:
            usernames.append(student.username)
            print("Name:" + student.name)
            print("Username:" + student.username)
            print("Assistance:" + str(student.assistance))
            print("-" * 10)

        i = input("Write the victim's username: ")
        return next((s for s in students if 
            s.username.lower() == i.lower()), students[-1])

    def clear(self):
        '''
        Limpia la terminal/consola
        '''
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
