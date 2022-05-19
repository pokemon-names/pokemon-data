import fileinput
import mwparserfromhell as mwp
import pprint as pp
import re

debug = 0

doc = ""
for line in fileinput.input():
    doc += line

# Parse the document with "MediaWiki Parser from Hell"
# Note: skip_style_tags=True is critically important;
# Without it an occurrence of ''' can silently break the parser,
# causing any following sections to be parsed incorrectly.
wikicode = mwp.parse(doc,skip_style_tags=True)

# Define names of the sections of interest
want_sections = [
    'Trivia',
    'Origin',
    'Name origin',
    'In other languages',
]
if debug: print("wanted: "); pp.pp(want_sections)

# Extract the wikitext for each section
interesting = {}
for section in wikicode.get_sections(include_lead=False,flat=True):
    if debug: print("------> SECTION ------> "+str(section))
    for want_section in want_sections:
        if debug: print("looking for: "+want_section)
        heading = section.filter_headings()[0];
        heading = heading.replace('=', '')
        if len(heading) == 0: raise ValueError('No headings found')
        if debug: print("heading: "+str(heading))

        if heading == want_section:
            interesting[ want_section ] = {
                'section_name': want_section,
                'content'     : section,
            }
if debug: print("INTERESTING = "); pp.pp(interesting)

exit(0)
