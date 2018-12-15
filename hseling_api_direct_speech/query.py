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


def get_tags_from(tree, tag_with_param):
    tag = tag_with_param["tag"]
    result = {}
    if "param" in tag_with_param:
        return [i.text for i in tree.findAll(tag, tag_with_param["param"])]
    else:
        return [i.text for i in tree.findAll(tag)]
    return result


def get_statistics(tree):
    result = {}
    tags_with_params = {"speech":[], "said":["type", "aloud"], "author_comment":[], "speech_verb":["semantic", "emotion"]}
    for tag in tags_with_params:
        result[tag] = len(tree.findAll(tag))
        for param in tags_with_params[tag]:
            result[tag+"_"+param] = len(tree.findAll(tag, ))
    return result


def get_examples(tree, tags):
    result = {}
    for tag in tags:
        result[tag] = [str(i) for i in tree.findAll(tag)]
    return result


def read_xml(text):
    return BeautifulSoup('<text>'+text+'</text>', "lxml")

filepath = "C:/Users/Irina/Downloads/PortableGit/hseling-api-direct-speech/app/static/gold.txt"
with open(filepath, "r", encoding="utf-8") as r:
    text = r.read()
tree = read_xml(text)
print(len(get_tags_from(tree, {"tag":"speech_verb", "param":{"characteristics": "neutral"}})))