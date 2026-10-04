from parser.pdf_reader import extract_text

text = extract_text("../samples/dp83tc818s-q1.pdf")

print(text[:2000])
