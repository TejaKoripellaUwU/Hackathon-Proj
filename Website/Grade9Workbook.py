import pylatex.basic
from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape, bold
from pylatex import *
from Website.Grade9 import*
from Website import Grade9
import random
from pdflatex import PDFLaTeX
import pylatex as pl


def fill_document(doc):
    """Add a section, a subsection and some text to the document.

    :param doc: the document
    :type doc: :class:pylatex.document.Document instance
    """
    with doc.create(Section('A section')):
        doc.append('Some regular text and some ')
        doc.append(italic('italic text. '))

        with doc.create(Subsection('A subsection')):
            doc.append('Also some crazy characters: $&#{}')

def problemSection(doc):
    doc.append(NoEscape('\huge'))
    doc.append(NoEscape(r'\vspace*{\fill}'))
    doc.append(NoEscape(r'\begin{center}'))
    doc.append(NoEscape('Problems'))
    doc.append(NoEscape(r'\end{center}'))
    doc.append(NoEscape(r'\vspace*{\fill}'))
    doc.append(NoEscape(r'\pagebreak'))
    doc.append(NoEscape(r'\normalsize'))
    return doc


def solutionSection(doc):
    doc.append(NoEscape('\huge'))
    doc.append(NoEscape(r'\vspace*{\fill}'))
    doc.append(NoEscape(r'\begin{center}'))
    doc.append(NoEscape('Solutions'))
    doc.append(NoEscape(r'\end{center}'))
    doc.append(NoEscape(r'\vspace*{\fill}'))
    doc.append(NoEscape(r'\normalsize'))
    doc.append(NoEscape(r'\pagebreak'))
    return doc


def genProblems(doc):
    s=[]

    for j in range(0, len(functions)):
        l=[]
        for i in range(1, 5):
            doc.append(NoEscape('\large'))
            doc.append(NoEscape(r'\begin{center}'))
            title=r'\textbf{' + functions[j][0] + '- Worksheet ' + str(i) + '}'
            doc.append(NoEscape(title))
            doc.append(NewLine())
            doc.append(NewLine())
            doc.append(NewLine())
            doc.append(NoEscape(r'\end{center} \normalsize'))

            problems, solutions=functions[j][1]
            l2=[]
            for k in range(0, len(problems)):
                doc.append(NoEscape(problems[k]))
                doc.append(NewLine())
                doc.append(NewLine())
                doc.append(NewLine())
                l2.append(solutions[k])

            l.append(l2)


            doc.append(NoEscape(r'\pagebreak'))

        s.append(l)

    return doc, s

def genSolutions(doc, s):
    #print(len(s))
    for j in range(0, len(s)):
        for i in range(0, 4):
            doc.append(NoEscape('\large'))
            doc.append(NoEscape(r'\begin{center}'))
            title=r'\textbf{' + functions[j][0] + '- Solution ' + str(i+1) + '}'
            doc.append(NoEscape(title))
            doc.append(NewLine())
            doc.append(NoEscape(r'\end{center} \normalsize'))
            #doc.append(NoEscape(r'\normalsize'))

            for k in (s[j][i]):
                doc.append(NoEscape(k))
                doc.append(NewLine())
            doc.append(NewPage())

    return doc


def title(doc):
    doc.packages.append(Package('tikz'))
    doc.packages.append(Package('pgfplots'))
    doc.preamble.append(Command('title', 'Algebra 1 Math Workbook'))
    doc.preamble.append(Command('author', 'Akshai Srinivasan, Teja Koripella, Skye Tyrrell, Angellou Sutharsan'))
    doc.preamble.append(Command('date', ''))
    doc.append(NoEscape(r'\maketitle'))
    doc.append(NoEscape(r'\vfill'))
    doc.append(NoEscape(r'\begin{center}'))
    doc.append("ISBN: 9798848825312")
    doc.append(NoEscape(r'\linebreak'))
    doc.append(NoEscape(r'\copyright'))
    doc.append('MathMaestro.org 2022')
    doc.append(NoEscape(r'\end{center}'))
    doc.append(NewPage())

    return doc


def tableOfContents(doc):

    with doc.create(Section('Table of Contents')):

        doc.append("Problems...........................................................................................Page 3")
        doc.append(NewLine())
        page=4
        for i in range (0, len(functions)):
            doc.append(functions[i][0])
            numOfDots=round((58-(len(functions[i][0])))*1.81034483)
            for j in range(0, numOfDots):
                doc.append(".")
            if (i==len(functions)-1):
                if (functions[i][0]=="Finding the Equation of a Line"):
                    doc.append("Page " + str(page) + "-" + str(page + (19)))
                    page+=19
                else:
                    doc.append("Page " + str(page) + "-" + str(page+((4*(3+functions[i][2]))+1)))
                    page += ((4*(3+functions[i][2]))+1)
            else:
                if (functions[i][0]=="Finding the Equation of a Line"):
                    doc.append("Page " + str(page) + "-" + str(page + (19)))
                    page+=20
                else:
                    doc.append("Page " + str(page) + "-" + str(page + ((4 * (3 + functions[i][2]))-1)))
                    page += ((4 * (3 + functions[i][2])))
            doc.append(NewLine())
        page += 1
        doc.append("Solutions......................................................................................Page " + str(page) )
        doc.append(NewLine())
        page+=1
        for i in range (0, len(functions)):
            doc.append(functions[i][0] + " Solutions")
            numOfDots=round((58-(len(functions[i][0] + " Solutions")))*1.81034483)
            for j in range(0, numOfDots):
                doc.append(".")
            doc.append("Page " + str(page) + "-" + str((page+((4 * (1 + functions[i][3]))))-1))
            page+=((4 * (1 + functions[i][3])))
            doc.append(NewLine())
        doc.append(NewPage())

    return doc

def genA1Book():
    doc = Document()

    # Make title
    doc=title(doc)

    # Make how to use page

    doc=tableOfContents(doc)

    doc=problemSection(doc)

    doc, s=genProblems(doc)

    doc=solutionSection(doc)
    doc=genSolutions(doc, s)

    # Generate .tex file
    try:
        doc.generate_pdf('Grade9Workbook', clean_tex=False)
    except:
        print("error")

genA1Book()