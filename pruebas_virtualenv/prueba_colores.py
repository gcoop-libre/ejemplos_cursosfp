import colorama
#from colorama import init, Fore, Back

colorama.init()

print colorama.Fore.RED + colorama.Back.GREEN + 'esto es rojo'
print colorama.Fore.RESET + colorama.Back.RESET + "esto ya no tambien"
