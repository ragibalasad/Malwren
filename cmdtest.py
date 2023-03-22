def command(cmd):

    valid_commands = ['actv', 'conn', 'dsconn']

    cmd_seq = cmd.split()

    if len(cmd_seq): # see if it is empty or not.

        if cmd_seq[0] not in valid_commands:
            print(f"invalid command '{cmd_seq[0]}'")

        else:
            if len(cmd_seq) >= 2:            
                if cmd_seq[0] == valid_commands[0]: # activities command
                    if cmd_seq[1] == 'count':
                        print("// it will print the number of active connections")
                    elif cmd_seq[1] == 'list':
                        print('// it will print the list of all active connections')
                    else:
                        print(f"invalid argument '{cmd_seq[1]}'")


                elif cmd_seq[0] == valid_commands[1]: # connect to a clients remote comand prompt
                    pass


            else:
                print(f"E: '{valid_commands[0]}' expects 1 follow up argument. 0 given.")
     

while True:
    cmd = input("$ ")
    command(cmd)