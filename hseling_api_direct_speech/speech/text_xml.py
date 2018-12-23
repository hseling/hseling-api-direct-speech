# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from sentimental import Sentimental

sent = Sentimental()

path = 'C:/Users/Irina/Downloads/PortableGit/speech/code/output/raw.txt'


def read_xml(text):
    return BeautifulSoup(text, "lxml")


def add_attributes(xml):
    saids = xml.findAll('said')
    for said in saids:
        said['aloud'] = 'True'
        said['type'] = 'direct'
        said['characteristic'] = define_characteristic(said)


def define_characteristic(said):
    result = sent.analyze(said.text)
    result = {'negative': result['negative'], 'positive': result["positive"]}
    if result['negative'] == result['positive']:
        sentiment = 'neutral'
    else:
        sentiment = sorted(result.items(),
                           key=lambda x: x[1], reverse=True)[0][0]
    return sentiment


with open(path, 'r', encoding='utf-8') as f:
    root = read_xml(f.read())
    speeches = root.find_all('speech')
    for i in speeches:
        print(i.text)
        print()

# ml for who said
# косяки с удалением тире и прочих знаков между тегами
