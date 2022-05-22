class Zoo:

    def __init__(self, animals = ''):
        self.animals = animals   # Input for chosen animal.

    def list_animals(self):
        # Retrieves all animals in the Zoo from txt file. Also don't forget to add path to txt file.
        with open("zoo_animals.txt", "r") as animals_file:
            zoo_animals_str = animals_file.read()
        zoo_animals = zoo_animals_str.split('-')
        return zoo_animals


class Visitor(Zoo):
    # Show_animals works as 2:nd argument so __init__ doesn't crash.
    def __init__(self, show_animals = '', animals = ''):
        super().__init__(animals)
        
        print(f'\nDjuren har liv som visas efter djurets namn.',
              f'Dessa är djuren som finns i zoo:et:\n\n |{zoo_animals[0]}  |',
              f'{zoo_animals[1]} | {zoo_animals[2]} | {zoo_animals[3]}|\n',
               '|-----------------------------------------|\n',
              f'|{zoo_animals[4]}    |    {zoo_animals[5]}   ',
              f'|    {zoo_animals[6]}    |\n\n(skriv endast djur med stor bokstav)\n')
        
        # Error handling for user input and check list if self.animals
        # Exist in zoo_animals.
        while True:
            correct_input = False
            self.animals = str(input('Vilket djur vill du besöka?: '))
            
            for check_animal in zoo_animals:
                if self.animals in check_animal:
                    correct_input = True
                    break
                    
            if correct_input == True:
                break
            else:
                print('du skrev inte in ett giltigt svar. Var god försök igen')

    def visitor_damage(self):
        # Choose user action and error handling.
        while True:
            harm = str(input('Vad vill du göra med djuret? (mata = 1, klappa = 2 eller slå = 3)\n:'))
            if harm == '1':
                break
            elif harm == '3':
                break
            elif harm == '2':
                print('\ndu försökte klappa ett djur', \
                      'och det ska man inte göra. Du dog.')
                exit()
            else:
                print('Du skrev inte in ett giltigt svar. Var god försök igen.')
        
        # Add self.animals to separate list.
        selected = []
        count = 0
        for search_list in zoo_animals:
            if self.animals in search_list:
                selected.append(search_list)
                break  
            count += 1
        
        # Convert from list to str and replace old hp with new hp.
        selected_str = ''
        for i in selected:
            selected_str += i
        selected_str = selected_str.replace('1', '0')
        selected_str = selected_str.replace('2', '1')
        
        # Replace old animal and hp with new animal and hp.
        zoo_animals.pop(int(count))
        zoo_animals.insert(int(count), selected_str)
        print(f'\n\n |{zoo_animals[0]}  |',
              f'{zoo_animals[1]} | {zoo_animals[2]} | {zoo_animals[3]}|\n',
               '|-----------------------------------------|\n',
              f'|{zoo_animals[4]}    |    {zoo_animals[5]}   ',
              f'|    {zoo_animals[6]}    |\n')
        return zoo_animals
        

class Worker(Zoo):
    # Show_animals works as 2:nd argument so __init__ doesn't crash.
    def __init__(self, show_animals = '', animals = ''):
        super().__init__(animals)
        
        print(f'\nDjuren har liv som visas efter djurets namn.',
              f'Dessa är djuren som finns i zoo:et:\n\n |{zoo_animals[0]}  |',
              f'{zoo_animals[1]} | {zoo_animals[2]} | {zoo_animals[3]}|\n',
               '|-----------------------------------------|\n',
              f'|{zoo_animals[4]}    |    {zoo_animals[5]}   ',
              f'|    {zoo_animals[6]}    |\n\n')
        
        # Error handling for user input and check list if self.animals
        # Exist in zoo_animals.
        while True:
            correct_input = False
            self.animals = str(input('Vilket djur vill du vårda?: '))
            
            for check_animal in zoo_animals:
                if self.animals in check_animal:
                    correct_input = True
                    break
                    
            if correct_input == True:
                break
            else:
                print('du skrev inte in ett giltigt svar. Var god försök igen')

    def worker_heal(self):
        # Choose user action and error handling.
        while True:
            harm = input('Vad vill du göra med djuret? (mata = 1, medicin = 2 eller behandla = 3)\n:')
            if harm == '1':
                break
            elif harm == '3':
                break
            elif harm == '2':
                break
            else:
                print('Du skrev inte in ett giltigt svar. Var god försök igen.')
        
        # Add self.animals to separate list.
        selected = []
        count = 0
        for search_list in zoo_animals:
            if self.animals in search_list:
                selected.append(search_list)
                break
            count += 1
        
        # Convert from list to str and replace old hp with new hp.
        selected_str = ''
        for i in selected:
            selected_str += i
        selected_str = selected_str.replace('1', '2')
        selected_str = selected_str.replace('0', '1')
        
        # Replace old animal and hp with new animal and hp.
        zoo_animals.pop(int(count))
        zoo_animals.insert(int(count), selected_str)
        print(f'\n\n |{zoo_animals[0]}  |',
              f'{zoo_animals[1]} | {zoo_animals[2]} | {zoo_animals[3]}|\n',
               '|-----------------------------------------|\n',
              f'|{zoo_animals[4]}    |    {zoo_animals[5]}   ',
              f'|    {zoo_animals[6]}    |\n')
        return zoo_animals


def exit_program():
    print('\nTack för att du ville plåga våra djur och hejdå.')
    exit()


def main():
    while True:
        print('\nVälkommen till Avgrundens Zoo.\nHär kan du interagera',
              'med djuren på olika sätt beroende på vad du vill åstadkomma.',
              'Ifall du vill avsluta programmet skriv "quit".\n')
        user_input = input('Är du besökare eller arbetare (b/a)\n: ')
        
        if user_input == 'b':
            Visitor().visitor_damage()
        elif user_input == 'B':
            Visitor().visitor_damage()
        elif user_input == 'a':
            Worker().worker_heal()
        elif user_input == 'A':
            Worker().worker_heal()
        elif user_input == 'quit':
            exit_program()
        else:
            print('Du skrev inte in ett giltigt alternativ. Var god försök igen.')


# Make zoo_animals accesible to all classes.
zoo_animals = Zoo().list_animals()
main()