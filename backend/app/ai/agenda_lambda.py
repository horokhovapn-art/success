import json
import logging
import time
from datetime import date

from app.ai.agenda import PARSER_MODEL, PROMPT_VERSION, AgendaParseError, cost_usd, parse_agenda

log = logging.getLogger()
log.setLevel(logging.INFO)

MAX_CHARS = 10_000


def _resp(code, body):
    return {
        "statusCode": code,
        "headers": {"content-type": "application/json"},
        "body": json.dumps(body, ensure_ascii=False),
    }


def handler(event, context):
    # TODO: перевірка Cognito-токена (401), якщо вистачить часу
    try:
        body = json.loads(event.get("body") or "{}")
        text = body["text"]
        today = date.fromisoformat(body["today"])
        tz = body["tz"]
    except (KeyError, ValueError):
        return _resp(400, {"error": "text, today and tz are required"})
    if len(text) > MAX_CHARS:
        return _resp(413, {"error": "text is too long (max 10000 characters)"})

    started = time.monotonic()
    try:
        agenda, usage = parse_agenda(text, today, tz)
    except AgendaParseError as e:
        return _resp(422, {"error": str(e)})
    except Exception:  # throttling, мережа, доступ до моделі
        log.exception("parse failed")
        return _resp(503, {"error": "the parsing service is busy or unavailable"})

    log.info(
        json.dumps(
            {
                "event": "agenda_parsed",
                "model": PARSER_MODEL,
                "prompt_version": PROMPT_VERSION,
                **usage,
                "latency_ms": int((time.monotonic() - started) * 1000),
                "cost_usd": cost_usd(PARSER_MODEL, usage),
            }
        )
    )
    return _resp(
        200,
        {
            "agenda": agenda.model_dump(mode="json"),
            "model": PARSER_MODEL,
            "prompt_version": PROMPT_VERSION,
        },
    )
