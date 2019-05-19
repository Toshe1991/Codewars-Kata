notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def chords(root):
    root_index = notes.index(root)
    
    major = [root, notes[(root_index + 4) % 12], notes[(root_index + 7) % 12]]
    minor = [root, notes[(root_index + 3) % 12], notes[(root_index + 7) % 12]]
    
    return [major, minor]
