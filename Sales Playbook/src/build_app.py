# -*- coding: utf-8 -*-
"""
Compiler script that combines Playbooks 0 through 10 into a single,
self-contained, hyper-interactive HTML application at:
/Users/mabaistrategies/Desktop/Sales Playbook/index.html
"""

import json
import os
from pb0_data import PLAYBOOK_0
from pb1_data import PLAYBOOK_1
from pb2_data import PLAYBOOK_2
from pb3_data import PLAYBOOK_3
from pb4_to_10_data import BONUS_PLAYBOOKS

ALL_PLAYBOOKS = [PLAYBOOK_0, PLAYBOOK_1, PLAYBOOK_2, PLAYBOOK_3] + BONUS_PLAYBOOKS

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en" class="dark scroll-smooth">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>MAB AI Strategies — The Agentic Enterprise Sales Academy & Playbook</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        charcoal: '#09090b',
                        tungsten: '#18181b',
                        electric: '#3b82f6',
                        electricDark: '#1d4ed8',
                        gold: '#eab308',
                        offwhite: '#f4f4f5'
                    },
                    fontFamily: {
                        serif: ['"Playfair Display"', 'serif'],
                        sans: ['Inter', 'sans-serif'],
                        mono: ['"JetBrains Mono"', 'monospace']
                    }
                }
            }
        }
    </script>
    <style>
        * { box-sizing: border-box; }
        body {
            background-color: #09090b;
            color: #e4e4e7;
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
        }
        ::-webkit-scrollbar { width: 7px; height: 7px; }
        ::-webkit-scrollbar-track { background: #09090b; }
        ::-webkit-scrollbar-thumb { background: #27272a; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #3b82f6; }

        /* Ambient architectural grid & circuit background */
        .global-bg {
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 0;
            background-size: 44px 44px;
            background-image:
                linear-gradient(to right, rgba(255,255,255,0.022) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(255,255,255,0.022) 1px, transparent 1px);
        }
        .ambient-glow {
            position: fixed;
            width: 650px;
            height: 650px;
            border-radius: 9999px;
            background: radial-gradient(circle, rgba(59,130,246,0.08) 0%, rgba(234,179,8,0.03) 45%, transparent 70%);
            top: -200px;
            right: -150px;
            pointer-events: none;
            z-index: 0;
        }

        /* Prose & Content Styling */
        .prose-section h3 {
            font-family: 'Playfair Display', serif;
            font-size: 1.55rem;
            color: #ffffff;
            margin-top: 1.75rem;
            margin-bottom: 0.75rem;
            font-weight: 600;
            letter-spacing: -0.01em;
        }
        .prose-section p {
            color: #d4d4d8;
            line-height: 1.75;
            margin-bottom: 1.1rem;
            font-size: 0.98rem;
        }
        .prose-section ul, .prose-section ol {
            margin-bottom: 1.25rem;
            padding-left: 1.35rem;
            color: #d4d4d8;
        }
        .prose-section ul { list-style-type: disc; }
        .prose-section ol { list-style-type: decimal; }
        .prose-section li {
            margin-bottom: 0.6rem;
            line-height: 1.68;
            font-size: 0.96rem;
        }
        .prose-section blockquote {
            border-left: 3px solid #3b82f6;
            background: rgba(59, 130, 246, 0.06);
            padding: 1.1rem 1.35rem;
            border-radius: 0 0.75rem 0.75rem 0;
            font-style: italic;
            color: #f4f4f5;
            margin: 1.25rem 0;
            line-height: 1.7;
        }

        /* Founder Note */
        .founder-note {
            background: linear-gradient(135deg, rgba(24,24,27,0.95) 0%, rgba(9,9,11,0.98) 100%);
            border: 1px solid rgba(59,130,246,0.35);
            border-left: 4px solid #3b82f6;
            border-radius: 0.85rem;
            padding: 1.35rem 1.5rem;
            margin: 1.25rem 0 1.75rem 0;
            box-shadow: 0 12px 32px -8px rgba(0,0,0,0.6);
        }
        .founder-badge {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            color: #3b82f6;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
        .founder-note p {
            margin-bottom: 0 !important;
            color: #f4f4f5 !important;
            font-size: 0.96rem !important;
        }

        /* Motto Banner */
        .motto-banner {
            background: linear-gradient(90deg, rgba(59,130,246,0.12), rgba(234,179,8,0.12), rgba(16,185,129,0.1));
            border: 1px solid rgba(234,179,8,0.35);
            border-radius: 1rem;
            padding: 1.5rem;
            text-align: center;
            margin: 1.25rem 0 1.75rem 0;
        }
        .motto-eyebrow {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.7rem;
            letter-spacing: 0.15em;
            color: #eab308;
            text-transform: uppercase;
            margin-bottom: 0.4rem;
        }
        .motto-text {
            font-family: 'Playfair Display', serif;
            font-size: 1.65rem;
            color: #ffffff;
            font-weight: 700;
        }

        /* Stat Grid */
        .stat-grid-4 {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
            gap: 1rem;
            margin: 1.5rem 0;
        }
        .stat-card {
            background: rgba(24, 24, 27, 0.85);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 0.85rem;
            padding: 1.15rem;
            text-align: center;
            transition: all 0.25s ease;
        }
        .stat-card:hover {
            border-color: rgba(59,130,246,0.5);
            transform: translateY(-2px);
        }
        .stat-num {
            display: block;
            font-family: 'Playfair Display', serif;
            font-size: 1.9rem;
            font-weight: 700;
            color: #3b82f6;
            line-height: 1.15;
        }
        .stat-label {
            display: block;
            font-size: 0.76rem;
            color: #a1a1aa;
            margin-top: 0.35rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        /* Visual Showcase Plates (Playbook 0 Images) */
        .visual-showcase {
            background: #121215;
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 1rem;
            overflow: hidden;
            margin: 1.75rem 0;
            box-shadow: 0 20px 45px -15px rgba(0,0,0,0.7);
        }
        .visual-header {
            padding: 0.75rem 1.25rem;
            background: rgba(255,255,255,0.03);
            border-bottom: 1px solid rgba(255,255,255,0.07);
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            gap: 0.5rem;
        }
        .visual-tag {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.7rem;
            color: #3b82f6;
            font-weight: 600;
            letter-spacing: 0.08em;
        }
        .visual-caption {
            font-size: 0.78rem;
            color: #a1a1aa;
        }
        .visual-frame {
            width: 100%;
            max-height: 410px;
            overflow: hidden;
            position: relative;
            background: #09090b;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .playbook-img {
            width: 100%;
            height: 390px;
            object-fit: cover;
            display: block;
            transition: transform 0.6s ease;
        }
        .visual-showcase:hover .playbook-img {
            transform: scale(1.02);
        }

        /* Comparison Cards */
        .comparison-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
            gap: 1.15rem;
            margin: 1.4rem 0;
        }
        .comp-card {
            border-radius: 0.85rem;
            padding: 1.25rem;
            border: 1px solid rgba(255,255,255,0.08);
        }
        .comp-bad {
            background: rgba(244, 63, 94, 0.06);
            border-color: rgba(244, 63, 94, 0.3);
        }
        .comp-bad h4 { color: #fb7185; font-weight: 700; margin-bottom: 0.5rem; font-size: 1rem; }
        .comp-good {
            background: rgba(16, 185, 129, 0.06);
            border-color: rgba(16, 185, 129, 0.35);
        }
        .comp-good h4 { color: #34d399; font-weight: 700; margin-bottom: 0.5rem; font-size: 1rem; }

        /* Spec & Module Cards */
        .module-cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(275px, 1fr));
            gap: 1.1rem;
            margin: 1.5rem 0;
        }
        .spec-card {
            background: rgba(24, 24, 27, 0.8);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 0.85rem;
            padding: 1.25rem;
            transition: all 0.25s ease;
        }
        .spec-card:hover {
            border-color: rgba(59, 130, 246, 0.45);
            background: rgba(24, 24, 27, 0.95);
        }
        .spec-num {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.68rem;
            color: #3b82f6;
            letter-spacing: 0.1em;
            margin-bottom: 0.3rem;
            font-weight: 600;
        }
        .spec-card h4 {
            font-family: 'Playfair Display', serif;
            font-size: 1.2rem;
            color: #ffffff;
            margin-bottom: 0.45rem;
            font-weight: 600;
        }
        .spec-tech {
            margin-top: 0.75rem;
            padding-top: 0.75rem;
            border-top: 1px solid rgba(255,255,255,0.06);
            display: flex;
            flex-direction: column;
            gap: 0.28rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.73rem;
            color: #a1a1aa;
        }

        /* Library 4-Pillar Grid */
        .library-grid-4 {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 1.1rem;
            margin: 1.5rem 0;
        }
        .lib-pillar {
            background: rgba(24,24,27,0.85);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 0.85rem;
            padding: 1.2rem;
        }
        .lib-header {
            font-weight: 700;
            font-size: 1.05rem;
            margin-bottom: 0.35rem;
        }
        .lib-sub {
            font-size: 0.8rem !important;
            color: #a1a1aa !important;
            margin-bottom: 0.75rem !important;
        }
        .lib-list {
            padding-left: 1rem !important;
            font-size: 0.83rem !important;
        }
        .lib-list li {
            margin-bottom: 0.4rem !important;
            font-size: 0.83rem !important;
        }

        /* Tier Cards */
        .tier-grid-3 {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(255px, 1fr));
            gap: 1.15rem;
            margin: 1.5rem 0;
        }
        .tier-card {
            background: rgba(24,24,27,0.8);
            border: 1px solid rgba(255,255,255,0.09);
            border-radius: 0.95rem;
            padding: 1.35rem;
            display: flex;
            flex-direction: column;
        }
        .tier-featured {
            border-color: #3b82f6;
            background: linear-gradient(180deg, rgba(59,130,246,0.1) 0%, rgba(24,24,27,0.92) 100%);
            box-shadow: 0 0 30px rgba(59,130,246,0.15);
        }
        .tier-badge {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.68rem;
            color: #eab308;
            letter-spacing: 0.08em;
            margin-bottom: 0.4rem;
            font-weight: 600;
        }
        .tier-card h4 {
            font-family: 'Playfair Display', serif;
            font-size: 1.4rem;
            color: #ffffff;
            margin-bottom: 0.5rem;
            font-weight: 700;
        }
        .tier-desc { font-size: 0.88rem !important; color: #cbd5e1 !important; }
        .tier-specs {
            background: rgba(0,0,0,0.35);
            border-radius: 0.5rem;
            padding: 0.75rem;
            font-size: 0.82rem;
            margin: 0.75rem 0;
            display: flex;
            flex-direction: column;
            gap: 0.3rem;
        }
        .tier-when {
            margin-top: auto;
            padding-top: 0.75rem;
            border-top: 1px solid rgba(255,255,255,0.07);
            font-size: 0.82rem;
            color: #a1a1aa;
        }
        .tier-list {
            list-style: none !important;
            padding-left: 0 !important;
            margin-top: 0.75rem;
            font-size: 0.85rem;
        }
        .tier-list li {
            margin-bottom: 0.45rem !important;
            font-size: 0.85rem !important;
        }
        .tier-muted { color: #52525b !important; }

        /* Interactive Infographics & Simulators */
        .infographic-box {
            background: linear-gradient(180deg, #141418 0%, #0d0d10 100%);
            border: 1px solid rgba(59,130,246,0.35);
            border-radius: 1rem;
            padding: 1.4rem;
            margin: 1.75rem 0;
            box-shadow: 0 15px 40px -10px rgba(0,0,0,0.65);
        }
        .infographic-header {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            gap: 0.75rem;
            padding-bottom: 1rem;
            margin-bottom: 1.2rem;
            border-bottom: 1px solid rgba(255,255,255,0.08);
        }
        .infographic-header h4 {
            font-family: 'Playfair Display', serif;
            font-size: 1.25rem;
            color: #ffffff;
            margin-top: 0.25rem;
        }
        .badge-electric, .badge-gold, .badge-emerald {
            display: inline-block;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.68rem;
            font-weight: 600;
            padding: 0.2rem 0.55rem;
            border-radius: 999px;
            letter-spacing: 0.08em;
        }
        .badge-electric { background: rgba(59,130,246,0.18); color: #60a5fa; border: 1px solid rgba(59,130,246,0.4); }
        .badge-gold { background: rgba(234,179,8,0.18); color: #facc15; border: 1px solid rgba(234,179,8,0.4); }
        .badge-emerald { background: rgba(16,185,129,0.18); color: #34d399; border: 1px solid rgba(16,185,129,0.4); }

        /* Impressions Pipeline Nodes */
        .impressions-pipeline {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            justify-content: space-between;
            gap: 0.5rem;
            margin-bottom: 1.25rem;
        }
        .imp-node {
            flex: 1;
            min-width: 150px;
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 0.75rem;
            padding: 0.9rem;
            text-align: left;
            transition: all 0.2s ease;
        }
        .imp-node:hover, .imp-node.active {
            background: rgba(59,130,246,0.15);
            border-color: #3b82f6;
            box-shadow: 0 0 20px rgba(59,130,246,0.2);
        }
        .imp-step { font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; color: #3b82f6; }
        .imp-title { font-weight: 700; color: #ffffff; font-size: 0.95rem; margin: 0.2rem 0; }
        .imp-metric { font-size: 0.75rem; color: #eab308; font-family: 'JetBrains Mono', monospace; }
        .imp-arrow { color: #52525b; font-weight: bold; font-size: 1.2rem; }
        .imp-detail-panel {
            background: rgba(0,0,0,0.45);
            border: 1px solid rgba(255,255,255,0.07);
            border-radius: 0.85rem;
            padding: 1.25rem;
        }
        .imp-detail-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 1.25rem;
        }
        .imp-detail-badge { font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: #10b981; }
        .imp-detail-panel h4 { font-size: 1.2rem; color: #fff; font-weight: 700; margin: 0.3rem 0 0.5rem 0; }
        .imp-deliverables {
            display: flex;
            flex-direction: column;
            gap: 0.3rem;
            font-size: 0.84rem;
            color: #cbd5e1;
            margin-top: 0.6rem;
        }
        .imp-talk-box {
            background: rgba(59,130,246,0.07);
            border: 1px solid rgba(59,130,246,0.25);
            border-radius: 0.75rem;
            padding: 1rem;
        }
        .imp-talk-label { font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #60a5fa; font-weight: 600; margin-bottom: 0.4rem; }
        .imp-kpi-bar {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 0.5rem;
            font-size: 0.78rem;
            color: #a1a1aa;
            margin-top: 0.75rem;
            padding-top: 0.6rem;
            border-top: 1px solid rgba(255,255,255,0.08);
        }

        /* Scenario Buttons & Outputs */
        .scenario-btn-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 1.15rem;
        }
        .scen-btn {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.1);
            color: #d4d4d8;
            padding: 0.55rem 0.9rem;
            border-radius: 0.55rem;
            font-size: 0.8rem;
            font-weight: 500;
            transition: all 0.2s;
        }
        .scen-btn:hover, .scen-btn.active {
            background: #3b82f6;
            color: #ffffff;
            border-color: #3b82f6;
        }
        .scen-output {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 1rem;
            background: rgba(0,0,0,0.45);
            border: 1px solid rgba(255,255,255,0.07);
            border-radius: 0.8rem;
            padding: 1.15rem;
        }
        .scen-label {
            display: block;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.68rem;
            color: #a1a1aa;
            margin-bottom: 0.3rem;
        }
        .scen-col h4 { font-size: 1.05rem; font-weight: 700; margin-bottom: 0.4rem; }
        .scen-tags { display: flex; flex-direction: column; gap: 0.35rem; margin-top: 0.4rem; }
        .scen-tags span {
            background: rgba(255,255,255,0.06);
            padding: 0.35rem 0.65rem;
            border-radius: 0.4rem;
            font-size: 0.8rem;
            color: #e4e4e7;
        }

        /* Case Study Card */
        .case-study-card {
            background: linear-gradient(135deg, rgba(16,185,129,0.08) 0%, rgba(24,24,27,0.95) 100%);
            border: 1px solid rgba(16,185,129,0.35);
            border-radius: 1rem;
            padding: 1.4rem;
            margin: 1.5rem 0;
        }
        .cs-header h4 {
            font-family: 'Playfair Display', serif;
            font-size: 1.35rem;
            color: #ffffff;
            margin-top: 0.35rem;
        }
        .cs-body {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 1.1rem;
            margin-top: 1rem;
        }
        .cs-col h5 { color: #34d399; font-weight: 700; font-size: 0.92rem; margin-bottom: 0.35rem; }

        /* Tables */
        .table-wrapper { overflow-x: auto; margin: 1.4rem 0; border-radius: 0.85rem; border: 1px solid rgba(255,255,255,0.09); }
        .playbook-table { width: 100%; border-collapse: collapse; font-size: 0.86rem; text-align: left; }
        .playbook-table th {
            background: rgba(255,255,255,0.05);
            color: #ffffff;
            padding: 0.85rem 1rem;
            font-weight: 600;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        .playbook-table td {
            padding: 0.85rem 1rem;
            border-bottom: 1px solid rgba(255,255,255,0.06);
            color: #d4d4d8;
            vertical-align: top;
        }
        .playbook-table .highlight-col {
            background: rgba(59,130,246,0.08);
            color: #f4f4f5;
        }

        /* Callouts */
        .callout-tip, .callout-warning {
            padding: 1.1rem 1.3rem;
            border-radius: 0.8rem;
            margin: 1.35rem 0;
            font-size: 0.92rem;
            line-height: 1.65;
        }
        .callout-tip { background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.3); color: #d1fae5; }
        .callout-warning { background: rgba(234,179,8,0.08); border: 1px solid rgba(234,179,8,0.35); color: #fef08a; }

        /* Flashcards */
        .flashcard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
            margin: 1.4rem 0;
        }
        .flashcard {
            background: rgba(24,24,27,0.9);
            border: 1px solid rgba(59,130,246,0.3);
            border-radius: 0.9rem;
            padding: 1.25rem;
            cursor: pointer;
            min-height: 185px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            transition: all 0.25s;
        }
        .flashcard:hover { border-color: #3b82f6; transform: translateY(-2px); }
        .flashcard .fc-back { display: none; }
        .flashcard.flipped { background: rgba(59,130,246,0.12); border-color: #10b981; }
        .flashcard.flipped .fc-front { display: none; }
        .flashcard.flipped .fc-back { display: block; }
        .fc-tag { font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; color: #3b82f6; }
        .fc-front h4 { color: #fff; font-weight: 600; font-size: 1rem; margin: 0.45rem 0; }
        .fc-hint { font-size: 0.75rem; color: #a1a1aa; }

        /* Calculator */
        .calc-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 1.5rem;
            align-items: center;
        }
        .calc-row { margin-bottom: 1rem; }
        .calc-row label { display: block; font-size: 0.86rem; color: #e4e4e7; margin-bottom: 0.35rem; }
        .calc-row input[type=range] { width: 100%; accent-color: #3b82f6; cursor: pointer; }
        .calc-results {
            background: rgba(0,0,0,0.5);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 0.85rem;
            padding: 1.2rem;
        }
        .calc-stat-row {
            display: flex;
            justify-content: space-between;
            padding: 0.45rem 0;
            border-bottom: 1px solid rgba(255,255,255,0.06);
            font-size: 0.9rem;
        }
        .calc-pitch-script {
            margin-top: 0.85rem;
            padding: 0.75rem;
            background: rgba(59,130,246,0.1);
            border-left: 3px solid #3b82f6;
            font-size: 0.83rem;
            font-style: italic;
            color: #f4f4f5;
        }

        /* Email & Script Previews */
        .email-preview-card {
            background: rgba(0,0,0,0.55);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 0.85rem;
            padding: 1.2rem;
        }
        .email-meta {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            gap: 0.5rem;
            padding-bottom: 0.75rem;
            margin-bottom: 0.75rem;
            border-bottom: 1px solid rgba(255,255,255,0.08);
            font-size: 0.84rem;
        }
        .email-body-pre {
            white-space: pre-wrap;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.82rem;
            line-height: 1.65;
            color: #f4f4f5;
            background: rgba(24,24,27,0.9);
            padding: 1.1rem;
            border-radius: 0.65rem;
            border: 1px solid rgba(255,255,255,0.07);
            overflow-x: auto;
        }
        .email-why {
            margin-top: 0.8rem;
            font-size: 0.82rem;
            color: #a1a1aa;
        }
        .script-block {
            background: rgba(24,24,27,0.85);
            border: 1px solid rgba(255,255,255,0.09);
            border-radius: 0.9rem;
            padding: 1.35rem;
            margin: 1.25rem 0;
        }
        .script-stage {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            color: #eab308;
            font-weight: 600;
            letter-spacing: 0.08em;
            margin-top: 1rem;
            margin-bottom: 0.35rem;
        }
        .script-stage:first-child { margin-top: 0; }
        .script-note { font-size: 0.82rem !important; color: #9ca3af !important; font-style: italic; }

        /* Timeline Walkthrough */
        .timeline-walkthrough {
            display: flex;
            flex-direction: column;
            gap: 0.9rem;
            margin: 1.25rem 0;
        }
        .tw-step {
            background: rgba(24,24,27,0.8);
            border-left: 3px solid #3b82f6;
            padding: 1rem 1.25rem;
            border-radius: 0 0.75rem 0.75rem 0;
        }
        .tw-badge {
            display: inline-block;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.7rem;
            color: #60a5fa;
            font-weight: 600;
            margin-bottom: 0.3rem;
        }

        /* Call Sim */
        .call-prospect-bubble {
            background: rgba(244,63,94,0.09);
            border: 1px solid rgba(244,63,94,0.35);
            padding: 1rem 1.2rem;
            border-radius: 0.8rem;
            margin-bottom: 1rem;
        }
        .call-speaker { font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #fb7185; font-weight: 600; }
        .call-options { display: flex; flex-direction: column; gap: 0.6rem; }
        .call-opt-btn {
            text-align: left;
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.1);
            padding: 0.85rem 1rem;
            border-radius: 0.65rem;
            font-size: 0.86rem;
            color: #e4e4e7;
            transition: all 0.2s;
        }
        .call-opt-btn:hover { border-color: #3b82f6; background: rgba(59,130,246,0.1); }
        .call-feedback {
            margin-top: 1rem;
            padding: 1rem;
            border-radius: 0.7rem;
            font-size: 0.88rem;
        }

        /* CRM Sim & Checklists */
        .crm-scenario-banner {
            background: rgba(59,130,246,0.08);
            border: 1px solid rgba(59,130,246,0.3);
            padding: 1rem;
            border-radius: 0.75rem;
            font-size: 0.86rem;
            line-height: 1.6;
            margin-bottom: 1.15rem;
        }
        .crm-form-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 1rem;
        }
        .crm-field label { display: block; font-size: 0.78rem; font-family: 'JetBrains Mono', monospace; color: #a1a1aa; margin-bottom: 0.35rem; }
        .form-input {
            width: 100%;
            background: #18181b;
            border: 1px solid rgba(255,255,255,0.15);
            color: #fff;
            padding: 0.65rem 0.8rem;
            border-radius: 0.5rem;
            font-size: 0.85rem;
        }
        .checklist-box {
            display: flex;
            flex-direction: column;
            gap: 0.65rem;
            background: rgba(24,24,27,0.85);
            border: 1px solid rgba(255,255,255,0.09);
            padding: 1.25rem;
            border-radius: 0.85rem;
        }
        .check-item {
            display: flex;
            align-items: flex-start;
            gap: 0.65rem;
            font-size: 0.9rem;
            cursor: pointer;
        }
        .check-item input { margin-top: 0.3rem; accent-color: #10b981; transform: scale(1.15); }

        /* Exam CTA */
        .exam-launch-cta {
            margin-top: 2rem;
            background: linear-gradient(135deg, rgba(59,130,246,0.18) 0%, rgba(234,179,8,0.12) 100%);
            border: 1px solid rgba(59,130,246,0.5);
            border-radius: 1rem;
            padding: 1.5rem;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
        }
        .exam-launch-cta h4 {
            font-family: 'Playfair Display', serif;
            font-size: 1.35rem;
            color: #ffffff;
            margin-bottom: 0.25rem;
        }
        .exam-launch-cta p { margin-bottom: 0 !important; font-size: 0.9rem !important; }
        .btn-primary-glow {
            background: #3b82f6;
            color: #ffffff;
            font-weight: 600;
            padding: 0.8rem 1.4rem;
            border-radius: 0.65rem;
            font-size: 0.9rem;
            box-shadow: 0 0 25px rgba(59,130,246,0.4);
            transition: all 0.2s;
            white-space: nowrap;
        }
        .btn-primary-glow:hover { background: #2563eb; transform: translateY(-1px); }
    </style>
</head>
<body class="min-h-screen flex flex-col selection:bg-electric selection:text-white">

<div class="global-bg"></div>
<div class="ambient-glow"></div>

<!-- TOP NAVIGATION BAR -->
<header class="sticky top-0 z-40 backdrop-blur-xl bg-charcoal/90 border-b border-white/10">
    <div class="max-w-[1600px] mx-auto px-4 md:px-6 h-16 flex items-center justify-between gap-3">
        <div class="flex items-center gap-3">
            <button onclick="toggleSidebarMobile()" class="lg:hidden p-2 rounded-lg bg-white/5 text-zinc-300 hover:text-white">
                ☰
            </button>
            <div class="flex items-center gap-2.5 cursor-pointer" onclick="selectPlaybook(0, 0)">
                <div class="w-9 h-9 rounded-lg bg-electric/20 border border-electric flex items-center justify-center font-serif font-bold text-white text-lg shadow-[0_0_15px_rgba(59,130,246,0.3)]">
                    M·AI
                </div>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="font-serif font-bold text-white tracking-tight text-base md:text-lg">MAB AI STRATEGIES</span>
                        <span class="hidden sm:inline-block text-[10px] font-mono uppercase px-2 py-0.5 rounded bg-electric/15 text-electric border border-electric/30">Sr. AE Academy</span>
                    </div>
                    <p class="text-[11px] text-zinc-400 hidden sm:block">Converting chaos into consistency, and consistency into currency.</p>
                </div>
            </div>
        </div>

        <!-- Trainee Status & Controls -->
        <div class="flex items-center gap-2 md:gap-3">
            <div class="hidden xl:flex items-center gap-2 bg-zinc-900/90 border border-white/10 px-3 py-1.5 rounded-lg text-xs">
                <span class="text-zinc-400">AE:</span>
                <button onclick="openProfileModal()" id="header-ae-name" class="font-semibold text-white hover:text-electric underline decoration-dotted">Set Trainee Name</button>
                <span class="text-zinc-600">|</span>
                <span class="text-gold font-mono font-semibold" id="header-xp">0 XP</span>
                <span class="text-zinc-600">|</span>
                <span class="text-emerald-400 font-mono" id="header-progress">0% Certified</span>
            </div>

            <button onclick="triggerRandomPopQuiz()" class="px-3 py-1.5 rounded-lg bg-gold/15 hover:bg-gold/25 border border-gold/40 text-gold text-xs font-mono font-semibold transition-all" title="Launch a 2-3 question random pop quiz from the current Playbook">
                ⚡ Pop Quiz
            </button>

            <button onclick="openTelemetryDashboard()" class="px-3 py-1.5 rounded-lg bg-white/5 hover:bg-white/10 border border-white/15 text-zinc-200 text-xs font-medium transition-all">
                📊 Scoreboard & Email Logs
            </button>

            <button onclick="toggleOwnerMode()" id="owner-mode-btn" class="px-3 py-1.5 rounded-lg bg-zinc-900 border border-white/15 text-zinc-400 hover:text-white text-xs font-mono transition-all" title="Mark Bockrath Owner Mode: Unlock all Playbooks for immediate inspection">
                🔒 Trainee Mode
            </button>
        </div>
    </div>
</header>

<!-- MAIN WORKSPACE LAYOUT -->
<div class="relative z-10 flex-1 max-w-[1600px] w-full mx-auto flex">

    <!-- LEFT SIDEBAR: PLAYBOOKS 0–10 & PHASE NAVIGATION -->
    <aside id="app-sidebar" class="w-80 shrink-0 border-r border-white/10 bg-charcoal/95 backdrop-blur-xl hidden lg:flex flex-col h-[calc(100vh-4rem)] sticky top-16">
        <div class="p-4 border-b border-white/10">
            <div class="flex items-center justify-between mb-2">
                <span class="text-[11px] font-mono uppercase tracking-wider text-zinc-400">Curriculum Modules (11)</span>
                <span class="text-[11px] font-mono text-electric" id="sidebar-unlocked-count">1 / 11 Unlocked</span>
            </div>
            <div class="w-full h-2 bg-zinc-800 rounded-full overflow-hidden">
                <div id="sidebar-progress-bar" class="h-full bg-gradient-to-r from-electric to-emerald-400 transition-all duration-500" style="width: 9%"></div>
            </div>
        </div>

        <div class="flex-1 overflow-y-auto p-3 space-y-2" id="sidebar-playbook-list">
            <!-- Populated dynamically by JS -->
        </div>

        <div class="p-3 border-t border-white/10 bg-zinc-950/80 text-[11px] text-zinc-400 flex flex-col gap-1">
            <div class="flex justify-between">
                <span>Test Telemetry Target:</span>
                <a href="mailto:mark@mabaistrategies.com" class="text-electric hover:underline font-mono">mark@mabaistrategies.com</a>
            </div>
            <div class="flex justify-between">
                <span>Pop Quiz Accuracy:</span>
                <span id="sidebar-pop-acc" class="text-emerald-400 font-mono">100%</span>
            </div>
        </div>
    </aside>

    <!-- CENTER CONTENT STAGE -->
    <main class="flex-1 min-w-0 flex flex-col">
        <!-- Playbook Banner & Phase Stepper -->
        <div class="border-b border-white/10 bg-tungsten/60 px-5 md:px-10 py-6">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
                <div class="flex items-center gap-2">
                    <span id="stage-pb-code" class="px-2.5 py-0.5 rounded text-xs font-mono font-semibold bg-electric/20 text-electric border border-electric/40">PLAYBOOK 00</span>
                    <span id="stage-pb-level" class="text-xs font-mono text-zinc-400">BUSINESS LEVEL</span>
                </div>
                <div class="flex items-center gap-2">
                    <span id="stage-page-counter" class="text-xs font-mono text-gold bg-gold/10 border border-gold/30 px-2.5 py-0.5 rounded">Page 1 of 12</span>
                    <button onclick="launchModuleExam(currentPlaybook.id)" class="text-xs font-mono px-3 py-1 rounded bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 border border-emerald-500/40 transition-all">
                        🎓 Take Module Test
                    </button>
                </div>
            </div>

            <h1 id="stage-pb-title" class="font-serif text-2xl md:text-3xl text-white font-bold tracking-tight mb-3">
                The Agentic Enterprise: Inside MAB AI Strategies
            </h1>

            <!-- Phase Pagination Pills -->
            <div id="phase-pills-container" class="flex items-center gap-1.5 overflow-x-auto pb-1 pt-1">
                <!-- Populated by JS -->
            </div>
        </div>

        <!-- Active Page Content Card -->
        <div class="flex-1 px-5 md:px-10 py-8 max-w-5xl w-full mx-auto">
            <div class="bg-tungsten/50 border border-white/10 rounded-2xl p-6 md:p-10 shadow-2xl">
                <div class="flex flex-wrap items-center justify-between gap-2 pb-4 mb-6 border-b border-white/10">
                    <div>
                        <span id="page-phase-tag" class="text-xs font-mono uppercase tracking-widest text-electric block mb-1">PHASE 0.1</span>
                        <h2 id="page-title" class="font-serif text-2xl md:text-4xl text-white font-bold">Welcome to the Arena</h2>
                    </div>
                    <button onclick="markPageCompletedAndNext()" class="px-4 py-2 rounded-lg bg-electric hover:bg-electricDark text-white text-xs font-semibold transition-all shadow-lg">
                        Complete Phase & Continue →
                    </button>
                </div>

                <p id="page-tagline" class="text-base md:text-lg text-zinc-300 italic mb-6 bg-white/[0.02] p-4 rounded-xl border border-white/5"></p>

                <!-- Key Takeaways Box -->
                <div class="mb-8 bg-charcoal/90 border border-electric/30 rounded-xl p-5">
                    <div class="text-xs font-mono uppercase tracking-wider text-electric font-semibold mb-2.5 flex items-center gap-2">
                        <span>⚡ EXECUTIVE KEY TAKEAWAYS (MEMORIZE COLD)</span>
                    </div>
                    <ul id="page-takeaways" class="space-y-1.5 text-sm text-zinc-200 list-disc pl-5"></ul>
                </div>

                <!-- Dynamic HTML Body -->
                <div id="page-body-content" class="prose-section"></div>

                <!-- Bottom Page Navigation Bar -->
                <div class="mt-10 pt-6 border-t border-white/10 flex flex-wrap items-center justify-between gap-4">
                    <button id="btn-prev-page" onclick="navigatePage(-1)" class="px-5 py-2.5 rounded-xl border border-white/15 bg-white/5 hover:bg-white/10 text-sm font-medium text-zinc-200 transition-all">
                        ← Previous Phase
                    </button>

                    <div class="text-xs font-mono text-zinc-400" id="bottom-page-indicator">
                        Phase 1 of 12
                    </div>

                    <button id="btn-next-page" onclick="markPageCompletedAndNext()" class="px-6 py-2.5 rounded-xl bg-electric hover:bg-electricDark text-white text-sm font-semibold shadow-[0_0_20px_rgba(59,130,246,0.35)] transition-all">
                        Next Phase →
                    </button>
                </div>
            </div>
        </div>
    </main>
</div>

<!-- ======================================================================= -->
<!-- MODAL 1: POP QUIZ MODAL (2-3 RANDOM QUESTIONS)                          -->
<!-- ======================================================================= -->
<div id="pop-quiz-modal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md hidden items-center justify-center p-4">
    <div class="bg-tungsten border border-gold/50 rounded-2xl max-w-2xl w-full p-6 md:p-8 shadow-2xl max-h-[90vh] overflow-y-auto">
        <div class="flex items-center justify-between pb-4 mb-5 border-b border-white/10">
            <div>
                <span class="badge-gold">⚡ SPOT CHECK · RANDOM POP QUIZ</span>
                <h3 id="pq-title" class="font-serif text-2xl text-white mt-1">Knowledge Verification</h3>
            </div>
            <button onclick="closePopQuizModal()" class="text-zinc-400 hover:text-white text-xl">✕</button>
        </div>
        <p class="text-xs text-zinc-400 mb-5">In the real arena, executives throw curveballs without warning. Answer these rapid-fire questions to lock in your retention.</p>
        <div id="pq-questions-container" class="space-y-6"></div>
        <div id="pq-feedback-banner" class="hidden mt-5 p-4 rounded-xl text-sm"></div>
        <div class="mt-6 flex justify-end gap-3">
            <button id="pq-submit-btn" onclick="submitPopQuiz()" class="px-6 py-2.5 rounded-xl bg-gold text-charcoal font-bold text-sm hover:brightness-110 transition-all">
                Verify Answers
            </button>
            <button id="pq-continue-btn" onclick="closePopQuizModal()" class="hidden px-6 py-2.5 rounded-xl bg-electric text-white font-semibold text-sm">
                Continue Training →
            </button>
        </div>
    </div>
</div>

<!-- ======================================================================= -->
<!-- MODAL 2: SCORED MODULE CERTIFICATION EXAM (10-15 QUESTIONS)             -->
<!-- ======================================================================= -->
<div id="exam-modal" class="fixed inset-0 z-50 bg-black/90 backdrop-blur-lg hidden items-center justify-center p-4">
    <div class="bg-charcoal border border-electric/50 rounded-2xl max-w-4xl w-full p-6 md:p-8 shadow-2xl max-h-[92vh] flex flex-col">
        <div class="flex items-center justify-between pb-4 mb-4 border-b border-white/10 shrink-0">
            <div>
                <span class="badge-electric" id="exam-badge">SCORED MODULE CERTIFICATION EXAM</span>
                <h3 id="exam-title" class="font-serif text-2xl md:text-3xl text-white mt-1">Playbook Certification</h3>
            </div>
            <button onclick="closeExamModal()" class="text-zinc-400 hover:text-white text-xl px-2">✕</button>
        </div>

        <div class="overflow-y-auto flex-1 pr-2 space-y-6" id="exam-body-scroll">
            <div class="bg-zinc-900/90 border border-white/10 rounded-xl p-4 text-xs text-zinc-300 flex flex-wrap justify-between gap-2">
                <span>🎯 <strong>Passing Score Required:</strong> 80% to unlock the next Playbook</span>
                <span>📧 <strong>Automatic Telemetry:</strong> Diagnostic results are compiled for <code class="text-electric">mark@mabaistrategies.com</code> upon completion</span>
            </div>

            <div id="exam-questions-list" class="space-y-6"></div>

            <!-- Exam Diagnostic Report & Email Dispatch View (Shown after submit) -->
            <div id="exam-results-panel" class="hidden space-y-6"></div>
        </div>

        <div class="pt-4 mt-4 border-t border-white/10 flex justify-between items-center shrink-0" id="exam-footer-controls">
            <span id="exam-answered-count" class="text-xs font-mono text-zinc-400">Answer all questions before submitting</span>
            <button id="exam-submit-btn" onclick="submitModuleExam()" class="px-6 py-3 rounded-xl bg-electric hover:bg-electricDark text-white font-bold text-sm shadow-[0_0_25px_rgba(59,130,246,0.4)]">
                Submit Scored Test & Generate Report →
            </button>
        </div>
    </div>
</div>

<!-- ======================================================================= -->
<!-- MODAL 3: TRAINEE PROFILE & TELEMETRY DASHBOARD                          -->
<!-- ======================================================================= -->
<div id="dashboard-modal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md hidden items-center justify-center p-4">
    <div class="bg-charcoal border border-white/15 rounded-2xl max-w-4xl w-full p-6 md:p-8 shadow-2xl max-h-[90vh] overflow-y-auto">
        <div class="flex items-center justify-between pb-4 mb-6 border-b border-white/10">
            <div>
                <span class="badge-emerald">EXECUTIVE TELEMETRY & COMPETENCY LOGS</span>
                <h3 class="font-serif text-2xl text-white mt-1">AE Training Performance & Email Dispatch Center</h3>
            </div>
            <button onclick="closeDashboardModal()" class="text-zinc-400 hover:text-white text-xl">✕</button>
        </div>

        <!-- Trainee Identity Form -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6 bg-zinc-900/80 p-4 rounded-xl border border-white/10">
            <div>
                <label class="block text-xs font-mono text-zinc-400 mb-1">Senior AE Full Name</label>
                <input id="prof-name-input" type="text" placeholder="e.g., Jordan Taylor" class="form-input" />
            </div>
            <div>
                <label class="block text-xs font-mono text-zinc-400 mb-1">AE Corporate Email</label>
                <input id="prof-email-input" type="email" placeholder="jordan@mabaistrategies.com" class="form-input" />
            </div>
            <div class="flex items-end">
                <button onclick="saveTraineeProfile()" class="w-full py-2.5 bg-electric hover:bg-electricDark text-white font-semibold rounded-lg text-xs transition-all">
                    Save AE Identity
                </button>
            </div>
        </div>

        <div id="dashboard-history-container" class="space-y-4"></div>

        <div class="mt-6 pt-4 border-t border-white/10 flex flex-wrap justify-between gap-3">
            <button onclick="emailMasterRollupToMark()" class="px-5 py-2.5 rounded-xl bg-electric text-white text-xs font-semibold hover:bg-electricDark">
                📧 Email Complete All-Module Transcript to mark@mabaistrategies.com
            </button>
            <button onclick="downloadMasterTranscriptJSON()" class="px-4 py-2.5 rounded-xl bg-white/5 border border-white/15 text-zinc-300 text-xs font-mono hover:bg-white/10">
                ⬇️ Export Full Telemetry (.json)
            </button>
        </div>
    </div>
</div>

<script>
// Embedded Playbook Curriculum Data (Playbooks 0 through 10)
const PLAYBOOKS = __PLAYBOOKS_JSON__;

// Interactive Data for Infographics & Simulators
const IMPRESSIONS_DATA = [
    {
        badge: "STAGE 01 · FORENSIC DIAGNOSTIC",
        title: "Diagnose the Chaos (AI Readiness Audit)",
        desc: "An AI Readiness Audit maps every leak in the prospect's operation—the repetitive tasks, the lagging handoffs, and the data rotting in silos. We quantify the cost of standing still, down to the hour and dollar.",
        list: ["✓ Process mining & bottleneck quantification", "✓ Hourly cost-of-inaction financial model", "✓ Prioritized, ROI-ranked automation roadmap"],
        quote: '"We never guess where to put AI. First, we run a forensic scan of your workflows to see exactly where manual handoffs and data silos are bleeding hours—and we price the exact dollar return of fixing each bottleneck before writing a line of code."',
        ttv: "1–2 Weeks",
        out: "Executive ROI Roadmap"
    },
    {
        badge: "STAGE 02 · BESPOKE ENGINEERING",
        title: "Architect the Agents (Built, Not Bolted On)",
        desc: "Custom AI agents engineered around their stack—not bolted on top of it. Multi-step reasoning, tool use, and human-in-the-loop guardrails designed by architects with 16+ years in mid-market & enterprise tech.",
        list: ["✓ LangGraph · CrewAI v0.9 · AG2 · OpenAI Agents SDK", "✓ o3 · Claude 4 · Gemini 2.5 Pro · Llama 4 (Vendor-Neutral)", "✓ Full human-in-the-loop checkpoints & SOC 2-aligned audit trails"],
        quote: '"Off-the-shelf software forces your team to log into another dashboard. Our agents are wired directly into your existing CRM, ATS, and ERP so the work executes automatically behind the scenes."',
        ttv: "5–15 Business Days",
        out: "Production Agent Architecture"
    },
    {
        badge: "STAGE 03 · 24/7 EXECUTION",
        title: "Automate Around the Clock (Workflows That Never Sleep)",
        desc: "Event-driven pipelines with automatic failure recovery. One deployment vetted candidates, ran outreach, and handled onboarding autonomously—returning 15 hours per week to a Director of Staff and roughly $40K in annual net liquidity.",
        list: ["✓ 24/7 autonomous execution with zero idle time", "✓ 15+ hours/week reclaimed per single deployment", "✓ ~$40,000 in annual net liquidity proven in the field"],
        quote: '"While your competitors wait until Monday morning to screen leads or chase onboarding paperwork, your autonomous workflows execute in seconds at 2:00 AM on a Sunday."',
        ttv: "Immediate Upon Go-Live",
        out: "15+ Hrs/Wk Reclaimed"
    },
    {
        badge: "STAGE 04 · COMPOUNDING RETURN",
        title: "Amplify Into Currency (Consistency → Currency)",
        desc: "Reclaimed hours become training, strategy, and revenue growth. Our clients have measured near-10% YoY output gains from redeployed human focus alone. Consistency, converted into currency.",
        list: ["✓ ~10% YoY output gains from redeployed human focus", "✓ Real-time KPI & liquidity dashboard tracking every run", "✓ Continuous expansion across departments"],
        quote: '"The real magic isn\'t just cutting admin cost—it\'s what happens when your sharpest leaders get 60 hours a month back to focus on closing deals, retaining clients, and scaling the business."',
        ttv: "30–90 Days Compounding",
        out: "~10% YoY Output Gain"
    }
];

const SCENARIO_MATCHER_DATA = [
    {
        title: "Standalone: AI Readiness Audit (1–2 Weeks)",
        why: "Because the prospect lacks process visibility, pitching a large retainer immediately triggers stall tactics. The 1–2 week AI Readiness Audit diagnoses the chaos, quantifies the hourly bleed, and hands them an ROI-ranked roadmap.",
        ascTitle: "Ascend → Accelerator Retainer",
        ascWhy: "At the Audit Executive Readout call, present the top 6 ROI workflows uncovered in the audit and transition seamlessly into the Accelerator Retainer backed by the 90-day ROI guarantee.",
        personas: ["COO / VP Ops (Champion)", "CEO (Economic Buyer)", "CFO Marcus (ROI Sign-off)"]
    },
    {
        title: "Standalone: Single Workflow or Agent Build (5–15 Days)",
        why: "They already know their exact bleeding wound (15 hrs/wk wasted on recruiting/onboarding). Solve that single bottleneck fast in 5–15 business days with 30-day post-deploy support to prove our engineering speed.",
        ascTitle: "Ascend → Accelerator Retainer at Day 30",
        ascWhy: "Once the first agent reclaims 15 hrs/wk (~$40K annual net liquidity), use the Day-30 Readout to roll them into Accelerator for their remaining 5 workflows.",
        personas: ["Director of Staff / VP HR (Champion)", "COO / Managing Partner (Economic Buyer)"]
    },
    {
        title: "Monthly Retainer: Foundation Tier",
        why: "Ideal for a 30-person business establishing its first AI automation layer: includes an AI Readiness Audit (up to 5 processes), up to 2 workflows/month, CRM/ATS integration, and monthly strategy calls.",
        ascTitle: "Ascend → Accelerator as Volume Scales",
        ascWhy: "After 90 days of steady 2-workflow/month execution, expand into custom LangGraph agents and ERP integration on Accelerator.",
        personas: ["Founder / CEO (Economic Buyer)", "Operations Manager (Champion)"]
    },
    {
        title: "Monthly Retainer: Accelerator Tier (Flagship)",
        why: "The mid-market engine: Unlimited AI Readiness Audit, up to 6 workflows/month, 1 custom AI agent/quarter (LangGraph/AG2), real-time synthesis dashboard, CRM/ATS/ERP integration, weekly calls + Slack, and our 90-Day ROI Guarantee.",
        ascTitle: "Ascend → Principal Retainer (Fractional CAIO)",
        ascWhy: "As autonomous workflows become central to their valuation, embed Mark as Fractional Chief AI Officer.",
        personas: ["COO (Champion)", "CEO & CFO (Economic Buyers)", "VP IT (Technical Gatekeeper)"]
    },
    {
        title: "Monthly Retainer: Principal Tier (Fractional CAIO)",
        why: "Embeds a named Fractional Chief AI Officer directly into their strategic and technical layer with unlimited workflows & agent builds, board briefings, custom model fine-tuning, and SOC 2 / GDPR compliance architecture.",
        ascTitle: "Multi-Year Enterprise Partnership",
        ascWhy: "Becomes the permanent intelligence architecture backbone of the enterprise across all business units.",
        personas: ["CEO / Board / PE Operating Partner", "CFO & General Counsel", "CTO / CISO"]
    }
];

const VERTICAL_CARDS = [
    {
        painTitle: "Manual Resume Screening, Outreach & Onboarding Lag",
        painDesc: "Recruiters and Directors of Staff waste 15+ hrs/wk reading unqualified resumes in Bullhorn/Greenhouse, playing calendar tag, and manually chasing onboarding packets.",
        trigTitle: "Hiring 'Recruiting Coordinator' or 'Talent Ops'",
        trigDesc: "Filter Apollo/LinkedIn for Staffing agencies (25–200 headcount) with open job reqs for Coordinators or Directors of Staff.",
        wedgeTitle: "Single Agent Build → Accelerator Retainer",
        wedgeDesc: "Lead with our proven 15 hr/wk & ~$40K net liquidity Director of Staff deployment (5–15 day build), then expand across outbound sourcing and billing on Accelerator."
    },
    {
        painTitle: "Partner Billable Hours Lost to Intake, Contract Review & Reporting",
        painDesc: "$400/hr attorneys, CPAs, and agency directors waste 12–20 hrs/wk provisioning client workspaces, reviewing standard MSAs, compiling monthly client reports, and chasing overdue invoices.",
        trigTitle: "Hiring 'Client Onboarding Specialist' or 'Billing Admin'",
        trigDesc: "Look for firms using Clio, HubSpot, QuickBooks, or NetSuite with growing headcount and manual client onboarding.",
        wedgeTitle: "AI Readiness Audit or Onboarding/Contract Agent → Accelerator",
        wedgeDesc: "Deploy Onboarding Bot + Contract Sentinel + Invoice Chaser to immediately unlock billable partner capacity."
    },
    {
        painTitle: "PDF Order Entry, Dispatch Handoffs & Carrier Reconciliation",
        painDesc: "Operations coordinators spend all day reading emailed PDFs/BOLs and re-keying rows into legacy ERPs, causing costly billing errors and slow quote turnarounds.",
        trigTitle: "Post-Merger ERP Silos or 'Logistics Coordinator' Job Posts",
        trigDesc: "Target regional logistics, distribution, and commercial field service operators with 40–300 employees.",
        wedgeTitle: "AI Readiness Audit → Accelerator / Principal",
        wedgeDesc: "Forensically map their ERP/CRM handoffs in a 1–2 week Audit, then deploy OCR Document Scrapers and Real-Time Data Synthesis."
    },
    {
        painTitle: "High-Volume Client Intake Triage & Compliance Governance",
        painDesc: "Advisors and intake teams drown in repetitive Tier-1 status calls, multi-page intake verification, and strict SOC 2 / GDPR / HIPAA security requirements.",
        trigTitle: "Slow Response Reviews or 'Intake / Operations Analyst' Reqs",
        trigDesc: "Target multi-advisor wealth firms, commercial insurance brokerages, and healthcare admin groups.",
        wedgeTitle: "Audit / Support Triage Agent → Principal Retainer",
        wedgeDesc: "Emphasize SOC 2 / GDPR-aligned governance, private RAG over policy docs, and Human-in-the-Loop guardrails."
    }
];

const WORKLIST_LEADS = [
    {
        sigTitle: "Bullhorn ATS + 2 Open Coordinator Reqs",
        sigDesc: "• Email: r.kim@sterlingstaffing.com (Hunter Verified 99%)<br/>• Direct Mobile: (410) 555-0194 (ZoomInfo)<br/>• Signal: Posted 2 jobs for 'Talent Onboarding Coordinator' 6 days ago.",
        badHook: '"Hi Rachel, I saw your profile on LinkedIn and wanted to introduce MAB AI Strategies. We build custom AI agents and automations for staffing companies..."',
        goodHook: '"Rachel — noticed Sterling has two open reqs for Talent Onboarding Coordinators to manage your Bullhorn handoffs. Before adding $120K in admin payroll, we deployed an autonomous vetting & onboarding agent for a Director of Staff that reclaimed 15 hrs/wk and ~$40K in net liquidity..."'
    },
    {
        sigTitle: "HubSpot + NetSuite + New VP Sales (<60 Days)",
        sigDesc: "• Email: d.ross@nexgenlogistics.com (Hunter Verified 98%)<br/>• Direct Mobile: (301) 555-0821 (ZoomInfo)<br/>• Signal: Hired as VP Sales 45 days ago; reps manually quoting across HubSpot & NetSuite.",
        badHook: '"Dear David, I hope this email finds you thriving in your new role! At MAB AI Strategies we leverage cutting-edge LLMs to revolutionize sales..."',
        goodHook: '"David — congrats on taking the helm of the sales org at NexGen. Usually when a new VP steps into a HubSpot + NetSuite environment, reps are losing 8+ hrs/wk manually building quotes and logging call notes instead of selling. Worth a 30-min briefing to map your top 3 speed-to-lead automations?"'
    },
    {
        sigTitle: "55-Person Law Firm + Hiring Billing & Intake Specialist",
        sigDesc: "• Email: mvance@vancelegal.com (Hunter Verified 99%)<br/>• Direct Mobile: (202) 555-0412 (ZoomInfo)<br/>• Signal: Job description mentions 'chasing client retainers, extracting PDF intake docs, and updating Clio'.",
        badHook: '"Hi Marcus, do you want to buy AI chatbots for your law firm? AI is replacing paralegals everywhere!"',
        goodHook: '"Marcus — saw your posting for a Billing & Intake Specialist to handle Clio intake extraction and aging receivable follow-ups. We engineer guardrailed workflows that automate 80% of that exact intake-to-invoice loop with full audit trails—returning ~$40K/yr in net liquidity per workflow. Open to a 30-min ROI briefing?"'
    }
];

const EMAIL_TEMPLATES = [
    {
        persona: "COO / VP Operations / Director of Staff",
        subject: "[Company] ops handoffs / 15 hrs a week",
        body: `[First Name] — noticed [Company] is scaling the team and currently hiring for [Role / managing handoffs across CRM & ops].

Most operations leaders we speak with aren't looking for another software login—they just want to stop their best people from losing 15+ hours a week to repetitive vetting, outreach, and onboarding handoffs.

We recently engineered an autonomous workflow integrated directly into a Director of Staff's existing stack that reclaimed 15 hours per week and roughly $40,000 in annual net liquidity from a single deployment.

Open to a 30-minute strategic briefing next week where we price out your top 3 highest-ROI automations and leave you with the roadmap—whether you use us or not?

Best,
[Your Name]
Sr. Account Executive | MAB AI Strategies
mabaistrategies.com`,
        why: "Zero fear-mongering, under 95 words, names their exact operational reality ('not looking for another software login'), drops verified field evidence (15 hrs/wk, $40K liquidity), and offers a no-obligation 30-minute roadmap."
    },
    {
        persona: "CEO / Founder ($10M–$100M Mid-Market)",
        subject: "converting chaos into currency at [Company]",
        body: `[First Name] — watched [Company]'s growth to [X] employees this year. Usually at that inflection point, operational complexity starts growing faster than headcount can keep up.

At MAB AI Strategies, our thesis is simple: converting chaos into consistency, and consistency into currency. We wire custom AI agents and 24/7 workflows directly into your existing stack—driving near-10% YoY output gains from redeployed human focus alone and $12M+ in proven B2B revenue impact.

Would you be opposed to a confidential 30-minute Strategic Briefing where Mark Bockrath and I quantify what manual bottlenecks are currently costing [Company] and hand you a 3-automation ROI roadmap?

Best,
[Your Name]
Sr. Account Executive | MAB AI Strategies`,
        why: "Speaks directly to the CEO's scoreboard: scaling output (~10% YoY gain) without linear headcount bloat, and uses 'Would you be opposed to...' (a high-converting Chris Voss no-oriented CTA)."
    },
    {
        persona: "CFO / Managing Partner ('Marcus' Persona)",
        subject: "pricing the cost of inaction / [Company]",
        body: `[First Name] — most AI initiatives fail the CFO test because vendors sell shiny licenses without measuring payback.

We take the opposite approach: every module we engineer ships measured against baseline hourly and dollar KPIs. A single recent deployment reclaimed 15 hours/week of manual coordination and returned ~$40,000 in annual net liquidity—and our mid-market Accelerator tier carries a contractual 90-day ROI guarantee or refund.

Open to a 30-minute diagnostic briefing to price the hourly cost of manual handoffs across your billing and ops stack—with zero obligation?

Best,
[Your Name]
Sr. Account Executive | MAB AI Strategies`,
        why: "Hits every CFO hot button: acknowledges why most AI fails, cites ~$40K net liquidity, and leads with the 90-day ROI guarantee."
    },
    {
        persona: "VP of Sales / CRO ('Titan' Persona)",
        subject: "[Company] rep selling time / speed-to-lead",
        body: `[First Name] — noticed you're scaling the revenue team at [Company] on [HubSpot / Salesforce].

When we audit mid-market sales orgs, we consistently find reps losing 10–12 hours a week researching leads, enriching CRM fields, and typing post-call notes instead of closing pipeline.

We build autonomous revenue workflows (instant lead enrichment, automated Zoom-to-CRM logging, and AI readiness briefings) wired straight into your CRM so reps spend 80% of their week actually selling.

Worth 30 minutes next Tuesday or Thursday to map the 3 highest-ROI revenue automations for your team?

Best,
[Your Name]
Sr. Account Executive | MAB AI Strategies`,
        why: "Frames AI around the CRO's #1 obsession: giving reps back 10+ hours/week of pure selling time and accelerating pipeline velocity."
    },
    {
        persona: "Day-14 Polite Walk-Away ('Win Fast, Lose Fast')",
        subject: "closing your file / [Company]",
        body: `[First Name] — haven't heard back, so I'm assuming that reclaiming 15+ hours a week of manual operational drag isn't a top-three priority for [Company] this quarter.

I'm closing out your file on my end so I'm not cluttering your inbox. If eliminating manual handoffs across your stack moves back onto the front burner later this year, feel free to reply here and we can grab a 30-minute Strategic Briefing.

Wishing you and the team a monster Q3,
[Your Name]
Sr. Account Executive | MAB AI Strategies`,
        why: "Enforces 'Win Fast, Lose Fast'. Removing the offer triggers loss aversion and consistently generates a 15–22% reply rate from busy executives saying 'Wait—don't close the file, let's talk Thursday.'"
    }
];

const CALL_SIM_SCENARIOS = [
    {
        speaker: "📞 PROSPECT (DANA, COO @ APEX STAFFING):",
        prompt: '"Look, we\'re super slammed right now and honestly I get ten calls a week about AI. Just send me an email with some information and if we need anything I\'ll reach out."',
        options: [
            'A) "Okay sorry to bother you! What\'s your email address? I\'ll send over our brochure PDF and check back in a month!"',
            'B) "Actually Dana, if you don\'t adopt AI right now your competitors are going to put you out of business, so you really need to give me 30 minutes!"',
            'C) "Totally fair, Dana—I\'ll fire over a quick note right after this. So I don\'t send you generic fluff that clutters your inbox: if you could wave a magic wand and erase one repetitive manual handoff your coordinators hate doing every week, would it be candidate screening or onboarding paperwork?"'
        ],
        correct: 2,
        feedbackGood: "✅ BULLSEYE! You agreed calmly without fighting ('Totally fair, I\\'ll fire over a quick note'), and immediately asked an Either/Or diagnostic question ('So I don\\'t send you generic fluff...'). 70% of the time, the prospect answers 'Honestly, onboarding paperwork is killing us'—and you lock the 30-minute briefing right there!",
        feedbackBad: "❌ ROOKIE TRAP: Option A surrenders into the 'send me an email' graveyard. Option B violates our core rule against fear-mongering. Option C acknowledges, aligns, and pivots with an Either/Or diagnostic question!"
    },
    {
        speaker: "📞 PROSPECT (MARCUS, CFO @ VANGUARD LOGISTICS):",
        prompt: '"We already bought Microsoft Copilot licenses for our team three months ago, so we\'re already covered on AI."',
        options: [
            'A) "Oh okay, Copilot is great, have a nice day!"',
            'B) "Copilot is awesome for helping an individual write an email faster—and most of our clients use it too. Where we come in is the cross-system architecture Copilot can\'t touch: wiring autonomous workflows between your ERP, CRM, and billing so data moves 24/7 without a human clicking buttons. Since rolling out Copilot, how much manual copy-pasting between systems is your ops team still stuck doing?"',
            'C) "Microsoft Copilot is terrible garbage and you wasted your money!"'
        ],
        correct: 1,
        feedbackGood: "✅ SURGICAL EXECUTION! Never insult a tool the buyer just paid for. Validate Copilot as a personal productivity assistant, then contrast it with cross-system autonomous architecture ('Built, Not Bolted On') and ask what manual handoffs still remain.",
        feedbackBad: "❌ MISSED OPPORTUNITY: Never hang up at the mention of Copilot, and never insult their purchase. Contrast individual chat seats with multi-system autonomous workflows!"
    },
    {
        speaker: "📞 PROSPECT (TOM, CEO @ MERIDIAN SERVICES):",
        prompt: '"Sounds interesting, but we\'ve frozen all new software and consulting budgets for the rest of the quarter."',
        options: [
            'A) "Totally respect that, Tom—in fact, freezing bloated software spend is smart. I\'m not calling to ask for budget today; our 30-minute Strategic Briefing is 100% free and leaves you with a quantified ROI roadmap showing where manual workflows are currently leaking cash, so when you plan next quarter\'s capital allocation you have the exact math in hand. Worth 30 minutes on Thursday at 11 AM?"',
            'B) "Well if you have no money I guess we can\'t talk."',
            'C) "We can work for free for 6 months!"'
        ],
        correct: 0,
        feedbackGood: "✅ ELITE CLOSER MOVE! Remember: on a cold call, the price of the 30-Minute Strategic Briefing is $0.00! Separating the free diagnostic briefing from 'buying a consulting contract today' neutralizes the budget-freeze objection immediately.",
        feedbackBad: "❌ Remember: you are selling a free 30-Minute Strategic Briefing ('Initiate Convergence') on a cold call, not asking for a wire transfer today!"
    }
];

const NOTEBOOK_PROMPTS = [
    {
        title: "Pre-Call Operational Leak & Taxonomy Mapper",
        sources: "Prospect Site URLs + 3 Open Job Postings + Exec LinkedIn Profiles",
        prompt: `Based strictly on the uploaded company pages, job descriptions, and executive profiles:
1. Identify every manual process, cross-departmental handoff, or software tool mentioned in their job postings.
2. What internal terminology do they use for their customers, projects, and deliverables?
3. Formulate 3 specific hypotheses for where their team is losing 10–20+ hours per week in operational drag.
4. Map each hypothesis to the exact MAB AI Strategies solution (AI Readiness Audit, Single Agent, or Accelerator Retainer) and give me a 30-second opening frame for the call.`
    },
    {
        title: "Persona-Specific Diagnostic Question Generator",
        sources: "Prospect Sources + MAB AI Capability Matrix",
        prompt: `I am meeting with [Name, Title] who matches the [COO / CFO / CEO / VP Sales] persona.
Using only the uploaded sources:
1. Generate 6 surgical Discovery questions that move from Layer 1 (Process Walkthrough) to Layer 2 (Weekly Hours & Dollar Bleed) to Layer 3 (Executive/Board Stakes).
2. Give me 3 'Either/Or' questions tailored to their vertical that make it effortless for them to reveal their #1 bottleneck while keeping my talk time under 20%.`
    },
    {
        title: "Post-Discovery Transcript → ROI & Nexus CRM Extractor",
        sources: "Discovery Zoom Transcript + Prospect Sources",
        prompt: `Analyze the uploaded Discovery Call transcript and extract the exact fields needed for Nexus CRM and our Architecture Readout:
1. QUANTIFIED PAIN MATH: Every number, hourly estimate, headcount figure, or delay mentioned by the prospect (with exact timestamps and direct quotes).
2. TECH STACK INVENTORY: Every CRM, ATS, ERP, or spreadsheet mentioned.
3. BUYING COMMITTEE: Identify the Champion, Economic Buyer, and any Technical Gatekeepers mentioned.
4. EXECUTIVE MIRROR RECAP EMAIL: Draft a crisp 5-bullet post-call recap email reiterating their cost of inaction and confirming the agenda for our upcoming Architecture Readout.`
    }
];

const TALK_TRACKS = [
    `1. HYPOTHESIS OPENER (MIN 3):
"Looking at your Bullhorn + HubSpot stack and your current hiring volume, we usually see recruiting and ops teams losing 15+ hours a week in two places: initial candidate vetting/outreach, and chasing onboarding packets. Walk me through how your team handles that flow today?"

2. PAIN QUANTIFICATION PROBE (MIN 10):
"So across your 4 coordinators, that's roughly 20 hours a week spent manually screening and chasing forms—about $55K a year in direct payroll drag, plus slower placements. How is that impacting your time-to-fill SLA?"

3. ARCHITECTURAL BRIDGE (MIN 19):
"That maps 1-to-1 to what we call 'Converting chaos into consistency, and consistency into currency.' For a Director of Staff in this exact spot, we engineered an autonomous agent wired directly into their stack that vets candidates, runs outreach, and handles onboarding 24/7—returning 15 hours/week and ~$40K in annual net liquidity."

4. NEXT-STEP LOCK (MIN 26):
"Rather than throwing a generic number at you today, let's get 30 minutes on the calendar for Thursday with Mark Bockrath where we present your exact 3-automation ROI roadmap and SOW options."`,

    `1. HYPOTHESIS OPENER (MIN 3):
"Seeing how your firm has scaled to 65 professionals, our experience with high-growth B2B advisory and legal firms is that highly paid partners and account managers get bogged down in three places: new client workspace provisioning, contract/intake review, and compiling monthly client reports. Which of those is eating the most billable capacity right now?"

2. PAIN QUANTIFICATION PROBE (MIN 10):
"If 5 senior staff are losing 4 hours a week each on non-billable intake and reporting—at a $250/hr billable opportunity cost, that's over $20,000 a month in trapped revenue capacity. Does that math feel conservative?"

3. ARCHITECTURAL BRIDGE (MIN 19):
"Instead of bolting on another tool, we wire our Onboarding Bot, Contract Sentinel, and Real-Time Data Synthesis directly into your CRM and document stack—so client workspaces provision in 30 seconds and executive reports compile autonomously."

4. NEXT-STEP LOCK (MIN 26):
"Let's bring your Managing Partner onto a 25-minute Architecture Readout on Tuesday at 2 PM where we walk through the exact ROI roadmap and our 90-day guaranteed Accelerator structure."`,

    `1. HYPOTHESIS OPENER (MIN 3):
"In multi-location logistics and field operations running legacy ERPs alongside modern CRMs, the biggest margin leak we diagnose is human staff acting as the copy-paste bridge—reading emailed PDF orders/invoices and hand-keying them into the ERP. Walk me through how orders and invoices flow from inbox to ERP today?"

2. PAIN QUANTIFICATION PROBE (MIN 10):
"So 3 dispatch/billing specialists spend 18 hours a week keying data and fixing mismatches—roughly $60K/yr in direct labor plus a 14-day lag in invoicing cashflow. What happens if volume jumps 25% next peak season?"

3. ARCHITECTURAL BRIDGE (MIN 19):
"We solve that by engineering deterministic & agentic document pipelines with human-in-the-loop guardrails—extracting PDFs with 99.8% accuracy, reconciling against your ERP, and only flagging exceptions for human review."

4. NEXT-STEP LOCK (MIN 26):
"Let's lock 30 minutes on Thursday with you and your CFO to review the forensic AI Readiness Audit & Accelerator options."`
];

// ============================================================================
// APPLICATION STATE & STORAGE ENGINE
// ============================================================================
const STORAGE_KEY = "MAB_AI_ACADEMY_STATE_V1";

let appState = {
    aeName: "",
    aeEmail: "",
    ownerMode: false,
    currentPbIndex: 0,
    currentPageIndex: 0,
    unlockedPlaybooks: ["pb0"],
    completedPages: {},
    xp: 0,
    popQuizStats: { taken: 0, correct: 0, total: 0 },
    examHistory: [] // Stores full diagnostic reports for each module test
};

function loadState() {
    try {
        const raw = localStorage.getItem(STORAGE_KEY);
        if (raw) {
            const parsed = JSON.parse(raw);
            appState = Object.assign(appState, parsed);
        }
    } catch (e) {
        console.warn("State load fallback:", e);
    }
}

function saveState() {
    try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(appState));
    } catch (e) {
        console.warn("State save fallback:", e);
    }
    updateHeaderStats();
    renderSidebar();
}

let currentPlaybook = PLAYBOOKS[0];
let activePopQuiz = null;
let activeExamPlaybook = null;

function isPlaybookUnlocked(pb) {
    if (appState.ownerMode) return true;
    if (!pb.unlockRequirement) return true;
    return appState.unlockedPlaybooks.includes(pb.id);
}

function updateHeaderStats() {
    const nameEl = document.getElementById("header-ae-name");
    nameEl.textContent = appState.aeName ? appState.aeName : "Set Trainee Name";
    document.getElementById("header-xp").textContent = `${appState.xp} XP`;

    const certifiedCount = Math.max(0, appState.unlockedPlaybooks.length - 1);
    const pct = Math.round((certifiedCount / PLAYBOOKS.length) * 100);
    document.getElementById("header-progress").textContent = `${pct}% Certified`;

    const unlockedTotal = appState.ownerMode ? PLAYBOOKS.length : appState.unlockedPlaybooks.length;
    document.getElementById("sidebar-unlocked-count").textContent = `${unlockedTotal} / ${PLAYBOOKS.length} Unlocked`;
    document.getElementById("sidebar-progress-bar").style.width = `${Math.max(9, Math.round((unlockedTotal / PLAYBOOKS.length) * 100))}%`;

    const popAcc = appState.popQuizStats.total > 0
        ? Math.round((appState.popQuizStats.correct / appState.popQuizStats.total) * 100)
        : 100;
    document.getElementById("sidebar-pop-acc").textContent = `${popAcc}% (${appState.popQuizStats.correct}/${appState.popQuizStats.total})`;

    const ownerBtn = document.getElementById("owner-mode-btn");
    if (appState.ownerMode) {
        ownerBtn.textContent = "🔓 Owner Mode (All Unlocked)";
        ownerBtn.className = "px-3 py-1.5 rounded-lg bg-electric/20 border border-electric text-electric text-xs font-mono font-semibold transition-all";
    } else {
        ownerBtn.textContent = "🔒 Trainee Mode";
        ownerBtn.className = "px-3 py-1.5 rounded-lg bg-zinc-900 border border-white/15 text-zinc-400 hover:text-white text-xs font-mono transition-all";
    }
}

function renderSidebar() {
    const list = document.getElementById("sidebar-playbook-list");
    list.innerHTML = "";

    PLAYBOOKS.forEach((pb, idx) => {
        const unlocked = isPlaybookUnlocked(pb);
        const isCurrent = idx === appState.currentPbIndex;
        const passedExam = appState.examHistory.some(e => e.playbookId === pb.id && e.passed);

        const card = document.createElement("div");
        card.className = `rounded-xl border transition-all ${
            isCurrent
                ? "bg-electric/15 border-electric shadow-[0_0_20px_rgba(59,130,246,0.15)]"
                : unlocked
                ? "bg-zinc-900/60 border-white/10 hover:border-white/25 cursor-pointer"
                : "bg-zinc-950/60 border-white/5 opacity-55 cursor-not-allowed"
        }`;

        const header = document.createElement("div");
        header.className = "p-3 flex items-start justify-between gap-2 cursor-pointer";
        header.onclick = () => {
            if (!unlocked) {
                alert(`🔒 Playbook ${pb.number} is currently locked. Pass the Playbook ${pb.number - 1} Certification Exam (or toggle 'Owner Mode' in the top right if you are Mark Bockrath) to unlock it!`);
                return;
            }
            selectPlaybook(idx, 0);
        };

        header.innerHTML = `
            <div class="min-w-0">
                <div class="flex items-center gap-1.5">
                    <span class="text-[10px] font-mono uppercase tracking-wider ${isCurrent ? 'text-electric font-bold' : 'text-zinc-400'}">${pb.code}</span>
                    ${passedExam ? '<span class="text-[10px] bg-emerald-500/20 text-emerald-300 px-1.5 py-0.2 rounded font-mono">✓ CERTIFIED</span>' : ''}
                </div>
                <div class="font-serif font-semibold text-sm text-white truncate mt-0.5">${pb.title}</div>
                <div class="text-[11px] text-zinc-400 mt-0.5">${pb.pages.length} Phases · ${pb.finalExam.questions.length}-Q Test</div>
            </div>
            <div class="text-sm shrink-0 mt-1">
                ${unlocked ? (isCurrent ? '📂' : '📘') : '🔒'}
            </div>
        `;
        card.appendChild(header);

        // If current playbook, render expandable page list
        if (isCurrent) {
            const pagesList = document.createElement("div");
            pagesList.className = "px-3 pb-3 pt-1 border-t border-white/10 space-y-1 max-h-60 overflow-y-auto";
            pb.pages.forEach((p, pIdx) => {
                const done = !!appState.completedPages[p.id];
                const activePage = pIdx === appState.currentPageIndex;
                const pBtn = document.createElement("button");
                pBtn.className = `w-full text-left px-2.5 py-1.5 rounded-lg text-xs flex items-center justify-between gap-2 transition-all ${
                    activePage
                        ? "bg-electric text-white font-semibold"
                        : "text-zinc-300 hover:bg-white/5"
                }`;
                pBtn.onclick = (e) => {
                    e.stopPropagation();
                    selectPlaybook(idx, pIdx);
                };
                pBtn.innerHTML = `
                    <span class="truncate">${pIdx + 1}. ${p.title}</span>
                    <span class="shrink-0 text-[10px]">${done ? '✓' : ''}</span>
                `;
                pagesList.appendChild(pBtn);
            });

            // Exam launch button inside sidebar
            const exBtn = document.createElement("button");
            exBtn.className = "w-full mt-2 py-2 px-3 rounded-lg bg-emerald-500/20 hover:bg-emerald-500/30 border border-emerald-500/40 text-emerald-300 text-xs font-mono font-semibold text-center transition-all";
            exBtn.textContent = `🎓 Take Playbook ${pb.number} Scored Test (${pb.finalExam.questions.length} Qs)`;
            exBtn.onclick = (e) => {
                e.stopPropagation();
                launchModuleExam(pb.id);
            };
            pagesList.appendChild(exBtn);
            card.appendChild(pagesList);
        }

        list.appendChild(card);
    });
}

function selectPlaybook(pbIdx, pageIdx) {
    const pb = PLAYBOOKS[pbIdx];
    if (!isPlaybookUnlocked(pb)) return;

    appState.currentPbIndex = pbIdx;
    appState.currentPageIndex = pageIdx || 0;
    currentPlaybook = pb;
    saveState();
    renderCurrentPage();
    window.scrollTo({ top: 0, behavior: "smooth" });
}

function renderCurrentPage() {
    const pb = currentPlaybook;
    const page = pb.pages[appState.currentPageIndex];

    document.getElementById("stage-pb-code").textContent = pb.code;
    document.getElementById("stage-pb-level").textContent = pb.level;
    document.getElementById("stage-pb-title").textContent = pb.title;
    document.getElementById("stage-page-counter").textContent = `Phase ${appState.currentPageIndex + 1} of ${pb.pages.length}`;

    // Render Phase Pills
    const pills = document.getElementById("phase-pills-container");
    pills.innerHTML = "";
    pb.pages.forEach((p, idx) => {
        const isDone = !!appState.completedPages[p.id];
        const isCurrent = idx === appState.currentPageIndex;
        const btn = document.createElement("button");
        btn.className = `px-3 py-1 rounded-full text-xs font-mono whitespace-nowrap transition-all ${
            isCurrent
                ? "bg-electric text-white font-bold shadow-[0_0_12px_rgba(59,130,246,0.5)]"
                : isDone
                ? "bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 hover:bg-emerald-500/25"
                : "bg-white/5 text-zinc-400 border border-white/10 hover:text-white"
        }`;
        btn.textContent = `${idx + 1}. ${p.phase.split('·')[0].trim()}`;
        btn.onclick = () => selectPlaybook(appState.currentPbIndex, idx);
        pills.appendChild(btn);
    });

    // Render Page Header & Takeaways
    document.getElementById("page-phase-tag").textContent = page.phase;
    document.getElementById("page-title").textContent = page.title;
    document.getElementById("page-tagline").textContent = page.tagline;

    const tkList = document.getElementById("page-takeaways");
    tkList.innerHTML = "";
    page.keyTakeaways.forEach(tk => {
        const li = document.createElement("li");
        li.textContent = tk;
        tkList.appendChild(li);
    });

    // Render Page HTML Content
    document.getElementById("page-body-content").innerHTML = page.content;

    // Update Bottom Nav Buttons
    document.getElementById("bottom-page-indicator").textContent = `Phase ${appState.currentPageIndex + 1} of ${pb.pages.length} · ${pb.code}`;
    const prevBtn = document.getElementById("btn-prev-page");
    prevBtn.disabled = appState.currentPageIndex === 0;
    prevBtn.style.opacity = appState.currentPageIndex === 0 ? "0.4" : "1";

    const nextBtn = document.getElementById("btn-next-page");
    if (appState.currentPageIndex === pb.pages.length - 1) {
        nextBtn.textContent = `🎓 Launch Playbook ${pb.number} Certification Exam →`;
    } else {
        nextBtn.textContent = `Complete Phase & Next (${appState.currentPageIndex + 2}/${pb.pages.length}) →`;
    }
}

function navigatePage(delta) {
    const newIdx = appState.currentPageIndex + delta;
    if (newIdx >= 0 && newIdx < currentPlaybook.pages.length) {
        selectPlaybook(appState.currentPbIndex, newIdx);
    }
}

function markPageCompletedAndNext() {
    const pb = currentPlaybook;
    const page = pb.pages[appState.currentPageIndex];

    if (!appState.completedPages[page.id]) {
        appState.completedPages[page.id] = true;
        appState.xp += 25;
        saveState();
    }

    // Check if there is a scheduled Pop Quiz triggered after this page (1-indexed page number)
    const pageNumber1Based = appState.currentPageIndex + 1;
    const scheduledQuiz = (pb.popQuizzes || []).find(q => q.triggerAfterPage === pageNumber1Based);

    if (scheduledQuiz && !appState.completedPages[scheduledQuiz.id]) {
        appState.completedPages[scheduledQuiz.id] = true;
        saveState();
        openPopQuizModal(scheduledQuiz, () => {
            advanceToNextPageOrExam();
        });
        return;
    }

    advanceToNextPageOrExam();
}

function advanceToNextPageOrExam() {
    const pb = currentPlaybook;
    if (appState.currentPageIndex < pb.pages.length - 1) {
        selectPlaybook(appState.currentPbIndex, appState.currentPageIndex + 1);
    } else {
        launchModuleExam(pb.id);
    }
}

function toggleOwnerMode() {
    appState.ownerMode = !appState.ownerMode;
    saveState();
}

function toggleSidebarMobile() {
    const sb = document.getElementById("app-sidebar");
    sb.classList.toggle("hidden");
    sb.classList.toggle("fixed");
    sb.classList.toggle("z-50");
}

// ============================================================================
// INTERACTIVE WIDGET CONTROLLERS
// ============================================================================
function selectImpressionNode(idx) {
    for (let i = 0; i < 4; i++) {
        const btn = document.getElementById(`imp-btn-${i}`);
        if (btn) btn.classList.toggle("active", i === idx);
    }
    const d = IMPRESSIONS_DATA[idx];
    document.getElementById("imp-d-badge").textContent = d.badge;
    document.getElementById("imp-d-title").textContent = d.title;
    document.getElementById("imp-d-desc").textContent = d.desc;
    document.getElementById("imp-d-list").innerHTML = d.list.map(x => `<span>${x}</span>`).join("");
    document.getElementById("imp-d-quote").textContent = d.quote;
    document.getElementById("imp-d-ttv").textContent = d.ttv;
    document.getElementById("imp-d-out").textContent = d.out;
}

function selectScenario(idx) {
    for (let i = 0; i < 5; i++) {
        const btn = document.getElementById(`scen-btn-${i}`);
        if (btn) btn.classList.toggle("active", i === idx);
    }
    const s = SCENARIO_MATCHER_DATA[idx];
    document.getElementById("scen-rec-title").textContent = s.title;
    document.getElementById("scen-rec-why").textContent = s.why;
    document.getElementById("scen-asc-title").textContent = s.ascTitle;
    document.getElementById("scen-asc-why").textContent = s.ascWhy;
    document.getElementById("scen-personas").innerHTML = s.personas.map(p => `<span>${p}</span>`).join("");
}

function updateROICalc() {
    const emp = parseInt(document.getElementById("calc-emp").value, 10);
    const hrs = parseInt(document.getElementById("calc-hrs").value, 10);
    const rate = parseInt(document.getElementById("calc-rate").value, 10);

    document.getElementById("calc-emp-val").textContent = emp;
    document.getElementById("calc-hrs-val").textContent = `${hrs} hrs`;
    document.getElementById("calc-rate-val").textContent = `$${rate}/hr`;

    const totalWeeklyHrs = emp * hrs;
    const annualHrs = totalWeeklyHrs * 52;
    const annualBleed = annualHrs * rate;
    const monthlyBleed = Math.round(annualBleed / 12);
    const recoverable = Math.round(annualBleed * 0.8);

    document.getElementById("calc-out-hrs").textContent = `${annualHrs.toLocaleString()} hrs/yr`;
    document.getElementById("calc-out-mo").textContent = `$${monthlyBleed.toLocaleString()} / month`;
    document.getElementById("calc-out-yr").textContent = `$${recoverable.toLocaleString()} / year`;
    document.getElementById("calc-out-script").textContent =
        `"So conservatively, across ${emp} staff losing ${hrs} hours a week at a $${rate}/hr burdened rate, leaving this process manual is costing you $${monthlyBleed.toLocaleString()} every single month—over $${annualBleed.toLocaleString()} a year in payroll drag alone."`;
}

function selectVerticalCard(idx) {
    for (let i = 0; i < 4; i++) {
        const b = document.getElementById(`vert-btn-${i}`);
        if (b) b.classList.toggle("active", i === idx);
    }
    const v = VERTICAL_CARDS[idx];
    document.getElementById("vert-pain-title").textContent = v.painTitle;
    document.getElementById("vert-pain-desc").textContent = v.painDesc;
    document.getElementById("vert-trig-title").textContent = v.trigTitle;
    document.getElementById("vert-trig-desc").textContent = v.trigDesc;
    document.getElementById("vert-wedge-title").textContent = v.wedgeTitle;
    document.getElementById("vert-wedge-desc").textContent = v.wedgeDesc;
}

function selectWorklistLead(idx) {
    for (let i = 0; i < 3; i++) {
        const b = document.getElementById(`wl-btn-${i}`);
        if (b) b.classList.toggle("active", i === idx);
    }
    const w = WORKLIST_LEADS[idx];
    document.getElementById("wl-sig-title").textContent = w.sigTitle;
    document.getElementById("wl-sig-desc").innerHTML = w.sigDesc;
    document.getElementById("wl-bad-hook").textContent = w.badHook;
    document.getElementById("wl-good-hook").textContent = w.goodHook;
}

function selectEmailTemplate(idx) {
    for (let i = 0; i < 5; i++) {
        const b = document.getElementById(`et-btn-${i}`);
        if (b) b.classList.toggle("active", i === idx);
    }
    const t = EMAIL_TEMPLATES[idx];
    document.getElementById("et-persona").textContent = t.persona;
    document.getElementById("et-subject").textContent = t.subject;
    document.getElementById("et-body").textContent = t.body;
    document.getElementById("et-why").innerHTML = `<strong>Why This Works:</strong> ${t.why}`;
}

function loadCallSimScenario(scenIdx) {
    const s = CALL_SIM_SCENARIOS[scenIdx];
    document.getElementById("call-sim-speaker").textContent = s.speaker;
    document.getElementById("call-sim-prompt").textContent = s.prompt;
    const opts = document.getElementById("call-sim-options");
    opts.innerHTML = s.options.map((o, i) =>
        `<button class="call-opt-btn" onclick="answerCallSim(${scenIdx}, ${i})">${o}</button>`
    ).join("");
    const fb = document.getElementById("call-sim-feedback");
    fb.classList.add("hidden");
}

function answerCallSim(scenIdx, choiceIdx) {
    const s = CALL_SIM_SCENARIOS[scenIdx];
    const fb = document.getElementById("call-sim-feedback");
    fb.classList.remove("hidden");
    if (choiceIdx === s.correct) {
        fb.className = "call-feedback bg-emerald-500/15 border border-emerald-500/40 text-emerald-200";
        fb.innerHTML = s.feedbackGood;
    } else {
        fb.className = "call-feedback bg-rose-500/15 border border-rose-500/40 text-rose-200";
        fb.innerHTML = s.feedbackBad;
    }
}

function selectNotebookMode(idx) {
    for (let i = 0; i < 3; i++) {
        const b = document.getElementById(`nb-btn-${i}`);
        if (b) b.classList.toggle("active", i === idx);
    }
    const n = NOTEBOOK_PROMPTS[idx];
    document.getElementById("nb-title").textContent = n.title;
    document.getElementById("nb-sources").textContent = n.sources;
    document.getElementById("nb-prompt").textContent = n.prompt;
}

function generateTalkTrack(idx) {
    for (let i = 0; i < 3; i++) {
        const b = document.getElementById(`tt-btn-${i}`);
        if (b) b.classList.toggle("active", i === idx);
    }
    document.getElementById("tt-output").textContent = TALK_TRACKS[idx];
}

function validateNexusCRMSim() {
    const s = document.getElementById("crm-stage").value;
    const p = document.getElementById("crm-pain").value;
    const b = document.getElementById("crm-buyers").value;
    const n = document.getElementById("crm-next").value;
    const fb = document.getElementById("crm-sim-feedback");
    fb.classList.remove("hidden");

    if (s === "s3" && p === "correct" && b === "correct" && n === "correct") {
        fb.className = "call-feedback bg-emerald-500/15 border border-emerald-500/40 text-emerald-200 mt-3";
        fb.innerHTML = "✅ <strong>100% NEXUS CRM DIAGNOSTIC COMPLIANCE!</strong> You logged the exact quantified annual bleed ($62,400/yr), mapped both the Champion (Elena) and Economic Buyer (Arthur), prescribed the Accelerator Tier with Single Agent wedge backup, and locked a concrete Dated Next Step (Thursday 2:00 PM ET Live Readout). +50 XP!";
        appState.xp += 50;
        saveState();
    } else {
        fb.className = "call-feedback bg-rose-500/15 border border-rose-500/40 text-rose-200 mt-3";
        fb.innerHTML = "❌ <strong>INCOMPLETE OR SLOPPY CRM RECORD:</strong> Check all 4 fields! Remember: Stage must advance to 'Stage 3: Discovery Completed → Readout Scheduled', Pain must be quantified ($62,400/yr), both Champion and Economic Buyer must be mapped, and a live Readout date must be locked.";
    }
}

// ============================================================================
// POP QUIZ ENGINE (2–3 RANDOM QUESTIONS)
// ============================================================================
let popQuizOnCloseCallback = null;

function triggerRandomPopQuiz() {
    // Draw 3 random questions from currentPlaybook's popQuizzes + finalExam pool
    const pool = [];
    (currentPlaybook.popQuizzes || []).forEach(pq => {
        pq.questions.forEach(q => pool.push(q));
    });
    currentPlaybook.finalExam.questions.forEach(q => pool.push(q));

    const shuffled = [...pool].sort(() => 0.5 - Math.random()).slice(0, 3);
    openPopQuizModal({
        title: `Random Spot-Check: ${currentPlaybook.code}`,
        questions: shuffled
    }, null);
}

function openPopQuizModal(quizObj, onCloseCb) {
    activePopQuiz = quizObj;
    popQuizOnCloseCallback = onCloseCb;

    document.getElementById("pq-title").textContent = quizObj.title;
    document.getElementById("pq-feedback-banner").classList.add("hidden");
    document.getElementById("pq-submit-btn").classList.remove("hidden");
    document.getElementById("pq-continue-btn").classList.add("hidden");

    const container = document.getElementById("pq-questions-container");
    container.innerHTML = quizObj.questions.map((q, qIdx) => `
        <div class="bg-charcoal/90 border border-white/10 rounded-xl p-4">
            <div class="text-xs font-mono text-gold mb-1">QUESTION 0${qIdx + 1}</div>
            <p class="text-sm font-semibold text-white mb-3">${q.q}</p>
            <div class="space-y-2">
                ${q.options.map((opt, oIdx) => `
                    <label class="flex items-start gap-2.5 p-2.5 rounded-lg bg-white/[0.03] hover:bg-white/[0.07] border border-white/5 cursor-pointer text-xs text-zinc-200">
                        <input type="radio" name="pq-q-${qIdx}" value="${oIdx}" class="mt-0.5 accent-electric" />
                        <span>${opt}</span>
                    </label>
                `).join("")}
            </div>
            <div id="pq-exp-${qIdx}" class="hidden mt-3 p-2.5 rounded-lg text-xs"></div>
        </div>
    `).join("");

    const modal = document.getElementById("pop-quiz-modal");
    modal.classList.remove("hidden");
    modal.classList.add("flex");
}

function submitPopQuiz() {
    if (!activePopQuiz) return;
    let correctCount = 0;
    const total = activePopQuiz.questions.length;

    for (let i = 0; i < total; i++) {
        const sel = document.querySelector(`input[name="pq-q-${i}"]:checked`);
        if (!sel) {
            alert(`Please select an answer for Question #${i + 1}.`);
            return;
        }
    }

    activePopQuiz.questions.forEach((q, i) => {
        const sel = parseInt(document.querySelector(`input[name="pq-q-${i}"]:checked`).value, 10);
        const expEl = document.getElementById(`pq-exp-${i}`);
        expEl.classList.remove("hidden");
        if (sel === q.correct) {
            correctCount++;
            expEl.className = "mt-3 p-2.5 rounded-lg text-xs bg-emerald-500/15 border border-emerald-500/40 text-emerald-200";
            expEl.innerHTML = `✓ <strong>Correct!</strong> ${q.explanation}`;
        } else {
            expEl.className = "mt-3 p-2.5 rounded-lg text-xs bg-rose-500/15 border border-rose-500/40 text-rose-200";
            expEl.innerHTML = `✕ <strong>Incorrect.</strong> Correct Answer: <em>${q.options[q.correct]}</em><br/>${q.explanation}`;
        }
    });

    appState.popQuizStats.taken += 1;
    appState.popQuizStats.correct += correctCount;
    appState.popQuizStats.total += total;
    appState.xp += correctCount * 20;
    saveState();

    const banner = document.getElementById("pq-feedback-banner");
    banner.classList.remove("hidden");
    banner.className = "mt-5 p-4 rounded-xl text-sm bg-electric/15 border border-electric/40 text-white";
    banner.innerHTML = `<strong>Spot-Check Score: ${correctCount} / ${total} (${Math.round((correctCount/total)*100)}%)</strong> · Earned +${correctCount * 20} XP!`;

    document.getElementById("pq-submit-btn").classList.add("hidden");
    document.getElementById("pq-continue-btn").classList.remove("hidden");
}

function closePopQuizModal() {
    const modal = document.getElementById("pop-quiz-modal");
    modal.classList.add("hidden");
    modal.classList.remove("flex");
    if (popQuizOnCloseCallback) {
        const cb = popQuizOnCloseCallback;
        popQuizOnCloseCallback = null;
        cb();
    }
}

// ============================================================================
// SCORED MODULE CERTIFICATION EXAM & EMAIL DISPATCH TO MARK BOCKRATH
// ============================================================================
function launchModuleExam(pbId) {
    const pb = PLAYBOOKS.find(p => p.id === pbId) || currentPlaybook;
    activeExamPlaybook = pb;

    document.getElementById("exam-badge").textContent = `${pb.code} · SCORED CERTIFICATION EXAM (${pb.finalExam.questions.length} QUESTIONS)`;
    document.getElementById("exam-title").textContent = pb.finalExam.title;
    document.getElementById("exam-results-panel").classList.add("hidden");
    document.getElementById("exam-questions-list").classList.remove("hidden");
    document.getElementById("exam-footer-controls").classList.remove("hidden");

    const qList = document.getElementById("exam-questions-list");
    qList.innerHTML = pb.finalExam.questions.map((q, idx) => `
        <div class="bg-tungsten/90 border border-white/10 rounded-xl p-5">
            <div class="flex items-center justify-between gap-2 mb-2">
                <span class="text-xs font-mono text-electric font-semibold">QUESTION ${idx + 1} OF ${pb.finalExam.questions.length}</span>
                <span class="text-[11px] font-mono px-2 py-0.5 rounded bg-white/5 text-zinc-400">Competency: ${q.category}</span>
            </div>
            <p class="text-base font-semibold text-white mb-4">${q.q}</p>
            <div class="space-y-2.5">
                ${q.options.map((opt, oIdx) => `
                    <label class="flex items-start gap-3 p-3 rounded-xl bg-charcoal/80 hover:bg-white/[0.06] border border-white/10 cursor-pointer text-sm text-zinc-200 transition-all">
                        <input type="radio" name="exam-q-${idx}" value="${oIdx}" class="mt-1 accent-electric" />
                        <span>${opt}</span>
                    </label>
                `).join("")}
            </div>
        </div>
    `).join("");

    const modal = document.getElementById("exam-modal");
    modal.classList.remove("hidden");
    modal.classList.add("flex");
    document.getElementById("exam-body-scroll").scrollTop = 0;
}

function closeExamModal() {
    const modal = document.getElementById("exam-modal");
    modal.classList.add("hidden");
    modal.classList.remove("flex");
}

function submitModuleExam() {
    const pb = activeExamPlaybook;
    const questions = pb.finalExam.questions;

    // Ensure all answered
    const userAnswers = [];
    for (let i = 0; i < questions.length; i++) {
        const checked = document.querySelector(`input[name="exam-q-${i}"]:checked`);
        if (!checked) {
            alert(`Please answer Question #${i + 1} before submitting your certification exam.`);
            return;
        }
        userAnswers.push(parseInt(checked.value, 10));
    }

    // Score & build category diagnostic matrix
    let correctCount = 0;
    const categoryStats = {};
    const missedDetails = [];

    questions.forEach((q, idx) => {
        if (!categoryStats[q.category]) {
            categoryStats[q.category] = { correct: 0, total: 0 };
        }
        categoryStats[q.category].total += 1;

        const isCorrect = userAnswers[idx] === q.correct;
        if (isCorrect) {
            correctCount += 1;
            categoryStats[q.category].correct += 1;
        } else {
            missedDetails.push({
                qNum: idx + 1,
                category: q.category,
                question: q.q,
                chosen: q.options[userAnswers[idx]],
                correctAnswer: q.options[q.correct],
                explanation: q.explanation
            });
        }
    });

    const pctScore = Math.round((correctCount / questions.length) * 100);
    const passed = pctScore >= pb.finalExam.passingScore;

    // Identify Keen Understanding vs. Coaching Needed
    const keenUnderstanding = [];
    const needsCoaching = [];
    Object.keys(categoryStats).forEach(cat => {
        const st = categoryStats[cat];
        const catPct = Math.round((st.correct / st.total) * 100);
        if (catPct >= 80) {
            keenUnderstanding.push(`${cat} (${catPct}% — ${st.correct}/${st.total})`);
        } else {
            needsCoaching.push(`${cat} (${catPct}% — ${st.correct}/${st.total})`);
        }
    });

    // Unlock next playbook!
    const currentIndexInAll = PLAYBOOKS.findIndex(p => p.id === pb.id);
    let nextPlaybookUnlockedName = null;
    if (currentIndexInAll >= 0 && currentIndexInAll + 1 < PLAYBOOKS.length) {
        const nextPb = PLAYBOOKS[currentIndexInAll + 1];
        if (!appState.unlockedPlaybooks.includes(nextPb.id)) {
            appState.unlockedPlaybooks.push(nextPb.id);
        }
        nextPlaybookUnlockedName = `${nextPb.code}: ${nextPb.title}`;
    }

    appState.xp += correctCount * 40 + (passed ? 200 : 50);

    // Build diagnostic report object
    const reportObj = {
        timestamp: new Date().toISOString(),
        aeName: appState.aeName || "New Senior AE (Unset Name)",
        aeEmail: appState.aeEmail || "Not Provided",
        playbookId: pb.id,
        playbookCode: pb.code,
        playbookTitle: pb.title,
        scorePct: pctScore,
        correctCount,
        totalQuestions: questions.length,
        passed,
        keenUnderstanding,
        needsCoaching,
        missedDetails,
        popQuizSummary: `${appState.popQuizStats.correct}/${appState.popQuizStats.total} correct across ${appState.popQuizStats.taken} pop quizzes`
    };

    appState.examHistory.unshift(reportObj);
    saveState();

    renderExamDiagnosticAndDispatch(reportObj, nextPlaybookUnlockedName, currentIndexInAll);
}

function buildEmailSubjectAndBody(report) {
    const statusTag = report.passed ? "PASSED" : "NEEDS REVIEW";
    const subject = `[MAB AI AE Exam - ${statusTag}] ${report.aeName} — ${report.playbookCode} (${report.scorePct}%)`;

    const keenText = report.keenUnderstanding.length > 0
        ? report.keenUnderstanding.map(x => `  • [KEEN UNDERSTANDING] ${x}`).join("\n")
        : "  • None >= 80% on this attempt";

    const coachText = report.needsCoaching.length > 0
        ? report.needsCoaching.map(x => `  • [NEEDS COACHING] ${x}`).join("\n")
        : "  • Zero weak categories! 100% category mastery.";

    const missedText = report.missedDetails.length > 0
        ? report.missedDetails.map(m =>
            `  Q${m.qNum} [${m.category}]: ${m.question}\n    - AE Answered: ${m.chosen}\n    - Correct Answer: ${m.correctAnswer}`
          ).join("\n\n")
        : "  • Perfect Score — 0 Missed Questions.";

    const body = `MARK BOCKRATH — MAB AI STRATEGIES AE TRAINING DIAGNOSTIC REPORT
==================================================================
Trainee Name: ${report.aeName}
Trainee Email: ${report.aeEmail}
Module Completed: ${report.playbookCode} — ${report.playbookTitle}
Timestamp: ${report.timestamp}

OVERALL EXAM SCORE: ${report.scorePct}% (${report.correctCount} / ${report.totalQuestions}) — ${statusTag}
Pop-Quiz Cumulative Accuracy: ${report.popQuizSummary}

1. WHERE THE AE HAS A KEEN UNDERSTANDING (STRENGTHS >= 80%):
${keenText}

2. WHERE THE AE NEEDS ADDITIONAL HELP / COACHING (< 80%):
${coachText}

3. QUESTION-BY-QUESTION MISSED DIAGNOSTIC LOG:
${missedText}
==================================================================
Generated by MAB AI Strategies Agentic Sales Academy`;

    return { subject, body };
}

function renderExamDiagnosticAndDispatch(report, nextUnlockedName, currentIdx) {
    document.getElementById("exam-questions-list").classList.add("hidden");
    document.getElementById("exam-footer-controls").classList.add("hidden");

    const panel = document.getElementById("exam-results-panel");
    panel.classList.remove("hidden");

    const { subject, body } = buildEmailSubjectAndBody(report);
    const mailtoHref = `mailto:mark@mabaistrategies.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    const gmailHref = `https://mail.google.com/mail/?view=cm&fs=1&to=mark@mabaistrategies.com&su=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;

    panel.innerHTML = `
        <div class="p-6 rounded-2xl border ${report.passed ? 'bg-emerald-500/10 border-emerald-500/40' : 'bg-amber-500/10 border-amber-500/40'}">
            <div class="flex flex-wrap items-center justify-between gap-4">
                <div>
                    <span class="text-xs font-mono uppercase tracking-wider ${report.passed ? 'text-emerald-400' : 'text-amber-400'}">
                        ${report.passed ? '✓ CERTIFICATION ACHIEVED & NEXT MODULE UNLOCKED' : '⚠️ MODULE COMPLETED — COACHING RECOMMENDED'}
                    </span>
                    <h4 class="font-serif text-3xl text-white mt-1">
                        Score: ${report.scorePct}% (${report.correctCount} / ${report.totalQuestions})
                    </h4>
                    ${nextUnlockedName ? `<p class="text-sm text-emerald-300 mt-1">🔓 Unlocked: <strong>${nextUnlockedName}</strong></p>` : ''}
                </div>
                <div class="flex flex-wrap gap-2">
                    ${currentIdx + 1 < PLAYBOOKS.length ? `
                        <button onclick="closeExamModal(); selectPlaybook(${currentIdx + 1}, 0);" class="px-5 py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-600 text-charcoal font-bold text-xs transition-all">
                            Proceed to Playbook ${currentIdx + 1} →
                        </button>
                    ` : ''}
                    <button onclick="launchModuleExam('${report.playbookId}')" class="px-4 py-2.5 rounded-xl bg-white/10 hover:bg-white/15 text-white text-xs font-medium">
                        Retake Exam
                    </button>
                </div>
            </div>
        </div>

        <!-- Executive Email Dispatch Box to mark@mabaistrategies.com -->
        <div class="bg-zinc-900 border border-electric/40 rounded-2xl p-5">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <div>
                    <span class="badge-electric">AUTOMATIC OWNER TELEMETRY DISPATCH</span>
                    <h5 class="text-base font-bold text-white mt-1">Send Diagnostic Results to Mark Bockrath (mark@mabaistrategies.com)</h5>
                </div>
                <span class="text-xs font-mono text-emerald-400">✓ Report Compiled & Saved Locally</span>
            </div>
            <p class="text-xs text-zinc-400 mb-4">
                Click below to transmit this exact diagnostic breakdown (Keen Understanding vs. Coaching Needed) directly to <code class="text-electric">mark@mabaistrategies.com</code> via your preferred zero-cost mail client:
            </p>
            <div class="flex flex-wrap gap-2.5 mb-4">
                <a href="${mailtoHref}" class="px-4 py-2.5 rounded-xl bg-electric hover:bg-electricDark text-white text-xs font-bold inline-flex items-center gap-1.5 shadow-lg">
                    📧 Send via Default Email App (mark@mabaistrategies.com)
                </a>
                <a href="${gmailHref}" target="_blank" class="px-4 py-2.5 rounded-xl bg-white/10 hover:bg-white/15 border border-white/15 text-white text-xs font-semibold inline-flex items-center gap-1.5">
                    📨 Open in Gmail Web Compose
                </a>
                <button onclick="copyLatestReportText()" class="px-4 py-2.5 rounded-xl bg-white/5 hover:bg-white/10 border border-white/15 text-zinc-200 text-xs font-mono">
                    📋 Copy Report Text
                </button>
            </div>
            <pre id="latest-report-pre" class="email-body-pre max-h-56 overflow-y-auto">${body}</pre>
        </div>

        <!-- Diagnostic Breakdown: Keen Understanding vs Needs Coaching -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-emerald-500/5 border border-emerald-500/30 rounded-xl p-4">
                <h5 class="text-sm font-bold text-emerald-400 mb-2">🟢 Keen Understanding (80–100% Mastery)</h5>
                <ul class="text-xs text-zinc-200 space-y-1.5 list-disc pl-4">
                    ${report.keenUnderstanding.length > 0
                        ? report.keenUnderstanding.map(k => `<li>${k}</li>`).join("")
                        : "<li>Review module phases to build category mastery above 80%.</li>"}
                </ul>
            </div>
            <div class="bg-rose-500/5 border border-rose-500/30 rounded-xl p-4">
                <h5 class="text-sm font-bold text-rose-400 mb-2">🔴 Needs Additional Help / Coaching (&lt;80%)</h5>
                <ul class="text-xs text-zinc-200 space-y-1.5 list-disc pl-4">
                    ${report.needsCoaching.length > 0
                        ? report.needsCoaching.map(c => `<li>${c}</li>`).join("")
                        : "<li>Zero weak categories—outstanding command of every phase in this Playbook!</li>"}
                </ul>
            </div>
        </div>
    `;

    // Trigger mailto automatically so Mark receives the email at the end of every test
    setTimeout(() => {
        window.location.href = mailtoHref;
    }, 400);
}

function copyLatestReportText() {
    const pre = document.getElementById("latest-report-pre");
    if (!pre) return;
    navigator.clipboard.writeText(pre.textContent).then(() => {
        alert("✓ Diagnostic report copied to clipboard! Ready to paste to mark@mabaistrategies.com.");
    });
}

// ============================================================================
// PROFILE & TELEMETRY DASHBOARD
// ============================================================================
function openProfileModal() {
    openTelemetryDashboard();
}

function openTelemetryDashboard() {
    document.getElementById("prof-name-input").value = appState.aeName || "";
    document.getElementById("prof-email-input").value = appState.aeEmail || "";

    const container = document.getElementById("dashboard-history-container");
    if (appState.examHistory.length === 0) {
        container.innerHTML = `
            <div class="p-6 rounded-xl bg-zinc-900/60 border border-white/10 text-center text-sm text-zinc-400">
                No module certification tests completed yet. Complete Playbook 0 and take the 12-question exam to generate your first diagnostic report for Mark Bockrath.
            </div>
        `;
    } else {
        container.innerHTML = appState.examHistory.map((rep, idx) => {
            const { subject, body } = buildEmailSubjectAndBody(rep);
            const mailto = `mailto:mark@mabaistrategies.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
            return `
                <div class="p-4 rounded-xl bg-zinc-900/90 border border-white/10 flex flex-col gap-2">
                    <div class="flex flex-wrap justify-between items-center gap-2">
                        <div>
                            <span class="text-xs font-mono text-electric font-bold">${rep.playbookCode}</span>
                            <span class="text-sm font-semibold text-white ml-2">${rep.playbookTitle}</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <span class="px-2.5 py-0.5 rounded text-xs font-mono font-bold ${rep.passed ? 'bg-emerald-500/20 text-emerald-300' : 'bg-amber-500/20 text-amber-300'}">
                                ${rep.scorePct}% (${rep.correctCount}/${rep.totalQuestions})
                            </span>
                            <a href="${mailto}" class="px-3 py-1 rounded bg-electric hover:bg-electricDark text-white text-xs font-semibold">
                                📧 Email Mark
                            </a>
                        </div>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs mt-1">
                        <div class="text-emerald-300"><strong>Strengths:</strong> ${rep.keenUnderstanding.join(", ") || "None"}</div>
                        <div class="text-rose-300"><strong>Needs Coaching:</strong> ${rep.needsCoaching.join(", ") || "None (100% Mastery)"}</div>
                    </div>
                </div>
            `;
        }).join("");
    }

    const modal = document.getElementById("dashboard-modal");
    modal.classList.remove("hidden");
    modal.classList.add("flex");
}

function closeDashboardModal() {
    const modal = document.getElementById("dashboard-modal");
    modal.classList.add("hidden");
    modal.classList.remove("flex");
}

function saveTraineeProfile() {
    appState.aeName = document.getElementById("prof-name-input").value.trim();
    appState.aeEmail = document.getElementById("prof-email-input").value.trim();
    saveState();
    alert("✓ Senior Account Executive profile saved!");
}

function emailMasterRollupToMark() {
    const subject = `[MAB AI Master Transcript] ${appState.aeName || 'New Sr. AE'} — ${appState.examHistory.length} Exams Logged`;
    const body = appState.examHistory.length > 0
        ? appState.examHistory.map(r => buildEmailSubjectAndBody(r).body).join("\n\n")
        : "No exams taken yet.";
    window.location.href = `mailto:mark@mabaistrategies.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
}

function downloadMasterTranscriptJSON() {
    const blob = new Blob([JSON.stringify(appState, null, 2)], { type: "application/json" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `mab_ai_ae_telemetry_${(appState.aeName || 'trainee').replace(/\s+/g, '_').toLowerCase()}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

// Initialize App on Load
window.addEventListener("DOMContentLoaded", () => {
    loadState();
    currentPlaybook = PLAYBOOKS[appState.currentPbIndex] || PLAYBOOKS[0];
    updateHeaderStats();
    renderSidebar();
    renderCurrentPage();
});
</script>
</body>
</html>
"""

def main():
    playbooks_json = json.dumps(ALL_PLAYBOOKS, ensure_ascii=False)
    final_html = HTML_TEMPLATE.replace("__PLAYBOOKS_JSON__", playbooks_json)
    out_path = "/Users/mabaistrategies/Desktop/Sales Playbook/index.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    total_pages = sum(len(pb["pages"]) for pb in ALL_PLAYBOOKS)
    total_exam_qs = sum(len(pb["finalExam"]["questions"]) for pb in ALL_PLAYBOOKS)
    total_pop_qs = sum(sum(len(pq["questions"]) for pq in pb.get("popQuizzes", [])) for pb in ALL_PLAYBOOKS)
    print(f"Successfully built {out_path}")
    print(f"Total Playbooks: {len(ALL_PLAYBOOKS)} (Playbooks 0 to 10)")
    print(f"Total Dense Phases/Pages: {total_pages}")
    print(f"Total Scored Exam Questions: {total_exam_qs}")
    print(f"Total Pop Quiz Questions: {total_pop_qs}")
    print(f"File Size: {os.path.getsize(out_path) / 1024:.1f} KB")

if __name__ == "__main__":
    main()
