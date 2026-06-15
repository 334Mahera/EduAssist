import streamlit as st
import google.generativeai as genai

# ---------------------------
# Configure Gemini API
# ---------------------------
GOOGLE_API_KEY = "AIzaSyBpVWcizUhVgc1wel-deleFcZgJufYLZ3Q"

genai.configure(api_key=GOOGLE_API_KEY)

# Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="EduAssist Chatbot")

st.title("🎓 EduAssist Chatbot")

# ---------------------------
# Session State
# ---------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "long_term_memory" not in st.session_state:
    st.session_state.long_term_memory = {}

# ---------------------------
# User Input
# ---------------------------
user_input = st.chat_input(
    "Ask your academic question..."
)

# ---------------------------
# Process User Input
# ---------------------------
if user_input:

    # ---------------------------
    # Message Filtering
    # ---------------------------
    if user_input.strip() == "":
        st.warning("Please enter valid text.")

    else:

        # ---------------------------
        # Long-Term Memory
        # ---------------------------
        if "beginner" in user_input.lower():
            st.session_state.long_term_memory[
                "level"
            ] = "Beginner"

        if "advanced" in user_input.lower():
            st.session_state.long_term_memory[
                "level"
            ] = "Advanced"

        # ---------------------------
        # Store User Message
        # ---------------------------
        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        # ---------------------------
        # Create Context
        # ---------------------------
        memory_info = ""

        if "level" in st.session_state.long_term_memory:

            memory_info = (
                "User learning level is "
                + st.session_state.long_term_memory["level"]
            )

        recent_messages = ""

        for msg in st.session_state.chat_history[-6:]:

            recent_messages += (
                f"{msg['role']}: "
                f"{msg['content']}\n"
            )

        prompt = f"""
        You are an educational chatbot.

        {memory_info}

        Previous Conversation:
        {recent_messages}

        Conversation Summary:
        {st.session_state.summary}

        User Question:
        {user_input}

        Give clear educational answers.
        """

        # ---------------------------
        # Generate Response
        # ---------------------------
        response = model.generate_content(prompt)

        bot_reply = response.text

        # ---------------------------
        # Store Assistant Reply
        # ---------------------------
        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": bot_reply
            }
        )

        # ---------------------------
        # Summarization
        # ---------------------------
        if len(st.session_state.chat_history) > 10:

            old_chat = ""

            for msg in st.session_state.chat_history[:-4]:

                old_chat += (
                    f"{msg['role']}: "
                    f"{msg['content']}\n"
                )

            summary_prompt = f"""
            Summarize this conversation briefly:

            {old_chat}
            """

            summary_response = model.generate_content(
                summary_prompt
            )

            st.session_state.summary = (
                summary_response.text
            )

            # Keep recent messages only
            st.session_state.chat_history = (
                st.session_state.chat_history[-4:]
            )

# ---------------------------
# Display Chat
# ---------------------------
for msg in st.session_state.chat_history:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------------------
# Sidebar Memory Display
# ---------------------------
st.sidebar.title("Memory")

st.sidebar.write(
    st.session_state.long_term_memory
)

if st.session_state.summary != "":
    st.sidebar.subheader(
        "Conversation Summary"
    )

    st.sidebar.write(
        st.session_state.summary
    )