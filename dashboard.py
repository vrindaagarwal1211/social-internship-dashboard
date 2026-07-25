import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="AI Governance Sentiment Dashboard",
    page_icon="🏛️",
    layout="wide"
)

# ==========================================================
# LOAD DATA
# ==========================================================

df = pd.read_excel("survey_data.xlsx")

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.block-container{
    padding-top:1.5rem;
    padding-bottom:1rem;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    padding:18px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.10);
}

h1,h2,h3{
    color:#003366;
}
.recommend-box{
    background:#F0FDF4;
    border-left:6px solid #10B981;
    border-radius:15px;
    padding:22px;
    color:#065F46;
    margin-top:20px;
    margin-bottom:20px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
    transition:all 0.35s ease;
    cursor:pointer;
}
.recommend-box:hover{
    transform:translateY(-6px) scale(1.02);
    box-shadow:0px 12px 28px rgba(16,185,129,0.25);
    border-left:8px solid #10B981;
}
.ai-box{
    background:#EEF4FF;
    border-left:6px solid #3B82F6;
    border-radius:15px;
    padding:22px;
    color:#1E3A8A;
    margin-top:20px;
    margin-bottom:20px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
    transition:all 0.35s ease;
    cursor:pointer;
}
.ai-box:hover{
    transform:translateY(-6px) scale(1.02);
    box-shadow:0px 12px 28px rgba(37,99,235,0.25);
    background:#E3F0FF;
}
.insight-box{
    background:#EAF3FF;
    border-radius:18px;
    padding:24px;
    color:#0F4C9A;
    margin-top:20px;
    margin-bottom:20px;
    box-shadow:0 4px 12px rgba(37,99,235,0.12);
    transition:all 0.35s ease;
}
.insight-title{
    font-size:22px;
    font-weight:700;
    color:#0B4EA2;
    margin-bottom:18px;
}

.bulb{
    display:inline-block;
    transition:all .35s ease;
}

.insight-box:hover .bulb{
    transform:scale(1.25) rotate(-8deg);
    filter:
        drop-shadow(0 0 6px #FFD54F)
        drop-shadow(0 0 12px #FFC107)
        drop-shadow(0 0 20px #FFEB3B);
}



</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/5/55/Emblem_of_India.svg",
    width=90
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Dashboard",
        "👥 Demographics",
        "🌐 Digital India",
        "🏥 Ayushman Bharat",
        "📊 Overall Analysis"
    ]
)

# ==========================================================
# DASHBOARD
# ==========================================================

if page == "🏠 Dashboard":

    st.title("🏛 Governance Sentiment Analysis Dashboard")

    st.caption(
        "Citizen Opinion Analysis on Government Welfare Schemes"
    )

    total = len(df)

    digital = round(
        (df["Q5. Are you aware of the Digital India Initiative launched by the Government of India?  "]=="Yes").mean()*100
    )

    ayushman = round(
        (df["Q12. Are you aware of the Ayushman Bharat (PM-JAY) health insurance scheme? "]=="Yes").mean()*100
    )

    benefited = round(
        (df["Q13. Have you or any member of your family ever benefited from the Ayushman Bharat (PM-JAY) scheme? "]=="Yes").mean()*100
    )

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Total Responses", total)
    col2.metric("Digital India Awareness", f"{digital}%")
    col3.metric("Ayushman Awareness", f"{ayushman}%")
    col4.metric("Beneficiaries", f"{benefited}%")

    st.divider()

    left,right = st.columns(2)

    with left:

        age = df["Q1. What is your age group?"].value_counts().reset_index()
        age.columns=["Age Group","Count"]

        fig = px.pie(
            age,
            names="Age Group",
            values="Count",
            hole=0.55,
            title="Age Distribution"
        )

        st.plotly_chart(fig,use_container_width=True)

    with right:

        gender=df["Q2. What is your gender? "].value_counts().reset_index()
        gender.columns=["Gender","Count"]

        fig=px.bar(
            gender,
            x="Gender",
            y="Count",
            color="Gender",
            text="Count",
            title="Gender Distribution"
        )

        st.plotly_chart(fig,use_container_width=True)

    st.divider()

    st.subheader("Quick Overview")

    overview = pd.DataFrame({
        "Metric":[
            "Total Survey Responses",
            "Digital India Awareness",
            "Ayushman Bharat Awareness",
            "Ayushman Beneficiaries"
        ],
        "Value":[
            total,
            f"{digital}%",
            f"{ayushman}%",
            f"{benefited}%"
        ]
    })

    st.dataframe(
        overview,
        use_container_width=True,
        hide_index=True
    )

# ==========================================================
# DEMOGRAPHICS
# ==========================================================

elif page == "👥 Demographics":

    st.title("👥 Demographic Analysis")

    # ---------------- Age ---------------- #

    left, right = st.columns(2)

    with left:

        age = df["Q1. What is your age group?"].value_counts().reset_index()
        age.columns = ["Age Group", "Count"]

        fig = px.pie(
            age,
            names="Age Group",
            values="Count",
            hole=0.55,
            title="Age Group Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:

        gender = df["Q2. What is your gender? "].value_counts().reset_index()
        gender.columns = ["Gender", "Count"]

        fig = px.bar(
            gender,
            x="Gender",
            y="Count",
            color="Gender",
            text="Count",
            title="Gender Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)
    st.subheader("📖 Interpretation")
    st.markdown("""<div class="recommend-box">
        • The survey represents a balanced mix of age groups, with the largest participation coming from individuals <b>aged 26–40 years</b>, followed closely by respondents <b>aged 41–60 years</b>.<br>
        • The responses mainly reflect the opinions of the <b>economically active and digitally engaged population</b>.<br>
        • Since the majority belongs to working-age groups, the findings are particularly relevant for evaluating digital public services.<br>
        • The inclusion of <b>younger respondents</b> suggests increasing awareness of government initiatives <b>among students</b> and <b>first-time digital users</b>.<br>
        • Female respondents slightly outnumber male respondents <b>(52% vs 48%)</b>.<br>
        • The <b>nearly equal gender representation</b> makes the survey balanced and reduces gender-based bias.<br>
        • Women's participation indicates growing engagement with digital governance and welfare schemes.
        </div>""", unsafe_allow_html=True)

    st.divider()

    # ---------------- Occupation ---------------- #

    left, right = st.columns(2)

    with left:

        occupation = df["Q3. What is your current occupation? "].value_counts().reset_index()
        occupation.columns = ["Occupation", "Count"]

        fig = px.bar(
            occupation,
            x="Occupation",
            y="Count",
            color="Occupation",
            text="Count",
            title="Occupation"
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:

        residence = df["Q4. Where do you currently reside? "].value_counts().reset_index()
        residence.columns = ["Residence", "Count"]

        fig = px.pie(
            residence,
            names="Residence",
            values="Count",
            hole=0.50,
            title="Residence"
        )

        st.plotly_chart(fig, use_container_width=True)
    st.subheader("📖 Interpretation")
    st.markdown("""<div class="recommend-box">
            • Responses come from <b>diverse professional backgrounds</b> rather than a single category.<br>
            • This diversity improves the reliability of the overall findings.<br>
            • <b>Students</b> being the largest group indicates higher digital exposure and awareness among younger citizens.<br>
            </div>""", unsafe_allow_html=True)
    

    st.divider()

    # ---------------- Q17 ---------------- #

    st.subheader("Primary Source of Information about Government Schemes")

    counter = Counter()

    for response in df[
        "Q17. What is your primary source of information about government welfare schemes? "
    ].dropna():

        responses = str(response).split(",")

        for item in responses:
            counter[item.strip()] += 1

    source_df = pd.DataFrame(
        counter.items(),
        columns=["Source", "Count"]
    )

    source_df = source_df.sort_values("Count")

    fig = px.bar(
        source_df,
        x="Count",
        y="Source",
        orientation="h",
        text="Count",
        color="Count",
        color_continuous_scale="Blues",
        title="Primary Sources of Information"
    )

    fig.update_layout(
        xaxis_title="Number of Responses",
        yaxis_title=""
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📖 Interpretation")
    st.markdown("""<div class="ai-box">
                • Social media has emerged as the dominant channel for disseminating information about government welfare schemes, highlighting the importance of digital platforms in public communication.<br>
                • Traditional media like newspapers and television still play a significant role, especially among older demographics.<br>
                • Peer networks (friends and family) are crucial for information dissemination, indicating the influence of personal recommendations.<br>
                • The relatively lower reliance on official government websites suggests a need for improved digital outreach and user-friendly online resources.<br>
                </div>""", unsafe_allow_html=True)
# ==========================================================
# DIGITAL INDIA
# ==========================================================

elif page == "🌐 Digital India":

    st.title("🌐 Digital India Initiative Analysis")
    st.markdown("### Citizen Awareness, Usage and Satisfaction")
    st.divider()

    # -------------------------------------------------------
    # Helper Function (for normal single-choice questions)
    # -------------------------------------------------------

    def plot_single(column, title, chart="bar"):

        chart_df = (
            df[column]
            .fillna("No Response")
            .value_counts()
            .reset_index()
        )

        chart_df.columns = ["Response", "Count"]

        if chart == "pie":

            fig = px.pie(
                chart_df,
                names="Response",
                values="Count",
                hole=0.55
            )

        else:

            fig = px.bar(
                chart_df,
                x="Response",
                y="Count",
                color="Response",
                text="Count"
            )

            fig.update_layout(showlegend=False)

        fig.update_layout(height=450)

        st.subheader(title)
        st.plotly_chart(fig, use_container_width=True)

    # =====================================================
    # Q5
    # =====================================================

    plot_single(
        "Q5. Are you aware of the Digital India Initiative launched by the Government of India?  ",
        "Q5. Awareness of Digital India",
        "pie"
    )

    st.divider()

    # =====================================================
    # Q6
    # =====================================================

    st.subheader("Q6. Digital India Services Used")

    responses = df["Q6. Which of the following Digital India services have you used? "]\
            .fillna("").astype(str)

    services = {
    "UPI (Google Pay, PhonePe, BHIM, etc.)":
        responses.str.contains("UPI", case=False).sum(),

    "DigiLocker":
        responses.str.contains("DigiLocker", case=False).sum(),

    "Aadhaar Online Services":
        responses.str.contains("Aadhaar", case=False).sum(),

    "UMANG App":
        responses.str.contains("UMANG", case=False).sum(),

    "Online Government Portals":
        responses.str.contains("Online Government", case=False).sum(),

    "None of the Above":
        responses.str.contains("None", case=False).sum()
}

    q6_df = pd.DataFrame({
        "Service": list(services.keys()),
        "Count": list(services.values())
    })

    fig = px.bar(
        q6_df,
        x="Service",
        y="Count",
        text="Count",
        color="Service"
    )

    fig.update_layout(
            height=500,
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # =====================================================
    # Q7
    # =====================================================

    plot_single(
        "Q7. How often do you use Digital India services?  ",
        "Q7. Frequency of Usage"
    )

    st.divider()

    # =====================================================
    # Q8
    # =====================================================

    plot_single(
        "Q8. How satisfied are you with your overall experience using Digital India services?",
        "Q8. Satisfaction Level",
        "bar"
    )

    st.divider()

    # =====================================================
    # Q9
    # =====================================================

    st.subheader("Q9. Challenges Faced")

    responses = df[
    "Q9. What challenges have you faced while using Digital India services?  "
].fillna("").astype(str)

    challenge_list = [
    "Slow websites",
    "Technical errors",
    "Lack of awareness about services",
    "Complicated registration process",
    "Internet connectivity issues",
    "No challenges faced"
]

    counts = []

    for challenge in challenge_list:

        counts.append(
        responses.str.contains(challenge, case=False).sum()
    )

    q9_df = pd.DataFrame({
    "Challenge": challenge_list,
    "Count": counts
})

    fig = px.bar(
    q9_df,
    x="Challenge",
    y="Count",
    text="Count",
    color="Challenge"
)

    fig.update_layout(
    showlegend=False,
    height=500
)

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # =====================================================
    # Q10
    # =====================================================

    plot_single(
        "Q10. Do you believe the Digital India Initiative has made government services more accessible to citizens? ",
        "Q10. Accessibility of Government Services due to Digital India Initiative",
        "pie"
    )

    st.divider()

    # =====================================================
    # Q11
    # =====================================================

    plot_single(
        "Q11. Which area of the Digital India Initiative requires the most improvement? ",
        "Q11. Areas Requiring Improvement"
    )
    

    st.divider()

    st.markdown("""
<div class="insight-box">

<div class="insight-title">
<span class="bulb">💡</span> Key Insights
</div>

• Most respondents are aware of the Digital India Initiative.<br>

• UPI and DigiLocker are the most frequently used digital services.<br>

• Most respondents have not faced major challenges, though digital literacy remains a concern.<br>

• Most respondents believe Digital India has improved access to government services.
</div>
""", unsafe_allow_html=True)
    st.success(
        "✅ Overall Observation: Survey responses indicate strong awareness of the Digital India Initiative. Citizens actively use digital government services, although challenges such as technical issues, digital literacy, and internet connectivity continue to affect the overall user experience."
    )
# ==========================================================
# AYUSHMAN BHARAT
# ==========================================================

elif page == "🏥 Ayushman Bharat":

    st.title("🏥 Ayushman Bharat (PM-JAY) Analysis")
    st.markdown("Citizen perception and awareness regarding the Ayushman Bharat health insurance scheme.")

    # ---------------- Q12 ---------------- #

    st.subheader("Q12. Awareness of Ayushman Bharat")

    q12 = df["Q12. Are you aware of the Ayushman Bharat (PM-JAY) health insurance scheme? "].value_counts().reset_index()
    q12.columns = ["Response","Count"]

    fig = px.pie(
        q12,
        names="Response",
        values="Count",
        hole=0.55,
        color_discrete_sequence=["#2E86DE","#AAB7B8"]
    )

    st.plotly_chart(fig,use_container_width=True)

    st.divider()

    # ---------------- Q13 ---------------- #

    st.subheader("Q13. Benefited from Ayushman Bharat")

    q13 = df["Q13. Have you or any member of your family ever benefited from the Ayushman Bharat (PM-JAY) scheme? "].value_counts().reset_index()
    q13.columns=["Response","Count"]

    fig = px.pie(
        q13,
        names="Response",
        values="Count",
        hole=0.55,
        color_discrete_sequence=[
    "#2E8B57",   # Yes
    "#E74C3C",   # No
    "#F4B400",   # Not Eligible
    "#5DADE2"    # Not Sure
]
    )

    st.plotly_chart(fig,use_container_width=True)

    st.divider()

    # ---------------- Q14 ---------------- #

    st.subheader("Q14. Overall Opinion")

    q14 = df["Q14. How would you rate your overall opinion of the Ayushman Bharat (PM-JAY) scheme based on your awareness or experience? "].value_counts().reset_index()

    q14.columns=["Opinion","Count"]

    fig = px.bar(
        q14,
        x="Count",
        y="Opinion",
        orientation="h",
        text="Count",
        color="Count",
        color_continuous_scale="Greens"
    )

    fig.update_layout(
        xaxis_title="Responses",
        yaxis_title=""
    )

    st.plotly_chart(fig,use_container_width=True)

    st.divider()

    # ---------------- Q15 ---------------- #

    st.subheader("Q15. Challenges Faced")

    counter = Counter()

    for response in df[
        "Q15. What challenges do citizens commonly face while accessing Ayushman Bharat (PM-JAY)? "
    ].dropna():

        for item in str(response).split(","):
            counter[item.strip()] += 1

    challenge = pd.DataFrame(
        counter.items(),
        columns=["Challenge","Count"]
    )

    challenge = challenge.sort_values("Count")

    fig = px.bar(
        challenge,
        x="Count",
        y="Challenge",
        orientation="h",
        text="Count",
        color="Count",
        color_continuous_scale="Oranges"
    )

    fig.update_layout(
        xaxis_title="Responses",
        yaxis_title=""
    )

    st.plotly_chart(fig,use_container_width=True)

    st.divider()

    # ---------------- Q16 ---------------- #

    st.subheader("Q16. Has Ayushman Bharat Improved Healthcare Access?")

    q16 = df["Q16. Do you believe Ayushman Bharat (PM-JAY) has improved access to affordable healthcare? "].value_counts().reset_index()

    q16.columns=["Response","Count"]

    fig = px.pie(
        q16,
        names="Response",
        values="Count",
        hole=0.55,
        color_discrete_sequence=["#00B894","#B2BEC3"]
    )

    st.plotly_chart(fig,use_container_width=True)
    st.divider()
    st.markdown("""
    <div class="insight-box">
    
    <div class="insight-title">
    <span class="bulb">💡</span> Key Insights
    </div>
    
    • Awareness of Ayushman Bharat is high among respondents.<br>
    
    • Many respondents or their family members have benefited from the scheme.<br>
    
    • Awareness and eligibility issues remain common challenges.<br>
    
    • Most respondents believe the scheme has improved access to affordable healthcare.
    </div>
    """, unsafe_allow_html=True)

    st.success("✅ Overall Observation: Most respondents are aware of Ayushman Bharat, but many still reported difficulties related to eligibility, documentation, and hospital accessibility.")
# ==========================================================
# OVERALL ANALYSIS
# ==========================================================

elif page == "📊 Overall Analysis":

    st.title("📊 Overall Analysis & Insights")

    st.markdown(
        "Comparative analysis of public perception towards the Digital India Initiative and Ayushman Bharat (PM-JAY)."
    )

    # ------------------------------------------------------
    # Q18 Comparison
    # ------------------------------------------------------

    st.subheader("Government Initiative with Greater Positive Impact")

    impact = df[
        "Q18. Which of the following government initiatives has had a greater positive impact on society, in your opinion?  "
    ].value_counts().reset_index()

    impact.columns = ["Scheme", "Votes"]

    fig = px.pie(
    impact,
    names="Scheme",
    values="Votes",
    hole=0.60,
    color="Scheme",
    color_discrete_map={
        "Digital India Initiative": "#2E7D32",              # Green
        "Ayushman Bharat (PM-JAY)": "#1976D2",              # Blue
        "Both have equal positive impact": "#F4B400",       # Gold
        "Neither has significant impact": "#E53935",        # Red
        "Not Sure": "#8E44AD"                               # Purple
    }
)

    fig.update_traces(
    textposition="inside",
    textinfo="percent+label",
    marker=dict(line=dict(color="white", width=2))
)

    fig.update_layout(
    legend_title="Response",
    showlegend=True
)

    st.plotly_chart(fig, use_container_width=True, key="q18_comparison")
    st.subheader("📈 Analysis of Public Opinion")

    # total_votes = impact["Votes"].sum()

    # for _, row in impact.iterrows():
    #     percentage = (row["Votes"] / total_votes) * 100
    #     st.write(f"• **{row['Scheme']}** was selected by **{percentage:.1f}%** of respondents.")

    # Calculate percentages

    total = impact["Votes"].sum()

    digital = impact.loc[impact["Scheme"]=="Digital India","Votes"].sum()/total*100
    ayushman = impact.loc[impact["Scheme"]=="Ayushman Bharat (PM-JAY)","Votes"].sum()/total*100
    both = impact.loc[impact["Scheme"]=="Both have had an equal impact","Votes"].sum()/total*100
    neither = impact.loc[impact["Scheme"]=="Neither","Votes"].sum()/total*100
    notsure = impact.loc[impact["Scheme"]=="Cannot Say","Votes"].sum()/total*100

    st.write(f"""

• **Digital India Initiative** was preferred by **{digital:.1f}%** of respondents, while **Ayushman Bharat (PM-JAY)** was preferred by **{ayushman:.1f}%**.

• **{both:.1f}%** of respondents believe that **both schemes have contributed equally** towards improving citizens' lives.

• Only **{neither:.1f}%** felt that **neither initiative has had a significant impact**, whereas **{notsure:.1f}%** were **uncertain** about their opinion.

• Overall, the survey indicates a **positive public perception** towards flagship government initiatives, with relatively few respondents expressing negative or uncertain views.
""")

    st.divider()
# ==========================================================
# SCHEME COMPARISON TABLE
# ==========================================================

    st.subheader("📋 Comparative Analysis of Government Schemes")

    digital_awareness = round(
    (df["Q5. Are you aware of the Digital India Initiative launched by the Government of India?  "] == "Yes").mean()*100,
    1
)

    ayushman_awareness = round(
    (df["Q12. Are you aware of the Ayushman Bharat (PM-JAY) health insurance scheme? "] == "Yes").mean()*100,
    1
)

    digital_positive = round(
    (df["Q10. Do you believe the Digital India Initiative has made government services more accessible to citizens? "] == "Yes").mean()*100,
    1
)

    ayushman_positive = round(
    (df["Q16. Do you believe Ayushman Bharat (PM-JAY) has improved access to affordable healthcare? "] == "Yes").mean()*100,
    1
)

    comparison = pd.DataFrame({

    "Parameter":[
        "Primary Objective",
        "Citizen Awareness (%)",
        "Positive Public Opinion (%)",
        "Main Benefit",
        "Major Challenge",
        "Target Sector"
    ],

    "Digital India":[
        "Digital Governance",
        f"{digital_awareness}%",
        f"{digital_positive}%",
        "Online Government Services",
        "Internet & Digital Literacy",
        "Technology"
    ],

    "Ayushman Bharat":[
        "Affordable Healthcare",
        f"{ayushman_awareness}%",
        f"{ayushman_positive}%",
        "Health Insurance",
        "Eligibility & Awareness",
        "Healthcare"
    ]

})

    st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)

    # ------------------------------------------------------
    # KPI CARDS
    # ------------------------------------------------------

    digital_awareness = round(
        (
            df["Q5. Are you aware of the Digital India Initiative launched by the Government of India?  "]
            == "Yes"
        ).mean() * 100
    )

    ayushman_awareness = round(
        (
            df["Q12. Are you aware of the Ayushman Bharat (PM-JAY) health insurance scheme? "]
            == "Yes"
        ).mean() * 100
    )

    avg_satisfaction = round(
        df[
            "Q8. How satisfied are you with your overall experience using Digital India services?"
        ].mean(),
        2
    )

    total = len(df)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Responses", total)
    c2.metric("Digital India Awareness", f"{digital_awareness}%")
    c3.metric("Ayushman Awareness", f"{ayushman_awareness}%")
    c4.metric("Average Satisfaction", avg_satisfaction)

    st.divider()

    # ------------------------------------------------------
    # AI INSIGHTS
    # ------------------------------------------------------

    st.subheader("💡 Major Findings")

    st.info(f"""
**Digital India Initiative**

• Digital India enjoys exceptionally high awareness and strong public acceptance.

• UPI has become the flagship success of Digital India, demonstrating widespread adoption.

• Most respondents are satisfied with digital government services despite occasional technical issues.

• Technical performance and digital literacy remain the biggest improvement areas.


**Ayushman Bharat (PM-JAY)**

• Ayushman Bharat is positively perceived but has lower awareness and utilization than Digital India.

• Administrative barriers such as documentation and eligibility reduce access to healthcare benefits.


• Social media has emerged as the dominant channel for disseminating information about government welfare schemes.

• Overall, respondents perceive Digital India as having the greater societal impact due to its integration into everyday life.
""")

    st.divider()

    # ------------------------------------------------------
    # RECOMMENDATIONS
    # ------------------------------------------------------

    st.subheader("📌 Recommendations")

    st.success("""
**Based on the survey responses, the following improvements are recommended:**

• Improve awareness campaigns in rural and semi-urban regions.

• Enhance digital literacy programs to increase service adoption.

• Improve website speed, platform reliability, and technical support to enhance the user experience.

• Simplify hospital enrollment and eligibility procedures under Ayushman Bharat.

• Continue collecting citizen feedback to support evidence-based policy improvements.
""")