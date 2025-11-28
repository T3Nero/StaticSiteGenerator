def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            # strip the leading "# " and return the rest as the title
            return line[2:].strip()
        else:
            raise Exception("extract_title('# Hello') should return 'Hello' (strip the leading #)")
    return "Untitled"