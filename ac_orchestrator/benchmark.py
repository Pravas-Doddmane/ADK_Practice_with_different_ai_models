import time
import asyncio

from google.adk.runners import InMemoryRunner
from google.adk.sessions import InMemorySessionService
from google.adk.events import UserContent

from ac_orchestrator.agent import root_agent


async def run_agent():
    # Create session service
    session_service = InMemorySessionService()

    # Create runner
    runner = InMemoryRunner(
        agent=root_agent,
        session_service=session_service,
    )

    session = await session_service.create_session(
        app_name="benchmark_app",
        user_id="benchmark_user",
    )

    while True:
        user_input = input("You: ")

        start = time.perf_counter()

        # Proper ADK call
        async for event in runner.run_async(
            session_id=session.id,
            new_message=UserContent(user_input),
        ):
            if event.is_final_response():
                response = event.content

        end = time.perf_counter()

        print("Agent:", response)
        print("⏱ Total Response Time:", round(end - start, 6), "seconds\n")


if __name__ == "__main__":
    asyncio.run(run_agent())