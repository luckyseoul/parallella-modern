"""
Mode configuration for the Parallel Idea Engine
"""

from enum import Enum

class EngineMode(Enum):
    PARALLEL_EXPLORATION = "exploration"
    LIGHT_CHATBOT = "chatbot"

# Default mode
CURRENT_MODE = EngineMode.PARALLEL_EXPLORATION

def set_mode(mode: EngineMode):
    global CURRENT_MODE
    CURRENT_MODE = mode

def is_chatbot_mode() -> bool:
    return CURRENT_MODE == EngineMode.LIGHT_CHATBOT