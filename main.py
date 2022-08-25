import Core_manager
import os


way = os.getcwd()
exit_m = 0


while exit_m != 1:
    initial_way = way + ' -> '
    command = input(initial_way)
    my_command = Core_manager.Way_commands(command, way)
    way = my_command.init_command()
    exit_m = my_command.exit_m