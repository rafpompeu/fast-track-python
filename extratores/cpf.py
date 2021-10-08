import re

adress = "Rua da Flores 72, apartamento 1, Laranjeiras, Belém, PA, 66045-120"

padron = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
search = padron.search(adress) 
if search:
    cep = search.group()
    print(cep)