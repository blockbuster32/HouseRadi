from pathlib import Path
path = Path('index.html')
text = path.read_text('utf-8')
start = text.index('<script>') + len('<script>')
end = text.index('</script>')
src = text[start:end]
lines = src.splitlines()
for i in range(1050, 1063):
    print(f"{i+1}: {lines[i]!r}")
