###### README.md >> markdown 
# 🟩 SMSToolKit
> Module SMS pour Android/Termux
   - Status : OPERATIONNEL
   - Version : 1.0
   - Compatibilité : Android + Termux
   - Mode : Open‑Source

> SMSToolKit est un toolkit complet permettant :
   - ✔ Extraction des SMS
   - ✔ Export JSON / TXT
   - ✔ Analyse statistique
   - ✔ Monitoring en temps réel dans termux
   - ✔ Sauvegarde automatique

### 🎯 Structure du projet
```text
ModuleSMS/
│
├── src/
│   ├── bash/
│   │   ├── dump_sms.sh
│   │   ├── monitor_sms.sh
│   │   └── export_sms.sh
│   ├── python/
│   │   ├── parser.py
│   │   ├── stats.py
│   │   └── export_json.py
│   └── termux/
│       ├── sms_dump.py
│       └── sms_watch.py
│
├── config/
│   ├── profiles/
│   │   ├── default.conf
│   │   └── legion.conf
│   └── settings.yaml
│
├── docs/
│   ├── INSTALL.md
│   ├── USAGE.md
│   └── API.md
│
├── tests/
│   ├── test_parser.py
│   └── test_stats.py
│
├── examples/
│   ├── sample_output.json
│   └── demo.sh
│
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── security.yml
│   ├── ISSUE_TEMPLATE.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── FUNDING.yml
│   └── SECURITY.md
│
└── README.md
```

### 📦 Installation
```clone git
git clone https://github.com/teremuhamblin/ModuleSMS
```
```text
cd ModuleSMS
```

### 🚀 Utilisation rapide
```bash
bash src/termux/termux_sms_dump.sh
```
```python
python3 src/python/sms_parser.py
```
```json
export.json
```

### 🛡 Sécurité
Toutes les données restent **locales** :
- Aucun envoi externe
- Mode **“Legion”** disponible dans **config/profiles/legion.json**

### ⭐ Soutien
Un ⭐ sur GitHub = 
**motivation + évolution du projet**
