import os
import sys
import logging
from subprocess import call
from typing import List, Tuple
from rich import print as rprint
from rich.table import Table

logging.basicConfig(level=logging.DEBUG)


def get_file_to_crack() -> str:
    """
    Retrieve the path to the file containing password hashes.
    
    Returns:
        str: The absolute path to the cracked.txt file or the user-defined file path.
    """
    hashes = os.path.abspath('cracked.txt')
    if not os.path.isfile(hashes):
        hashes = input("Word list file: ")
    else:
        logging.info(f'cracked.txt found at {hashes}\n')

    return hashes


def list_current_directory_files() -> None:
    """
    List all files in the current directory.
    """
    curr_dir = os.listdir()
    for f in curr_dir:
        print(f)


def read_db_hashes(filename: str) -> List[str]:
    """
    Read database hashes from the specified file.
    
    Args:
        filename (str): The name of the file containing the hashes.
    
    Returns:
        List[str]: A list of hashes read from the file.
    """
    while True:
        try:
            with open(filename) as f:
                content = [line.strip() for line in f.readlines()]
            break
        except FileNotFoundError:
            logging.error("Please enter a valid file directory")

    return content


def run_hashcat(output_file_name: str, hashes: str) -> None:
    """
    Execute the hashcat command with the provided arguments.
    
    Args:
        output_file_name (str): The name of the output file containing parsed hashes.
        hashes (str): The path to the file containing password hashes.
    """
    logging.info("\nHere's what was found...\n")
    pot_file = "outfile.txt"
    with open(pot_file, "w") as pot:
        pot.truncate(0)
    call(["hashcat", "-m", "0", output_file_name, hashes, "-o", pot_file, "--potfile-disable"])


def parse_cracked_hashes() -> List[Tuple[str, str]]:
    """
    Parse the cracked hashes from the outfile.txt file.
    
    Returns:
        List[Tuple[str, str]]: A list of tuples containing the username and cracked password hash.
    """
    with open("outfile.txt") as new_f:
        out_content = [tuple(line.strip().split(":")) for line in new_f.readlines()]

    return out_content


def create_table() -> Table:
    """
    Create a table to display cracked passwords.
    
    Returns:
        Table: A Rich Table object with columns for the username and password.
    """
    table = Table(title="Cracked Passwords")
    table.add_column("Username", justify="left")
    table.add_column("Password", justify="left")

    return table


def main() -> None:
    """
    The main function for the password cracking script.
    """
    hashes = get_file_to_crack()
    while True:
        list_current_directory_files()

        user_pass_file_dir = input("\nWhat is the name of the file you want to crack? ")

        content = read_db_hashes(user_pass_file_dir)

        output_file_name = "parsed_hashes.txt"
        with open(output_file_name, 'w') as new_file:
            new_file.writelines(f"{line.split(':')[1]}\n" for line in content if ':' in line)

        run_hashcat(output_file_name, hashes)
        break

    table = create_table()

    hash_dict = dict(parse_cracked_hashes())

    for value in content:
        username, password = value.split(":")
        table.add_row(username, hash_dict.get(password, "Not found in table"))

    rprint(table)


if __name__ == '__main__':
    main()
