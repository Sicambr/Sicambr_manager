"""This modul does main operation
"""

import os

class Way_commands:
    def __init__(self,command_cmd, way):
        self.command_cmd = command_cmd.lstrip(' ').rstrip(' ')
        self.way = way
        self.exit_m = 0


    def init_command(self):
        if self.command_cmd == 'dir':
            self.dir_command()
        elif 'cd' in self.command_cmd and self.command_cmd[:2] == 'cd':
            self.cd_command()
        elif self.command_cmd == 'exit':
            self.exit_m = 1
        return self.way


    # Action for command 'dir'
    def dir_command(self):
        print(os.listdir(self.way))


    # Action for command 'cd'
    def cd_command(self):
        if len(self.command_cmd) == 2:
            print('Error - укажите директорию для перехода')
        elif self.command_cmd == 'cd ..' or self.command_cmd == 'cd..':
            i = len(self.way)
            if self.way.count('\\') > 1:
                while ((i > 0) and self.way.count('\\') > 1):
                    if self.way[i-1] != '\\':
                        i -= 1
                    else:
                        self.way = self.way[:(i-1)]
                        break
            else:
                self.way = self.way.partition('\\')[0] + '\\'
        elif self.command_cmd[:3] == 'cd ' and len(self.command_cmd) > 3:
            new_way = self.command_cmd.partition('cd ')[2]
            self.way = self.way + '\\' + new_way
        else:
            print('Error - Неверная команда командной строки')
