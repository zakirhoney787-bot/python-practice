# from pypdf import PdfWriter

# pdfs=[]
# number= int(input("how many pdfs you want to merge in ? ===> "))
# for i in range(number):
#     name =input("what is the name of the pdf")
#     pdfs.append(name)

# from pypdf import PdfMerger

# # 1. Initialize the merger
# merger = PdfMerger()

# # 2. Append your files
# merger.append("safari.pdf")
# merger.append("safari2.pdf")

# # 3. Write and close
# merger.write("combined_output.pdf")
# merger.close()


from pypdf import PdfWriter

merger = PdfWriter()

pdfs = ["safari.pdf", "safari2.pdf"]

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
print("PDFs merged successfully!")