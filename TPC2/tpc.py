import re

header = re.compile("^\#\s+(.*)")
header2 = re.compile("^\#{2}\s+(.*)$")
header3 = re.compile("^\#{3}\s+(.*)$")
bold = re.compile("\*\*([^*]+)\*\*$")
italic = re.compile("^\*([^*]+)\*$")
block_quote = re.compile("^>\s+(.*)$")
ordered_list = re.compile("^\d+\.\s+(.*)$")
unordered_list = re.compile("^\-\s+(.*)$")  
code = re.compile("^`(.*)`$")
horizontal_rule = re.compile("^--$")
link = re.compile("^\[(.*)\]\((.*)\)$")
image = re.compile("^!\[(.*)\]\((.*)\)$")

replacements = {
    header: r"<p><h1>\1</h1></p>",
    header2: r"<p><h2>\1</h2></p>",
    header3: r"<p><h3>\1</h3></p>",
    bold: r"<p><b>\1</b></p>",
    italic: r"<p><i>\1</i></p>",
    block_quote: r"<p><blockquote>\1</blockquote></p>",
    code: r"<p><code>\1</code></p>",
    horizontal_rule: r"<p><hr></p>",
    link: r"<p><a href='\2'>\1</a></p>",
    image: r"<p><img src='\2' alt='\1'></p>"
}

def transformer(filename):
    with open(filename, "r") as f: 
        lines = f.readlines()

    in_ordered_list = False
    in_unordered_list = False

    for i, line in enumerate(lines):
        for pattern, replacement in replacements.items():
            line = pattern.sub(replacement, line)

        if ordered_list.match(line) and not in_ordered_list:
            line = "<ol><li>\n" + line[2:] + "</li>"
            in_ordered_list = True
        elif not ordered_list.match(line) and in_ordered_list:
            line = "</ol>\n" + line
            in_ordered_list = False
        elif ordered_list.match(line):
            line = "<li>" + line[2:] + "</li>"

        if unordered_list.match(line) and not in_unordered_list:
            line = "<ul><li>\n" + line[2:] + "</li>"
            in_unordered_list = True
        elif not unordered_list.match(line) and in_unordered_list:
            line = "</ul>\n" + line
            in_unordered_list = False
        elif unordered_list.match(line):
            line = "<li>" + line[2:] + "</li>"
        
        lines[i] = line

    data = "".join(lines)

    return data
    

final = """
    <!DOCTYPE html>
    <html>
    """ + transformer("test.md") + """
    </html>
    """

with open("test.html", "w") as file:
    file.write(final)

