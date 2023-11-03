#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a vari├ível LANG devidamente configurada ex:

   export LANG=pt_BR

Execu├º├úo:

     python3 hello.py
     ou
     ./hello.py
"""
__version__="0.0.1"
__author__= "Luiz Rocha"
__lincense__= "Unlicense"

import os 

current_language =  os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"


if current_language == "pt_BR":
   msg = "Ol├í, Mundo!"
elif current_language == "it_IT":
   msg = "Ciao, Mondo!"
elif current_language == "fr_FR":
   msg = "Bonjour le monde!"
print(msg)  # bult-in (J├í vem incluida na linguagem)
