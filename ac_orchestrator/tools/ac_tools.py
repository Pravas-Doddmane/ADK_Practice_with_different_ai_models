import time

# Mock AC state
AC_STATE = {
    "power": "OFF",
    "temperature": 24
}

def control_ac(action: str, value: int = None) -> dict:
    """
    Controls AC device (mock implementation).
    Measures tool execution time.
    """
    start_time = time.perf_counter()   # more accurate than time.time()

    if action == "TURN_ON":
        AC_STATE["power"] = "ON"

    elif action == "TURN_OFF":
        AC_STATE["power"] = "OFF"

    elif action == "SET_TEMP":
        AC_STATE["temperature"] = value

    elif action == "INCREASE_TEMP":
        AC_STATE["temperature"] += value

    elif action == "DECREASE_TEMP":
        AC_STATE["temperature"] -= value

    else:
        return {
            "status": "error",
            "message": "Invalid action",
            "execution_time": 0
        }

    end_time = time.perf_counter()

    return {
        "status": "success",
        "ac_state": AC_STATE,
        "tool_execution_time": round(end_time - start_time, 6)
    }