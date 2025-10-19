# CLOSE DAY — demo01-bot

## Résumé
- Local OK (smokes) → Render OK → Twilio Sandbox OK.
- Mémoire courte RAM : `MEMORY_MAX=100`.
- LLM prod : gpt-4o-mini (MOCK désactivé sur Render).

## Service
- URL : https://demo01-bot.onrender.com
- Date : (sera rempli ci-dessous automatiquement)

## Preuves live
(Seront ajoutées par les commandes : code HTTP + reply non-MOCK)

## Backlog (extraits)
- Cron Render (ping quotidien un endpoint interne).
- Postgres + DBeaver (persistance/analytics) — “DB plus tard”.
- Numéro WhatsApp dédié (sortie prod).
- Mini tests unitaires mémoire.
DATETIME=19/10/2025 15:38:47,05
HTTP/1.1 200 OK
{"ok":true,"reply":"Salut ! Je suis l\u00e0 pour ton check-in de fin de journ\u00e9e. As-tu une m\u00e9t\u00e9o disponible ? Sinon, partage-moi tes priorit\u00e9s pour le soir et je te donnerai un conseil. \n\n\u2014 A\u00efcha \ud83e\udd1d","request_text":"close day check"}
