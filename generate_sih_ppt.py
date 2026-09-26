# -*- coding: utf-8 -*-
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen layout
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Theme Colors
    NAVY = RGBColor(16, 44, 87)       # #102C57
    ROYAL = RGBColor(26, 77, 146)     # #1A4D92
    TEAL = RGBColor(0, 150, 169)      # #0096A9
    DARK_GRAY = RGBColor(50, 50, 50)
    LIGHT_BG = RGBColor(245, 247, 250)
    WHITE = RGBColor(255, 255, 255)
    ACCENT_ORANGE = RGBColor(235, 94, 40)
    ACCENT_GREEN = RGBColor(46, 117, 89)
    ACCENT_PURPLE = RGBColor(112, 48, 160)
    BORDER_GRAY = RGBColor(210, 215, 222)
    LIGHT_BLUE = RGBColor(234, 242, 250)
    LIGHT_GREEN = RGBColor(232, 245, 233)
    LIGHT_ORANGE = RGBColor(254, 243, 235)
    LIGHT_PURPLE = RGBColor(245, 238, 250)

    def add_header(slide, title_text, slide_num):
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.85))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = WHITE
        top_bar.line.color.rgb = BORDER_GRAY

        txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.1), Inches(9.5), Inches(0.65))
        tf = txBox.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = "Calibri"
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = NAVY

        tagBox = slide.shapes.add_textbox(Inches(9.8), Inches(0.1), Inches(3.0), Inches(0.65))
        tag_tf = tagBox.text_frame
        p_tag = tag_tf.paragraphs[0]
        p_tag.alignment = PP_ALIGN.RIGHT
        p_tag.text = "SMART INDIA HACKATHON 2025"
        p_tag.font.name = "Calibri"
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = ROYAL

        p_tag2 = tag_tf.add_paragraph()
        p_tag2.alignment = PP_ALIGN.RIGHT
        p_tag2.text = "Ministry of Home Affairs • SSB Defense"
        p_tag2.font.name = "Calibri"
        p_tag2.font.size = Pt(9.5)
        p_tag2.font.color.rgb = ACCENT_ORANGE

        bot_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(7.15), Inches(13.333), Inches(0.35))
        bot_bar.fill.solid()
        bot_bar.fill.fore_color.rgb = NAVY
        bot_bar.line.fill.background()

        botBox = slide.shapes.add_textbox(Inches(0.5), Inches(7.15), Inches(10.0), Inches(0.35))
        b_tf = botBox.text_frame
        bp = b_tf.paragraphs[0]
        bp.text = "SMART INDIA HACKATHON 2025  |  RakshaScan AI: Dual-Mode Border Identity Forensics  |  MHA / SSB"
        bp.font.name = "Calibri"
        bp.font.size = Pt(10)
        bp.font.color.rgb = WHITE

        numBox = slide.shapes.add_textbox(Inches(12.0), Inches(7.15), Inches(1.0), Inches(0.35))
        n_tf = numBox.text_frame
        np = n_tf.paragraphs[0]
        np.alignment = PP_ALIGN.RIGHT
        np.text = str(slide_num)
        np.font.name = "Calibri"
        np.font.size = Pt(11)
        np.font.bold = True
        np.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 1: TITLE PAGE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = LIGHT_BG
    bg1.line.fill.background()

    title_box = s1.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(11.5), Inches(0.8))
    tf1 = title_box.text_frame
    p = tf1.paragraphs[0]
    p.text = "SMART INDIA HACKATHON 2025"
    p.font.name = "Calibri"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = NAVY

    sub_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.4), Inches(11.7), Inches(0.06))
    sub_bar.fill.solid()
    sub_bar.fill.fore_color.rgb = ACCENT_ORANGE
    sub_bar.line.fill.background()

    info_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(7.8), Inches(4.8))
    info_card.fill.solid()
    info_card.fill.fore_color.rgb = WHITE
    info_card.line.color.rgb = BORDER_GRAY

    itf = info_card.text_frame
    itf.word_wrap = True

    entries = [
        ("Problem Statement ID", "SIH1642 (or allotted ID)"),
        ("Problem Statement Title", "AI-Based Fake Identity & Document Screening System"),
        ("Project Codename", "RakshaScan AI - Dual-Mode Border Identity Forensics"),
        ("Theme", "Smart Automation / Homeland Security & Defense"),
        ("PS Category", "Software / Defense Edge AI"),
        ("Target End-Users", "Sashastra Seema Bal (SSB), BSF, Bureau of Immigration (BOI)"),
        ("Team ID", "[Your Team ID]"),
        ("Team Name", "[Your Team Name]")
    ]

    for i, (k, v) in enumerate(entries):
        p = itf.paragraphs[0] if i == 0 else itf.add_paragraph()
        p.space_after = Pt(7)
        r1 = p.add_run()
        r1.text = f"•  {k} :  "
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = NAVY
        r2 = p.add_run()
        r2.text = v
        r2.font.size = Pt(13)
        r2.font.color.rgb = DARK_GRAY

    brand_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.9), Inches(1.75), Inches(3.6), Inches(4.8))
    brand_card.fill.solid()
    brand_card.fill.fore_color.rgb = NAVY
    brand_card.line.color.rgb = ROYAL

    btf = brand_card.text_frame
    btf.word_wrap = True
    bp = btf.paragraphs[0]
    bp.alignment = PP_ALIGN.CENTER
    bp.space_before = Pt(25)
    bp.text = "🛡️ RakshaScan AI"
    bp.font.size = Pt(23)
    bp.font.bold = True
    bp.font.color.rgb = WHITE

    bp2 = btf.add_paragraph()
    bp2.alignment = PP_ALIGN.CENTER
    bp2.space_before = Pt(10)
    bp2.text = "Dual-Environment Border Screening\n(Formal ICPs + Porous Patrols)"
    bp2.font.size = Pt(12)
    bp2.font.color.rgb = LIGHT_BLUE

    bullets = [
        "✅ Mode A: Fixed ICP PC Station",
        "✅ Mode B: Offline Mobile Patrol",
        "✅ Bilateral Treaty Policy Engine",
        "✅ Indian Voter ID & Nagarikta Rules",
        "✅ ELA & Noise Forgery Heatmaps",
        "✅ 10-Lakh Local Cache (10 GB)"
    ]
    for b in bullets:
        bp_b = btf.add_paragraph()
        bp_b.space_before = Pt(7)
        bp_b.text = b
        bp_b.font.size = Pt(11)
        bp_b.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 2: PROPOSED SOLUTION & DUAL-ENVIRONMENT ARCHITECTURE
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "PROPOSED SOLUTION: DUAL-ENVIRONMENT BORDER ARCHITECTURE", 2)

    sub_title = s2.shapes.add_textbox(Inches(0.5), Inches(0.85), Inches(12.333), Inches(0.4))
    stf = sub_title.text_frame
    sp = stf.paragraphs[0]
    sp.text = "Designed for India–Nepal (1,751 km) & India–Bhutan (699 km) Borders: Fixed ICPs + Porous Patrols"
    sp.font.bold = True
    sp.font.size = Pt(13)
    sp.font.color.rgb = ROYAL

    # Left Container: Mode A vs Mode B
    left_card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.3), Inches(6.0), Inches(4.0))
    left_card.fill.solid()
    left_card.fill.fore_color.rgb = WHITE
    left_card.line.color.rgb = BORDER_GRAY

    ltf = left_card.text_frame
    ltf.word_wrap = True
    lp1 = ltf.paragraphs[0]
    lp1.text = "🏢 Mode A: Formal ICPs & Land Check Posts"
    lp1.font.bold = True
    lp1.font.size = Pt(13)
    lp1.font.color.rgb = NAVY

    p_items = [
        "Locations: Raxaul, Jogbani, Banbasa, Jaigaon, Darranga.",
        "Setup: Fixed PC terminal, high-res optical scanner, eye-level webcam.",
        "Role: High-throughput screening (<3s), split-screen ELA heatmaps, 10-Lakh edge database search."
    ]
    for pi in p_items:
        p = ltf.add_paragraph()
        p.text = f"• {pi}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_GRAY

    lp2 = ltf.add_paragraph()
    lp2.space_before = Pt(10)
    lp2.text = "🚙 Mode B: Porous Border Patrol (Naka-Bandi & Outposts)"
    lp2.font.bold = True
    lp2.font.size = Pt(13)
    lp2.font.color.rgb = ACCENT_ORANGE

    s_items = [
        "Locations: Agricultural gates, riverine routes, train/bus inspections.",
        "Setup: SSB jawan's rugged Android phone/tablet (Offline PWA).",
        "Role: Mobile camera document scan + selfie match. Connects to patrol vehicle edge hub over local Wi-Fi when needed."
    ]
    for si in s_items:
        p = ltf.add_paragraph()
        p.text = f"• {si}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_GRAY

    # Right Container: Bilateral Treaty Policy Engine
    right_card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.3), Inches(6.0), Inches(4.0))
    right_card.fill.solid()
    right_card.fill.fore_color.rgb = LIGHT_BLUE
    right_card.line.color.rgb = ROYAL

    rtf = right_card.text_frame
    rtf.word_wrap = True
    rp1 = rtf.paragraphs[0]
    rp1.text = "📜 Configurable Bilateral Document Policy Engine"
    rp1.font.bold = True
    rp1.font.size = Pt(13)
    rp1.font.color.rgb = NAVY

    policies = [
        ("Indian Citizens (Land Crossing)", "Accepted: Indian Passport, Voter ID (EPIC), or Emergency Certificate. No mandatory passport requirement."),
        ("Nepalese Citizens (Land Crossing)", "Accepted: Nepalese Passport, Citizenship Certificate (Nagarikta), or Voter Card. Validates Devanagari script & district seal."),
        ("Bhutanese Citizens (Land Crossing)", "Accepted: Bhutanese Passport, Citizenship ID (CID 11-digit), or Voter Card. Dzongkhag code validation."),
        ("Third-Country Nationals (Foreigners)", "Strictly requires Passport + Valid Indian Visa/e-Visa. Must use designated formal ICP gates only.")
    ]
    for cat, rule in policies:
        p = rtf.add_paragraph()
        p.space_before = Pt(5)
        r = p.add_run()
        r.text = f"• {cat}: "
        r.font.bold = True
        r.font.size = Pt(10.5)
        r.font.color.rgb = ROYAL
        r2 = p.add_run()
        r2.text = rule
        r2.font.size = Pt(10)
        r2.font.color.rgb = DARK_GRAY

    # Bottom 5 Innovation Cards
    card_w = Inches(2.26)
    card_h = Inches(1.55)
    y_pos = Inches(5.45)

    innovations = [
        ("Dual-Mode Deploy", "Fixed PC counter or mobile jawan tablet; works seamlessly on both.", ROYAL),
        ("Bilateral Policy", "Treaty-aware: clears Voter IDs and Nagarikta without passport bias.", ACCENT_ORANGE),
        ("ELA Heatmaps", "Visual proof highlighting exact spliced photo & altered date pixels.", TEAL),
        ("Anti-Spoofing", "ArcFace + Fourier texture & eye-blink blocks phone screen replays.", ACCENT_GREEN),
        ("10-Lakh Local Cache", "10 GB edge storage holds 10 lakh local commuters for 15ms offline search.", NAVY)
    ]

    for idx, (title, desc, color) in enumerate(innovations):
        x_pos = Inches(0.5) + idx * Inches(2.5)
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x_pos, y_pos, card_w, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = color
        card.line.width = Pt(1.5)

        ctf = card.text_frame
        ctf.word_wrap = True
        cp = ctf.paragraphs[0]
        cp.text = title
        cp.font.bold = True
        cp.font.size = Pt(11)
        cp.font.color.rgb = color

        cp2 = ctf.add_paragraph()
        cp2.space_before = Pt(3)
        cp2.text = desc
        cp2.font.size = Pt(9.5)
        cp2.font.color.rgb = DARK_GRAY

    # =========================================================================
    # SLIDE 3: TECHNICAL APPROACH: MULTI-TRACK BRANCHING PIPELINE (MIRRORING SLIDE)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "TECHNICAL APPROACH: MULTI-TRACK BORDER SCREENING PIPELINE", 3)

    # Top Central Decision Pill: "Start Here"
    decision_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.5), Inches(0.9), Inches(8.333), Inches(0.55))
    decision_box.fill.solid()
    decision_box.fill.fore_color.rgb = NAVY
    decision_box.line.color.rgb = ACCENT_ORANGE
    decision_box.line.width = Pt(2)

    dtf = decision_box.text_frame
    dtf.word_wrap = True
    dp = dtf.paragraphs[0]
    dp.alignment = PP_ALIGN.CENTER
    dr1 = dp.add_run()
    dr1.text = "🚀 START HERE: "
    dr1.font.bold = True
    dr1.font.size = Pt(12)
    dr1.font.color.rgb = ACCENT_ORANGE
    dr2 = dp.add_run()
    dr2.text = "Traveler Arrives at Border: What is Traveler Category & Permitted Document?"
    dr2.font.bold = True
    dr2.font.size = Pt(12)
    dr2.font.color.rgb = WHITE

    # 4 Parallel Track Columns
    col_w = Inches(2.9)
    col_gap = Inches(0.2)
    col_y = Inches(1.55)
    col_h = Inches(4.05)

    tracks = [
        {
            "name": "Track 1: Indian Citizen",
            "sub": "Voter ID (EPIC) / Passport / Minor ID",
            "color": ACCENT_ORANGE,
            "bg": LIGHT_ORANGE,
            "steps": [
                "📸 Step 1: Scan Voter ID or Passport (ICP Scanner / Tablet)",
                "🔍 Module 1: Hindi/Eng OCR (PaddleOCR parses EPIC No & Name)",
                "🛡️ Module 2: Security AI (ECI Regex + Hologram + ELA Check)",
                "👤 Module 3: Face Biometrics (ArcFace 512-d + Liveness)",
                "⚖️ Module 4: Treaty Policy (Voter ID 100% Valid; 10L Cache Check)"
            ],
            "outcome_good": "🟢 Score < 25 (< 2.4s): GREEN LANE CLEAR",
            "outcome_bad": "🔴 Score > 70: Escalate to Shift Officer"
        },
        {
            "name": "Track 2: Nepalese / Bhutanese",
            "sub": "Nagarikta / Bhutanese CID / Voter Card",
            "color": ROYAL,
            "bg": LIGHT_BLUE,
            "steps": [
                "📸 Step 1: Capture Paper Nagarikta or 11-digit CID Card",
                "🔤 Module 1: Multilingual OCR (Nepali Devanagari & Dzongkha)",
                "🔬 Module 2: Texture & Seal AI (DAO Rubber Stamp + Fiber ELA)",
                "👁️ Module 3: Face Match (Aging Compensation Model)",
                "📋 Module 4: DAO Registry (District Verification against Master)"
            ],
            "outcome_good": "🟢 Score < 30 (< 2.8s): ENTRY AUTHORIZED",
            "outcome_bad": "🟡 Score 30-70: Secondary Desk (Seal Review)"
        },
        {
            "name": "Track 3: Third-Country Foreigner",
            "sub": "ICAO Passport + Valid Indian Visa / e-Visa",
            "color": ACCENT_PURPLE,
            "bg": LIGHT_PURPLE,
            "steps": [
                "📖 Step 1: Optical Bio-Page + UV/IR Light Spectrum Scan",
                "🧮 Module 1 & 2: MRZ Checksum Math (ICAO 9303 + Font Check)",
                "🛂 Module 2: Visa Validation (Matches BOI IVFRT Edge Cache)",
                "🚨 Module 3: 1:N Biometric Watchlist (FAISS wanted vector index)",
                "🛑 Module 4: Route Enforce (Mandatory Formal ICP Land Gate!)"
            ],
            "outcome_good": "🟢 Valid Visa (< 2.9s): FORMAL ICP STAMP",
            "outcome_bad": "⛔ No Land Permit: IMMEDIATE SSB CUSTODY"
        },
        {
            "name": "Track 4: Commercial Cargo Driver",
            "sub": "Bilateral Commercial DL + Customs Manifest QR",
            "color": ACCENT_GREEN,
            "bg": LIGHT_GREEN,
            "steps": [
                "📄 Step 1: Dual Scan (Commercial DL + Manifest Transit QR)",
                "⚡ Module 1: Fast QR & License OCR (Sarathi / Nepal DL Parser)",
                "📸 Module 2: Cab Height Face Match (Driver vs Fleet Manifest)",
                "📦 Module 3: ANPR Cross-Check (Truck Plate vs Land Customs Gate)",
                "⚖️ Module 4: Transit Integrity (Electronic Seal Confirmed)"
            ],
            "outcome_good": "🟢 Cleared (< 2.1s): BOOM BARRIER AUTO-LIFT",
            "outcome_bad": "🛑 Mismatch: Divert to Physical Cargo Pit"
        }
    ]

    for idx, tr in enumerate(tracks):
        x = Inches(0.5) + idx * (col_w + col_gap)
        c_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, col_y, col_w, col_h)
        c_box.fill.solid()
        c_box.fill.fore_color.rgb = WHITE
        c_box.line.color.rgb = tr["color"]
        c_box.line.width = Pt(1.5)

        ctf = c_box.text_frame
        ctf.word_wrap = True

        # Header Pill inside Column
        hp = ctf.paragraphs[0]
        hp.text = tr["name"]
        hp.font.bold = True
        hp.font.size = Pt(11.5)
        hp.font.color.rgb = tr["color"]

        h_sub = ctf.add_paragraph()
        h_sub.text = tr["sub"]
        h_sub.font.size = Pt(8.5)
        h_sub.font.color.rgb = DARK_GRAY

        # Step Nodes
        for st in tr["steps"]:
            p = ctf.add_paragraph()
            p.space_before = Pt(4)
            p.text = st
            p.font.size = Pt(8.5)
            p.font.color.rgb = DARK_GRAY

        # Outcomes at bottom
        og = ctf.add_paragraph()
        og.space_before = Pt(6)
        og.text = tr["outcome_good"]
        og.font.bold = True
        og.font.size = Pt(8.5)
        og.font.color.rgb = ACCENT_GREEN

        ob = ctf.add_paragraph()
        ob.space_before = Pt(2)
        ob.text = tr["outcome_bad"]
        ob.font.bold = True
        ob.font.size = Pt(8.5)
        ob.font.color.rgb = ACCENT_ORANGE if "Secondary" in tr["outcome_bad"] else RGBColor(190, 30, 30)

    # Bottom Left: Tech Stack Box (Mirroring Slide)
    tech_w = Inches(5.8)
    tech_h = Inches(1.35)
    tech_y = Inches(5.7)

    tech_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), tech_y, tech_w, tech_h)
    tech_box.fill.solid()
    tech_box.fill.fore_color.rgb = LIGHT_BLUE
    tech_box.line.color.rgb = ROYAL
    tech_box.line.width = Pt(1.5)

    ttf = tech_box.text_frame
    ttf.word_wrap = True
    tp1 = ttf.paragraphs[0]
    tp1.text = "🛠️ TECH STACK (100% Offline Edge Defense Suite):"
    tp1.font.bold = True
    tp1.font.size = Pt(10.5)
    tp1.font.color.rgb = NAVY

    tp2 = ttf.add_paragraph()
    tp2.space_before = Pt(3)
    tp2.text = "• Core AI: Python 3.11  |  PyTorch (Inference)  |  PaddleOCR (Devanagari & Multilingual OCR)\n• Forensics: OpenCV (ELA pixel analysis, Edge blur, Laplacian micro-cut detection)\n• Biometrics: ArcFace 512-d Vectors  |  FAISS Sub-ms Vector Search (10-Lakh Commuters)\n• Platform: FastAPI Async Engine  |  Docker Edge Container  |  Offline PWA & SQLite"
    tp2.font.size = Pt(9)
    tp2.font.color.rgb = DARK_GRAY

    # Bottom Right: 5 Expected Impacts Box (Mirroring Slide)
    imp_w = Inches(6.33)
    imp_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.5), tech_y, imp_w, tech_h)
    imp_box.fill.solid()
    imp_box.fill.fore_color.rgb = LIGHT_GREEN
    imp_box.line.color.rgb = ACCENT_GREEN
    imp_box.line.width = Pt(1.5)

    itf = imp_box.text_frame
    itf.word_wrap = True
    ip1 = itf.paragraphs[0]
    ip1.text = "🎯 5 EXPECTED IMPACTS FULFILLED (PS.MD SECTION 4):"
    ip1.font.bold = True
    ip1.font.size = Pt(10.5)
    ip1.font.color.rgb = ACCENT_GREEN

    ip2 = itf.add_paragraph()
    ip2.space_before = Pt(3)
    ip2.text = "1. Dramatic Speedup: Slashes verification from several mins to < 2.8s (Zero queue freezes)\n2. Enhanced Security: > 98.4% detection of photo-swaps, fake seals & deepfakes (ELA AI)\n3. Standardized Governance: Uniform bilateral treaty rules across all posts (Zero jawan fatigue)\n4. Explainable Decisions: Transparent 0-100 risk score breakdown + visual forensic heatmaps\n5. Digital Audit Trail: Cryptographic SHA-256 tamper-evident hash chain (BSA Court Admissible)"
    ip2.font.size = Pt(8.5)
    ip2.font.color.rgb = DARK_GRAY

    # =========================================================================
    # SLIDE 4: FEASIBILITY, VIABILITY & TELECOM REALITY
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "FEASIBILITY, VIABILITY & BORDER TELECOM REALITY", 4)

    col_w = Inches(3.95)
    col_h = Inches(2.15)

    c1 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.1), col_w, col_h)
    c1.fill.solid()
    c1.fill.fore_color.rgb = WHITE
    c1.line.color.rgb = ROYAL
    c1_tf = c1.text_frame
    c1_tf.word_wrap = True
    p = c1_tf.paragraphs[0]
    p.text = "🎯 Feasibility"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = ROYAL
    bullets_f = [
        "Proven open-source stack: PaddleOCR, OpenCV, ArcFace (>99.6% accuracy).",
        "100% offline edge execution: zero network latency or cloud server fees.",
        "Fits on standard ₹30k mini-PCs and existing Android tablets."
    ]
    for b in bullets_f:
        bp = c1_tf.add_paragraph()
        bp.text = f"• {b}"
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = DARK_GRAY

    c2 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.7), Inches(1.1), col_w, col_h)
    c2.fill.solid()
    c2.fill.fore_color.rgb = WHITE
    c2.line.color.rgb = TEAL
    c2_tf = c2.text_frame
    c2_tf.word_wrap = True
    p = c2_tf.paragraphs[0]
    p.text = "📈 Viability"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = TEAL
    bullets_v = [
        "Covers 2,450 km of Indo-Nepal and Indo-Bhutan borders across 7 states.",
        "Replaces ₹10-Lakh foreign hardware with commercial-off-the-shelf devices.",
        "Tier-1 edge clears 95% of traffic locally, saving 95% of satellite bandwidth."
    ]
    for b in bullets_v:
        bp = c2_tf.add_paragraph()
        bp.text = f"• {b}"
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = DARK_GRAY

    c3 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.9), Inches(1.1), col_w, col_h)
    c3.fill.solid()
    c3.fill.fore_color.rgb = WHITE
    c3.line.color.rgb = ACCENT_ORANGE
    c3_tf = c3.text_frame
    c3_tf.word_wrap = True
    p = c3_tf.paragraphs[0]
    p.text = "🚀 Practical Implementation"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = ACCENT_ORANGE
    bullets_p = [
        "Ready for pilot deployment at ICP Raxaul & Banbasa within 3-6 months.",
        "Configurable policy table adapts to treaty updates without code changes.",
        "Touch-first interface designed for jawans without requiring IT expertise."
    ]
    for b in bullets_p:
        bp = c3_tf.add_paragraph()
        bp.text = f"• {b}"
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = DARK_GRAY

    # Bottom: Official Telecom Evidence & Mitigations
    chal_card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(3.45), Inches(5.9), Inches(3.55))
    chal_card.fill.solid()
    chal_card.fill.fore_color.rgb = LIGHT_ORANGE
    chal_card.line.color.rgb = ACCENT_ORANGE

    ch_tf = chal_card.text_frame
    ch_tf.word_wrap = True
    p = ch_tf.paragraphs[0]
    p.text = "⚠️ Real Border Challenges (Official Government Data):"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = ACCENT_ORANGE

    challenges = [
        ("01", "75% Fiber Deficit: DoT 2025 data (Rajya Sabha Q498) shows ~75% of border panchayats in Uttarakhand lack fiber readiness."),
        ("02", "Weather Outages: DoT Year-End 2025 records landslides cutting optical fiber for up to 14 days in high-altitude zones."),
        ("03", "Low Satellite Bandwidth: POLNET/VSAT links provide only kilobits/sec, unable to stream heavy passport images."),
        ("04", "Diverse Documents: Travelers carry Voter IDs, Nagarikta, and permits rather than international ICAO passports."),
        ("05", "Presentation Spoofs: Impersonators holding smartphone screens or paper photos to bypass face matching.")
    ]
    for num, txt in challenges:
        bp = ch_tf.add_paragraph()
        bp.space_before = Pt(3)
        r1 = bp.add_run()
        r1.text = f"[{num}] "
        r1.font.bold = True
        r1.font.color.rgb = ACCENT_ORANGE
        r2 = bp.add_run()
        r2.text = txt
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = DARK_GRAY

    strat_card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(3.45), Inches(6.0), Inches(3.55))
    strat_card.fill.solid()
    strat_card.fill.fore_color.rgb = LIGHT_GREEN
    strat_card.line.color.rgb = ACCENT_GREEN

    st_tf = strat_card.text_frame
    st_tf.word_wrap = True
    p = st_tf.paragraphs[0]
    p.text = "🛡️ How RakshaScan Solves Each Challenge:"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = ACCENT_GREEN

    strategies = [
        ("01", "Offline-First Edge AI: Complete inference runs locally on the checkpoint PC/tablet with zero internet dependency."),
        ("02", "10-Lakh Local Cache: 10 GB edge storage holds 10 lakh local commuters, operating through weeks of fiber blackout."),
        ("03", "Zero-Bandwidth Screening: Primary screening uses 0 KB. Only tiny 2 KB text audit hashes sync when link restores."),
        ("04", "Bilateral Policy Engine: Automatically routes Indian Voter IDs, Nepalese Nagarikta, and foreign visas with custom rules."),
        ("05", "Active & Passive Liveness: Fourier texture analysis + eye-blink tracking defeats phone screen replays instantly.")
    ]
    for num, txt in strategies:
        bp = st_tf.add_paragraph()
        bp.space_before = Pt(3)
        r1 = bp.add_run()
        r1.text = f"[{num}] "
        r1.font.bold = True
        r1.font.color.rgb = ACCENT_GREEN
        r2 = bp.add_run()
        r2.text = txt
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = DARK_GRAY

    # =========================================================================
    # SLIDE 5: USER JOURNEY: PASSENGER EASE & SSB RELIEF ACROSS ALL 4 CASES
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "USER JOURNEY: PASSENGER EASE & SSB JAWAN RELIEF ACROSS ALL CASES", 5)

    # Top Comparison Banner: Before vs After
    top_ban = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(0.95), Inches(12.333), Inches(0.6))
    top_ban.fill.solid()
    top_ban.fill.fore_color.rgb = LIGHT_BLUE
    top_ban.line.color.rgb = ROYAL
    q_tf = top_ban.text_frame
    qp = q_tf.paragraphs[0]
    qp.alignment = PP_ALIGN.CENTER
    qp.text = "⚡ TRANSFORMATION: Manual 45-Min Queue Nightmare (14-20% Error Rate) ➔ RakshaScan < 2.8s Frictionless Flow"
    qp.font.bold = True
    qp.font.size = Pt(11.5)
    qp.font.color.rgb = NAVY

    # 4 Traveler Case Cards
    case_w = Inches(2.9)
    case_gap = Inches(0.2)
    case_y = Inches(1.65)
    case_h = Inches(5.35)

    cases = [
        {
            "num": "CASE 1",
            "title": "Indian Resident / Trader",
            "id": "Voter ID (EPIC) / Passport",
            "color": ACCENT_ORANGE,
            "bg": LIGHT_ORANGE,
            "old_flow": "• 45-min physical queue in 40°C heat.\n• Jawan squinting at faded plastic card.\n• Manual register handwriting.\n• High commuter frustration & delay.",
            "new_flow": "• Tap card + camera glance (< 1.8s).\n• PaddleOCR parses EPIC ABC1234567.\n• Hologram verified + 1:1 ArcFace match.\n• Local 10L cache confirms bona fide.\n• Green barrier auto-opens in < 2.4s.",
            "impact": "Ease: Zero interrogation, saves 2 hrs daily."
        },
        {
            "num": "CASE 2",
            "title": "Nepalese / Bhutanese",
            "id": "Nagarikta / 11-digit CID",
            "color": ROYAL,
            "bg": LIGHT_BLUE,
            "old_flow": "• Faded Nepali Devanagari handwriting.\n• Non-native jawans struggle to read seals.\n• 15-minute argument & queue stall.\n• Fake photocopy certificates pass through.",
            "new_flow": "• Devanagari OCR parses DAO Morang.\n• Laplacian AI verifies genuine fiber paper.\n• ArcFace aging model matches vintage photo.\n• Bilateral treaty rule: 100% valid.\n• Dignified clearance in 2.6 seconds.",
            "impact": "Ease: Respectful, zero linguistic barrier."
        },
        {
            "num": "CASE 3",
            "title": "Third-Country Infiltrator",
            "id": "Forged PVC Indian Voter ID",
            "color": ACCENT_PURPLE,
            "bg": LIGHT_PURPLE,
            "old_flow": "• Fraudster buys fake PVC card at border.\n• Tired jawan (400th check) misses razor cut.\n• Impersonator slips into Indian interior.\n• Critical national security breach.",
            "new_flow": "• ELA Forensics catches photo border splice.\n• Missing Election Commission watermark.\n• FAISS vector search hits SSB Watchlist.\n• Risk Score: 88/100 (CRITICAL THREAT).\n• Main queue moves; suspect quietly detained.",
            "impact": "Security: Infiltration blocked with SHA-256 proof."
        },
        {
            "num": "CASE 4",
            "title": "Commercial Cargo Driver",
            "id": "Commercial DL + Manifest QR",
            "color": ACCENT_GREEN,
            "bg": LIGHT_GREEN,
            "old_flow": "• 6 to 18-hour border truck gridlock.\n• Jawan climbs into truck cab in dust/heat.\n• Manual paper manifest and seal inspection.\n• Severe bilateral trade disruption.",
            "new_flow": "• Driver scans DL & Customs QR from cab.\n• ANPR matches truck plate with manifest.\n• Cab camera verifies driver biometrics.\n• Customs electronic seal validated.\n• Boom barrier auto-lifts in < 2.1s.",
            "impact": "Speedup: Slashes truck clearance from 20m to 2.1s."
        }
    ]

    for idx, cs in enumerate(cases):
        cx = Inches(0.5) + idx * (case_w + case_gap)
        c_card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, case_y, case_w, case_h)
        c_card.fill.solid()
        c_card.fill.fore_color.rgb = WHITE
        c_card.line.color.rgb = cs["color"]
        c_card.line.width = Pt(1.5)

        ctf = c_card.text_frame
        ctf.word_wrap = True

        cp1 = ctf.paragraphs[0]
        cp1.text = f"{cs['num']}: {cs['title']}"
        cp1.font.bold = True
        cp1.font.size = Pt(11)
        cp1.font.color.rgb = cs["color"]

        cid = ctf.add_paragraph()
        cid.text = f"ID: {cs['id']}"
        cid.font.bold = True
        cid.font.size = Pt(8.5)
        cid.font.color.rgb = NAVY

        # Old Flow
        cold = ctf.add_paragraph()
        cold.space_before = Pt(4)
        cold.text = "❌ OLD MANUAL NIGHTMARE:"
        cold.font.bold = True
        cold.font.size = Pt(8.5)
        cold.font.color.rgb = RGBColor(190, 30, 30)

        cold_txt = ctf.add_paragraph()
        cold_txt.text = cs["old_flow"]
        cold_txt.font.size = Pt(8)
        cold_txt.font.color.rgb = DARK_GRAY

        # New Flow
        cnew = ctf.add_paragraph()
        cnew.space_before = Pt(4)
        cnew.text = "✅ RAKSHASCAN AI STREAMLINE:"
        cnew.font.bold = True
        cnew.font.size = Pt(8.5)
        cnew.font.color.rgb = ACCENT_GREEN

        cnew_txt = ctf.add_paragraph()
        cnew_txt.text = cs["new_flow"]
        cnew_txt.font.size = Pt(8)
        cnew_txt.font.color.rgb = DARK_GRAY

        # Outcome Ease
        cimp = ctf.add_paragraph()
        cimp.space_before = Pt(4)
        cimp.text = f"🎯 {cs['impact']}"
        cimp.font.bold = True
        cimp.font.size = Pt(8.5)
        cimp.font.color.rgb = cs["color"]

    # =========================================================================
    # SLIDE 6: RESEARCH, REFERENCES & COMPETITIVE ADVANTAGE
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "RESEARCH, REFERENCES & COMPETITIVE ADVANTAGE", 6)

    top_res = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.05), Inches(12.333), Inches(2.3))
    top_res.fill.solid()
    top_res.fill.fore_color.rgb = WHITE
    top_res.line.color.rgb = BORDER_GRAY

    tr_tf = top_res.text_frame
    tr_tf.word_wrap = True
    p = tr_tf.paragraphs[0]
    p.text = "📚 Government Standards & Official Citations:"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = NAVY

    refs = [
        "DoT Year-End Review 2025 (PIB Delhi) & Rajya Sabha Q498 / Q1297: Confirms border telecom shadow zones and 75% rural fiber deficit in border states.",
        "MHA Annual Report: Details SSB deployment at high-altitude BOPs and mandates for satellite-backed communication and offline-ready border edge systems.",
        "ICAO Doc 9303: Machine Readable Travel Documents specification & 7-3-1 modulo-10 check digit algorithms for biometric passports and ID cards.",
        "ScienceDirect (2019): 'The challenge of detecting false documents at the border' (Confirms 14-20% human officer error rate under fatigue).",
        "NIST AI 100-1 RMF & DPDP Act 2023: Guidelines for trustworthy, transparent, and privacy-preserving biometric edge processing."
    ]
    for r in refs:
        bp = tr_tf.add_paragraph()
        bp.space_before = Pt(2)
        bp.text = f"• {r}"
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = DARK_GRAY

    ex_card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(3.55), Inches(5.9), Inches(2.2))
    ex_card.fill.solid()
    ex_card.fill.fore_color.rgb = LIGHT_ORANGE
    ex_card.line.color.rgb = ACCENT_ORANGE

    etf = ex_card.text_frame
    etf.word_wrap = True
    p = etf.paragraphs[0]
    p.text = "❌ EXISTING SOLUTIONS"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = ACCENT_ORANGE

    e_pts = [
        "Rigid 'passport-only' design; useless at open land borders where citizens use Voter IDs/Nagarikta.",
        "Require expensive proprietary optical hardware scanners (₹8-15 Lakh per booth).",
        "Cloud-dependent: fails completely during frequent border optical fiber cuts.",
        "Black-box AI classifiers provide only 'fake/genuine' with zero visual proof."
    ]
    for pt in e_pts:
        bp = etf.add_paragraph()
        bp.text = f"• {pt}"
        bp.font.size = Pt(9)
        bp.font.color.rgb = DARK_GRAY

    our_card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(3.55), Inches(6.0), Inches(2.2))
    our_card.fill.solid()
    our_card.fill.fore_color.rgb = LIGHT_GREEN
    our_card.line.color.rgb = ACCENT_GREEN

    otf = our_card.text_frame
    otf.word_wrap = True
    p = otf.paragraphs[0]
    p.text = "✅ OUR SOLUTION STANDS OUT"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = ACCENT_GREEN

    o_pts = [
        "Dual-Environment: Works at fixed ICP counters (PC) and porous border naka patrols (Mobile).",
        "Treaty-Aware: Configurable policy table validates Indian Voter IDs, Nepalese Nagarikta & Visas.",
        "100% Offline Edge: 10-Lakh local cache (10 GB) operates without internet in under 3 seconds.",
        "Visual ELA & Noise Heatmaps give officers indisputable courtroom evidence."
    ]
    for pt in o_pts:
        bp = otf.add_paragraph()
        bp.text = f"• {pt}"
        bp.font.size = Pt(9)
        bp.font.color.rgb = DARK_GRAY

    res_box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(5.9), Inches(12.333), Inches(1.15))
    res_box.fill.solid()
    res_box.fill.fore_color.rgb = LIGHT_BLUE
    res_box.line.color.rgb = ROYAL

    rtf = res_box.text_frame
    rtf.word_wrap = True
    p = rtf.paragraphs[0]
    p.text = "🔗 PROJECT RESOURCES & REPOSITORY"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = NAVY

    p2 = rtf.add_paragraph()
    p2.space_before = Pt(3)
    p2.text = "• Live Prototype / Repo: https://github.com/YourTeam/RakshaScan-AI  |  • Architecture Doc: PROJECT_BLUEPRINT.md  |  • Research Dossier: research_dossier.html"
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = DARK_GRAY

    output_path = r"c:\Users\aryan\OneDrive\Desktop\fake_Identity_ai\RakshaScan_AI_SIH2025_Presentation.pptx"
    prs.save(output_path)
    print(f"Presentation successfully updated and saved to: {output_path}")

if __name__ == "__main__":
    create_deck()
