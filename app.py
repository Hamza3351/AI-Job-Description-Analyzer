import streamlit as st
from analyzer import run_analysis

st.set_page_config(page_title="AI Job Analyzer", layout="wide")
st.title("AI Job Description Analyzer")
st.markdown(
    "Analyze a resume against a job description, see missing skills, match %, and AI improvement suggestions."
)

#Input areas
st.markdown("### 1) Enter Job Description & Resume")
jd_text = st.text_area("Job Description", height=200)
resume_text = st.text_area("Resume Text", height=200)

if st.button("Analyze Resume"):
    if not jd_text.strip() or not resume_text.strip():
        st.error("Please enter both Job Description and Resume text.")
    else:
        with st.spinner("Running analysis..."):
            output = run_analysis(jd_text, resume_text)

        #Match % and Resume Score
        st.markdown("### 2) Match & Resume Scores")
        with st.container():
            st.markdown(
                f"""
                <div style="display: flex; gap: 20px;">
                    <div style="background-color:#E8F0FE;padding:20px;border-radius:10px;flex:1;text-align:center">
                        <h3 style="color:#1E40AF">Match %</h3>
                        <h1 style="color:#1E40AF">{output['match_pct']}%</h1>
                    </div>
                    <div style="background-color:#FEF3E8;padding:20px;border-radius:10px;flex:1;text-align:center">
                        <h3 style="color:#B45309">Resume Score</h3>
                        <h1 style="color:#B45309">{output['score']}/100</h1>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        #Skills Analysis
        st.markdown("### 3) Skills Analysis")
        st.markdown(
            f"""
            <div style="background-color:#F0FDF4;padding:15px;border-radius:10px;">
            <h4 style="color:#065F46">Job Skills</h4>
            <p style="color:#065F46">{', '.join(output['job_skills'])}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div style="background-color:#FEF0F0;padding:15px;border-radius:10px;margin-top:10px;">
            <h4 style="color:#B91C1C">Resume Skills</h4>
            <p style="color:#B91C1C">{', '.join(output['resume_skills'])}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        #Missing Skills as badges with colored text
        st.markdown(
            f"""
            <div style="background-color:#FFF7ED;padding:15px;border-radius:10px;margin-top:10px;">
            <h4 style="color:#B45309">Missing Skills</h4>
            {" ".join(
                f'<span style="background-color:#FEE2E2;color:#B91C1C;padding:5px 10px;margin:3px;border-radius:5px;display:inline-block">{skill}</span>'
                for skill in output["missing_skills"]
            )}
            </div>
            """,
            unsafe_allow_html=True,
        )

        #LLM Suggestions
        st.markdown("### 4) AI Improvement Suggestions")
        suggestions = output["suggestions"]

        #Headline
        st.markdown(
            f"""
            <div style="background-color:#ECFDF5;padding:15px;border-radius:10px;">
            <h4 style="color:#065F46">Suggested Headline</h4>
            <p style="font-weight:bold;color:#065F46">{suggestions['headline']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        #Bullets
        st.markdown(
            f"""
            <div style="background-color:#FEFCE8;padding:15px;border-radius:10px;margin-top:10px;">
            <h4 style="color:#78350F">Suggested Resume Bullets</h4>
            {"".join(f'<p style="margin:2px 0;color:#78350F">• {b}</p>' for b in suggestions["bullets"])}
            </div>
            """,
            unsafe_allow_html=True,
        )

        #Rationale
        st.markdown(
            f"""
            <div style="background-color:#E0F2FE;padding:15px;border-radius:10px;margin-top:10px;">
            <h4 style="color:#1E40AF">Rationale</h4>
            <p style="color:#1E40AF">{suggestions['rationale']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        #Optional Raw JSON
        with st.expander("Show Raw JSON Output (Optional)"):
            st.code(output, language="json")
