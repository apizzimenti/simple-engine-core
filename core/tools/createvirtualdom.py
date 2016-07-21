#!/usr/bin/env python3


def createvirtualdom(element):

    obj = {
        "option": element["id"],
        "attrs": element.attrs,
        "type": element.name,
        "text": element.contents[0].strip(),
        "children": {}
    }

    children = element.find_all(True, recursive=False)

    if children:
        for child in children:
            obj["children"][child["id"]] = createvirtualdom(child)

    return obj
