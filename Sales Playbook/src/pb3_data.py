# -*- coding: utf-8 -*-
"""
PLAYBOOK 3: THE MEETING — MASTERING THE DISCOVERY MEETING
18 Dense Pages | Interactive Gemini Notebook Studio, Talk Track Builder & Nexus CRM Simulator
Random Pop Quizzes | 12-Question Scored Certification Exam
"""

PLAYBOOK_3 = {
    "id": "pb3",
    "number": 3,
    "code": "PLAYBOOK 03",
    "title": "The Meeting: Mastering the 30-Minute Discovery Briefing",
    "subtitle": "AI Reconnaissance, Gemini Notebook Strategy, 'Find the Pain', Custom Talk Tracks, The 80/20 Rule, Sales Triggers, Nexus CRM Logging & When to Talk Numbers",
    "level": "INDIVIDUAL AE EXECUTION · LIVE DISCOVERY",
    "duration": "120 Mins · 6 Phases (18 Pages) · Nexus CRM Sandbox & AI Prep Lab · 12-Q Exam",
    "unlockRequirement": "pb2",
    "overview": "You booked the 30-Minute Strategic Briefing. Now the real money is made or lost. Playbook 3 teaches you how to use AI and Gemini Notebook to know a prospect's business better than they do before the Zoom even starts, how to 'Find the Pain' and price it, how to generate a custom talk track, how to enforce the 80/20 listening rule, how to spot verbal sales triggers, how to log everything in Nexus CRM, how to execute the Post-Meeting Checklist, and exactly when (and how) to talk numbers.",
    "pages": [
        # =====================================================================
        # PHASE 3A: HOW TO PREPARE FOR THE MEETING — AI RESEARCH (3 PAGES)
        # =====================================================================
        {
            "id": "pb3-p1",
            "phase": "PHASE 3A · PRE-MEETING AI RECONNAISSANCE (PAGE 1 OF 3)",
            "title": "Why Showing Up Unprepared Is a Fireable Offense",
            "tagline": "If you ever start a Discovery Call at MAB AI Strategies by asking 'So, tell me what your company does,' you just murdered the deal.",
            "keyTakeaways": [
                "Asking basic firmographic questions you could have researched in 3 minutes insults an executive's time and destroys your authority.",
                "Our standard: Show up knowing their business model, their customer profile, their software stack, their open job reqs, and their top 3 likely operational bottlenecks BEFORE minute one.",
                "When you open a meeting by proving you did surgical homework, the executive instantly drops their guard and treats you as a peer advisor."
            ],
            "content": """
                <div class="prose-section">
                    <div class="founder-note">
                        <div class="founder-badge">DIRECTIVE FROM MARK BOCKRATH · THE D1 PREP STANDARD</div>
                        <p>"In Division 1 basketball, you don't show up at tip-off and ask the ref whether the opposing point guard is left-handed. You watched 6 hours of game tape, you know his crossover tendencies, and you take away his strong hand on possession #1. In B2B AI sales, showing up to a 30-minute briefing and asking 'So what does your company do?' is pure laziness. We represent an AI intelligence firm—if you don't use AI to prepare for the meeting, why the hell should they pay us to build AI for them?"</p>
                    </div>

                    <h3>The 2-Minute Authority Contrast</h3>
                    <div class="comparison-grid">
                        <div class="comp-card comp-bad">
                            <h4>❌ The Lazy Rep (Dead in 90 Seconds)</h4>
                            <p><em>"Thanks for joining, Sarah! So to kick things off, tell me a little bit about Acme Logistics and what you guys do?"</em><br/><br/>
                            <strong>Sarah's Brain:</strong> "Are you kidding me? You cold-emailed me three times begging for 30 minutes and you didn't even read our homepage? I'm ending this call in 10 minutes."</p>
                        </div>
                        <div class="comp-card comp-good">
                            <h4>✅ The MAB AI Prepared Architect (Instant Respect)</h4>
                            <p><em>"Sarah, excited to dive in. Before we hopped on, I mapped out Acme's footprint—saw you've scaled to 110 employees across 3 regional hubs, running McLeod ERP alongside HubSpot, and currently have 3 open reqs for Freight Billing Coordinators. Usually when we see that exact setup, carrier invoice reconciliation and dispatch handoffs are eating 20+ hours a week. How close am I to the bullseye?"</em><br/><br/>
                            <strong>Sarah's Brain:</strong> "Holy shit, this person actually understands our business. Let me tell them everything."</p>
                        </div>
                    </div>
                </div>
            """
        },
        {
            "id": "pb3-p2",
            "phase": "PHASE 3A · PRE-MEETING AI RECONNAISSANCE (PAGE 2 OF 3)",
            "title": "The 15-Minute AI Research Protocol: Knowing Their Business Better Than They Do",
            "tagline": "How to combine Perplexity, Briefing Bot GEM, LinkedIn, and Job Boards to build a surgical Executive Dossier in 15 minutes flat.",
            "keyTakeaways": [
                "Minute 0–4 (Perplexity / Web): Extract business model, pricing model, recent news, M&A, and key competitors.",
                "Minute 4–8 (LinkedIn + Job Boards): Audit departmental headcount ratios and read every bullet point of their open job descriptions (job descriptions literally list their manual processes!).",
                "Minute 8–12 (Apollo + Reviews): Check tech stack tags and scan Glassdoor/G2/Google reviews for complaints about 'slow onboarding', 'manual paperwork', or 'poor communication'.",
                "Minute 12–15 (Briefing Bot GEM): Synthesize into a 1-page Pre-Call Dossier."
            ],
            "content": """
                <div class="prose-section">
                    <h3>Why Open Job Descriptions Are Secret Blueprints of Their Chaos</h3>
                    <p>Want to know how to know a prospect's internal workflows better than their own CEO does? <strong>Read the bullet points of their active or recent job postings on LinkedIn/Indeed.</strong></p>
                    <p>When an Operations Manager writes a job description for an Administrative Coordinator, they literally type out a confession of every manual, un-automated task in their company:</p>
                    <ul>
                        <li><em>"Responsible for downloading daily PDF orders from inbox and entering line items into NetSuite..."</em> → <strong>BOOM: Receipt/Document Scraper + ERP Workflow!</strong></li>
                        <li><em>"Screen incoming resumes in Greenhouse, send scheduling links, and follow up on background check forms..."</em> → <strong>BOOM: Autonomous Vetting & Onboarding Agent!</strong></li>
                        <li><em>"Compile weekly KPI spreadsheets from HubSpot and QuickBooks for Monday leadership meetings..."</em> → <strong>BOOM: Real-Time Data Synthesis Dashboard + Weekly Report Automation!</strong></li>
                    </ul>

                    <h3>Copy-Paste Deep Reconnaissance Prompt (Perplexity / Claude / GPT-4)</h3>
                    <pre class="email-body-pre">Act as Mark Bockrath's Senior Enterprise AI Architect at MAB AI Strategies. I have a 30-Minute Strategic Briefing with [Prospect Name, Title] at [Company Name] ([Website URL]) in 20 minutes.

Analyze their public footprint, industry vertical, job postings, and business model, and generate a 1-Page Executive Reconnaissance Brief:
1. REVENUE ENGINE: How exactly do they make money, what is their approximate deal size, and where do margins get squeezed in their vertical?
2. LIKELY WORKFLOW CHAOS: What are the top 3 repetitive manual workflows, lagging handoffs, or data silos a company of their size ([X] employees) in [Vertical] faces every week?
3. THE IMPRESSIONS LAYER FIT: Which specific MAB AI modules (AI Readiness Audit, Single Agent/Workflow, Foundation/Accelerator/Principal Retainer) and Intelligence Library templates (e.g., Onboarding Bot, Invoice Chaser, Lead Enricher, Support Triage Agent) map directly to their operation?
4. 5 SURGICAL DISCOVERY QUESTIONS: Give me 5 high-status, diagnostic questions tailored to [Prospect Title] that expose hourly and financial drag.</pre>
                </div>
            """
        },
        {
            "id": "pb3-p3",
            "phase": "PHASE 3A · PRE-MEETING AI RECONNAISSANCE (PAGE 3 OF 3)",
            "title": "Entering Every Call With 3 Educated Hypotheses",
            "tagline": "Never walk into a meeting empty-handed. Walk in with 3 specific hypotheses to test.",
            "keyTakeaways": [
                "Executives hate educating salespeople from scratch, but they LOVE correcting or validating an educated hypothesis.",
                "Even if your hypothesis is 20% off, the executive will immediately correct you with the exact truth ('Actually, it's not billing that's killing us right now—it's subcontractor compliance tracking').",
                "Always prepare Hypothesis A (Front-Office/Revenue), Hypothesis B (Mid-Office/Delivery & Ops), and Hypothesis C (Back-Office/Finance & Admin)."
            ],
            "content": """
                <div class="prose-section">
                    <h3>Cunningham's Law Applied to B2B Discovery</h3>
                    <p>There is an old rule on the internet called Cunningham's Law: <em>"The fastest way to get the right answer is not to ask a question—it is to state a specific hypothesis so someone corrects you."</em></p>
                    <p>When you ask a CEO a lazy open question like, <em>"Where could you use automation?"</em>, their brain freezes because the question is too broad. When you state a sharp hypothesis—<em>"Based on your growth from 40 to 75 employees this year, my hypothesis is that either client onboarding handoffs from Sales to Ops are lagging, or monthly reporting is eating up 15+ hours a week—which of those is closer to reality?"</em>—they immediately open the vault.</p>
                </div>
            """
        },

        # =====================================================================
        # PHASE 3B: USING GEMINI NOTEBOOK STRATEGICALLY (2 PAGES)
        # =====================================================================
        {
            "id": "pb3-p4",
            "phase": "PHASE 3B · GEMINI NOTEBOOK STRATEGY (PAGE 1 OF 2)",
            "title": "Using Gemini Notebook (NotebookLM) Strategically as Your Deal War Room",
            "tagline": "Turn scattered prospect links, transcripts, PDFs, and notes into a grounded, zero-hallucination Deal Brain.",
            "keyTakeaways": [
                "Why Gemini Notebook (NotebookLM) is a game-changer for Senior AEs: Unlike open web chatbots that mix in random internet noise, Gemini Notebook ONLY reasons over the exact sources you upload into that prospect's notebook.",
                "Create one dedicated Notebook per qualified mid-market/enterprise Opportunity (named: '[Account Name] — MAB AI Deal Room').",
                "Ingest 5 core source types before Discovery and keep adding call transcripts through Proposal and Close."
            ],
            "content": """
                <div class="prose-section">
                    <h3>Why Gemini Notebook Is Your Unfair Advantage</h3>
                    <p>Most salespeople have prospect research scattered across 14 browser tabs, a messy notepad, and half-remembered emails. At MAB AI Strategies, we use <strong>Gemini Notebook (NotebookLM)</strong> to create a dedicated, source-grounded AI War Room for every qualified prospect.</p>

                    <div class="module-cards-grid">
                        <div class="spec-card">
                            <div class="spec-num">SOURCE 01 · WEBSITE & SERVICES</div>
                            <h4>Ingest Their Core URLs</h4>
                            <p>Paste the prospect's homepage, About page, Services/Product pages, and Case Studies URLs directly into the Gemini Notebook so it understands their exact nomenclature.</p>
                        </div>
                        <div class="spec-card">
                            <div class="spec-num">SOURCE 02 · JOB DESCRIPTIONS & LINKEDIN</div>
                            <h4>Paste Job Reqs & Exec Bios</h4>
                            <p>Copy-paste the text of their last 3–5 job postings and the LinkedIn "About / Experience" sections of the executives attending the call.</p>
                        </div>
                        <div class="spec-card">
                            <div class="spec-num">SOURCE 03 · MAB AI CAPABILITY MATRIX</div>
                            <h4>Include Our Offerings Doc</h4>
                            <p>Keep a standard source doc of MAB AI Strategies' tiers (Audit, Single Agent, Foundation, Accelerator, Principal) and our 250+ Automation Library inside the notebook so Gemini can map their exact pains to our exact SKU.</p>
                        </div>
                        <div class="spec-card">
                            <div class="spec-num">SOURCE 04 · CALL TRANSCRIPTS & EMAILS</div>
                            <h4>Compound the Intelligence</h4>
                            <p>After Discovery, drop the Zoom transcript into the same Notebook. Now you can query the exact quotes, numbers, and objections the CEO said at minute 14:22 to build a bulletproof Proposal!</p>
                        </div>
                    </div>
                </div>
            """
        },
        {
            "id": "pb3-p5",
            "phase": "PHASE 3B · GEMINI NOTEBOOK STRATEGY (PAGE 2 OF 2)",
            "title": "Interactive Gemini Notebook Prompt Studio & Audio Overview Hack",
            "tagline": "Use the Audio Overview 10 minutes before the call, and run these exact prompts inside Gemini Notebook.",
            "keyTakeaways": [
                "The 6-Minute Audio Overview Hack: Generate a Gemini Notebook Audio Overview of the prospect's sources and listen to it at 1.5x speed while grabbing coffee before the Zoom call—you'll enter the room with total conversational fluency.",
                "Use the interactive Gemini Notebook Prompt Studio below to generate pre-call and post-call war-room outputs."
            ],
            "content": """
                <div class="prose-section">
                    <div class="infographic-box" id="gemini-notebook-box">
                        <div class="infographic-header">
                            <div>
                                <span class="badge-electric">INTERACTIVE GEMINI NOTEBOOK STUDIO</span>
                                <h4>STRATEGIC NOTEBOOKLM WORKFLOWS FOR SENIOR AEs</h4>
                            </div>
                            <span class="text-xs font-mono text-zinc-400">SELECT WORKFLOW STAGE TO GENERATE EXACT NOTEBOOK PROMPT</span>
                        </div>

                        <div class="scenario-btn-grid">
                            <button class="scen-btn active" onclick="selectNotebookMode(0)" id="nb-btn-0">1. Pre-Call Operational Leak Finder</button>
                            <button class="scen-btn" onclick="selectNotebookMode(1)" id="nb-btn-1">2. Persona-Specific Question Generator</button>
                            <button class="scen-btn" onclick="selectNotebookMode(2)" id="nb-btn-2">3. Post-Discovery Transcript → ROI Extractor</button>
                        </div>

                        <div class="email-preview-card">
                            <div class="email-meta">
                                <div><strong>Notebook Workflow:</strong> <span id="nb-title" class="text-electric">Pre-Call Operational Leak & Taxonomy Mapper</span></div>
                                <div><strong>Sources Loaded:</strong> <span id="nb-sources" class="font-mono text-gold">Prospect Site URLs + 3 Open Job Postings + Exec LinkedIn Profiles</span></div>
                            </div>
                            <pre class="email-body-pre" id="nb-prompt">Based strictly on the uploaded company pages, job descriptions, and executive profiles:
1. Identify every manual process, cross-departmental handoff, or software tool mentioned in their job postings.
2. What internal terminology do they use for their customers, projects, and deliverables?
3. Formulate 3 specific hypotheses for where their team is losing 10–20+ hours per week in operational drag.
4. Map each hypothesis to the exact MAB AI Strategies solution (AI Readiness Audit, Single Agent, or Accelerator Retainer) and give me a 30-second opening frame for the call.</pre>
                            <div class="email-why" id="nb-tip">
                                <strong>🔥 Pro Hack — Audio Overview Prep:</strong> Click "Generate Audio Overview" in Gemini Notebook 15 minutes before tip-off. Listening to two AI hosts dissect the prospect's business model for 5 minutes primes your brain to speak their exact industry language naturally.
                            </div>
                        </div>
                    </div>
                </div>
            """
        },

        # =====================================================================
        # PHASE 3C: 'FIND THE PAIN' (3 PAGES)
        # =====================================================================
        {
            "id": "pb3-p6",
            "phase": "PHASE 3C · 'FIND THE PAIN' (PAGE 1 OF 3)",
            "title": "'Find the Pain': Why Surface Complaints Never Close Deals",
            "tagline": "No pain, no change. If you only uncover a minor annoyance, they will ghost you after the call. You must excavate down to the financial and personal bone.",
            "keyTakeaways": [
                "Level 1 (Surface Symptom): 'Our onboarding process is a bit slow.' -> Worth $0. Nobody signs a contract over 'a bit slow.'",
                "Level 2 (Quantified Operational Pain): '3 coordinators spend 6 hours a week each manually chasing onboarding docs across 4 systems, costing $58,000/yr and delaying revenue recognition by 11 days.' -> Worth a serious look.",
                "Level 3 (Executive / Personal Impact): 'If we don't fix our gross margin by 4% before Q4, our PE board is freezing our expansion bonus and halting new hires.' -> Deal closes in 7 days."
            ],
            "content": """
                <div class="prose-section">
                    <h3>The 3 Levels of Pain Excavation</h3>
                    <p>When you ask a prospect what's wrong, their first answer is always a polite, surface-level platitude: <em>"Yeah, we're trying to be more efficient with our data."</em></p>
                    <p>Rookie salespeople hear the word "data" and immediately jump into pitching: <em>"Awesome! We build Real-Time Data Synthesis dashboards with PostgreSQL!"</em> <strong>STOP!</strong> You haven't found the pain yet—you found a symptom.</p>
                    <p>To <strong>Find the Pain</strong>, you must drill down through three distinct geological layers before you ever mention our solution:</p>

                    <div class="tier-grid-3">
                        <div class="tier-card">
                            <div class="tier-badge">LAYER 01 · SURFACE SYMPTOM</div>
                            <h4>"What Is Happening?"</h4>
                            <p class="tier-desc">The technical or process annoyance: <em>"Our reps take too long to update the CRM and send proposals."</em></p>
                            <div class="tier-when"><strong>If you stop here:</strong> The prospect thinks it's a minor inconvenience and delays for 6 months.</div>
                        </div>
                        <div class="tier-card tier-featured">
                            <div class="tier-badge">LAYER 02 · FINANCIAL BLEED</div>
                            <h4>"What Does It Cost in Hours & Dollars?"</h4>
                            <p class="tier-desc">The hard math: <em>"8 reps × 5 hrs/wk = 40 hrs/wk of lost selling time ($145K/yr payroll drag), plus slow proposals drop our close rate from 28% to 19%."</em></p>
                            <div class="tier-when"><strong>Why this matters:</strong> Gives the CFO the mathematical justification to approve budget.</div>
                        </div>
                        <div class="tier-card">
                            <div class="tier-badge">LAYER 03 · PERSONAL STAKES</div>
                            <h4>"What Happens to YOU If This Doesn't Change?"</h4>
                            <p class="tier-desc">The emotional & career driver: <em>"I'm working 65 hours a week babysitting this, and if we miss Q3 targets, my board is breathing down my neck."</em></p>
                            <div class="tier-when"><strong>Why this matters:</strong> Creates unstoppable urgency to act <em>this week</em>.</div>
                        </div>
                    </div>
                </div>
            """
        },
        {
            "id": "pb3-p7",
            "phase": "PHASE 3C · 'FIND THE PAIN' (PAGE 2 OF 3)",
            "title": "The 5-Step Pain Funnel Question Sequence",
            "tagline": "Memorize these 5 follow-up questions. They turn a 1-sentence answer into a $50,000 business case.",
            "keyTakeaways": [
                "Question 1 (Walkthrough): 'Walk me through how [Workflow X] happens today from start to finish—what happens first, and where does it get handed off?'",
                "Question 2 (Frequency & Volume): 'How many times a week does that happen, and how many minutes/hours does each one take manually?'",
                "Question 3 (Failure / Error Rate): 'How often does something get dropped, delayed, or keyed in wrong during that handoff?'",
                "Question 4 (Financial Quantification): 'So if 3 people are spending 15 hours a week on that, that's roughly $75K–$90K a year in payroll drag alone—does that math sound right to you?'",
                "Question 5 (Duration & Priority): 'How long has this been going on, and what happens over the next 6 months if you scale volume by 30% without fixing it?'"
            ],
            "content": """
                <div class="prose-section">
                    <h3>How to Drill Down Without Sounding Like an Interrogator</h3>
                    <p>The secret to great Discovery is <strong>genuine diagnostic curiosity</strong>. When a prospect mentions a manual bottleneck, use this exact 5-step sequence to unpack it:</p>

                    <div class="script-block">
                        <div class="script-stage">1. THE PROCESS X-RAY ("WALK ME THROUGH...")</div>
                        <p><strong>YOU:</strong> "When a new client signs [or candidate applies / order comes in], walk me through the exact steps that happen behind the scenes today. Who touches it first, what tools do they open, and who do they hand it to next?"</p>

                        <div class="script-stage">2. THE VOLUME & TIME MULTIPLIER</div>
                        <p><strong>YOU:</strong> "Got it—so Sarah's team downloads the PDF, keys it into the CRM, and slacks Finance. How many times a week is your team running that play, and roughly how many hours a week does that eat up across the team?"</p>

                        <div class="script-stage">3. THE FRICTION & ERROR COST</div>
                        <p><strong>YOU:</strong> "And when the team gets slammed on a busy week, where does that process usually break or lag? Are balls getting dropped on response time, or are mistakes sneaking into billing?"</p>

                        <div class="script-stage">4. THE LIVE MATH CONFIRMATION</div>
                        <p><strong>YOU:</strong> "Let me check my napkin math with you: 15 hours a week across two senior coordinators is 780 hours a year—plus the management time you spend double-checking it. At a fully burdened cost, that single manual workflow is quietly burning $40,000 to $50,000 a year. Does that sound conservative or about right?"</p>

                        <div class="script-stage">5. THE FUTURE BREAKING POINT</div>
                        <p><strong>YOU:</strong> "You mentioned your goal is to grow revenue 25% over the next 12 months. If you hit that growth target on top of this manual process without automating it, what breaks first—do you have to hire two more headcount, or does client delivery suffer?"</p>
                    </div>
                </div>
            """
        },
        {
            "id": "pb3-p8",
            "phase": "PHASE 3C · 'FIND THE PAIN' (PAGE 3 OF 3)",
            "title": "Diagnosing the 4 Core Leaks of 'The Impressions Layer'",
            "tagline": "Categorize every pain you hear on the call into one of our 4 architectural buckets.",
            "keyTakeaways": [
                "Bucket 1: Repetitive Human-API Tasks (copy-pasting, data entry, screening, formatting).",
                "Bucket 2: Lagging Inter-Departmental Handoffs (Sales -> Ops, Recruiting -> HR, Ops -> Billing).",
                "Bucket 3: Data Rotting in Silos (no unified KPI dashboard, manual Friday Excel rollups, zero RAG search).",
                "Bucket 4: After-Hours / Speed-to-Lead Gaps (leads or tickets waiting 12+ hours overnight for a human to wake up)."
            ],
            "content": """
                <div class="prose-section">
                    <h3>Your Diagnostic Mental Checklist During Discovery</h3>
                    <p>While the prospect is talking, your notepad (and Nexus CRM record) should be divided into these 4 leak categories. The moment you uncover 2 or 3 of these leaks and attach hourly numbers to them, you have everything you need to close an Audit, Single Agent, or Retainer:</p>
                    <ol>
                        <li><strong>Leak #1 — The "Human API" Tax:</strong> Where are humans reading an email/PDF and typing it into another software box? (Solved by <em>Workflow Automation + OCR/Document Agents</em>).</li>
                        <li><strong>Leak #2 — The Handoff Black Hole:</strong> Where does a process stall for 24–72 hours waiting for Person A to notify Person B? (Solved by <em>Event-Driven Triggers & Autonomous Orchestration</em>).</li>
                        <li><strong>Leak #3 — Siloed Blindness:</strong> Where is leadership flying blind until someone spends 6 hours every Friday building a spreadsheet? (Solved by <em>Real-Time Data Synthesis & RAG Pipelines</em>).</li>
                        <li><strong>Leak #4 — The 9-to-5 Bottleneck:</strong> What critical revenue or support activity stops completely at 5:00 PM because humans go home to sleep? (Solved by <em>24/7 Autonomous Agents & Voice AI</em>).</li>
                    </ol>
                </div>
            """
        },

        # =====================================================================
        # PHASE 3D: GENERATING A TALK TRACK & THE 80-20 RULE (3 PAGES)
        # =====================================================================
        {
            "id": "pb3-p9",
            "phase": "PHASE 3D · TALK TRACK & THE 80/20 RULE (PAGE 1 OF 3)",
            "title": "Generating a Custom Talk Track for the 30-Minute Strategic Briefing",
            "tagline": "Every 30-minute Discovery Call follows a strict 4-act choreography. Control the frame from Minute 0:01.",
            "keyTakeaways": [
                "Act I (Min 0–3): Rapport, Time Check & The 'Upfront Agenda Contract'.",
                "Act II (Min 3–18): Deep Pain Excavation & Live Napkin Math (Prospect talks 80%+ here).",
                "Act III (Min 18–24): Architectural Mirroring & The Director of Staff / Field Evidence Bridge.",
                "Act IV (Min 24–30): Ballpark Positioning & Locking the Proposal / Architecture Readout Meeting on the Calendar."
            ],
            "content": """
                <div class="prose-section">
                    <h3>The 30-Minute Strategic Briefing Choreography</h3>
                    <p>Never let a prospect hijack the meeting in Minute 1 with, <em>"We only have 15 minutes, just tell me what you guys do and how much you charge."</em> You take control of the room in the first 90 seconds using the <strong>Upfront Agenda Contract</strong>:</p>

                    <div class="script-block">
                        <div class="script-stage">ACT I · THE UPFRONT AGENDA CONTRACT (MINUTES 0–3)</div>
                        <p><strong>YOU:</strong> "Appreciate you carving out the 30 minutes, [Name]. Do you still have a hard stop at the bottom of the hour? ... Perfect. Here's how we make these 30 minutes massively valuable for you: first, I did some homework on [Company] and have 2 or 3 quick hypotheses on where manual workflows might be eating up your team's week—I'd love to get your take on how things run today and price out what those bottlenecks are costing. Second, I'll share how we've architected autonomous workflows for similar operators to reclaim 15+ hours a week. And third, at the 25-minute mark, if there's an obvious ROI fit, we'll set up a dedicated readout where Mark Bockrath and I walk you through your custom ROI roadmap—and if there isn't a fit, we'll part ways as friends and you keep our initial diagnostic notes. Sound fair?"</p>
                    </div>

                    <!-- INTERACTIVE TALK TRACK GENERATOR -->
                    <div class="infographic-box" id="talk-track-box">
                        <div class="infographic-header">
                            <div>
                                <span class="badge-gold">INTERACTIVE TALK TRACK GENERATOR</span>
                                <h4>BUILD YOUR CUSTOM 30-MINUTE DISCOVERY TALK TRACK</h4>
                            </div>
                            <span class="text-xs font-mono text-zinc-400">SELECT VERTICAL & PERSONA TO GENERATE CALL SCRIPT</span>
                        </div>
                        <div class="scenario-btn-grid">
                            <button class="scen-btn active" onclick="generateTalkTrack(0)" id="tt-btn-0">Staffing / Recruiting · COO / Director of Staff</button>
                            <button class="scen-btn" onclick="generateTalkTrack(1)" id="tt-btn-1">B2B Professional Services · Managing Partner / CEO</button>
                            <button class="scen-btn" onclick="generateTalkTrack(2)" id="tt-btn-2">Logistics / Field Ops · VP Operations / CFO</button>
                        </div>
                        <pre class="email-body-pre" id="tt-output">1. HYPOTHESIS OPENER (MIN 3):
"Looking at your Bullhorn + HubSpot stack and your current hiring volume, we usually see recruiting and ops teams losing 15+ hours a week in two places: initial candidate vetting/outreach, and chasing onboarding packets. Walk me through how your team handles that flow today?"

2. PAIN QUANTIFICATION PROBE (MIN 10):
"So across your 4 coordinators, that's roughly 20 hours a week spent manually screening and chasing forms—about $55K a year in direct payroll drag, plus slower placements. How is that impacting your time-to-fill SLA?"

3. ARCHITECTURAL BRIDGE (MIN 19):
"That maps 1-to-1 to what we call 'Converting chaos into consistency, and consistency into currency.' For a Director of Staff in this exact spot, we engineered an autonomous agent wired directly into their stack that vets candidates, runs outreach, and handles onboarding 24/7—returning 15 hours/week and ~$40K in annual net liquidity."

4. NEXT-STEP LOCK (MIN 26):
"Rather than throwing a generic number at you today, let's get 30 minutes on the calendar for Thursday with Mark Bockrath where we present your exact 3-automation ROI roadmap and SOW options."</pre>
                    </div>
                </div>
            """
        },
        {
            "id": "pb3-p10",
            "phase": "PHASE 3D · TALK TRACK & THE 80/20 RULE (PAGE 2 OF 3)",
            "title": "The 80/20 Rule: Listen 80% of the Time, Speak 20%",
            "tagline": "God gave you two ears and one mouth—and in enterprise discovery, that's still not enough ears. If you are talking, you aren't learning; and if you aren't learning, you aren't closing.",
            "keyTakeaways": [
                "Data across millions of B2B discovery calls proves that when a sales rep talks more than 55% of the time, close rates plummet by over 60%.",
                "At MAB AI Strategies, our standard in Discovery is the 80/20 Rule: the prospect speaks 80% of the time, and you speak 20% (mostly asking surgical questions and mirroring back their math).",
                "Master the '4-Second Tactical Pause'—the secret weapon that makes executives spill the real truth."
            ],
            "content": """
                <div class="prose-section">
                    <h3>Why Silence Is the Highest-Paid Skill in B2B Sales</h3>
                    <p>When a prospect finishes answering a question, what does a nervous rookie do within 0.2 seconds? They jump in and start talking because silence feels awkward to them.</p>
                    <p>Here is a secret that top 1% enterprise closers know: <strong>An executive's first answer is their polite PR answer. Their real answer comes 3 seconds after they stop talking—if you keep your mouth shut.</strong></p>

                    <div class="founder-note">
                        <div class="founder-badge">THE 4-SECOND TACTICAL PAUSE DRILL</div>
                        <p>When a prospect finishes a sentence during Discovery, <strong>nod your head slowly, take a note, and count "One-one-thousand, two-one-thousand, three-one-thousand, four-one-thousand" in your head before speaking</strong>. Or simply say two words: <em>"Tell me more..."</em> or <em>"...and how does that impact your margin?"</em><br/><br/>
                        Nine times out of ten, the prospect will fill that 4-second silence by sighing and saying: <em>"Honestly, the real issue is that our top account manager threatened to quit last week because she's drowning in manual reporting..."</em> <strong>Boom.</strong> You just struck gold because you shut up and listened.</p>
                    </div>
                </div>
            """
        },
        {
            "id": "pb3-p11",
            "phase": "PHASE 3D · TALK TRACK & THE 80/20 RULE (PAGE 3 OF 3)",
            "title": "Tactical Labeling & Mirroring (Making the 20% Count)",
            "tagline": "How to make an executive feel more understood in 20 minutes than they have felt in 5 years.",
            "keyTakeaways": [
                "Tactical Mirroring: Repeat the last 2 to 4 critical words the prospect said with a curious upward inflection.",
                "Tactical Labeling: 'It sounds like...', 'It seems like...', 'What I'm hearing is that...'",
                "Never interrupt a prospect while they are quantifying their own pain."
            ],
            "content": """
                <div class="prose-section">
                    <h3>How to Keep Them Talking 80% of the Time</h3>
                    <p>You don't need 50 complicated questions to maintain an 80/20 listening ratio. You need two simple psychological tools popularized by FBI hostage negotiators (like Chris Voss) and adapted for enterprise discovery:</p>
                    <ul>
                        <li><strong>1. The 3-Word Mirror:</strong><br/>
                        <em>Prospect:</em> "We tried building an automation in Zapier last year, but it kept breaking whenever a client sent a weird PDF."<br/>
                        <em>Rookie (Bad):</em> "Oh we use Make.com and Python FastAPI with OCR so ours never breaks!" (Now the prospect stops talking.)<br/>
                        <em>MAB AI Pro (Mirror):</em> "Kept breaking on weird PDFs?" (Pause.)<br/>
                        <em>Prospect:</em> "Yeah! Every Friday my billing lead had to spend 4 hours fixing failed runs manually, and it delayed $80K in invoices..."</li>
                        <li><strong>2. The Diagnostic Label:</strong><br/>
                        <em>"It sounds like your team isn't short on talent—they're just trapped acting as the human glue between three systems that don't talk to each other."</em> (Then pause and let them agree!)</li>
                    </ul>
                </div>
            """
        },

        # =====================================================================
        # PHASE 3E: HOW TO RECOGNIZE SALES TRIGGERS & LISTEN FOR OPPORTUNITIES (2 PAGES)
        # =====================================================================
        {
            "id": "pb3-p12",
            "phase": "PHASE 3E · RECOGNIZING SALES TRIGGERS (PAGE 1 OF 2)",
            "title": "Verbal Sales Triggers: Catching the Million-Dollar Clues Hid in Casual Sentences",
            "tagline": "Prospects rarely say 'Please sell me an Accelerator Retainer.' Instead, they drop casual phrases that are screaming buying signals—if your ears are trained.",
            "keyTakeaways": [
                "A 'Verbal Sales Trigger' is a casual comment about headcount, software frustration, growth targets, or board pressure that reveals an immediate revenue opportunity.",
                "Learn the 6 High-Value Verbal Triggers and how to immediately hook into them."
            ],
            "content": """
                <div class="prose-section">
                    <h3>Train Your Ears to Catch These 6 Verbal Triggers Live</h3>
                    <div class="table-wrapper">
                        <table class="playbook-table">
                            <thead>
                                <tr>
                                    <th>What the Prospect Casually Says</th>
                                    <th>What It Actually Means (The Opportunity)</th>
                                    <th class="highlight-col">Your Immediate Follow-Up Question</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><em>"We're trying to hire two more ops/admin people right now."</em></td>
                                    <td>They have $120K–$150K in approved budget to solve a manual volume bottleneck.</td>
                                    <td class="highlight-col"><strong>"What exact daily tasks will those two new hires be doing—and if an agent handled 80% of that 24/7, would you still need both hires?"</strong></td>
                                </tr>
                                <tr>
                                    <td><em>"We bought HubSpot / Salesforce / Copilot, but adoption has been rough."</em></td>
                                    <td>They suffered from "bolted-on" tools requiring manual human effort.</td>
                                    <td class="highlight-col"><strong>"Where is the friction—are reps having to manually enter data instead of the workflow running automatically in the background?"</strong></td>
                                </tr>
                                <tr>
                                    <td><em>"Everything lives in Sarah's head—if she takes a vacation, we panic."</em></td>
                                    <td>Massive key-person risk & undocumented tribal chaos.</td>
                                    <td class="highlight-col"><strong>"How much of Sarah's week is spent on repeatable coordination that we could codify into an autonomous pipeline?"</strong></td>
                                </tr>
                                <tr>
                                    <td><em>"It takes us 3–4 days to turn around a client quote / onboarding packet."</em></td>
                                    <td>Lagging handoff is directly killing their close rate and revenue velocity.</td>
                                    <td class="highlight-col"><strong>"What happens to your win rate if we compress that 4-day turnaround down to 4 minutes?"</strong></td>
                                </tr>
                                <tr>
                                    <td><em>"Our board / PE partners want us to expand EBITDA margins this year."</em></td>
                                    <td>Mandate from the Economic Buyer to cut operational drag immediately.</td>
                                    <td class="highlight-col"><strong>"What is the board's target timeline for seeing measurable margin lift—this quarter or next?"</strong></td>
                                </tr>
                                <tr>
                                    <td><em>"We don't even know which department is leaking the most time."</em></td>
                                    <td>Slam-dunk candidate for our Standalone <strong>AI Readiness Audit</strong>.</td>
                                    <td class="highlight-col"><strong>"If we ran a 1–2 week forensic AI Readiness Audit to rank every workflow by dollar ROI, which 3 departments would we scan first?"</strong></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            """
        },
        {
            "id": "pb3-p13",
            "phase": "PHASE 3E · RECOGNIZING SALES TRIGGERS (PAGE 2 OF 2)",
            "title": "Spotting Expansion Opportunities During Discovery (Multi-Threading)",
            "tagline": "How to turn a $5,000 single-workflow conversation into a $75,000 enterprise architecture relationship.",
            "keyTakeaways": [
                "Whenever a prospect describes a bottleneck in Department A, always ask what happens upstream (before it arrives) and downstream (after it leaves).",
                "Upstream + Downstream questioning naturally uncovers 4 to 6 connected workflows—turning a Single Workflow lead into an Accelerator or Principal Retainer!"
            ],
            "content": """
                <div class="prose-section">
                    <h3>The "Upstream / Downstream" Expansion Technique</h3>
                    <p>Suppose a COO gets on the call to talk about automating <strong>Candidate Onboarding</strong> (1 workflow). If you only ask about Candidate Onboarding, you can only sell a Single Workflow.</p>
                    <p>Watch what happens when you ask one <strong>Upstream</strong> question and one <strong>Downstream</strong> question:</p>
                    <ul>
                        <li><strong>Upstream Question:</strong> <em>"Before a candidate ever reaches onboarding, how much time is the team losing upstream on resume vetting, outreach, and interview scheduling?"</em> → Uncovers 2 more workflows!</li>
                        <li><strong>Downstream Question:</strong> <em>"And once onboarding is complete, how does that data flow downstream into payroll, client billing in QuickBooks, and weekly executive reporting?"</em> → Uncovers 3 more workflows!</li>
                    </ul>
                    <p>In 90 seconds, you just uncovered <strong>6 interconnected workflows across ATS, CRM, and ERP</strong>—which is the exact textbook definition of our <strong>Accelerator Retainer</strong>!</p>
                </div>
            """
        },

        # =====================================================================
        # PHASE 3F: LOGGING IN NEXUS CRM, POST-MEETING CHECKLIST & NUMBERS (5 PAGES)
        # =====================================================================
        {
            "id": "pb3-p14",
            "phase": "PHASE 3F · NEXUS CRM, CHECKLIST & NUMBERS (PAGE 1 OF 5)",
            "title": "Logging and Documenting Results in Nexus CRM",
            "tagline": "A great Discovery call with sloppy CRM notes is like performing a brilliant surgery and forgetting to stitch the patient closed.",
            "keyTakeaways": [
                "Every completed Discovery Call must be logged in Nexus CRM within 15 minutes of hanging up.",
                "The 7 Mandatory Nexus CRM Discovery Fields: (1) Current State / Tech Stack, (2) Quantified Pain (Hours/Wk + Annual $ Bleed), (3) Desired Future State & Timeline, (4) Identified Economic Buyer & Champion, (5) Prescribed MAB AI Offer/Tier, (6) Gemini Notebook & Transcript URI, (7) Dated Next Step (Architecture Readout Date).",
                "Why? Mark Bockrath reviews your Nexus CRM Opportunity record before joining the Architecture Readout / Proposal call."
            ],
            "content": """
                <div class="prose-section">
                    <h3>The MAB AI Standard for Nexus CRM Discovery Notes</h3>
                    <p>Never write lazy, useless CRM notes like: <em>"Had a good call with Dana, she liked what we do, following up next week."</em> If I open Nexus CRM and see that note on one of your deals, we are going to have a very uncomfortable conversation.</p>
                    <p>Why? Because <em>"had a good call"</em> tells our engineering and architecture team zero about what hurts, what stack they run, how much money they are bleeding, or who controls the checkbook. Every Discovery Opportunity in <strong>Nexus CRM</strong> must populate the structured <strong>MAB AI Diagnostic Template</strong>:</p>
                    <ul>
                        <li><strong>1. Tech Stack Inventory:</strong> Exact CRM, ATS, ERP, Comms, and DB tools currently in place.</li>
                        <li><strong>2. Quantified Operational Bleed:</strong> Exact math agreed to on the call (e.g., <code>3 staff × 6 hrs/wk × $55/hr × 52 wks = $51,480/yr</code>).</li>
                        <li><strong>3. Top 3 Bottlenecks Uncovered:</strong> Ranked in order of pain severity.</li>
                        <li><strong>4. Buying Committee Map:</strong> Who is the Champion? Who is the Economic Buyer? Who is the Technical Gatekeeper?</li>
                        <li><strong>5. Prescribed Architecture Tier:</strong> Standalone Audit / Single Agent / Foundation / Accelerator / Principal.</li>
                        <li><strong>6. Locked Next Step Date:</strong> Exact date & time of the live Architecture Readout (Proposal) meeting.</li>
                    </ul>
                </div>
            """
        },
        {
            "id": "pb3-p15",
            "phase": "PHASE 3F · NEXUS CRM, CHECKLIST & NUMBERS (PAGE 2 OF 5)",
            "title": "Interactive Nexus CRM Discovery Logging Simulator",
            "tagline": "Practice logging a real Discovery Call into Nexus CRM right now and get instant diagnostic scoring.",
            "keyTakeaways": [
                "Complete the interactive Nexus CRM Sandbox below based on the call transcript summary provided.",
                "Verify that all required fields and the Iron Law of the Dated Next Step are satisfied."
            ],
            "content": """
                <div class="prose-section">
                    <div class="infographic-box" id="nexus-crm-sim">
                        <div class="infographic-header">
                            <div>
                                <span class="badge-emerald">INTERACTIVE NEXUS CRM SANDBOX</span>
                                <h4>NEXUS CRM · OPPORTUNITY DIAGNOSTIC LOGGER</h4>
                            </div>
                            <span class="text-xs font-mono text-zinc-400">COMPLETE ALL FIELDS FROM THE CALL BRIEF & CLICK VALIDATE</span>
                        </div>

                        <div class="crm-scenario-banner">
                            <strong>📋 CALL SUMMARY TO LOG:</strong> You just finished a 30-min Discovery Call with <strong>Elena Rostova (COO)</strong> at <strong>Meridian Legal Group</strong> (60 employees, $19M rev). They use <strong>Clio + HubSpot + QuickBooks + Slack</strong>. Elena revealed that <strong>4 paralegals each spend 5 hours/week</strong> manually extracting intake docs and chasing client signatures at a <strong>$60/hr</strong> burdened rate (<strong>$62,400/yr bleed</strong>). Managing Partner <strong>Arthur Pendelton (CEO)</strong> is the Economic Buyer and will join the Architecture Readout on <strong>Thursday at 2:00 PM ET</strong>. You are prescribing the <strong>Accelerator Retainer</strong> (with Single Agent wedge backup).
                        </div>

                        <div class="crm-form-grid">
                            <div class="crm-field">
                                <label>1. Account & Opportunity Stage</label>
                                <select id="crm-stage" class="form-input">
                                    <option value="">-- Select Stage --</option>
                                    <option value="s1">Stage 1: Cold Prospecting</option>
                                    <option value="s3">Stage 3: Discovery Completed → Readout Scheduled</option>
                                    <option value="s6">Stage 6: Closed Won</option>
                                </select>
                            </div>
                            <div class="crm-field">
                                <label>2. Quantified Annual Pain ($/yr)</label>
                                <select id="crm-pain" class="form-input">
                                    <option value="">-- Select Quantified Bleed --</option>
                                    <option value="wrong1">Unknown / Didn't Ask</option>
                                    <option value="correct">$62,400/yr (20 hrs/wk × $60/hr × 52 wks)</option>
                                    <option value="wrong2">$5,000/yr guess</option>
                                </select>
                            </div>
                            <div class="crm-field">
                                <label>3. Champion & Economic Buyer</label>
                                <select id="crm-buyers" class="form-input">
                                    <option value="">-- Select Buying Committee --</option>
                                    <option value="wrong1">Elena Rostova only (No Economic Buyer needed)</option>
                                    <option value="correct">Champion: Elena Rostova (COO) | Economic Buyer: Arthur Pendelton (Managing Partner)</option>
                                </select>
                            </div>
                            <div class="crm-field">
                                <label>4. Prescribed Tier & Dated Next Step</label>
                                <select id="crm-next" class="form-input">
                                    <option value="">-- Select Prescription & Next Step --</option>
                                    <option value="wrong1">Email PDF quote and wait for them to call back</option>
                                    <option value="correct">Accelerator Retainer (Single Agent Wedge) | Live Readout: Thursday 2:00 PM ET w/ Arthur & Elena</option>
                                </select>
                            </div>
                        </div>
                        <button class="btn-primary-glow mt-4" onclick="validateNexusCRMSim()">Save & Validate Nexus CRM Record →</button>
                        <div id="crm-sim-feedback" class="call-feedback hidden mt-3"></div>
                    </div>
                </div>
            """
        },
        {
            "id": "pb3-p16",
            "phase": "PHASE 3F · NEXUS CRM, CHECKLIST & NUMBERS (PAGE 3 OF 5)",
            "title": "The Mandatory 15-Minute Post-Meeting Checklist",
            "tagline": "What you do in the 15 minutes immediately after the Zoom ends determines whether the deal maintains velocity or cools off.",
            "keyTakeaways": [
                "Never stack back-to-back Discovery Calls without a 15-minute buffer block between them.",
                "Execute all 7 steps of the Post-Meeting Checklist before moving to your next task."
            ],
            "content": """
                <div class="prose-section">
                    <h3>Your 7-Step Post-Discovery Execution Protocol</h3>
                    <p>Check off these 7 items within 15 minutes of ending every Discovery Briefing:</p>
                    <div class="checklist-box">
                        <label class="check-item"><input type="checkbox" /> <strong>1. Export Transcript to Gemini Notebook:</strong> Upload the Zoom transcript / Zoom Summary output into the prospect's dedicated Gemini Notebook Deal Room.</label>
                        <label class="check-item"><input type="checkbox" /> <strong>2. Update Nexus CRM Opportunity:</strong> Fill in all 6 diagnostic fields (Tech Stack, Quantified Weekly/Annual Pain, Top 3 Bottlenecks, Champion + Economic Buyer, Prescribed Tier, Dated Next Step).</label>
                        <label class="check-item"><input type="checkbox" /> <strong>3. Send Calendar Invite for the Architecture Readout (Proposal Meeting):</strong> Lock the exact time on the calendar while still on the call (or within 5 minutes), including the Economic Buyer's email.</label>
                        <label class="check-item"><input type="checkbox" /> <strong>4. Send the "Executive Mirror Recap Email" (via Email Polisher GEM):</strong> Send a crisp 5-bullet recap confirming: (a) their current bottlenecks, (b) the agreed hourly/annual cost of inaction math, and (c) the agenda for Thursday's Architecture Readout.</label>
                        <label class="check-item"><input type="checkbox" /> <strong>5. Connect with All Attendees on LinkedIn:</strong> Send a short connection request to everyone on the call plus the Economic Buyer who will join the next call.</label>
                        <label class="check-item"><input type="checkbox" /> <strong>6. Brief Mark / Engineering on Slack (If Accelerator or Principal Scope):</strong> Drop the Nexus CRM link and 3-bullet pain summary so architecture specs are ready.</label>
                        <label class="check-item"><input type="checkbox" /> <strong>7. Draft the Architecture Readout Outline:</strong> Use <em>The Architect GEM</em> to map their 3 highest-ROI workflows while the conversation is fresh in your mind.</label>
                    </div>
                </div>
            """
        },
        {
            "id": "pb3-p17",
            "phase": "PHASE 3F · NEXUS CRM, CHECKLIST & NUMBERS (PAGE 4 OF 5)",
            "title": "When to Talk Numbers (And How Not to Shoot Yourself in the Foot)",
            "tagline": "Never quote an exact SOW price before quantifying the pain—and never dodge a direct pricing question like a slippery politician.",
            "keyTakeaways": [
                "The Cardinal Rule of Numbers: NEVER talk price before you have calculated the Cost of Inaction with the prospect. Price without ROI context always sounds expensive.",
                "What if they ask 'How much do you charge?' in Minute 4 of Discovery? Give a transparent 'Architecture Bracket' tied to outcomes, then pivot straight back to diagnosing their scope.",
                "When to talk numbers in Discovery: In the final 5 minutes (Min 25–30), after agreeing that their manual chaos costs $60K–$150K+/yr, share the appropriate tier bracket so there is zero sticker shock on the Proposal Call."
            ],
            "content": """
                <div class="prose-section">
                    <div class="founder-note">
                        <div class="founder-badge">CRITICAL RULE · WHEN TO TALK NUMBERS</div>
                        <p>"Timing is everything when talking money. If you quote a price in Minute 5 before you know what their problem costs them, even $3,000 sounds like an expense. If you wait until Minute 25—right after the COO just admitted out loud that manual handoffs are burning $95,000 a year—then our investment looks like a 4x to 10x money printer. Diagnose first, quantify the bleed second, talk numbers third."</p>
                    </div>

                    <h3>Scenario 1: The Prospect Asks "How Much Does This Cost?" in Minute 4</h3>
                    <p>Never be evasive (<em>"I can't tell you until next week"</em>—that pisses executives off), and never blurt out a random number without context. Use the <strong>Bracket + Pivot Technique</strong>:</p>
                    <blockquote>
                        "Happy to give you the ballpark right now so there's zero mystery. Depending on whether a client starts with a standalone 1–2 week AI Readiness Audit or Single Agent build, or embeds us on an ongoing monthly retainer like our Foundation, Accelerator, or Principal tiers, engagements typically range from a low four-figure diagnostic sprint up to a mid-to-high four-figure or five-figure monthly architecture retainer—and our Accelerator tier carries a 90-day ROI guarantee. Where you fall in that range depends entirely on how many workflows we're automating and what the hourly bleed looks like. To see which bucket even makes sense for [Company], walk me through how your team handles [Workflow X] today?"
                    </blockquote>

                    <h3>Scenario 2: The Right Moment to Talk Numbers (Minutes 24–28 of Discovery)</h3>
                    <p>Once you have quantified the pain (e.g., <em>"Okay, so we agree this manual bottleneck is costing you roughly $7,500 every single month..."</em>), you <strong>must</strong> drop a temperature-check bracket before booking the Proposal Meeting:</p>
                    <blockquote>
                        "So if leaving this broken is costing you $7,500 a month—$90,000 a year—and on Thursday's Architecture Readout we show you how to eliminate 80% of that drag with an investment that pays for itself inside 60 to 90 days, is there any reason we wouldn't get started this month?"
                    </blockquote>
                </div>
            """
        },
        {
            "id": "pb3-p18",
            "phase": "PHASE 3F · NEXUS CRM, CHECKLIST & NUMBERS (PAGE 5 OF 5)",
            "title": "Playbook 3 Mastery Synthesis & Certification Exam Launch",
            "tagline": "You now possess the complete playbook from Business Thesis (PB0) to Market Economics (PB1), Outbound Prospecting (PB2), and Discovery Mastery (PB3).",
            "keyTakeaways": [
                "Review the core Discovery pillars: 15-min AI Reconnaissance, Gemini Notebook War Rooms, 3-Layer Pain Excavation, 80/20 Listening Rule, Verbal Sales Triggers, Nexus CRM Hygiene, Post-Meeting Checklist, and Pricing After Pain.",
                "Bonus Playbooks 4 through 10 await you right after this exam—covering Proposals, Negotiations, Closing, Payment/Signature, Follow-Up, Implementation, and Escalations!"
            ],
            "content": """
                <div class="prose-section">
                    <h3>Your Pre-Exam Discovery Checklist</h3>
                    <ul>
                        <li>✅ <strong>Preparation:</strong> Know their business better than they do via Perplexity, LinkedIn job descriptions, and Briefing Bot.</li>
                        <li>✅ <strong>Gemini Notebook:</strong> Ground every deal in a dedicated source-verified NotebookLM war room + 5-min Audio Overview.</li>
                        <li>✅ <strong>Find the Pain:</strong> Drill past surface symptoms to quantified hours/dollars lost and personal executive stakes.</li>
                        <li>✅ <strong>The 80/20 Rule:</strong> Listen 80% of the time, speak 20%, and wield the 4-Second Tactical Pause.</li>
                        <li>✅ <strong>Nexus CRM & Post-Meeting Checklist:</strong> Log all 6 mandatory fields within 15 minutes and send the Executive Mirror Recap.</li>
                        <li>✅ <strong>When to Talk Numbers:</strong> Never quote exact prices before quantifying the Cost of Inaction.</li>
                    </ul>

                    <div class="exam-launch-cta">
                        <div>
                            <h4>Ready to Certify on Playbook 3?</h4>
                            <p>Complete the 12-question Playbook 3 Certification Exam to unlock the Bonus Advanced Playbooks (Playbooks 4–10) and email your diagnostic report to Mark Bockrath.</p>
                        </div>
                        <button class="btn-primary-glow" onclick="launchModuleExam('pb3')">Launch Playbook 3 Certification Exam →</button>
                    </div>
                </div>
            """
        }
    ],
    "popQuizzes": [
        {
            "id": "pb3-pop1",
            "triggerAfterPage": 5,
            "title": "Pop Quiz: AI Reconnaissance & Gemini Notebook",
            "questions": [
                {
                    "q": "Why is reading the bullet points of a prospect's active job postings on LinkedIn/Indeed one of the best pre-call research hacks?",
                    "options": [
                        "Because we want to apply for a part-time job there.",
                        "Because job descriptions for admin/coordinator roles literally list every repetitive, manual workflow and software tool the company is currently struggling to handle.",
                        "Because job postings list the CEO's personal cell phone number.",
                        "It isn't useful."
                    ],
                    "correct": 1,
                    "explanation": "Job descriptions are public confessions of a company's manual workflows and software silos."
                },
                {
                    "q": "What makes Gemini Notebook (NotebookLM) uniquely powerful as a Deal War Room compared to a generic web chat prompt?",
                    "options": [
                        "It automatically sends cold emails.",
                        "It grounds its reasoning strictly in the verified prospect sources you upload (URLs, job posts, transcripts, MAB AI Capability Matrix) with zero outside web hallucinations, plus generates 5-minute Audio Overviews.",
                        "It replaces Nexus CRM.",
                        "It only works for coding Python."
                    ],
                    "correct": 1,
                    "explanation": "Gemini Notebook is source-grounded in the exact documents and transcripts uploaded for that specific deal."
                }
            ]
        },
        {
            "id": "pb3-pop2",
            "triggerAfterPage": 11,
            "title": "Pop Quiz: 'Find the Pain' & The 80/20 Rule",
            "questions": [
                {
                    "q": "During a 30-Minute Discovery Briefing, what is the target talk-to-listen ratio, and how do you enforce it?",
                    "options": [
                        "Speak 80% of the time pitching features; listen 20%.",
                        "The 80/20 Rule: Listen 80% of the time and speak 20% of the time—using surgical questions, 3-word mirrors, diagnostic labels, and the 4-Second Tactical Pause.",
                        "50/50 debate.",
                        "Read a slide deck for 28 minutes straight."
                    ],
                    "correct": 1,
                    "explanation": "Listen 80%, speak 20%. When you pause for 4 seconds after their initial answer, they reveal the real operational and personal pain."
                },
                {
                    "q": "What are the 3 layers of pain excavation you must drill through during Discovery?",
                    "options": [
                        "Past, Present, Future",
                        "Layer 1: Surface Symptom -> Layer 2: Quantified Financial/Hourly Bleed -> Layer 3: Personal Executive Stakes",
                        "Email, Phone, LinkedIn",
                        "Small, Medium, Large"
                    ],
                    "correct": 1,
                    "explanation": "Surface complaints don't close deals; quantified financial bleed + personal executive stakes close deals."
                }
            ]
        }
    ],
    "finalExam": {
        "title": "Playbook 3 Certification Exam: The Discovery Meeting Mastery",
        "passingScore": 80,
        "questions": [
            {
                "category": "Pre-Meeting Preparation",
                "q": "Why is opening a Discovery Call with 'So tell me what your company does' strictly forbidden at MAB AI Strategies?",
                "options": [
                    "Because it takes too long to say.",
                    "Because it proves you did zero homework, insults the executive's time, and destroys your credibility as an AI intelligence partner.",
                    "Because CEOs don't know what their company does.",
                    "Because Zoom records the first minute."
                ],
                "correct": 1,
                "explanation": "Showing up cold is amateur hour. We open with 2–3 researched hypotheses that prove we know their business better than they do."
            },
            {
                "category": "Pre-Meeting Preparation",
                "q": "In our 15-Minute AI Reconnaissance Protocol, why do we bring 3 educated hypotheses to the start of the call?",
                "options": [
                    "To prove we can guess randomly.",
                    "Because busy executives hate educating salespeople from scratch, but they gladly validate or correct a specific, researched hypothesis—immediately opening up about their real bottlenecks.",
                    "So we don't have to ask any questions.",
                    "To make the call last 2 hours."
                ],
                "correct": 1,
                "explanation": "Cunningham's Law in Discovery: stating an educated hypothesis gets you to the truth 5x faster than vague generic questions."
            },
            {
                "category": "Gemini Notebook Strategy",
                "q": "Which 4 source types should you load into a prospect's dedicated Gemini Notebook Deal Room?",
                "options": [
                    "Random Wikipedia articles.",
                    "1. Prospect Website/Service URLs, 2. Active Job Descriptions & Exec LinkedIn Profiles, 3. MAB AI Capability & Tier Matrix, and 4. Call Transcripts/Notes as the deal progresses.",
                    "Only competitor websites.",
                    "Only your personal resume."
                ],
                "correct": 1,
                "explanation": "Combining prospect URLs, job reqs, MAB AI's capability matrix, and call transcripts creates a complete Deal Brain."
            },
            {
                "category": "Find the Pain",
                "q": "A COO says on Discovery, 'Our client onboarding is a little clunky.' If you immediately start pitching our Onboarding Bot without asking follow-up questions, what mistake did you just make?",
                "options": [
                    "You pitched at Layer 1 (Surface Symptom) before excavating Layer 2 (Quantified Hours & Dollars Lost) and Layer 3 (Executive/Board Impact).",
                    "You spoke too softly.",
                    "You didn't screen-share fast enough.",
                    "No mistake—always pitch immediately."
                ],
                "correct": 0,
                "explanation": "'A little clunky' is a $0 surface symptom. You must quantify weekly hours, hourly cost, error impact, and executive stakes first."
            },
            {
                "category": "Find the Pain",
                "q": "What are the 4 core operational leak buckets you are diagnosing during Discovery?",
                "options": [
                    "1. Repetitive 'Human-API' Tasks, 2. Lagging Inter-Departmental Handoffs, 3. Data Rotting in Silos, and 4. After-Hours / Speed-to-Lead Gaps",
                    "1. Office rent, 2. Company cars, 3. Catering, 4. Travel",
                    "1. Logos, 2. Fonts, 3. Colors, 4. Slogans",
                    "1. Hardware, 2. Printers, 3. Cables, 4. Monitors"
                ],
                "correct": 0,
                "explanation": "Those four leaks map directly to The Impressions Layer and our Refractive Core modules."
            },
            {
                "category": "Custom Talk Track",
                "q": "What is the purpose of the 'Upfront Agenda Contract' in Minutes 0–3 of the Discovery Meeting?",
                "options": [
                    "To get them to sign a legal NDA.",
                    "To confirm time boundaries, establish peer frame control, align on the 3-step agenda (diagnose & price bottlenecks -> share peer architecture -> lock next steps if ROI is clear), and give them permission to say no if there isn't a fit.",
                    "To read a 10-minute company history.",
                    "To ask for their credit card in minute 1."
                ],
                "correct": 1,
                "explanation": "The Upfront Agenda Contract puts you in control of the clock and the outcome from Minute 1."
            },
            {
                "category": "The 80/20 Rule",
                "q": "What is the '4-Second Tactical Pause' and why does it work?",
                "options": [
                    "Muting your microphone when you sneeze.",
                    "Waiting 3–4 seconds in calm, nodding silence after the prospect finishes their initial polite answer—which prompts them to keep talking and reveal the deeper, unvarnished truth.",
                    "Hanging up if they don't talk for 4 seconds.",
                    "Speaking only 4 words per minute."
                ],
                "correct": 1,
                "explanation": "An executive's first answer is their PR answer; their second answer after a 4-second pause is the real truth."
            },
            {
                "category": "Sales Triggers & Opportunities",
                "q": "When a prospect mentions a single bottleneck (e.g., 'Candidate onboarding takes too long'), how do you use 'Upstream / Downstream' questioning to expand the deal into an Accelerator Retainer?",
                "options": [
                    "Ignore onboarding and talk about something unrelated.",
                    "Ask what happens right BEFORE that step (upstream: vetting, outreach, scheduling) and right AFTER that step (downstream: payroll, billing, KPI reporting) to uncover 4–6 connected workflows.",
                    "Tell them we don't do single workflows.",
                    "Ask them to double their budget for no reason."
                ],
                "correct": 1,
                "explanation": "Upstream and Downstream probing turns a single-task conversation into an end-to-end multi-workflow architecture."
            },
            {
                "category": "Nexus CRM Documentation",
                "q": "Which of the following is REQUIRED when logging a completed Discovery Call in Nexus CRM?",
                "options": [
                    "Writing 'Good call, will follow up soon.'",
                    "Logging Tech Stack, Quantified Pain (hrs/wk + $/yr), Top 3 Bottlenecks, Buying Committee (Champion + Economic Buyer), Prescribed Tier, Gemini Notebook URI, and a Dated Next Step for the Architecture Readout.",
                    "Only logging the prospect's first name.",
                    "Waiting until the end of the month to log the call."
                ],
                "correct": 1,
                "explanation": "All 6+ diagnostic fields and the Dated Next Step must be logged in Nexus CRM within 15 minutes."
            },
            {
                "category": "Post-Meeting Checklist",
                "q": "How quickly after a Discovery Call should the 7-step Post-Meeting Checklist (Nexus CRM update, calendar invite, Executive Mirror Recap email) be completed?",
                "options": [
                    "Within 15 minutes of hanging up.",
                    "On Friday afternoon.",
                    "Two weeks later.",
                    "Only if the prospect emails you first."
                ],
                "correct": 0,
                "explanation": "Speed and precision after the call demonstrate the exact consistency we sell."
            },
            {
                "category": "When to Talk Numbers",
                "q": "Why must you NEVER quote an exact SOW price before quantifying the prospect's Cost of Inaction?",
                "options": [
                    "Because our prices change every hour.",
                    "Because without the anchor of their own quantified financial bleed (e.g., '$8,000/month lost to manual drag'), any price looks like an unbudgeted expense rather than a high-return investment.",
                    "Because we don't know our prices.",
                    "Because talking about money is rude."
                ],
                "correct": 1,
                "explanation": "Price before pain = sticker shock. Price after proving $90K/yr in pain = a no-brainer investment."
            },
            {
                "category": "When to Talk Numbers",
                "q": "If an impatient prospect demands 'Just tell me how much you guys cost' in Minute 4 of Discovery, what is the right move?",
                "options": [
                    "Refuse to answer and argue with them.",
                    "Give a calm, transparent 'Architecture Bracket' (from standalone audits/single agents up to Foundation, Accelerator, and Principal retainers), explain that exact placement depends on workflow count and ROI math, and pivot right back to a diagnostic question.",
                    "Quote the cheapest possible price and offer a 50% discount.",
                    "End the Zoom call immediately."
                ],
                "correct": 1,
                "explanation": "The Bracket + Pivot technique satisfies their need for transparency without boxing you into the wrong scope prematurely."
            }
        ]
    }
}
