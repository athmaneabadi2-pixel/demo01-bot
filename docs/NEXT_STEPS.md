# NEXT STEPS — demo01-bot

## Semaine prochaine (priorité haute)
- [ ] Render Cron → appeler `/internal/checkin?to=whatsapp:+33XXXXXXXXX`
- [ ] Ajouter `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_SANDBOX_FROM`, `USER_WHATSAPP_TO` (ENV Render, pas dans le repo)
- [ ] Durcir prompt & garde-fous (tokens, timeouts httpx)
- [ ] Logs lisibles (niveau INFO + corrélation requête)

## Palier “DB plus tard”
- [ ] Render PostgreSQL + `DATABASE_URL`
- [ ] SQLAlchemy + Alembic (tables: users, messages, jobs, job_runs)
- [ ] DBeaver pour prod/debug
- [ ] Politique rétention & purge (RGPD)

## Qualité
- [ ] Tests unitaires mémoire (FIFO, cap à 100)
- [ ] Script `make dev/prod` (bat) pour ENV
