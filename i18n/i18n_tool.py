"""SunoForge widget translation pack: one shared file of translations, built into ready screens.

  python3 -I -X utf8 i18n_tool.py extract   once: English templates -> plugin/widgets_src/*.src.html (tokens) + i18n/en.json
  python3 -I -X utf8 i18n_tool.py build     src + i18n/<lang>.json -> plugin/widgets/<file> (en) and plugin/widgets/<lang>/<file>
  python3 -I -X utf8 i18n_tool.py check     every language has every key; placeholders and codes kept

Translatable units:
  html.<file>.<key>  a text node or a placeholder/aria-label attribute of the live HTML and of the commented example
                     blocks (the persona catalogue, the cards) — tokens {{t:<key>}} in the src template
  js.<file>.<path>   a label of the script dictionaries: editor T, panel L (prompt words, Suno tags and send codes stay)
"""
import json, os, re, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jslit import lit as jslit
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
WID = os.path.join(ROOT, '..', 'plugin', 'widgets')
MIRROR = os.path.join(ROOT, '..', 'plugin', 'skills', 'sunoforge', 'references', 'widgets')
SRC = os.path.join(ROOT, 'widgets_src')
I18N = os.path.join(ROOT, 'widgets_i18n')
FILES = ['menu.html', 'hub.html', 'mcp.html', 'editor.html', 'take.html', 'edit.html', 'songs.html', 'voices.html', 'next.html']
LANGS = ['en', 'ru', 'uk', 'de', 'es', 'fr', 'it', 'pt-BR', 'id']   # nine interface languages
NAMES = {'en': 'English', 'ru': 'Русский', 'uk': 'Українська', 'de': 'Deutsch', 'es': 'Español', 'fr': 'Français',
         'id': 'Indonesia', 'it': 'Italiano', 'pt-BR': 'Português', 'hi': 'हिन्दी', 'ko': '한국어', 'ja': '日本語', 'zh': '简体中文'}
RTL = set()
# text that never changes: codes, numbers, product names, the languages' own names, the view names (commands)
KEEP = set(NAMES.values()) | {'Suno', 'OK', 'BPM', 'mp3', 'wav', 'v6', 'MCP', 'Max Mode', 'suno.com'}
# word messages a button sends: shown in the user's chat bubble, so they go in the user's language
WORD_SENDS = {'edit the card', 'cancel', 'save'}
# example slot values of the live root (the model copies them): shown in the output language, so translated too
EXAMPLE_ATTRS = {'hub.html': ('data-st',), 'next.html': ('data-b',), 'edit.html': ('data-title', 'data-inst'), 'take.html': ('data-title', 'data-sub', 'data-t'), 'songs.html': ('data-t', 'data-d'), 'menu.html': ('data-l',)}
CUR = {'f': ''}
KEEP_RE = re.compile(r'^(\[?\d{1,2}[a-p]?\]?|\d+([.,:]\d+)*|[\W\d_]+|m:ss\.mmm|\{\{[A-Z_:]+\}\})$')

def is_text(t):
    t = t.strip()
    bare = re.sub(r'\{\{[A-Z_:]+\}\}', '', t)
    return bool(t) and t not in KEEP and not KEEP_RE.match(t) and bool(re.search(r'[A-Za-z]', bare))

def slug(t, used):
    b = re.sub(r'\{\{[A-Z_:]+\}\}', '', t)
    b = re.sub(r'[^A-Za-z0-9]+', '_', b).strip('_').lower()[:28] or 'x'
    k, n = b, 2
    while k in used and used[k] != t:
        k = f'{b}_{n}'; n += 1
    used[k] = t
    return k

class Ex(HTMLParser):
    """Collects (start, end, text) of translatable text nodes and attributes of an HTML fragment."""
    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.src = src; self.hits = []; self.skip = 0
        self.lines = [0]
        for m in re.finditer('\n', src): self.lines.append(m.end())
    def pos(self):
        l, c = self.getpos(); return self.lines[l - 1] + c
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'): self.skip += 1; return
        raw = self.get_starttag_text(); p = self.pos()
        for a in ('placeholder', 'aria-label', 'title', 'data-send') + EXAMPLE_ATTRS.get(CUR['f'], ()):
            m = re.search(r'\s%s="([^"]*)"' % a, raw)
            if not m or '{{' in m.group(1): continue
            if a == 'data-send' and m.group(1) not in WORD_SENDS: continue   # codes stay; only word messages are translated
            if is_text(m.group(1)):
                self.hits.append((p + m.start(1), p + m.end(1), m.group(1)))
    def handle_endtag(self, tag):
        if tag in ('script', 'style'): self.skip -= 1
    def handle_data(self, d):
        if self.skip or not is_text(d): return
        p = self.pos(); lead = len(d) - len(d.lstrip()); core = d.strip()
        self.hits.append((p + lead, p + lead + len(core), core))

def html_units(text):
    """Translatable units of the live HTML and of the commented example blocks (<!--\\n<div ... -->)."""
    out = []
    live = re.sub(r'(?s)<!--.*?-->', lambda m: ' ' * len(m.group(0)), text)
    cut = live.find('<script>')
    e = Ex(live[:cut] if cut >= 0 else live); e.feed(e.src); e.close(); out += e.hits
    for m in re.finditer(r'(?s)<!--\n(<(?:div|p)\b.*?)-->', text):
        e = Ex(m.group(1)); e.feed(m.group(1)); e.close()
        out += [(m.start(1) + a, m.start(1) + b, t) for a, b, t in e.hits]
    return sorted(set(out))

# ── the script dictionaries ──
def js_obj(text, name):
    head = 'var ' + name + '={'
    i = text.index(head); j = text.index('};', i) + 2
    lit = text[i + len(head) - 1:j - 1]
    js = subprocess.run(['node', '-e', f'process.stdout.write(JSON.stringify({lit}))'], capture_output=True, text=True, check=True).stdout
    return i, j, json.loads(js)

def js_leaves(name, obj):
    """paths of the translatable labels; prompt words, Suno tags and send codes are left out"""
    out = {}
    for k, v in obj.items():
        if isinstance(v, str): out[k] = v
        elif name == 'T' and k in ('la', 'sa'):
            for n, pair in enumerate(v): out[f'{k}.{n}'] = pair[1]
        elif name == 'T' and k == 'qa':
            for kk, vv in v.items(): out[f'qa.{kk}'] = vv
        elif name == 'T' and k == 'D':
            for n, row in enumerate(v): out[f'D.{n}.0'] = row[0]; out[f'D.{n}.1'] = row[1]
    return out

def js_apply(obj, leaves):
    o = json.loads(json.dumps(obj))
    for p, v in leaves.items():
        parts = p.split('.')
        if len(parts) == 1: o[p] = v
        elif parts[0] in ('la', 'sa'): o[parts[0]][int(parts[1])][1] = v
        elif parts[0] == 'qa': o['qa'][parts[1]] = v
        elif parts[0] == 'D': o['D'][int(parts[1])][int(parts[2])] = v
    return o

DICTS = {'editor.html': ['T'], 'mcp.html': ['L'], 'menu.html': ['M', 'SUB', 'UI'], 'hub.html': ['L'], 'take.html': ['L'], 'edit.html': ['L'], 'songs.html': ['L'], 'voices.html': ['L'], 'next.html': ['L']}

def extract():
    os.makedirs(SRC, exist_ok=True); os.makedirs(I18N, exist_ok=True)
    en = {}
    for f in FILES:
        t = open(os.path.join(WID, f), encoding='utf-8').read()
        CUR['f'] = f; used = {}; units = html_units(t); out = []; last = 0
        for a, b, txt in units:
            k = slug(txt, used); en[f'html.{f}.{k}'] = txt
            out.append(t[last:a]); out.append('{{t:%s}}' % k); last = b
        out.append(t[last:]); s = ''.join(out)
        for name in DICTS[f]:
            i, j, obj = js_obj(s, name)
            for p, v in js_leaves(name, obj).items(): en[f'js.{f}.{name}.{p}'] = v
            json.dump(obj, open(os.path.join(SRC, f'{f}.{name}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
            s = s[:i] + f'var {name}=%%{name}%%;' + s[j:]
        open(os.path.join(SRC, f + '.src'), 'w', encoding='utf-8').write(s)
        print(f, len(units), 'html units', sum(1 for k in en if k.startswith(f'js.{f}.')), 'js labels')
    json.dump(en, open(os.path.join(I18N, 'en.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('en.json', len(en), 'strings')

def esc(v):
    return v.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

PH = re.compile(r'\{\{[A-Z_:]+\}\}|`[^`]*`|\b\d{1,2}[a-p]\b|\[\d{1,2}\]')

def check(verbose=True):
    en = json.load(open(os.path.join(I18N, 'en.json'), encoding='utf-8')); bad = []
    for lang in LANGS[1:]:
        p = os.path.join(I18N, f'{lang}.json')
        if not os.path.exists(p): bad.append(f'{lang}: no file'); continue
        tr = json.load(open(p, encoding='utf-8'))
        for k, v in en.items():
            if k not in tr: bad.append(f'{lang}: missing {k}'); continue
            if not isinstance(tr[k], str) or not tr[k].strip(): bad.append(f'{lang}: empty {k}'); continue
            a, b = sorted(PH.findall(v)), sorted(PH.findall(tr[k]))
            if a != b: bad.append(f'{lang}: {k} placeholders {a} -> {b}')
        for k in tr:
            if k not in en: bad.append(f'{lang}: unknown key {k}')
    if verbose:
        for b in bad[:60]: print(' -', b)
        print('check:', len(bad), 'problems')
    return bad

def build():
    en = json.load(open(os.path.join(I18N, 'en.json'), encoding='utf-8'))
    langs = [l for l in LANGS if os.path.exists(os.path.join(I18N, f'{l}.json'))]
    sizes = {}
    for lang in langs:
        tr = dict(en); tr.update(json.load(open(os.path.join(I18N, f'{lang}.json'), encoding='utf-8')))
        outdir = WID if lang == 'en' else os.path.join(WID, lang)
        os.makedirs(outdir, exist_ok=True)
        for f in FILES:
            s = open(os.path.join(SRC, f + '.src'), encoding='utf-8').read()
            s = re.sub(r'\{\{t:([a-z0-9_]+)\}\}', lambda m: esc(tr[f'html.{f}.{m.group(1)}']), s)
            for name in DICTS[f]:
                obj = json.load(open(os.path.join(SRC, f'{f}.{name}.json'), encoding='utf-8'))
                pre = f'js.{f}.{name}.'
                leaves = {k[len(pre):]: v for k, v in tr.items() if k.startswith(pre)}
                lit = jslit(js_apply(obj, leaves))
                s = s.replace(f'var {name}=%%{name}%%;', f'var {name}={lit};', 1)
            if lang != 'en':
                note = (f'LANGUAGE: this copy is already in {NAMES[lang]} ({lang}) — every label, the script dictionaries '
                        f'included, is translated; do NOT translate again: fill the slots, write slot text in {NAMES[lang]}. ')
                s = s.replace('<!-- SunoForge v5.0', '<!-- ' + note + '\nSunoForge v5.0', 1)
                if lang in RTL:
                    s = re.sub(r'<div class="(sf|sm|ed)"', r'<div dir="rtl" class="\1"', s, count=1)
            assert '{{t:' not in s and '%%' not in s, (lang, f)
            for base in (WID, MIRROR):   # the plugin keeps every screen twice; both must match
                od = base if lang == 'en' else os.path.join(base, lang)
                os.makedirs(od, exist_ok=True)
                open(os.path.join(od, f), 'w', encoding='utf-8', newline='\n').write(s)
            sizes[(lang, f)] = len(s)
    # one common file with every language, next to the templates
    allp = {l: json.load(open(os.path.join(I18N, f'{l}.json'), encoding='utf-8')) for l in langs}
    json.dump(allp, open(os.path.join(ROOT, 'all_languages.json'), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=0)
    print('built', len(langs), 'languages:', ' '.join(langs), '+ widgets/i18n.json')
    return sizes

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'check'
    {'extract': extract, 'build': build, 'check': check}[cmd]()
