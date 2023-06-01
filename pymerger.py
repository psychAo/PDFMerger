import os
from PyPDF2 import PdfMerger
 
def merge_pdf(pdf_path):
 
    pdf_lst = [f for f in os.listdir(pdf_path) if f.endswith('.pdf')]
    pdf_lst = [os.path.join(pdf_path, pdf_name) for pdf_name in pdf_lst]
 
    pdf_merger = PdfMerger() # 实例化
 
    for pdf in pdf_lst: # 逐个读取需要合并的pdf文件
        with open (pdf, 'rb') as input:
            pdf_merger.append(input)
 
    with open ('output.pdf','wb') as output:
        pdf_merger.write(output) # 将多个pdf文件合并后保存为output.pdf
 
 
if __name__ == '__main__':
 
    pdf_path = 'C:\\Users\\xxx\\Desktop\\' # 相对路径，多个需要合并的pdf文件存放在pre_pdf文件夹下
    merge_pdf(pdf_path)
