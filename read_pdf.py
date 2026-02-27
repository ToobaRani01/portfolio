import sys
try:
    import fitz
    print("Testing PyMuPDF...")
    doc = fitz.open(sys.argv[1])
    text = ""
    for page in doc:
        text += page.get_text()
    print(text[:1000])
except ImportError:
    print("No PyMuPDF, trying PyPDF2...")
    try:
        import PyPDF2
        with open(sys.argv[1], 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for i in range(len(reader.pages)):
                text += reader.pages[i].extract_text()
            print(text[:1000])
    except Exception as e:
        print("Failed to read PDF:", e)
