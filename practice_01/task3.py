from enum import Enum
from typing import Set, List, Dict
from dataclasses import dataclass


class AccessRules(Enum):
    READ = 'r'
    WRITE = 'w'
    EXECUTE = 'x'


class Commands(Enum):
    READ = 'read'
    WRITE = 'write'
    EXECUTE = 'execute'


commands_rules: Dict[Commands, AccessRules] = {
    Commands.EXECUTE: AccessRules.EXECUTE,
    Commands.WRITE: AccessRules.WRITE,
    Commands.READ: AccessRules.READ,
}


@dataclass
class File:
    name: str
    access_rules: Set[AccessRules]


def parse_access_rules(raw_access_rules: List[str]) -> Set[AccessRules]:
    access_rules = set()
    for raw_access_rule in raw_access_rules:
        try:
            access_rule = AccessRules(raw_access_rule)
        except BaseException:
            print(f'unknown rule: {raw_access_rule}')
        else:
            access_rules.add(access_rule)
    return access_rules


files: Dict[str, File] = {}


def init_file(raw_file: str):
    splitted_raw_file = raw_file.split(' ')
    name = splitted_raw_file[0]
    raw_access_rules = splitted_raw_file[1:]
    access_rules = parse_access_rules(raw_access_rules)
    file = File(name=name, access_rules=access_rules)
    files[name] = file


def init_files(files_number: int):
    for i in range(files_number):
        raw_file = input(f'Enter file[{i + 1}|{files_number}]: ')
        init_file(raw_file)


def execute_command(raw_command: str):
    splitted_raw_command = raw_command.split(' ')
    command_name = splitted_raw_command[0]
    try:
        command = Commands(command_name)
    except BaseException:
        print(f'unknown command: {command_name}')
        return
    try:
        filename = splitted_raw_command[1]
    except BaseException:
        print('empty filename')
        return
    try:
        file = files[filename]
    except KeyError:
        print(f'file with name {filename} does not exists')
        return
    command_rule = commands_rules[command]
    if command_rule in file.access_rules:
        return "OK"
    return "Access denied"


def execute_commands(commands_number: int):
    for i in range(commands_number):
        raw_command = input(f'Enter command[{i + 1}|{commands_number}]: ')
        result = execute_command(raw_command)
        if result:
            print(result)


def main():
    files_number = int(input('Enter files number: '))
    init_files(files_number);
    commands_number = int(input('Enter commands number: '))
    execute_commands(commands_number)


if __name__ == "__main__":
    main()
