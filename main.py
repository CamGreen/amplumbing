import streamlit as st
import os

# Page configuration
st.set_page_config(page_title="AM Plumbing", layout="wide")
image_dir = "assets"
gallery_images = [
    ("Solar Geyser.jpeg", "Solar Geyser"),
    ("Backup Water Solution with pumps.jpeg", "Backup Water Solution with pumps"),
    ("Backup Water Solution with pump.jpeg", "Backup Water Solution with pump"),
    ("Water Filter Installation.jpeg", "Water Filter Installation"),
    ("gasGeyser2.jpeg", "Gas Geyser Installation"),
    ("burstPipe.jpeg", "Burst Pipe Repair")]

banner_base64 = get_base64_image(r"C:\amplumbing\assets\banner2.png")

# Session state page
if "page" not in st.session_state:
    st.session_state.page = "Home"

# 🌄 Full width HTML banner with text overlay
st.markdown(
    f"""
    <style>
    .banner {{
        position: relative;
        height: 460px;
        width: 100%;
        background-image: url("{banner_base64}");
        background-size: cover;
        background-position: center;
    }}
    .banner-text {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
    }}
    .banner-text h1 {{
        font-size: 52px;
        margin-bottom: 10px;
    }}
    .banner-text h4 {{
        font-size: 22px;
        font-weight: normal;
    }}
    </style>

    <div class="banner">
    </div>
    """,
    unsafe_allow_html=True
)

# 🧭 Top Navigation Bar
st.markdown(" ")  # Small spacing
nav_cols = st.columns(4)
pages = ["Home", "Services", "Gallery", "Contact"]
for i, nav in enumerate(pages):
    if nav_cols[i].button(nav):
        st.session_state.page = nav
st.markdown("---")

# 🧱 Main Content Based on Page
page = st.session_state.page

if page == "Home":
    st.subheader("Welcome to AM Plumbing")

    st.write("""
At AM Plumbing, we pride ourselves on delivering trusted, affordable plumbing services throughout your area.  
With over 30 years of experience, our licensed professionals bring a level of expertise, quality, and customer care that sets us apart.
""")

    st.success("Call us 24/7 for emergencies: 083 783 9093")

    st.markdown("### What Makes Us Different?")
    st.write("""
In a parity environment where most plumbing companies offer similar services, it's not just about what we do — it's about how and why we do it better.

Our 30+ years of experience set us apart by offering:
""")

    st.markdown("""
1. **Expert Problem-Solving** – We accurately diagnose and fix issues faster than less-experienced providers.  
2. **Reliability & Quality Workmanship** – We do it right the first time, saving you from repeat issues and stress.  
3. **Personalized Customer Service** – We understand your unique needs and tailor solutions that work best for your home or business.  
4. **Reputation & Trust** – Our long-standing track record speaks for itself — our clients trust us again and again.  
5. **Efficiency & Time Savings** – We get the job done quickly and cleanly, minimizing disruption to your day.  
""")

    st.info("We’ve built our reputation on trust, dependability, and consistent high-quality plumbing services.")

    st.markdown("#### Why Choose AM Plumbing?")
    st.markdown("""
- ✅ Fully Licensed & Insured Technicians  
- ✅ 30+ Years of Industry Experience  
- ✅ Transparent, Upfront Pricing  
- ✅ Emergency Calls Always Welcome  
- ✅ 100% Customer Satisfaction Guarantee  
    """)

elif page == "Services":
    st.subheader("Our Services")
    services = {
        "Back Up Water Solutions": "Installation of back up water tanks and pumps to suit your needs.",
        "Residential Plumbing": "Leaks, pipe repair, fixture installs, pipe rerouting, toilets and more.",
        "Commercial Plumbing": "Backflow prevention, system maintenance, drain/sewer inspection.",
        "Water Heater Installation": "Service & installation gas, electric and solar systems.",
        "Emergency Repairs (24/7)": "Rapid response for major leaks, burst pipes, flooded basements.",
        "Drain Cleaning": "Hydro-jetting, camera inspection, and root removal.",
        "Bathroom & Kitchen Renovations": "Full-service plumbing for upgrades and complete remodels."
    }

    for service, desc in services.items():
        st.markdown(f"### 🔹 {service}")
        st.write(desc)
        st.markdown("---")

# elif page == "Gallery":
#     st.subheader("Project Gallery")
#     st.write("Check out a few highlights from our recent plumbing projects.")
#
#     # 🔧 Specify the image filenames and captions
#     image_dir = "assets"
#     gallery_images = [
#         ("Solar Geyser.jpeg", "Solar Geyser"),
#         ("Backup Water Solution with pumps.jpeg", "Backup Water Solution with pumps"),
#         ("Backup Water Solution with pump.jpeg", "Backup Water Solution with pump"),
#         ("Water Filter Installation.jpeg", "Water Filter Installation")]
#
#     # ➕ Create 3-column layout
#     cols = st.columns(3)
#
#     # 🖼️ Display each image in a column
#     for i, (filename, caption) in enumerate(gallery_images):
#         image_path = os.path.join(image_dir, filename)
#         if os.path.exists(image_path):
#             with cols[i % 3]:
#                 st.image(image_path, use_container_width=True, caption=caption)

elif page == "Gallery":
    st.subheader("Project Gallery")
    st.write("Check out a few highlights from our recent plumbing projects.")

    image_dir = "assets"

    # 👇 Update for your image names and captions
    # gallery_images = [
    #     ("solar_geyser.jpg", "Solar Geyser Installation"),
    #     ("backup_water_pumps.jpg", "Backup Water Solution with Pumps"),
    #     ("backup_water_pump.jpg", "Backup Water Solution with Pump"),
    #     ("water_filter.jpg", "Water Filtration System")
    # ]

    cols = st.columns(3)

    img_fixed_height = 200  # px

    for i, (filename, caption) in enumerate(gallery_images):
        img_path = os.path.join(image_dir, filename)
        if os.path.exists(img_path):
            with cols[i % 3]:
                st.image(img_path, caption=caption, width=300)  # Fixed width
                st.markdown(
                    f"""<style>
                    img {{
                        height: {img_fixed_height}px !important;
                        object-fit: cover;
                        border-radius: 8px;
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )

elif page == "Contact":
    st.subheader("Contact Us")

    st.write("Whether it’s an emergency or you’d like to plan ahead, we’re here to help!")

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        message = st.text_area("How can we help you?")
        submitted = st.form_submit_button("Submit")

        if submitted:
            if name and email and message:
                st.success("Your message has been sent! We'll respond shortly.")
                # In production, you can send an email or save to your DB
            else:
                st.warning("Please fill in at least your name, email, and message.")

    st.markdown("---")
    st.markdown("📍 **Based in:** Pretoria and Johanessburg Areas")
    st.markdown("📞 **Phone:** 083 783 9093")
    st.markdown("📧 **Email:** info@amplumbing.com")

