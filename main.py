import re
import music

def xmlparser(f):
    """
function that turns an xml file into a messy mix of tuples and lists

f is a text file that supports readlines()
"""
    stack = [("xml",[])]
    for line in f.readlines():
        line = line.strip()
        inline = re.fullmatch("<[^<>\/]+>[^<]+<\/[^<>\/]+>", line)
        opentag = re.fullmatch("<[^<>\/]+>", line)
        closetag = re.fullmatch("<\/[^>]+>", line)
        if line.startswith("<?"):
            continue
        if inline:
            tag = re.match("<[^<>\/]+>", line)
            content = line[tag.end(0):-(tag.end(0)+1)]
            stack[-1][1].append((tag.group(0)[1:-1],content))
        if opentag:
            stack.append((line[1:-1],[]))
        if closetag:
            stack[-2][1].append(stack.pop())
    return stack[0][1]

with open("testscore/test.mscx") as f:
    tree = xmlparser(f)
print(tree)