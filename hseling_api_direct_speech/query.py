from bs4 import BeautifulSoup


def query_data(contents, tags):
    if isinstance(contents, bytes):
        text = contents.decode('utf-8')
    else:
        text = contents
    tag_result = {}
    param_result = {}
    if "tags" in tags:
        tag_result = get_tags_from(text, tags["tags"])
    if "params" in tags:
        param_result = get_params_from(text, tags["params"])
    return {"tags": tag_result, "params": param_result}


def get_tags_from(text, taglist):
    result = {}
    tree = read_xml(text)
    for tag in taglist:
        result[tag] = [i.text for i in tree.findAll(tag)]
    return result


def get_params_from(text, params):
    result = {}
    tree = read_xml(text)
    for param in params:
        all_results = tree.select("[{}]".format(param))
        result[param] = [i[param] for i in all_results]
    return result


def read_xml(text):
    return BeautifulSoup('<text>'+text+'</text>', "lxml")

