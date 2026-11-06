# i18n — the source of SunoForge's screens

Not part of the plugin: the plugin ships the built screens, this folder builds them.

- `widgets_src/` — the English templates with `{{t:key}}` tokens and their script dictionaries
- `widgets_i18n/<lang>.json` — every string of every screen, one file per language
- `i18n_tool.py` — `check` (every language has every key) and `build`, which writes the screens into BOTH
  `plugin/widgets/` and `plugin/skills/sunoforge/references/widgets/`: the plugin keeps every screen twice and
  the two copies must stay identical

A wrong word in one language is one line in its `.json`, then:

```
python3 -I -X utf8 i18n/i18n_tool.py check
python3 -I -X utf8 i18n/i18n_tool.py build
```
