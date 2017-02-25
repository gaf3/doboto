import re
import yaml
import json
from doboto.DO import DO

do = DO(token="secret")

DEFINITIONS = re.compile('def (\w+)\(\s*?(.+)\s*?\)')


def write_data(doc_file, args, indent=""):

    if isinstance(args, list):
        for arg in args:
            write_data(doc_file, arg, indent)
    elif isinstance(args, dict):
        for key, value in args.iteritems():
            write_data(doc_file, key, indent)
            write_data(doc_file, value, "%s  " % indent)
    elif isinstance(args, basestring):
        if " - " in args:
            (name, rest) = args.split(" - ", 1)
            doc_file.write("%s- *%s* - %s\n\n" % (indent, name, rest))
        else:
            doc_file.write("%s- %s\n\n" % (indent, args))


for sub_name in dir(do):

    sub = getattr(do, sub_name)

    if callable(sub) or sub_name[:2] == "__":
        continue

    sub_doc = yaml.load(sub.__doc__)

    print sub_name
    print sub.__class__.__name__
    print json.dumps(sub_doc, indent=2, sort_keys=True)

    sub_file = open("doboto/%s.py" % sub.__class__.__name__, "rb")
    sub_text = sub_file.read()
    sub_file.close()

    doc_file = open("docs/%s.rst" % sub_name, "wb")

    doc_file.write(""".. DOBOTO documentation sub class file, created bysphinxter.py.

%s (do.%s)
============================================

%s
""" % (sub.__class__.__name__, sub_name, sub_doc["description"].replace("\n", "\n\n")))

    method_order = []
    method_args = {}
    for definition in DEFINITIONS.findall(sub_text):

        if definition[0] == '__init__':
            continue

        method_order.append(definition[0])
        method_args[definition[0]] = definition[1].split(', ')

    methods = {}
    for method_name in dir(sub):

        method = getattr(sub, method_name)

        if not callable(method) or method_name[:2] == "__":
            continue

        methods[method_name] = method

    print methods

    for method_name in method_order:

        if method_name not in methods:
            continue

        method_doc = yaml.load(methods[method_name].__doc__)

        if "description" not in method_doc:
            continue

        print "%s.%s" % (sub_name, method_name)
        print method_args[method_name][1:]
        print json.dumps(method_doc, indent=2, sort_keys=True)

        intitial_description = method_doc["description"].split("\n")[0]
        full_description = ""

        if "\n" in method_doc["description"]:
            full_description = "\n%s\n" % method_doc["description"].split("\n",1)[1:][0]

        doc_file.write("""\n\n%s
----------------------------------------------------------------------------------------------------
%s
.. method:: do.%s.%s(%s)

""" % (
            intitial_description,
            full_description.replace("\n", "\n\n"),
            sub_name,
            method_name,
            ", ".join(method_args[method_name][1:])
    ))

        if "in" in method_doc:
            write_data(doc_file, method_doc["in"])

        if "out" in method_doc:
            doc_file.write("\nReturns:\n\n")
            write_data(doc_file, method_doc["out"])

        if "related" in method_doc:

            related = method_doc["related"]

            if not isinstance(related, list):
                related = [related]

            doc_file.write("\n\nRelated:\n\n")

            for link in related:
                doc_file.write("* `<%s>`_\n\n" % link)
