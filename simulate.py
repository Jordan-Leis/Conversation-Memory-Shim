from memory_shim import ConversationMemoryShim


def run_conversation(use_memory: bool):
    shim = ConversationMemoryShim() if use_memory else None
    transcript = []
    metrics = {
        "repeat_constraint_count": 0,
        "time_to_first_correct_action": None,  # in message count
        "csat": None,
    }

    # Message 1: user provides constraint
    transcript.append(("user", "Please deliver at 8pm."))
    if use_memory and shim:
        shim.add_constraint("delivery_time", "8pm")
        # Assistant remembers and acts correctly immediately
        transcript.append(("assistant", "Got it, I'll deliver at 8pm."))
        metrics["time_to_first_correct_action"] = len(transcript)
    else:
        # Assistant forgets constraint
        transcript.append(("assistant", "When should I deliver it?"))
        # User repeats constraint
        transcript.append(("user", "I said 8pm."))
        metrics["repeat_constraint_count"] += 1
        # Assistant acknowledges
        transcript.append(("assistant", "Thanks, I'll deliver at 8pm."))
        metrics["time_to_first_correct_action"] = len(transcript)

    metrics["csat"] = 5 if use_memory else 3
    return transcript, metrics


def main():
    scenarios = [(False, "baseline"), (True, "with_memory")]
    for use_memory, name in scenarios:
        transcript, metrics = run_conversation(use_memory)
        print(f"=== {name} ===")
        for speaker, msg in transcript:
            print(f"{speaker}: {msg}")
        print("metrics:", metrics)
        print()


if __name__ == "__main__":
    main()
