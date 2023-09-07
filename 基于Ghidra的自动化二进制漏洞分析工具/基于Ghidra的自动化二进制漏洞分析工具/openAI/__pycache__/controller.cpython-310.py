# Visit https://www.lddgo.net/string/pyc-compile-decompile for more information
# Version : Python 3.10

import openai
import tiktoken
from prettytable import PrettyTable, ALL
Colors = {
    'RED': '\x1b[1;31m',
    'YELLOW': '\x1b[1;33m',
    'BLUE': '\x1b[1;34m',
    'CYAN': '\x1b[1;36m',
    'WHITE': '\x1b[1;37m',
    'GREEN': '\x1b[0;32m',
    'RESET': '\x1b[0;0m',
    'BOLD': '\x1b[;1m',
    'REVERSE': '\x1b[;7m' }

class OpenAI:
    
    def __init__(self, controller):
        self.apiKey = controller.apiKey
        self.vulnExistenceKey = 'contains a security vulnerability'
        self.prompt = ''

    
    def davinci(self, promptData, model):
        openai.api_key = self.apiKey
    # WARNING: Decompyle incomplete

    
    def analyzeC(self, function, semgrep):
        vulnInspection = ''
        self.prompt = 'Please start with analyzing this C function for any security vulnerabilities with the highest accuracy possible. Here is the output from the semgrep static analysis tool: ' + semgrep + 'Please validate, refute or use this data to aid with the vulnerability analysis of the function. Please identify if any additional vulnerabilities exist and                             add any additional findings that may differ from the provided semgrep data.                            Here is the C function to analyze: \n' + function
        if self.calcToken() > 4096:
            vulnInspection = self.davinci(self.prompt, 'gpt-3.5-turbo-16k')
            print(Colors['YELLOW'] + '[+] Using gpt-3.5-turbo-16k model for AI analysis' + Colors['RESET'])
            return vulnInspection
        vulnInspection = None.davinci(self.prompt, 'gpt-3.5-turbo')
        print(Colors['YELLOW'] + '[+] Using gpt-3.5-turbo model for AI analysis' + Colors['RESET'])
        return vulnInspection

    
    def calcToken(self):
        enc = tiktoken.get_encoding('cl100k_base')
        encoded = enc.encode(self.prompt)
        return len(encoded)