mkdir -p ~/success/docs/adr
cat > ~/success/docs/adr/0006-llm-agenda-parsing.md << 'EOF'
# ADR 0006: LLM agenda parsing

## Context
Users paste agendas as free text (emails, chats). We parse them into a structured agenda that the user checks and saves. Constraints: no NAT gateway, low cost, pasted text comes from outside and may contain instructions.

## Decision
- Model: Amazon Nova Lite via the Bedrock Converse API. Claude was the planned model, but the account (AWS Free plan) returned AccessDeniedException for all Anthropic models. The model ID is configuration (PARSER_MODEL).
- The parser is a separate Lambda outside the VPC with a function URL. It needs no database, reaches Bedrock without NAT or VPC endpoint, and costs nothing when idle.
- The model never writes. It returns JSON validated by a Pydantic schema; saving goes through the existing API.
- Pasted text is delimited and declared as data in the system prompt. Output is validated, with one retry.

## Alternatives considered
- Bedrock from the API through a VPC interface endpoint: about $7.30 a month per endpoint, breaks "$0 when idle".
- Claude API directly: needs an API key and a card, and leaves AWS IAM and billing.
- Regular-expression parser: cannot handle free-form text in several languages.

## Consequences
- About $0.0001 to $0.0002 per parse. Each parse logs model, prompt version, tokens, latency and cost.
- Nova Lite makes mistakes with dates and Ukrainian spelling, and followed an injected instruction in testing, so a human reviews every field before saving.
- If Bedrock is down, the user types the agenda by hand and the rest of the app keeps working.
