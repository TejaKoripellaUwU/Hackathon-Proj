from pylatex.utils import italic, bold
from pylatex import *
from Website import Grade1
from Website.Grade1 import *
from Website import Grade2
from Website.Grade2 import *
from Website import Grade4
from Website.Grade4 import *
import Website.Grade1
import Website.Grade2
import Website.Grade4

allFunc = g1Functions+g2Functions+g4Functions
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


def genProblems(doc,functions):
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
            #doc.append(NoEscape(r'\normalsize'))

            problems, solutions = functions[j][1]
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

def genSolutions(doc, s,autoFunctions):
    #print(len(s))
    for j in range(0, len(s)):
        for i in range(0, 4):
            doc.append(NoEscape('\large'))
            doc.append(NoEscape(r'\begin{center}'))
            title=r'\textbf{' + autoFunctions[j][0] + '- Solution ' + str(i+1) + '}'
            doc.append(NoEscape(title))
            doc.append(NewLine())
            doc.append(NoEscape(r'\end{center} \normalsize'))
            #doc.append(NoEscape(r'\normalsize'))

            for k in (s[j][i]):
                doc.append(k)
                doc.append(NewLine())
            doc.append(NewPage())

    return doc


def title(doc,title):

    doc.preamble.append(Command('title', title))
    doc.preamble.append(Command('author', 'Akshai Srinivasan, Teja Koripella, Skye Tyrrell, Angellou Sutharsan'))
    doc.preamble.append(Command('date', ''))
    doc.append(NoEscape(r'\maketitle'))
    doc.append(NoEscape(r'\vfill'))
    doc.append(NoEscape(r'\begin{center}'))
    doc.append("ISBN: 9798848749724")
    doc.append(NoEscape(r'\linebreak'))
    doc.append(NoEscape(r'\copyright'))
    doc.append('MathMaestro.org')
    doc.append(NoEscape(r'\end{center}'))
    doc.append(NewPage())

    return doc


def tableOfContents(doc,allFunctions):

    with doc.create(Section('Table of Contents')):

        doc.append(
            "Problems...........................................................................................Page 3")
        doc.append(NewLine())
        page = 4
        for i in range(0, len(allFunctions)):
            doc.append(allFunctions[i][0])
            numOfDots = round((58 - (len(allFunctions[i][0]))) * 1.81034483)
            for j in range(0, numOfDots):
                doc.append(".")
            if (i == len(allFunctions) - 1):

                doc.append("Page " + str(page) + "-" + str(page + ((4 * (3 + allFunctions[i][2])) + 1)))

                page += ((4 * (3 + allFunctions[i][2])) + 1)
            else:
                doc.append("Page " + str(page) + "-" + str(page + ((4 * (3 + allFunctions[i][2])) - 1)))
                page += ((4 * (3 + allFunctions[i][2])))
            doc.append(NewLine())
        page += 1
        doc.append(
            "Solutions......................................................................................Page " + str(
                page))
        doc.append(NewLine())
        page += 1
        for i in range(0, len(allFunctions)):
            doc.append(allFunctions[i][0] + " Solutions")
            numOfDots = round((58 - (len(allFunctions[i][0] + " Solutions"))) * 1.81034483)
            for j in range(0, numOfDots):
                doc.append(".")
            doc.append("Page " + str(page) + "-" + str((page + ((4 * (1 + allFunctions[i][2])))) - 1))
            page += ((4 * (1 + allFunctions[i][2])))
            doc.append(NewLine())
        doc.append(NewPage())

    return doc

def genG1Book(functions, theRealTitle, pdf):
    doc = Document()

    # Make title
    doc=title(doc,theRealTitle)

    doc=tableOfContents(doc,functions)

    doc=problemSection(doc)

    doc, s=genProblems(doc,functions)

    doc=solutionSection(doc)
    doc=genSolutions(doc, s,functions)

    # Generate .tex file
    try:
        doc.generate_pdf(pdf, clean_tex=False)
    except:
        print("error")

#genG1Book()