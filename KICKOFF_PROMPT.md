# Kickoff prompt for Claude Code

Paste this as the first message in a `claude` session started from the repository root
(`D:\SHOPS\AI Projects\YT_Crime\YT-Studio`). CLAUDE.md loads automatically and gives Claude Code
project context — this prompt gives it the actual first task, scoped narrowly on purpose.

---

Ты работаешь в репозитории Fatal Affairs Production Studio. CLAUDE.md уже загружен —
следуй его правилам без исключений.

Сначала прочитай целиком:
1. ProductionStudio/README.md
2. ProductionStudio/Documentation/ARCHITECTURE.md
3. ProductionStudio/Documentation/HANDOFF_TO_CLAUDE_CODE.md

Сейчас нужно выполнить ТОЛЬКО шаги 1-2 из HANDOFF_TO_CLAUDE_CODE.md (Repo setup, Orchestrator).
Не переходи к credentials, wiring agents, video assembly или чему-либо ещё, пока я явно не
подтвержу, что эти два шага завершены и одобрены.

Конкретно:
1. Проверь текущее состояние репозитория: git status, git log, структуру папок. Подтверди,
   что ProductionStudio/ цела, без лишней вложенности, ничего не потерялось при загрузке.
2. Составь план установки n8n на моём Hetzner VPS — но не устанавливай и не меняй ничего на
   реальном сервере, пока я не дам доступ и не подтвержу план.
3. Если что-то в брифах неоднозначно или не решено (например, выбор image-провайдера —
   Midjourney или Flux) — остановись и спроси меня, не выбирай сам.
4. Работай в Plan Mode: сначала покажи план, я одобрю — потом действуй.

Не трогай main без моего явного "да" на каждый пуш.
