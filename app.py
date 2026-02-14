import io
from datetime import date
from typing import List

import streamlit as st
from PyPDF2 import PdfReader

from gst_knowledge import format_gst_references


def read_pdf(file_bytes: bytes) -> str:
    reader = PdfReader(io.BytesIO(file_bytes))
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n".join(pages).strip()


def read_upload(file) -> str:
    if file is None:
        return ""
    data = file.read()
    if file.type == "application/pdf":
        return read_pdf(data)
    return data.decode("utf-8", errors="ignore").strip()


def build_facts_section(notice_text: str) -> str:
    if not notice_text:
        return "Facts of the notice were reviewed and are summarized below."
    lines = [
        "Facts stated in the notice (summary):",
        notice_text.strip(),
    ]
    return "\n".join(lines)


def build_response_section(opinion: str, support_texts: List[str]) -> str:
    response_lines = [
        "Our response and justification:",
        "- The notice has been analyzed with reference to the records, filings, and supporting workings.",
    ]
    if support_texts:
        response_lines.append("- Supporting workings submitted:")
        for idx, text in enumerate(support_texts, start=1):
            label = f"  {idx}. Working Paper {idx}:"
            response_lines.append(label)
            response_lines.append(text.strip() or "(No text extracted)")
    if opinion:
        response_lines.append("- Specific points/clarifications provided by the taxpayer:")
        response_lines.append(opinion.strip())
    response_lines.append(
        "- Based on the above, the proposed demand/observation should be dropped or suitably modified."
    )
    return "\n".join(response_lines)


def generate_reply(
    notice_text: str,
    sample_reply: str,
    opinion: str,
    support_texts: List[str],
) -> str:
    today = date.today().strftime("%d-%m-%Y")
    sections = [
        "To,\nThe Proper Officer,\n[Jurisdiction]\n",
        f"Subject: Reply to GST Notice dated [DD-MM-YYYY] - submitted on {today}\n",
        "Respected Sir/Madam,\n",
        "We submit this reply in response to the above notice. Our submission is as follows:\n",
        build_facts_section(notice_text),
        "\n",
        build_response_section(opinion, support_texts),
        "\n",
        "Relevant GST law references (indicative):",
        format_gst_references(),
        "\n",
        "We request a personal hearing if required and seek a reasoned order after considering our submission.",
        "\n",
        "Thanking you,\nAuthorized Signatory\n[Name]\n[GSTIN]\n[Contact Details]",
    ]
    draft = "\n".join(sections)
    if sample_reply:
        draft = (
            "Sample reply format provided (for reference):\n"
            f"{sample_reply}\n\n---\n\nGenerated reply following the same structure:\n"
            f"{draft}"
        )
    return draft


def main() -> None:
    st.set_page_config(page_title="GST Notice Reply Draft Assistant", layout="wide")
    st.title("GST Notice Reply Draft Assistant")
    st.write(
        "Upload a GST notice and supporting workings. Optionally include a sample reply format and your "
        "specific points. The app will generate a structured reply draft."
    )

    col1, col2 = st.columns(2)

    with col1:
        notice_file = st.file_uploader(
            "Upload GST Notice (PDF/TXT)",
            type=["pdf", "txt"],
        )
        sample_reply = st.text_area(
            "Sample Reply Format (optional)",
            placeholder="Paste a sample reply format you want to follow...",
            height=200,
        )

    with col2:
        support_files = st.file_uploader(
            "Upload Supporting Workings (PDF/TXT, multiple)",
            type=["pdf", "txt"],
            accept_multiple_files=True,
        )
        opinion = st.text_area(
            "Your specific points / opinion (optional)",
            placeholder="Add any specific point or clarification you want included...",
            height=200,
        )

    notice_text = read_upload(notice_file) if notice_file else ""
    support_texts = [read_upload(file) for file in support_files] if support_files else []

    if st.button("Generate Reply"):
        reply = generate_reply(notice_text, sample_reply, opinion, support_texts)
        st.subheader("Draft Reply")
        st.text_area("", value=reply, height=600)
        st.download_button(
            label="Download Reply",
            data=reply,
            file_name="gst_notice_reply.txt",
            mime="text/plain",
        )


if __name__ == "__main__":
    main()
