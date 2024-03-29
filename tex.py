import re
import sys

def count_words(document_content):
    # this ignores:
    exclusion_pattern = (
        r'\\begin\{minted\}[\s\S]*?\\end\{minted\}'  # minted blocks
        r'|\\[a-zA-Z]+(?:\[[^\]]*\])?(?:\{.*?\})?'   # LaTeX commands, with optional [] and optional {}
        r'|(?<=\s)%.*?\n'                            # comments
    )

    # gets all the words
    cleaned_document = re.sub(exclusion_pattern, ' ', document_content, flags=re.DOTALL|re.MULTILINE)
    words = re.findall(r"\b\w+(?:['’.-]\w+)?\b", cleaned_document)

    return len(words)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tex.py <tex_path>")
        sys.exit(1)

    tex_path = sys.argv[1]
    with open(tex_path, 'r', encoding='utf-8') as file:
        tex_content = file.read()
    
    word_count = count_words(tex_content)
    print("Total words in the document:", word_count)
