from pathlib import Path
import esprima

path = Path('index.html')
text = path.read_text('utf-8')
start = text.index('<script>') + len('<script>')
end = text.index('</script>')
src = text[start:end]
try:
    esprima.parseScript(src, {'tolerant': False, 'loc': True})
    print('ok')
except Exception as e:
    print(type(e).__name__)
    print(e)
    if hasattr(e, 'lineNumber'):
        print('lineNumber', e.lineNumber)
    if hasattr(e, 'column'):
        print('column', e.column)
