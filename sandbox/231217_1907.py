from pathlib import Path

this_path = Path(__file__)
sndlib_path = Path(this_path.parent, '../snd-lib')

for p in sndlib_path.iterdir():
  print(p.name)
