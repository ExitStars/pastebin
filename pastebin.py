#-*-coding:utf-8-*-
from os.path import split, splitext
from modules.panel import Panel
from json import loads, dumps
from os import system, name
from pyperclip import copy
from requests import post
from time import strftime
from re import findall
from sys import argv

bold, underline, endcolor = "\033[1m", "\033[4m", "\033[0m"
green, blue, yellow, red = "\033[92m", "\033[94m", "\033[93m", "\033[91m"

def logo():
    system("clear")
    print "--==["+bold+blue+"nickname"+endcolor+"] [ MuReCoder"
    print "--==["+bold+yellow+"MyGitHub"+endcolor+"] [ https://github.com/MuReCoder"
    print "--==["+bold+green+"software"+endcolor+"] [ Pastebin Code Share v0.1"
    print "-"*45

def sending(script, jData):
    fName, ext = script
    fileName = fName+ext
    code = open(fileName, "r").read()
    langu = {".txt": "text", ".vb": "basic", ".asm": "x86asm", ".aspx": "aspectj", ".py": "py", ".html": "html", ".rb": "rb", ".php": "php"}
    lang = langu[ext]
    data = {"title": str(fName),
        "poster": str(jData[0]["poster"]),
        "lastday": "long",
        "codes": str(code),
        "lang": str(lang)
    }
    request = post("http://pastebin.yeg/index.php", data = data).text
    bul = findall("RSS (.*?) KID", request)
    print bold+yellow+"[+] Ekleme Başarılı: http://pastebin.yeg/code.php?kid="+str(bul[0])+endcolor

    try:
        lData = loads(open("json/pasteList.json", "r").read())
    except:
        lData = []

    newData = {"kid": str(bul[0]),
        "poster": str(jData[0]["poster"]),
        "baslik": str(fName),
        "tarih": str(strftime("%Y-%m-%d %H:%M:%S"))
    }
    lData.append(newData)

    file = open("json/pasteList.json", "w")
    file.write(dumps(lData))
    file.close()

    link = "http://pastebin.yeg/code.php?kid="+str(bul[0])
    copy(link)

def scriptParse(script):
    fileName, ext = splitext(script)
    return fileName, ext

def main():
    if len(argv) == 1:
        print bold+red+"[!] Lütfen Eklenecek Dosyaları Giriniz."+endcolor
        print "-"*45
    elif argv[1] == "--panel":
            panel = Panel()
            panel.panel()
    else:
        try:
            jData = loads(open("json/ayar.json", "r").read())
        except Exception as e:
            print bold+red+"[!] Ayar Dosyasi Bulunamadı!"+endcolor
            jData = [{"name": "CodeSH", "poster": "esw0rmer"}]
        scripts = map(scriptParse, argv[1:])
        for script in scripts:
            sending(script, jData)

if __name__ == '__main__':
    if name == "posix":
        logo()
        main()
    else:
        logo()
        print bold+red+"Program v0.1 Sürümü Sadece Linux İçindir."+endcolor
        print "-"*45
        exit()
