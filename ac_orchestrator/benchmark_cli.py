import subprocess
import time

def run_agent_with_latency(user_input: str):
    start = time.perf_counter()

    process = subprocess.Popen(
        ["adk", "run", "ac_orchestrator"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Send only user input first
    process.stdin.write(user_input + "\n")
    process.stdin.flush()

    # Wait a bit for response to generate
    time.sleep(3)

    # Now send exit
    process.stdin.write("exit\n")
    process.stdin.flush()

    output, error = process.communicate()

    end = time.perf_counter()

    print("Agent Output:\n", output)
    print("⏱ Total Response Time:", round(end - start, 6), "seconds\n")


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        run_agent_with_latency(user_input)