"""
Simple prompt templates for Light Chatbot mode
"""

CHECKIN_PROMPTS = [
    "Haven't heard from you in a while. How are things going?",
    "Just checking in — anything interesting on your mind lately?",
    "Been quiet for a bit. Everything alright?",
    "Quick check-in: how's your week been so far?",
]

FOLLOWUP_PROMPTS = [
    "Last time we talked about {topic}. How did that turn out?",
    "You mentioned {topic} before — any updates?",
]

def get_checkin_prompt():
    import random
    return random.choice(CHECKIN_PROMPTS)