import argparse, json, re, os
from collections import Counter
from rapidfuzz import fuzz
import spacy
from model_interface import generate

nlp = spacy.load("en_core_web_sm")

#Remove stopwords that are common in job descriptions
STOPWORDS = set([
    "something", "we", "need", "require", "looking",
    "years", "experience", "candidate", "role", "job"
])

def normalize_skill(s):
    """
    Normalize skill text and remove noise/stopwords.
    """
    s_clean = re.sub(r"[^a-z0-9 +#-]", " ", s.lower()).strip()
    if not s_clean or s_clean in STOPWORDS or len(s_clean.split()) > 4:
        return None
    return s_clean

#Extract candidate skills
def extract_candidates(text):
    doc = nlp(text)
    candidates = []

    for chunk in doc.noun_chunks:
        txt = chunk.text.strip().lower()
        if len(txt) > 1:
            candidates.append(txt)

    for ent in doc.ents:
        candidates.append(ent.text.strip().lower())

    for token in doc:
        if token.pos_ in ("NOUN", "PROPN", "ADJ") and len(token.text) > 2:
            candidates.append(token.lemma_.lower())

    counts = Counter(candidates)
    common = [k for k, v in counts.items() if len(k.split()) <= 4][:200]

    cleaned = []
    for s in common:
        ns = normalize_skill(s)
        if ns:
            cleaned.append(ns)

    return list(dict.fromkeys(cleaned))  

#Match job description skills to resume skills
def compute_match(jd_skills, resume_skills):
    matched = []
    for j in jd_skills:
        best = None
        score = 0
        for r in resume_skills:
            s = fuzz.token_sort_ratio(j, r)
            if s > score:
                score = s
                best = r
        if score >= 80:
            matched.append((j, best, score))

    pct = int(len(matched) / max(1, len(jd_skills)) * 100)
    missing = [j for j in jd_skills if j not in [m[0] for m in matched]]

    return pct, matched, missing

#LLM Suggestions
def safe_json(raw):
    cleaned = raw.strip().replace("```json", "").replace("```", "").strip()
    try:
        return json.loads(cleaned)
    except:
        if "{" in cleaned and "}" in cleaned:
            core = cleaned[cleaned.find("{"): cleaned.rfind("}") + 1]
            try:
                return json.loads(core)
            except:
                pass
        return None

#Get suggestions from LLM
def llm_suggestions(jd_text, resume_text, missing_skills):
    prompt = f"""
You are a concise recruiter assistant. Given the job description and resume below, produce:
1) 3 short resume bullet suggestions to highlight missing skills (each 10-15 words)
2) A one-line suggested headline
3) A 2-sentence rationale of the match percentage.

Job description:
{jd_text}

Resume:
{resume_text}

Missing skills:
{', '.join(missing_skills)}

Output JSON with keys: bullets, headline, rationale.
Return only JSON.
"""
    raw = generate(prompt, max_tokens=200)
    parsed = safe_json(raw)
    if parsed:
        return parsed

    return {
        "bullets": [f"Add {s} to resume showing experience." for s in missing_skills[:3]],
        "headline": "Experienced professional aligned with core job skills",
        "rationale": "Automated structured suggestion based on missing skills."
    }

#The main function to run analysis from command line
def main(jd_path, resume_path):
    jd_text = open(jd_path, encoding="utf-8").read()
    resume_text = open(resume_path, encoding="utf-8").read()

    jd_candidates = extract_candidates(jd_text)
    resume_candidates = extract_candidates(resume_text)

    jd_skills = [s for s in jd_candidates][:60]
    resume_skills = [s for s in resume_candidates][:120]

    match_pct, matched, missing = compute_match(jd_skills, resume_skills)

    score = min(100, int(40 + match_pct * 0.5 + len(matched)*2))

    llm_out = llm_suggestions(jd_text, resume_text, missing)

    output = {
        "job_skills": jd_skills,
        "resume_skills": resume_skills,
        "match_pct": match_pct,
        "matched": matched,
        "missing_skills": missing,
        "score": score,
        "suggestions": llm_out
    }

    print(json.dumps(output, indent=2))

    os.makedirs("demo_output_examples", exist_ok=True)
    open("demo_output_examples/example_output.json", "w", encoding="utf-8").write(
        json.dumps(output, indent=2)
    )

#Function to run on streamlit
def run_analysis(jd_text, resume_text):
    jd_candidates = extract_candidates(jd_text)
    resume_candidates = extract_candidates(resume_text)

    jd_skills = [s for s in jd_candidates][:60]
    resume_skills = [s for s in resume_candidates][:120]

    match_pct, matched, missing = compute_match(jd_skills, resume_skills)

    score = min(100, int(40 + match_pct*0.5 + len(matched)*2))

    llm_out = llm_suggestions(jd_text, resume_text, missing)

    return {
        "job_skills": jd_skills,
        "resume_skills": resume_skills,
        "match_pct": match_pct,
        "matched": matched,
        "missing_skills": missing,
        "score": score,
        "suggestions": llm_out
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--jd", required=True)
    parser.add_argument("--resume", required=True)
    args = parser.parse_args()
    main(args.jd, args.resume)
