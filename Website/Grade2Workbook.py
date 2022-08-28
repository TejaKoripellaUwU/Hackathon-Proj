from pylatex.utils import italic, bold
from pylatex import *

from Website import Grade2
from Website.Grade2 import *


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

    for j in range(0, len(g2Functions)):
        l=[]
        for i in range(1, 5):
            doc.append(NoEscape('\large'))
            doc.append(NoEscape(r'\begin{center}'))
            title=r'\textbf{' + g2Functions[j][0] + '- Worksheet ' + str(i) + '}'
            doc.append(NoEscape(title))
            doc.append(NewLine())
            doc.append(NoEscape(r'\end{center} \normalsize'))
            #doc.append(NoEscape(r'\normalsize'))

            f = getattr(Grade2, g2Functions[j][1])
            problems, solutions=f(30)
            l2=[]
            for k in range(0, len(problems)):
                doc.append(problems[k])
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
            title=r'\textbf{' + g2Functions[j][0] + '- Solution ' + str(i+1) + '}'
            doc.append(NoEscape(title))
            doc.append(NewLine())
            doc.append(NoEscape(r'\end{center} \normalsize'))
            #doc.append(NoEscape(r'\normalsize'))

            for k in (s[j][i]):
                doc.append(k)
                doc.append(NewLine())
            doc.append(NewPage())

    return doc


def title(doc):

    doc.preamble.append(Command('title', 'Grade 2 Math Workbook'))
    doc.preamble.append(Command('author', 'Akshai Srinivasan, Teja Koripella, Skye Tyrrell, Angellou Sutharsan'))
    doc.preamble.append(Command('date', ''))
    doc.append(NoEscape(r'\maketitle'))
    doc.append(NewPage())

    return doc


def tableOfContents(doc):

    with doc.create(Section('Table of Contents')):

        doc.append("Problems...........................................................................................Page 3")
        doc.append(NewLine())
        page=4
        for i in range (0, len(g2Functions)):
            doc.append(g2Functions[i][0])
            numOfDots=round((58-(len(g2Functions[i][0])))*1.81034483)
            for j in range(0, numOfDots):
                doc.append(".")
            if (i==len(g2Functions)-1):
                doc.append("Page " + str(page) + "-" + str(page+13))
                page += 14
            else:
                doc.append("Page " + str(page) + "-" + str(page + 11))
                page += 12
            doc.append(NewLine())
        doc.append("Solutions......................................................................................Page " + str(page) )
        doc.append(NewLine())
        page+=1
        for i in range (0, len(g2Functions)):
            doc.append(g2Functions[i][0] + " Solutions")
            numOfDots=round((58-(len(g2Functions[i][0] + " Solutions")))*1.81034483)
            for j in range(0, numOfDots):
                doc.append(".")
            doc.append("Page " + str(page) + "-" + str(page+3))
            page+=4
            doc.append(NewLine())
        doc.append(NewPage())



    return doc
def genG2Book():
    doc = Document()

    # Make title
    doc=title(doc)

    doc=tableOfContents(doc)

    doc=problemSection(doc)

    doc, s=genProblems(doc)

    doc=solutionSection(doc)
    doc=genSolutions(doc, s)

    # Generate .tex file
    try:
        doc.generate_pdf('Grade2Workbook', clean_tex=False)
    except:
        print("error")

genG2Book()