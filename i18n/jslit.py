# Compact JS object literal: bare keys where valid, single-quoted strings. In a show_widget call the widget code travels
# as a JSON string, where every double quote costs a backslash; single quotes cost nothing.
import json, re

IDENT = re.compile(r'^[A-Za-z_$][A-Za-z0-9_$]*$')
RESERVED = {'in', 'do', 'if', 'for', 'new', 'try', 'var', 'case', 'else', 'enum', 'null', 'this', 'true', 'void', 'with',
            'break', 'catch', 'class', 'const', 'false', 'super', 'throw', 'while', 'yield', 'delete', 'export', 'import',
            'public', 'return', 'static', 'switch', 'typeof', 'default', 'extends', 'finally', 'package', 'private',
            'continue', 'debugger', 'function', 'arguments', 'interface', 'protected', 'implements', 'instanceof'}

def s(v):
    return "'" + v.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n').replace('\r', '').replace('</', '<\\/') + "'"

def key(k):
    k = str(k)
    if IDENT.match(k) and k not in RESERVED:
        return k
    if re.match(r'^(0|[1-9][0-9]*)$', k):
        return k
    return s(k)

def lit(o):
    if isinstance(o, dict):
        return '{' + ','.join(key(k) + ':' + lit(v) for k, v in o.items()) + '}'
    if isinstance(o, list):
        return '[' + ','.join(lit(v) for v in o) + ']'
    if isinstance(o, str):
        return s(o)
    return json.dumps(o)

def tool_chars(code, title='SunoForge menu', loading=('…',)):
    """Characters of the show_widget input as JSON — what the model actually prints."""
    return len(json.dumps({'loading_messages': list(loading), 'title': title, 'widget_code': code}, ensure_ascii=False))
