import re
import music as m

def xmlparser(f):
    stack = [("xml",[])]
    score = m.score(120)
    voices = []
    for line in f.readlines():
        line = line.strip()
        inline = re.fullmatch("<[^<>\/]+>[^<]+<\/[^<>\/]+>", line)
        opentag = re.fullmatch("<[^<>\/]+>", line)
        closetag = re.fullmatch("<\/[^>]+>", line)
        chord = {"length":0}
        notes = []
        note = {"pitch":0}
        rest = {"length":0}
        if line.startswith("<?"):
            continue
        if inline:
            tag = re.match("<[^<>\/]+>", line)
            content = line[tag.end(0):-(tag.end(0)+1)]
            stack[-1][1].append((tag.group(0)[1:-1],content))
            if tag.group(0)[1:-1]:
                continue
        if opentag:
            stack.append((line[1:-1],[]))
            if line[1:-1].startswith("Staff") and not stack[-1][0].startswith("Part"):
                score.add_voice(m.voice(1,m.waveforms.sin))
            elif line[1:-1].startswith("Chord"):
                chord = {"length":0}
                notes = []
            elif line[1:-1].startswith("Note"):
                note = {"pitch":0}
            elif line[1:-1].startswith("Rest"):
                rest = {"length":0}
        if closetag:
            if line[2:-1].startswith("Chord"):
                chord = m.chord(chord["length"])
                for n in notes:
                    chord.add_note(m.note(n["pitch"]))
                score.voices[-1].add_chord(chord)
            elif line[2:-1].startswith("Note"):
                notes.append(m.note(note["pitch"]))
            elif line[2:-1].startswith("Rest"):
                score.voices[-1].add_chord(m.rest(rest["length"]))
            stack[-2][1].append(stack.pop())
    return stack[0][1]

with open("testscore/test.mscx") as f:
    tree = xmlparser(f)
print(tree)