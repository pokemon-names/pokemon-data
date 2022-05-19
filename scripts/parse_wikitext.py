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
# (in a manner to approximate `qw` in Perl)
want_sections = list(map(str.strip, '''
    Trivia
    Origin
    Name origin
    In other languages
'''.split('\n')[1:-1]
))
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

# __DATA__

    # ====Origin===
    # Pikachu is based on a {{wp|mouse}} after its name. Its cheek pouches were also inspired by {{wp|squirrel}}s, which store food in their cheeks. The stripes on its back and its lightning bolt-shaped tail were given for aesthetic reasons.<ref name=int/>
    # 
    # Pikachu's designer, [[Atsuko Nishida]], revealed in an interview that it was originally a {{wp|daifuku}}-like creature with ears. Its black ear tips are remnants from this original concept.<ref name=int/>
    # 
    # Pikachu's [[Gigantamax]] form is most likely a reference to its earlier, more rotund design from [[Generation I|Generations I]] and {{gen|II}}.

    # ====Name origin====
    # Pikachu is a combination of ピカピカ ''pikapika'' (onomatopoeia for sparkle) and チューチュー ''chūchū'' (the sound of a mouse squeaking).<ref>[http://edition.cnn.com/ASIANOW/time/magazine/99/1122/pokemon6.fullinterview2.html TIME - The Ultimate Game Freak]</ref>

    # ==In other languages==
    # ...
