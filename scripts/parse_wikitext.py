import fileinput
import pprint as pp
import re
import wikitextparser as wtp

debug = 1

print("working...")

doc = ""
for line in fileinput.input():
    doc += line

parsed = wtp.parse(doc)

i=0
for section in parsed.sections:

    # ====Origin===
    # Pikachu is based on a {{wp|mouse}} after its name. Its cheek pouches were also inspired by {{wp|squirrel}}s, which store food in their cheeks. The stripes on its back and its lightning bolt-shaped tail were given for aesthetic reasons.<ref name=int/>
    # 
    # Pikachu's designer, [[Atsuko Nishida]], revealed in an interview that it was originally a {{wp|daifuku}}-like creature with ears. Its black ear tips are remnants from this original concept.<ref name=int/>
    # 
    # Pikachu's [[Gigantamax]] form is most likely a reference to its earlier, more rotund design from [[Generation I|Generations I]] and {{gen|II}}.
    origin = re.search(
        re.compile("^=+Origin=+\n(.+?)(^=+)", flags=re.DOTALL|re.MULTILINE),
        str(section)
    )
    if origin:
        if debug: print("\n\n#############################################################################\n")
        if debug: print("#### MATCH = "); pp.pp(origin)
        if debug: print("#### MATCH = "); pp.pp(origin.group(1))
        if debug: print("#### SECTION = "+str(i)+" ="+str(section))

    # ====Name origin====
    # Pikachu is a combination of ピカピカ ''pikapika'' (onomatopoeia for sparkle) and チューチュー ''chūchū'' (the sound of a mouse squeaking).<ref>[http://edition.cnn.com/ASIANOW/time/magazine/99/1122/pokemon6.fullinterview2.html TIME - The Ultimate Game Freak]</ref>

    # ==In other languages==
    i=i+1

