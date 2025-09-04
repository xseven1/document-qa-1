import streamlit as st
from openai import OpenAI
import fitz

#Helper function to read PDFs
def read_pdf(uploaded_file):
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# Show title and description.
st.title("♨️HOMEWORK 1")
st.write(
    "Upload a document below and ask a question about it – GPT will answer! "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:

    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Let the user upload a file via `st.file_uploader`.
    uploaded_file = st.file_uploader(
        "Upload a document (.txt or .pdf)", type=("txt", "pdf")
    )

    document = None
    if uploaded_file:
        file_extension = uploaded_file.name.split(".")[-1].lower()
        if file_extension == "txt":
            document = uploaded_file.read().decode("utf-8")
        elif file_extension == "pdf":
            document = read_pdf(uploaded_file)
        else:
            st.error("Unsupported file type")

    # Ask the user for a question via `st.text_area`.
    question = st.text_area(
        "Now ask a question about the document!",
        placeholder="Is this course hard?",
        disabled=not document,
    )

    if document and question:
        st.subheader("Responses")

        models = [
            "gpt-3.5-turbo",
            "gpt-4.1",
            "gpt-5-chat-latest",
            "gpt-5-nano",
        ]

        responses = {}

        for model in models:
            with st.spinner(f"Querying {model}..."):
                try:
                    response = client.chat.completions.create(
                        model = model,
                        messages=[
                             {"role": "user", "content": f"Document:\n{document}\n\nQuestion: {question}"},
                        ]
                    )
                    responses[model] = response.choices[0].message.content
                except Exception as e:
                    responses[model] = f"Error: {e}"

        for model, answer in responses.items():
            st.markdown(f"### {model}")
            st.write(answer)
            st.markdown("---")