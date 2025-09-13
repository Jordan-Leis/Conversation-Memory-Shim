# Conversation Memory Shim

This repo contains a tiny prototype that demonstrates how keeping a short conversation memory reduces repeat constraint mentions. The shim stores user-provided constraints and lets the assistant act on them without asking again.

## How it works
- `memory_shim.py` implements a minimal in-memory store for constraints.
- `simulate.py` runs two conversations:
  - **baseline**: no memory. The assistant forgets and the user repeats a constraint.
  - **with_memory**: uses the shim to remember the constraint immediately.

## Metrics
The simulation records three metrics per conversation:

| scenario      | repeat\_constraint\_count | time\_to\_first\_correct\_action (msgs) | csat |
|---------------|-----------------------------|------------------------------------------|------|
| baseline      | 1                           | 4                                        | 3    |
| with_memory   | 0                           | 2                                        | 5    |

## Running it
```
python simulate.py
```

The output shows the conversation transcripts and metric values above.
