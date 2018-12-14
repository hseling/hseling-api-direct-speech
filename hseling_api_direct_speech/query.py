from bs4 import BeautifulSoup


def query_data(query_type, contents, tags):
    if isinstance(contents, bytes):
        text = contents.decode('utf-8')
    else:
        text = contents
    tree = read_xml(text)
    print(query_type)
    if query_type == "tags":
        return {"tags": get_tags_from(tree, tags)}
    elif query_type == "statistics":
        return get_statistics(tree)
    elif query_type == "examples":
        return {"tags": get_examples(tree, tags)}
    else:
        return {"error": "incorrect query type"}


def get_tags_from(tree, tag):
    tag = tag["tag"]
    result = {}
    if "param" in tag:
        result[tag] = [i.text for i in tree.findAll(tag, tag["param"])]
    else:
        result[tag] = [i.text for i in tree.findAll(tag)]
    return result


def get_statistics(tree):
    return {"statistics": 0}


def get_examples(tree, tags):
    result = {}
    for tag in tags:
        result[tag] = [str(i) for i in tree.findAll(tag)]
    return result


def read_xml(text):
    return BeautifulSoup('<text>'+text+'</text>', "lxml")

