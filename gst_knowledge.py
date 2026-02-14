GST_LAW_REFERENCES = [
    {
        "topic": "Notice reply timelines",
        "summary": "Reply within the time specified in the notice. Seek extension with reasons if required.",
        "citation": "CGST Act, Section 73/74 (demand and adjudication).",
    },
    {
        "topic": "Principles of natural justice",
        "summary": "Opportunity of being heard, reasoned order, and disclosure of relied-upon documents.",
        "citation": "General legal principles; reflected in CGST rules/procedures.",
    },
    {
        "topic": "Input tax credit conditions",
        "summary": "ITC allowed subject to possession of tax invoice, receipt of goods/services, tax paid, and filing of returns.",
        "citation": "CGST Act, Section 16.",
    },
    {
        "topic": "ITC blocked credits",
        "summary": "Certain credits are blocked, e.g., personal use or specific goods/services.",
        "citation": "CGST Act, Section 17(5).",
    },
    {
        "topic": "Mismatch and reconciliation",
        "summary": "Explain reconciliations between returns/books and provide working papers.",
        "citation": "Return matching and reconciliation practices under CGST rules.",
    },
]


def format_gst_references() -> str:
    lines = []
    for item in GST_LAW_REFERENCES:
        lines.append(
            f"- {item['topic']}: {item['summary']} ({item['citation']})"
        )
    return "\n".join(lines)
