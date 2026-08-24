import streamlit as st
from PIL import Image
import pandas as pd

from defect_detector import ConcreteDefectDetector
from recommendations import get_recommendation


# ------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------

st.set_page_config(
    page_title="Concrete Defect AI",
    page_icon="🏗️",
    layout="wide"
)


# ------------------------------------------------
# HEADER
# ------------------------------------------------

st.title("🏗️ AI-Enabled Concrete Defect Detection")

st.write(
    "Upload a concrete image to detect visible defects "
    "and receive prevention and inspection recommendations."
)

st.divider()


# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------

st.sidebar.header("⚙️ Inspection Settings")

confidence_threshold = st.sidebar.slider(
    "Detection Confidence",
    0.10,
    0.95,
    0.25
)

st.sidebar.info(
    "The AI result is intended for preliminary inspection "
    "support and should not replace professional structural assessment."
)


# ------------------------------------------------
# IMAGE UPLOAD
# ------------------------------------------------

uploaded_file = st.file_uploader(
    "📷 Upload Concrete Image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Original Image")

        st.image(
            image,
            use_container_width=True
        )


    # ------------------------------------------------
    # LOAD MODEL
    # ------------------------------------------------

    try:

        detector = ConcreteDefectDetector(
            "models/best.pt"
        )

        with st.spinner("🤖 AI is analyzing the concrete image..."):

            result, detections = detector.detect(image)

    except Exception as e:

        st.error(
            "AI model could not be loaded. "
            "Make sure models/best.pt exists."
        )

        st.exception(e)

        st.stop()


    # ------------------------------------------------
    # DISPLAY DETECTED IMAGE
    # ------------------------------------------------

    with col2:

        st.subheader("AI Detection")

        annotated_image = result.plot()

        st.image(
            annotated_image,
            channels="BGR",
            use_container_width=True
        )


    st.divider()


    # ------------------------------------------------
    # RESULTS
    # ------------------------------------------------

    st.header("🔍 Detection Results")


    if len(detections) == 0:

        st.warning(
            "No trained concrete defect was detected."
        )

    else:

        data = []

        for detection in detections:

            defect = detection["defect"]

            confidence = detection["confidence"]

            data.append({
                "Defect": defect,
                "Confidence": f"{confidence * 100:.2f}%"
            })


        df = pd.DataFrame(data)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )


        # ------------------------------------------------
        # RECOMMENDATIONS
        # ------------------------------------------------

        st.header("💡 AI Recommendations")


        for detection in detections:

            defect = detection["defect"]

            confidence = detection["confidence"]

            recommendation = get_recommendation(
                defect
            )


            st.subheader(
                f"🚨 {defect.title()}"
            )

            st.write(
                f"**Confidence:** "
                f"{confidence * 100:.2f}%"
            )


            # Possible Causes

            st.markdown("### 🔎 Possible Causes")

            for cause in recommendation["cause"]:

                st.write(
                    f"• {cause}"
                )


            # Prevention

            st.markdown(
                "### 🛡️ Prevention"
            )

            for prevention in recommendation["prevention"]:

                st.write(
                    f"• {prevention}"
                )


            # Action

            st.markdown(
                "### 🔧 Recommended Action"
            )

            for action in recommendation["action"]:

                st.write(
                    f"• {action}"
                )


            st.divider()


# ------------------------------------------------
# FOOTER
# ------------------------------------------------

st.caption(
    "AI Concrete Defect Detection & Recommendation System"
)
