import pyttsx3
import os
import nltk
from PyPDF2 import PdfFileReader
from pdfminer.high_level import extract_text
import docx2txt

choice = input("Type of file\n1. PDF\n2. Word Document\n")

if int(choice) == 1:
	# path to PDF file
	pdf_file = input('Enter PDF path')
	if pdf_file != '':
		# obtain file name 
		base = os.path.basename(pdf_file)
		file_name, file_format = os.path.splitext(base)

		def pypdf2(pdfdf_file):
			py_pdf_file = open(pdf_file, 'rb') 
			# create PDFFileReader object to read the file
			pdfReader = PdfFileReader(py_pdf_file)
			# obtain no, of pages
			numOfPages = pdfReader.getNumPages()
			# final return text string
			#text = "PDF File name : " + str(pdfReader.getDocumentInfo().title)
			# text list to contain all pdf text 
			text_lst = list()
			# itterate over all pages
			for i in range(0, numOfPages):
				# obtain page no.
				pageObj = pdfReader.getPage(i)
				# append page content to list
				text_lst.append('\n' + pageObj.extractText())
			# close the PDF file object
			py_pdf_file.close()
			# join all pages text into single string variable
			text_temp = " ".join(text_lst)
			#return text + text_temp
			return text_temp

		def pdfminer(pdf_file):
			# extract text from pdf
			text = extract_text(pdf_file)
			return text
		text = pypdf2(pdf_file)

if int(choice) == 2:
	docx_path = input('Enter Docx path')
	if docx_path != '':
		text=docx2txt.process(docx_path)

def blooms(text):
	nltk_tokens = nltk.word_tokenize(text)
	#print(nltk_tokens)

	c1=c2=c3=c4=c5=c6=0

	level1=["choose","define",'find','how','label','list','match','name','omit','recall','relate','select','show',
	'spell','tell','what','why','when','who','where','which']
	level2=['classify','compare','contrast','demonstrate','explain','extend','illustrate','infer',
	'interpret','outline','relate','rephrase','show','summarize','translate']
	level3=['apply','build','choose','construct','develop','experiment with','identify','interview'
	'make use of','model','organize','plan','select','solve','utilize']
	level4=['analyze','assume','categorize','classify','compare','conclusion','contrast','discover',
	'dissect','distinguish','divide','examine','function','inference','inspect','list','motive','relationships',
	'simplify','survey','take part in','test for','theme']
	level5=['agree','appraise','assess','award','choose','compare','conclude','criteria',
	'criticize','decide','deduct','defend','determine','disprove','dispute','estimate',
	'evaluate','explain','importance','influence','interpret','judge','justify','mark',
	'measure','opinion','perceive','prioritize','prove','rate','recommend','rule on',
	'select','support','value']
	level6=['adapt','build','change','choose','combine','compile','compose','construct','create',
	'delete','design','develop','discuss','elaborate','estimate','formulate','happen','imagine',
	'improve','invent','make up','maximize','minimize','modify','original','originate','plan',
	'predict','propose','solution','solve','suppose','test','theory']

	for i in nltk_tokens:
	    if i in level1:
	        c1+=1
	    elif i in level2:
	        c2+=1
	    elif i in level3:
	        c3+=1
	    elif i in level4:
	        c4+=1
	    elif i in level5:
	        c5+=1
	    elif i in level6:
	        c6+=1
	l1=[c1,c2,c3,c4,c5,c6]

	print("\n")
	print("The paper has %d questions that come under the category of remember."%c1)
	print("The paper has %d questions that come under the category of understand."%c2)
	print("The paper has %d questions that come under the category of application."%c3)
	print("The paper has %d questions that come under the category of analysis."%c4)
	print("The paper has %d questions that come under the category of evaluate."%c5)
	print("The paper has %d questions that come under the category of creation."%c6)

	l2=sorted(l1)

	audio_ouput = None

blooms(text)