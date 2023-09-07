#!/usr/bin/env python
# visit https://tool.lu/pyc/ for more information
# Version: Python 3.9

import os
import time
import openai
import json
from prettytable import PrettyTable, ALL

RED = "[1;31m"
YELLOW = "[1;33m"
BLUE = "[1;34m"
CYAN = "[1;36m"
WHITE = "[1;37m"
GREEN = "[0;32m"
RESET = "[0;0m"
BOLD = "[;1m"
REVERSE = "[;7m"


class OpenAI:
    def __init__(self):
        self.api_key = "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"
        self.vulnExistenceKey = "<span>"

    def davinci(self, promptData):
        openai.api_key = self.api_key
        response = openai.Completion.create(
            "text-davinci-003",
            promptData,
            0,
            500,
            **("model", "prompt", "temperature", "max_tokens")
        )
        resp = json.loads(json.dumps(response))
        resp = resp["choices"][0]["text"]
        if self.vulnExistenceKey in resp:
            resp = resp.replace("<span>", RED)
            resp = resp.replace("</span>", YELLOW)
            return resp
        return None

    def analyzeC(self):
        responseContent = {}
        f = open("output.c", "r")
        contents = f.read()
        functions = contents.split("~~~~~")
        tick = 0
        for function in functions:
            if tick < 2:
                print("[+] Analyzing...")
                vulnInspection = self.davinci(
                    "Please analyze this C function and determine if any security vulnerabilities exist. If vulnerabilities are found,                                               please wrap the vulnerable components of the C code in <span> tags, not the comments, add code comments containing explanations about the vulnerability above the vulnerable components,                                               add line numbers to the comments as well, and return the function.                                              Here is the C function to analyze: "
                    + function
                )
                if vulnInspection is not False:
                    responseContent[tick] = [vulnInspection, function]
                else:
                    print("Not Vulnerable")
            tick += 1
        return responseContent