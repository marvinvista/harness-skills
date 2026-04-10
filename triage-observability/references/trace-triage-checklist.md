# Trace Triage Checklist

Check:
- which span is actually slow
- whether the slow span is repeated or one-off
- whether the delay is inside the service or in a downstream dependency
- whether errors and retries align with the slow trace
- whether the budget violation matches the reported user journey
