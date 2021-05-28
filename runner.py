import re
import sys
import output
import shlex
import school_bag
import error


def run(lines, check_awake, check_sleep, loop_tab_amount):

    awake = False
    place = 'Home'

    loop = [[]]

    for index in range(0, len(lines)):
        line = lines[index]
        if not re.match(".*fuck.*", line, re.IGNORECASE) is None:  # Do not f**k loli
            error.print_error_msg("FBIError: Wtf r u thinkin'? r u stupid?")

        if line == 'Awake\n' or line == 'Awake':
            awake = True
        if line == 'Sleep\n' or line == 'Sleep':
            if place.lower() != 'home':
                print('Loli fell asleep. But sleeping outside is really dangerous. Don\'t you want to make her sleep '
                      'at home?')
            sys.exit(0)

        if awake or not check_awake:
            line_args = shlex.split(line)
            if not re.match("(Say ).+", line) is None:  # Say
                if len(line_args) >= 2 and line_args[0] == 'Say':
                    output.say(line_args[1])
            elif not re.match("(Put ).+( into school bag)", line) is None:  # Put var in school bag
                if len(line_args) >= 5:
                    school_bag.put(line[4:-17])
            elif not re.match("(Take out ).+( from school bag)", line) is None:  # Prepare for var
                if len(line_args) >= 6:
                    school_bag.takeout(line[9:-17])
            elif not re.match("(Speak ).+", line) is None:  # Print var value
                if len(line_args) >= 2:
                    school_bag.speak(line[6:-1])
            elif not re.match("(Show ).+", line) is None:  # Print var value
                if len(line_args) >= 2:
                    school_bag.speak(line[5:-1])
            elif not re.match("(Clearly |Simply )(speak ).+", line) is None:  # Print var value
                if len(line_args) >= 3:
                    school_bag.speak_int(line[line.index('speak ')+6:-1])
            elif not re.match("(Clearly |Simply )(show ).+", line) is None:  # Print var value
                if len(line_args) >= 3:
                    school_bag.speak_int(line[line.index('show ')+5:-1])
            elif not re.match("(Call ).+", line) is None:  # Print unicode char that the code is var value
                if len(line_args) >= 2:
                    school_bag.call(line[5:-1])
            elif not re.match("(Have ).+", line) is None:  # Input value
                if len(line_args) >= 2:
                    school_bag.take(line[5:-1], input())
            elif not re.match("(Take ).+", line) is None:  # Input value
                if len(line_args) >= 2:
                    school_bag.take(line[5:-1], input())
            elif not re.match("(Go to ).+", line) is None:  # Change place
                if len(line_args) >= 3:
                    place = line[6:-1]
            elif not re.match("(Go ).+", line) is None:  # Change place
                if len(line_args) >= 2:
                    place = line[3:-1]
            elif not re.match("(Dump ).*[^ ].*", line) is None:  # Delete var
                if len(line_args) >= 2:
                    name = line[5:-1]
                    if name in school_bag.out:
                        del school_bag.out[name]
                    else:
                        error.print_error_msg(f'Error: {name} is not in hand')
            elif not re.match("(Eat ).*[^ ].*", line) is None:  # Delete var
                if len(line_args) >= 2:
                    name = line[4:-1]
                    if name in school_bag.out:
                        del school_bag.out[name]
                    else:
                        error.print_error_msg(f'{name} is not in hand')
            elif not re.match("(Drink ).*[^ ].*", line) is None:  # Delete var
                if len(line_args) >= 2:
                    name = line[6:-1]
                    if name in school_bag.out:
                        del school_bag.out[name]
                    else:
                        error.print_error_msg(f'Error: {name} is not in hand')
            elif not re.match("(Replace ).*[^ ].*( with ).*[^ ].*", line) is None:  # Valuation
                if len(line_args) >= 4:
                    name1 = line[8:line.index(' with ')]
                    name2 = line[line.index(' with ') + 6:-1]
                    value2 = 0
                    if name1 not in school_bag.out:
                        error.print_error_msg(f'Error: {name1} is not in hand')
                    if name2 in school_bag.out:
                        value2 = school_bag.out[name2]
                    else:
                        error.print_error_msg(f'Error: {name2} is not in hand')
                    school_bag.place_out(name1, value2)
            elif not re.match("(Throw away ).*[^ ].*( and replace with ).*[^ ].*", line) is None:  # Valuation
                if len(line_args) >= 7:
                    name1 = line[11:line.index(' with ')]
                    name2 = line[line.index(' with ') + 6:-1]
                    value2 = 0
                    if name1 not in school_bag.out:
                        error.print_error_msg(f'Error: {name1} is not in hand')
                    if name2 in school_bag.out:
                        value2 = school_bag.out[name2]
                    else:
                        error.print_error_msg(f'Error: {name2} is not in hand')
                    school_bag.place_out(name1, value2)
            elif not re.match("(Add ).*[^ ].*( and ).*[^ ].*( together into ).*[^ ].*", line) is None:  # Add
                if len(line_args) >= 7:
                    add(line, 4)
            elif not re.match("(Mix ).*[^ ].*( and ).*[^ ].*( together into ).*[^ ].*", line) is None:  # Add
                if len(line_args) >= 7:
                    add(line, 4)
            elif not re.match("(Put ).*[^ ].*( and ).*[^ ].*( together into ).*[^ ].*", line) is None:  # Add
                if len(line_args) >= 7:
                    add(line, 4)
            elif not re.match("(Take ).*[^ ].*( out of ).*[^ ].*", line) is None:  # Subtract
                if len(line_args) >= 5:
                    name1 = line[5:line.index(' out of ')]
                    name2 = line[line.index(' out of ') + 8:-1]
                    if name1 in school_bag.out:
                        value1 = school_bag.out[name1]
                    else:
                        value1 = school_bag.default_value(name1)
                    if name2 in school_bag.out:
                        value2 = school_bag.out[name2]
                    else:
                        value2 = school_bag.default_value(name2)
                    school_bag.place_out(name2, value2 - value1)
            elif not re.match("(Drop ).*[^ ].*( out of ).*[^ ].*", line) is None:  # Subtract
                if len(line_args) >= 4:
                    name1 = line[5:line.index(' out of ')]
                    name2 = line[line.index(' out of ') + 8:-1]
                    if name1 in school_bag.out:
                        value1 = school_bag.out[name1]
                    else:
                        value1 = school_bag.default_value(name1)
                    if name2 in school_bag.out:
                        value2 = school_bag.out[name2]
                    else:
                        value2 = school_bag.default_value(name2)
                    school_bag.place_out(name2, value2 - value1)
            elif not re.match("(Drop ).*[^ ].*( from ).*[^ ].*", line) is None:  # Subtract
                if len(line_args) >= 4:
                    name1 = line[5:line.index(' from ')]
                    name2 = line[line.index(' from ') + 6:-1]
                    if name1 in school_bag.out:
                        value1 = school_bag.out[name1]
                    else:
                        value1 = school_bag.default_value(name1)
                    if name2 in school_bag.out:
                        value2 = school_bag.out[name2]
                    else:
                        value2 = school_bag.default_value(name2)
                    school_bag.place_out(name2, value2 - value1)
            elif not re.match("(Give out ).*[^ ].*( from ).*[^ ].*", line) is None:  # Subtract
                if len(line_args) >= 5:
                    name1 = line[5:line.index(' from ')]
                    name2 = line[line.index(' from ') + 6:-1]
                    if name1 in school_bag.out:
                        value1 = school_bag.out[name1]
                    else:
                        value1 = school_bag.default_value(name1)
                    if name2 in school_bag.out:
                        value2 = school_bag.out[name2]
                    else:
                        value2 = school_bag.default_value(name2)
                    school_bag.place_out(name2, value2 - value1)
            elif not re.match("(Slice ).*[^ ].*( into )[0-9]+( ).*[^ ].*( and take )[0-9]+", line) is None:  # Divide
                if len(line_args) >= 8:
                    name = line[6:line.index(' into ')]
                    divide_name = float(line_args[line_args.index("into") + 1])
                    having_name = float(line_args[-1])
                    if having_name > divide_name:
                        error.print_error_msg('Error: Loli can\'t take something is greater than its original is')
                    value = 0
                    if name in school_bag.out:
                        value = school_bag.out[name]
                    else:
                        error.print_error_msg(f'Error: {name} is not in hand')
                    school_bag.out[name] = (value / divide_name) * having_name
            elif not re.match("(Cut ).*[^ ].*( into )[0-9]+( ).*[^ ].*( and take )[0-9]+", line) is None:  # Divide
                if len(line_args) >= 8:
                    name = line[4:line.index(' into ')]
                    divide_name = float(line_args[line_args.index("into") + 1])
                    having_name = float(line_args[-1])
                    if having_name > divide_name:
                        error.print_error_msg('Error: Loli can\'t take something is greater than its original is')
                    value = 0.0
                    if name in school_bag.out:
                        value = school_bag.out[name]
                    else:
                        error.print_error_msg(f'Error: {name} is not in hand')
                    school_bag.out[name] = (value / divide_name) * having_name
            elif not re.match("(Split ).*[^ ].*( into )[0-9]+( ).*[^ ].*( and take )[0-9]+", line) is None:  # Divide
                if len(line_args) >= 8:
                    name = line[6:line.index(' into ')]
                    divide_name = float(line_args[line_args.index("into") + 1])
                    having_name = float(line_args[-1])
                    if having_name > divide_name:
                        error.print_error_msg('Error: Loli can\'t take something is greater than its original is')
                    value = 0.0
                    if name in school_bag.out:
                        value = school_bag.out[name]
                    else:
                        error.print_error_msg(f'Error: {name} is not in hand')
                    school_bag.out[name] = (value / divide_name) * having_name
            elif not re.match("(Keep ).*[^ ].*", line) is None:  # While var is not 0, it loops
                var = 0
                if line[5:-1] in school_bag.out:
                    var = school_bag.out[line[5:-1]]
                else:
                    error.print_error_msg(f'Error: {line[5:-1]} is not in hand')

                tabs = ''
                for i in range(0, loop_tab_amount):
                    tabs += '\t'

                for i in range(index, len(lines)):
                    line_in_keep = lines[i]
                    if line_in_keep.startswith(tabs):
                        loop[loop_tab_amount-1].append(line_in_keep[loop_tab_amount:])
                while var != 0:
                    run(loop[loop_tab_amount-1], False, False, loop_tab_amount + 1)
                    var = var - 1
            else:
                continue
            line_args.clear()
        else:
            error.print_error_msg('Error: Loli is still sleeping!')
    if check_sleep:
        error.print_error_msg('Warning: The day off, but loli is still not sleeping')


def read(filepath):
    file = open(filepath, encoding="utf-8")
    return file.readlines()


def add(line, start_index):
    name1 = line[start_index:line.index(' and ')]
    name2 = line[line.index(' and ') + 5:line.index(' together into ')]
    name3 = line[line.index(' together into ') + 15:-1]
    if name1 in school_bag.out:
        value1 = school_bag.out[name1]
    else:
        value1 = school_bag.default_value(name1)
    if name2 in school_bag.out:
        value2 = school_bag.out[name2]
    else:
        value2 = school_bag.default_value(name2)
    school_bag.take(name3, value1 + value2)
