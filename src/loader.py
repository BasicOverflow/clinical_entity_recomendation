"""Load the public corpus into an existing Neo4j database."""

from __future__ import annotations

import json
from pathlib import Path

from src.config import CORPUS_TAG
from src.graph import connect

ROOT = Path(__file__).resolve().parents[1]
STUDIES = ROOT / "corpus" / "studies"


def _parent_number(section_number: str) -> str | None:
    if not section_number or "." not in section_number:
        return None
    return section_number.rsplit(".", 1)[0]


def clear_corpus(session) -> None:
    session.run(
        "MATCH (n {corpus: $corpus}) DETACH DELETE n",
        corpus=CORPUS_TAG,
    )


def _write_sections(session, nct_id: str, doc_type: str, sections: list[dict]) -> None:
    label = doc_type
    session.run(
        f"""
        MATCH (s:STUDY {{name: $nct, corpus: $corpus}})
        MERGE (d:{label} {{name: $doc_name, corpus: $corpus}})
        SET d.document_type = $doc_type
        MERGE (s)-[:HAS_DOCUMENT]->(d)
        """,
        nct=nct_id,
        corpus=CORPUS_TAG,
        doc_name=f"{nct_id}:{doc_type}",
        doc_type=doc_type,
    )
    by_number: dict[str, str] = {}
    for index, section in enumerate(sections):
        section_id = f"{nct_id}:{doc_type}:{index}"
        by_number[section.get("section_number") or ""] = section_id
        session.run(
            """
            MATCH (d {name: $doc_name, corpus: $corpus})
            MERGE (c:SECTION_CONTENT {section_id: $section_id, corpus: $corpus})
            SET c.name = $name,
                c.section_number = $section_number,
                c.section_title = $section_title,
                c.text = $text,
                c.document_type = $doc_type
            MERGE (d)-[:HAS_CONTENT]->(c)
            """,
            doc_name=f"{nct_id}:{doc_type}",
            corpus=CORPUS_TAG,
            section_id=section_id,
            name=section.get("name") or section.get("section_title"),
            section_number=section.get("section_number") or "",
            section_title=section.get("section_title") or "",
            text=section.get("text") or "",
            doc_type=doc_type,
        )
    if doc_type != "PROTOCOL":
        return
    session.run(
        """
        MATCH (d:PROTOCOL {name: $doc_name, corpus: $corpus})
        MERGE (t:TABLE_OF_CONTENTS {name: $toc_name, corpus: $corpus})
        MERGE (d)-[:HAS_TABLE_OF_CONTENTS]->(t)
        """,
        doc_name=f"{nct_id}:{doc_type}",
        corpus=CORPUS_TAG,
        toc_name=f"{nct_id}:TOC",
    )
    for index, section in enumerate(sections):
        section_id = f"{nct_id}:{doc_type}:{index}"
        session.run(
            """
            MATCH (t:TABLE_OF_CONTENTS {name: $toc_name, corpus: $corpus})
            MATCH (c:SECTION_CONTENT {section_id: $section_id, corpus: $corpus})
            MERGE (sec:TOC_SECTION {section_id: $section_id, corpus: $corpus})
            SET sec.name = $name,
                sec.section_number = $section_number,
                sec.section_title = $section_title
            MERGE (sec)-[:REFERENCES]->(c)
            """,
            toc_name=f"{nct_id}:TOC",
            corpus=CORPUS_TAG,
            section_id=section_id,
            name=section.get("name") or section.get("section_title"),
            section_number=section.get("section_number") or "",
            section_title=section.get("section_title") or "",
        )
        parent = _parent_number(section.get("section_number") or "")
        parent_id = by_number.get(parent or "")
        if parent_id:
            session.run(
                """
                MATCH (p:TOC_SECTION {section_id: $parent_id, corpus: $corpus})
                MATCH (c:TOC_SECTION {section_id: $section_id, corpus: $corpus})
                MERGE (p)-[:HAS_SUBSECTION]->(c)
                """,
                parent_id=parent_id,
                section_id=section_id,
                corpus=CORPUS_TAG,
            )
        else:
            session.run(
                """
                MATCH (t:TABLE_OF_CONTENTS {name: $toc_name, corpus: $corpus})
                MATCH (c:TOC_SECTION {section_id: $section_id, corpus: $corpus})
                MERGE (t)-[:HAS_TOC_SECTION]->(c)
                """,
                toc_name=f"{nct_id}:TOC",
                section_id=section_id,
                corpus=CORPUS_TAG,
            )


def load_study(session, study_dir: Path) -> None:
    meta = json.loads((study_dir / "study.json").read_text(encoding="utf-8"))
    nct = meta["nct_id"]
    session.run(
        """
        MERGE (s:STUDY {name: $nct, corpus: $corpus})
        SET s.study_title = $study_title,
            s.study_phase = $study_phase,
            s.study_status = $study_status,
            s.indication = $indication,
            s.subject_type = $subject_type,
            s.comparative_study = $comparative_study,
            s.design = $design,
            s.blinding = $blinding,
            s.allocation = $allocation,
            s.sex = $sex,
            s.sponsor = $sponsor,
            s.enrollment = $enrollment,
            s.pediatric_study = $pediatric
        """,
        nct=nct,
        corpus=CORPUS_TAG,
        study_title=meta.get("study_title"),
        study_phase=meta.get("study_phase"),
        study_status=meta.get("study_status"),
        indication=meta.get("indication"),
        subject_type=meta.get("subject_type"),
        comparative_study=meta.get("comparative_study"),
        design=meta.get("design"),
        blinding=meta.get("blinding"),
        allocation=meta.get("allocation"),
        sex=meta.get("sex"),
        sponsor=meta.get("sponsor"),
        enrollment=meta.get("enrollment"),
        pediatric="Y" if "pediatric" in (meta.get("study_title") or "").lower() else "N",
    )
    criteria = (meta.get("eligibility_criteria") or "").strip()
    for kind, filename in (("PROTOCOL", "protocol_sections.json"), ("SAP", "sap_sections.json"), ("CSR", "csr_sections.json")):
        path = study_dir / filename
        if not path.exists():
            continue
        sections = json.loads(path.read_text(encoding="utf-8"))
        sections.sort(key=lambda item: [int(part) if str(part).isdigit() else 0 for part in str(item.get("section_number") or "0").split(".")])
        if kind == "PROTOCOL" and criteria:
            sections = [{
                "section_number": "0",
                "section_title": "Eligibility Criteria",
                "name": "0 Eligibility Criteria",
                "text": criteria[:12000],
            }] + sections
        _write_sections(session, nct, kind, sections)


def load_corpus() -> dict:
    driver, settings = connect()
    loaded = 0
    with driver.session(database=settings.database) as session:
        clear_corpus(session)
        for study_dir in sorted(STUDIES.iterdir()):
            if (study_dir / "study.json").exists():
                load_study(session, study_dir)
                loaded += 1
        counts = session.run(
            """
            MATCH (n {corpus: $corpus})
            RETURN labels(n) AS labels, count(*) AS n
            """,
            corpus=CORPUS_TAG,
        ).data()
    return {"studies": loaded, "counts": counts}


if __name__ == "__main__":
    print(load_corpus())
