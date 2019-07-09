from argparse import ArgumentParser
from bs4 import BeautifulSoup
from pygments.lexers import guess_lexer_for_filename, get_lexer_by_name
from pygments.lexers.python import Python3Lexer
from pygments.util import ClassNotFound
from colorama import Fore, Style
from getpass import getuser
from typing import List, Dict, Any
import requests
import pathlib

LANG_FILE = pathlib.Path(__file__).absolute().parent / 'langs.txt'


def log(text: str, level: str = 'info'):
    levels = {
        'success': Fore.GREEN,
        'info': Fore.LIGHTCYAN_EX,
        'warn': Fore.YELLOW,
        'error': Fore.RED
    }
    print(f"{levels.get(level)}{text}")
    print(Style.RESET_ALL, end="")


class Sloth:
    URL = "https://paste.ubuntu.com"
    soup: BeautifulSoup = None

    def __init__(self, *args: List, **kwargs: Dict[str, str]):
        self.options = kwargs
        log(f'[i] {len(self.options["file"])} files entered...')
        log(f"[i] Poster: {self.options['poster']}...")
        print(f"{'=' * 30}")
        for file in self.options['file']:
            payload = self.prepare_payload(file)
            if payload:
                share_link = self.get_link(payload)
                log(f"[+] Paste link: {share_link}", 'success')
            print(f"\n{'=' * 30}\n")
            

    def prepare_payload(self, file) -> Dict[str, str]:
        log(f"[i] File: {file}")
        payload = dict()
        try:
            with open(file, 'r') as file_obj:
                file_content = file_obj.read()
            
            if self.options.get('syntax'):
                wanted_lang = self.options.get('syntax').lower()
                langs = [line.rstrip('\n') for line in LANG_FILE.open(mode='r')]
                
                if wanted_lang in langs:
                    syntax_type = wanted_lang
                else:
                    syntax_type = 'text'
                    log(f"[*] {wanted_lang} language not not supported by {self.URL}") 
            else:    
                syntax_type = guess_lexer_for_filename(file, file_content).aliases[0]

            if syntax_type in ['python2', 'python']:
                syntax_type = 'python3'    ## Python 2 is dead, Just Python 3
            log(f"[i] Detected language {syntax_type}")



        except ClassNotFound:
            syntax_type = 'text'
            log(f"[*] Language not detected. Used raw text")
        
        payload = {
            'poster': self.options['poster'],
            'syntax': syntax_type,
            'content': file_content,
        }
        if not self.options.get('exp') is None:
            log(f"[*] Expiration: {self.options['exp']}")
            payload['expiration'] = self.options['exp']

        return payload

        

    def get_link(self, payload: Dict[str, str]):
        req = requests.post(self.URL, data=payload)
        self.soup = BeautifulSoup(req.text, "html.parser")
        
        return f"{self.URL}{self.soup.a.get('href').replace('plain/', '')}"


def main():
    parser = ArgumentParser(description="Code sharing app for lazy people.")
    parser.add_argument('file', nargs="+", help="File to share content")
    parser.add_argument(
        '-p', '--poster', default=getuser(), help="Author name")
    parser.add_argument('--syntax', help="Desired syntax (py, js, cpp...)")
    parser.add_argument(
        '--exp', choices=['day', 'week', 'year'], help="Expiration time")

    args = parser.parse_args()
    Sloth(**vars(args))


if __name__ == '__main__':
    main()
