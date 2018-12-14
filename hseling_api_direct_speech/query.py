from bs4 import BeautifulSoup


def query_data(query_type, contents, tags):
    if isinstance(contents, bytes):
        text = contents.decode('utf-8')
    else:
        text = contents

    if query_type == "tags":
        return {"tags": get_tags_from(text, tags["tags"], tags["params"])}
    elif query_type == "statistics":
        return {"statistics": 0}
    elif query_type == "examples":
        return {"tags": get_tags_from(text, ["text"])}
    else:
        return {"error": "incorrect query type"}


def get_tags_from(text, taglist, paramlist=None):
    result = {}
    tree = read_xml(text)
    for tag in taglist:
        result[tag] = [i.text for i in tree.findAll(tag)]
    return result


def read_xml(text):
    return BeautifulSoup('<text>'+text+'</text>', "lxml")

