from bs4 import BeautifulSoup


def query_data(query_type, contents, tags):
    if isinstance(contents, bytes):
        text = contents.decode('utf-8')
    else:
        text = contents
    print(query_type)
    if query_type == "tags":
        return {"tags": get_tags_from(text, tags)}
    elif query_type == "statistics":
        return {"statistics": 0}
    elif query_type == "examples":
        return {"tags": get_examples(text, tags)}
    else:
        return {"error": "incorrect query type"}


def get_tags_from(text, taglist):
    tags = taglist["tags"]
    result = {}
    tree = read_xml(text)
    for tag in tags:
        result[tag] = [i.text for i in tree.findAll(tag)]
    if "params" in taglist:
        params = taglist["params"]
    return result


def get_examples(text, tags):
    result = {}
    tree = read_xml(text)
    for tag in tags:
        result[tag] = [str(i) for i in tree.findAll(tag)]
    return result


def read_xml(text):
    return BeautifulSoup('<text>'+text+'</text>', "lxml")

