import json
import os
import sys
import time
from datetime import date

from app.ai.agenda import PARSER_MODEL, PROMPT_VERSION, cost_usd, parse_agenda

arg = sys.argv[1]
text = open(arg, encoding="utf-8").read() if os.path.exists(arg) else arg
started = time.monotonic()
agenda, usage = parse_agenda(text, date.today(), "Europe/Kyiv")
print(json.dumps(agenda.model_dump(mode="json"), ensure_ascii=False, indent=2))
print(
    {
        "model": PARSER_MODEL,
        "prompt_version": PROMPT_VERSION,
        **usage,
        "latency_s": round(time.monotonic() - started, 2),
        "cost_usd": cost_usd(PARSER_MODEL, usage),
    }
)
