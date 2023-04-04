from bs4 import BeautifulSoup , sys,os
current_dir = os.getcwd()


print("\033c\033[44;30m");
# Carrega o arquivo HTML
with open(current_dir+"\\"+sys.argv[1]) as fp:
    soup = BeautifulSoup(fp,"html.parser")

# Encontra todas as tags que deseja substituir
tags = soup.find_all("tag")

# Substitui as tags pelo código de escape "\e"
for tag in tags:
    tag.replace_with( tag.text)

# Imprime o resultado na tela
print(soup.prettify())
