# -*- coding: utf-8 -*-
import sys
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

with open('research_dossier.html', 'r', encoding='utf-8') as f:
    text = f.read()

checks = [
    ("Tab 1: Research", 'id="tab-research"'),
    ("Tab 2: Journey", 'id="tab-journey"'),
    ("Tab 3: Architecture", 'id="tab-architecture"'),
    ("Tab 4: Mockup", 'id="tab-mockup"'),
    ("Multi-Track Flowchart", 'TECHNICAL APPROACH: MULTI-TRACK SCREENING ENGINE'),
    ("Decision Box: Start Here", 'START HERE'),
    ("Traveler Category Question", 'Traveler Arrives at Border: What is Traveler Category'),
    ("Track 1: Indian Citizen", 'Indian Citizen'),
    ("Track 2: Nepalese & Bhutanese", 'Nepalese & Bhutanese'),
    ("Track 3: Third-Country Foreigner", 'Third-Country Foreigner'),
    ("Track 4: Cargo & Transit Driver", 'Cargo & Transit Driver'),
    ("Tech Stack Box", 'TECH STACK'),
    ("5 Expected Impacts Section", '5 Expected Impacts Fulfilled'),
    ("Before vs After Comparison", 'THE OLD MANUAL QUEUE NIGHTMARE (BEFORE)'),
    ("Case 1: Indian Citizen", 'CASE 1: Indian Citizen'),
    ("Case 2: Nepalese/Bhutanese", 'CASE 2: Nepalese / Bhutanese'),
    ("Case 3: Third-Country", 'CASE 3: Third-Country National'),
    ("Case 4: Commercial Cargo", 'CASE 4: Commercial Cargo Driver'),
    ("5 Impacts Matrix", 'How RakshaScan AI Fulfills All 5 Expected Impacts'),
]

all_pass = True
for name, query in checks:
    found = query in text
    if not found:
        all_pass = False
    print(f"[{'PASS' if found else 'FAIL'}] {name}")

print("\nOverall Status:", "ALL TESTS PASSED!" if all_pass else "SOME CHECKS FAILED")
