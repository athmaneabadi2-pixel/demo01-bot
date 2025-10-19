set SERVICE=https://demo01-bot.onrender.com
mkdir docs 2>nul
(
  echo # J3 snapshot (Render)
  echo SERVICE=%SERVICE%
  echo DATETIME=%DATE% %TIME%
  curl.exe -s -o NUL -w "HEALTH %%{http_code}\n" "%SERVICE%/health"
  curl.exe -s -H "X-Token: dev-123" -H "Content-Type: application/json" -d "{\"text\":\"Hello J3\"}" "%SERVICE%/internal/send"
) > docs\day3_snapshot.md
