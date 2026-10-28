# -*- coding: utf-8 -*-
"""
PLAYBOOK 1: INTRO PHASES — INDUSTRY, MARKET, B2B SALES, ICP, VERTICALS, OUTREACH, CRM & PSYCHOLOGY
22 Dense Pages across 7 Comprehensive Intro Phases | Interactive Calculators & Simulators
Random Pop Quizzes | 12-Question Scored Certification Exam
"""

PLAYBOOK_1 = {
    "id": "pb1",
    "number": 1,
    "code": "PLAYBOOK 01",
    "title": "Market, B2B Economics, ICP, Verticals & Sales Psychology",
    "subtitle": "From Zero Industry Context to Fluent B2B Diagnostic Strategist across 7 Intensive Intro Phases",
    "level": "INDUSTRY & ROLE FOUNDATION · 22 PAGES",
    "duration": "120 Mins · 7 Phases (22 Pages) · Interactive ROI Engine · 12-Q Exam",
    "unlockRequirement": "pb0",
    "overview": "You passed Playbook 0—now we wire your brain for the AI automation market and enterprise B2B sales. This playbook takes you through 7 foundational phases: the AI/Agent market shift (5 pages), B2B sales economics (4 pages), ICP & decision makers, verticals & low-hanging fruit, prospecting & sequencing, Nexus CRM mastery, and executive sales psychology.",
    "pages": [
        # =====================================================================
        # PHASE 1A: INTRODUCTION TO THE INDUSTRY AND THE MARKET (5 PAGES)
        # =====================================================================
        {
            "id": "pb1-p1",
            "phase": "PHASE 1A · INDUSTRY & MARKET (PAGE 1 OF 5)",
            "title": "The Great Tectonic Shift: From SaaS to 'Service-as-Software'",
            "tagline": "For twenty years, businesses bought tools to help humans click buttons faster. Today, they buy digital workers that click the buttons for them.",
            "keyTakeaways": [
                "The SaaS Era (2004–2023) sold 'shovels'—software logins that still required expensive human labor to operate.",
                "The Agentic Era (2024–Present) sells 'Service-as-Software'—autonomous workflows and AI agents that execute the labor itself.",
                "The new enterprise org chart blends human strategists with silicon employees that require architecture, KPIs, and guardrails."
            ],
            "content": """
                <div class="prose-section">
                    <div class="founder-note">
                        <div class="founder-badge">FIELD NOTE EXCERPT · THE AGENTIC WORKFORCE</div>
                        <p>"We are witnessing the end of the 'Software as a Service' era and the beginning of the 'Service as a Software' era. For the last two decades, we bought tools to help humans work faster. Now, we are buying agents to do the work itself. The traditional org chart, defined by headcount and hierarchy, is obsolete. The new org chart includes silicon employees."</p>
                    </div>

                    <h3>Why This Shift Is Printing Billions (And Why Most Companies Are Lost)</h3>
                    <p>If you are brand new to technology and AI, let's strip away the Silicon Valley nerd-speak and look at the cold, hard business history:</p>
                    <ul>
                        <li><strong>Wave 1: On-Premise Software (1990s):</strong> Companies bought CD-ROMs and server racks in their basement. Slow, expensive, painful.</li>
                        <li><strong>Wave 2: Cloud SaaS — Software-as-a-Service (2004–2023):</strong> Salesforce, HubSpot, Workday, Zendesk, Slack. Companies rented cloud logins for $100/month per employee. <strong>The Catch:</strong> Buying 50 SaaS tools meant hiring 20 operations coordinators just to copy-paste data from Tool A into Tool B.</li>
                        <li><strong>Wave 3: The Agentic Enterprise — Service-as-Software (Right Fucking Now):</strong> Instead of buying another dashboard for an overworked human to stare at, companies hire <strong>MAB AI Strategies</strong> to wire autonomous workflows and reasoning agents across their existing tools so the work happens automatically.</li>
                    </ul>

                    <div class="comparison-grid">
                        <div class="comp-card comp-bad">
                            <h4>Old SaaS Mentality (Selling Seats)</h4>
                            <p>"Buy our software for $50/user/month! Your recruiting team will love logging in for 4 hours a day to filter resumes manually!"</p>
                        </div>
                        <div class="comp-card comp-good">
                            <h4>MAB AI Agentic Mentality (Selling Outcomes)</h4>
                            <p>"Don't make your Director of Staff stare at another dashboard. Our agent vets candidates, triggers outreach, and provisions onboarding autonomously—giving you back 15 hours a week and $40K in annual net liquidity."</p>
                        </div>
                    </div>
                </div>
            """
        },
        {
            "id": "pb1-p2",
            "phase": "PHASE 1A · INDUSTRY & MARKET (PAGE 2 OF 5)",
            "title": "The Anatomy of AI: Chatbots vs. Automations vs. Autonomous Agents",
            "tagline": "If you confuse a deterministic Zapier script with a multi-step LangGraph agent on a call, a CTO will eat you alive. Learn the difference right here.",
            "keyTakeaways": [
                "Level 1 — Standalone LLMs / Chatbots (ChatGPT, Claude web): Passive text boxes. Great for drafting an email, useless for running an enterprise pipeline autonomously.",
                "Level 2 — Deterministic Workflow Automation (Make.com, n8n, Zapier, Workato): Strict 'If This, Then That' railroad tracks. Zero reasoning, massive speed.",
                "Level 3 — RAG (Retrieval-Augmented Generation): Connecting an LLM to a company's private data (Pinecone, Supabase, PostgreSQL) so it answers with zero hallucinations.",
                "Level 4 — Autonomous AI Agents (LangGraph, CrewAI v0.9, AG2, OpenAI Agents SDK): Multi-step reasoning loops that can use tools, check their own work, and escalate to humans when needed."
            ],
            "content": """
                <div class="prose-section">
                    <h3>The 4-Layer Intelligence Stack (Explained Like You're Having a Beer)</h3>
                    <p>You don't need to know how to code these four layers, but you <strong>must</strong> know what each one does and when we use it:</p>

                    <div class="module-cards-grid">
                        <div class="spec-card">
                            <div class="spec-num">LAYER 01 · THE BRAIN (LLMs)</div>
                            <h4>Large Language Models</h4>
                            <p>Think of an LLM (OpenAI <strong>o3 / GPT-4</strong>, Anthropic <strong>Claude 4 / 3.5 Sonnet</strong>, Google <strong>Gemini 2.5 Pro</strong>, Meta <strong>Llama 4</strong>) as a brilliant Harvard graduate locked in a room with no internet, no phone, and no access to your company's files. Smart as hell, but can't take action alone.</p>
                        </div>
                        <div class="spec-card">
                            <div class="spec-num">LAYER 02 · THE MEMORY (RAG)</div>
                            <h4>Retrieval-Augmented Generation & Vector DBs</h4>
                            <p>How do we stop the LLM from making shit up ("hallucinating")? We build a <strong>RAG pipeline</strong> using <strong>Pinecone, Supabase, or PostgreSQL</strong>. Before the LLM speaks, it searches the client's verified contracts, SOPs, and pricing tables in milliseconds and cites the exact truth.</p>
                        </div>
                        <div class="spec-card">
                            <div class="spec-num">LAYER 03 · THE NERVOUS SYSTEM (WORKFLOWS)</div>
                            <h4>Deterministic Automation (Make · n8n · Workato)</h4>
                            <p>These are the digital railroad tracks connecting APIs: <em>"When a contract is signed in DocuSign → create a folder in Google Drive → create a project in Jira → post in Slack → send invoice in Stripe."</em> It runs 24/7 with zero creativity needed.</p>
                        </div>
                        <div class="spec-card">
                            <div class="spec-num">LAYER 04 · THE DIGITAL WORKER (AGENTS)</div>
                            <h4>Autonomous Multi-Step Agents (LangGraph · CrewAI · AG2)</h4>
                            <p>When a task requires <strong>judgment, multi-step reasoning, and tool orchestration</strong>—like researching a new lead, deciding which vertical they fit, drafting a custom response, and pausing for human approval if deal size exceeds $50K—we engineer an Autonomous Agent.</p>
                        </div>
                    </div>

                    <div class="callout-tip">
                        <strong>💡 Bonus Layer — Voice AI (Vapi, Bland AI, ElevenLabs, Retell AI, Twilio):</strong> We also deploy ultra-low-latency voice agents that answer inbound customer calls, qualify leads, and book appointments directly onto calendars in natural human voices.
                    </div>
                </div>
            """
        },
        {
            "id": "pb1-p3",
            "phase": "PHASE 1A · INDUSTRY & MARKET (PAGE 3 OF 5)",
            "title": "Why 85% of Corporate AI Initiatives Fail Miserably",
            "tagline": "Every executive you call has either wasted money on a failed AI tool or is afraid of wasting money on one. Use that scar tissue to your advantage.",
            "keyTakeaways": [
                "Failure Reason #1: 'Shadow AI' & ChatGPT License Graveyards (buying 100 Copilot/ChatGPT Enterprise seats with zero workflow integration).",
                "Failure Reason #2: Automating Dirty Data & Undefined Processes (skipping the AI Readiness Audit).",
                "Failure Reason #3: Zero Human-in-the-Loop (HITL) Guardrails (letting an unguarded bot email customers directly).",
                "Failure Reason #4: No Telemetry or Baseline Measurement (nobody can prove to the CFO whether the tool saved a single dime)."
            ],
            "content": """
                <div class="prose-section">
                    <h3>The 4 Diseases Killing Corporate AI Projects Today</h3>
                    <p>When a prospect tells you, <em>"We tried AI six months ago and it didn't really move the needle,"</em> don't get defensive! Lean back, smile, and say: <em>"Let me guess—you bought a bunch of standalone licenses or bolted a chatbot onto an unmapped process, and after three weeks nobody was using it."</em></p>
                    <p>When you diagnose why their past attempt failed, you instantly establish yourself as an expert. Here are the four failure modes happening in the market right now:</p>

                    <ol>
                        <li><strong>The "License Graveyard" Illusion:</strong> A CEO buys 50 seats of Microsoft Copilot or ChatGPT Team thinking their staff will magically become 40% more productive. In reality, employees use it twice to write a birthday poem and go right back to their manual spreadsheets because <strong>training humans is hard; re-architecting the workflow is permanent</strong>.</li>
                        <li><strong>"Shadow AI" Compliance Nightmares:</strong> Because the company hasn't built a secure, SOC 2 / GDPR-aware internal AI pipeline, well-meaning employees paste confidential client financials and legal contracts into public free LLMs. Mention this to a CFO or General Counsel and watch their blood pressure spike.</li>
                        <li><strong>No Human-in-the-Loop (HITL) Checkpoints:</strong> Amateur agencies hook an LLM straight up to an outbound email server with no guardrails. The bot hallucinates a 90% discount, emails 400 clients, and gets fired. Every MAB AI agent ships with <strong>human-in-the-loop checkpoints and full audit logs</strong>.</li>
                        <li><strong>Zero ROI Telemetry:</strong> Nobody measured how long the process took <em>before</em> deployment, so nobody can prove what it saved <em>after</em> deployment. At MAB AI, <strong>every module ships measured</strong>.</li>
                    </ol>
                </div>
            """
        },
        {
            "id": "pb1-p4",
            "phase": "PHASE 1A · INDUSTRY & MARKET (PAGE 4 OF 5)",
            "title": "The Economics of Operational Drag: Where Companies Bleed Cash",
            "tagline": "Companies rarely go broke from one giant explosion. They bleed to death from ten thousand invisible 15-minute delays.",
            "keyTakeaways": [
                "Operational Drag is the compound tax of manual data entry, slow handoffs, context switching, and human error.",
                "Every time a human switches between two software tabs to copy-paste information, it costs 23 minutes of deep focus recovery.",
                "Our job is to make invisible operational drag painfully visible—and price it down to the hour."
            ],
            "content": """
                <div class="prose-section">
                    <h3>What Is "Operational Drag"?</h3>
                    <p>If a pipe bursts in a warehouse and floods the floor, the CEO fixes it in an hour because they can <em>see</em> the water. Operational drag is an <strong>invisible leak inside the payroll ledger</strong>.</p>
                    <p>Look at where a typical $20M/year mid-market company bleeds $250,000+ every single year without realizing it:</p>

                    <div class="table-wrapper">
                        <table class="playbook-table">
                            <thead>
                                <tr>
                                    <th>Department</th>
                                    <th>The Manual Chaos ("Human API" Work)</th>
                                    <th>Weekly Hours Lost</th>
                                    <th>Annual Cash Bleed</th>
                                    <th class="highlight-col">MAB AI Fix</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>Recruiting / HR</strong></td>
                                    <td>Screening resumes, scheduling screens, provisioning accounts</td>
                                    <td>15–25 hrs/wk</td>
                                    <td>$40,000 – $65,000/yr</td>
                                    <td class="highlight-col"><strong>Autonomous Vetting & Onboarding Agent</strong></td>
                                </tr>
                                <tr>
                                    <td><strong>Sales / RevOps</strong></td>
                                    <td>Researching leads, enriching CRM fields, typing call notes, slow speed-to-lead</td>
                                    <td>20–40 hrs/wk across team</td>
                                    <td>$80,000+ in lost pipeline</td>
                                    <td class="highlight-col"><strong>Lead Enricher + Zoom Summary + Outbound SDR Agent</strong></td>
                                </tr>
                                <tr>
                                    <td><strong>Finance / Admin</strong></td>
                                    <td>Scraping PDF invoices, chasing overdue receivables, reconciling ERP rows</td>
                                    <td>12–20 hrs/wk</td>
                                    <td>$35,000 + delayed cashflow</td>
                                    <td class="highlight-col"><strong>Receipt Scraper + Autonomous Invoice Chaser</strong></td>
                                </tr>
                                <tr>
                                    <td><strong>Customer Support / Ops</strong></td>
                                    <td>Answering repetitive Tier-1 status questions & manually creating Jira/ops tickets</td>
                                    <td>25–50 hrs/wk</td>
                                    <td>$75,000+ & slow SLAs</td>
                                    <td class="highlight-col"><strong>Support Triage Agent + Slack-to-Jira Pipeline</strong></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            """
        },
        {
            "id": "pb1-p5",
            "phase": "PHASE 1A · INDUSTRY & MARKET (PAGE 5 OF 5)",
            "title": "Market Positioning: Why the Mid-Market ($5M–$150M) Is Our Goldmine",
            "tagline": "Fortune 100 giants move at the speed of glaciers. Broke startups can't pay invoices. The SMB & Mid-Market arena is where deals close fast and compound for years.",
            "keyTakeaways": [
                "Our sweet spot: Established SMB and Mid-Market organizations ($5M to $150M in annual revenue, 20 to 500 employees).",
                "Why? They have real operational chaos, real payroll costs to offset, and direct access to C-Suite decision makers who can sign off in days rather than 14 months.",
                "How to crush the #1 market objection: 'Why shouldn't our internal IT team just build this?'"
            ],
            "content": """
                <div class="prose-section">
                    <h3>Why We Dominate the Mid-Market & Upper-SMB Space</h3>
                    <p>In B2B sales, picking the right pond to fish in is half the battle. Why is a $15M–$100M business the ultimate client for MAB AI Strategies?</p>
                    <ul>
                        <li><strong>They have outgrown manual processes:</strong> What worked when they had 8 employees in a garage is now breaking at 60 employees. They feel the pain acutely every single day.</li>
                        <li><strong>They cannot afford a $400,000 full-time Chief AI Officer + 3 ML Engineers:</strong> Hiring an internal AI team would cost them $800K+/year and take 9 months just to recruit. Hiring MAB AI Strategies on an <strong>Accelerator or Principal Retainer</strong> gives them an entire 16-year enterprise architecture team immediately at a fraction of the cost.</li>
                        <li><strong>Short Decision Cycles:</strong> You aren't navigating 19 layers of bureaucracy. You are talking directly to the CEO, COO, CFO, or VP of Operations.</li>
                    </ul>

                    <div class="founder-note">
                        <div class="founder-badge">OBJECTION CRUSHER · "OUR INTERNAL IT GUY CAN DO THIS"</div>
                        <p>When a prospect says, <em>"We have an IT director / developer internally who is looking into AI,"</em> never insult their IT guy. Say this instead:<br/><br/>
                        <strong>"That's great—having strong internal IT makes our deployments ten times smoother. What we find with 95% of our mid-market clients is that internal IT is already at 110% capacity keeping the lights on, managing security, and supporting staff tickets. Expecting them to also architect LangGraph agents and mine cross-departmental workflows from scratch usually delays ROI by 12 to 18 months. We partner with your IT lead, bring 250+ pre-built workflow templates, and deploy in weeks so they look like a hero."</strong></p>
                    </div>
                </div>
            """
        },

        # =====================================================================
        # PHASE 1B: INTRODUCTION TO SALES, SPECIFICALLY B2B (4 PAGES)
        # =====================================================================
        {
            "id": "pb1-p6",
            "phase": "PHASE 1B · B2B SALES FUNDAMENTALS (PAGE 1 OF 4)",
            "title": "B2C vs. B2B Sales: Dopamine vs. The P&L Statement",
            "tagline": "In B2C, people buy with their feelings to look cool or feel good. In B2B, companies buy for only three reasons—and if you can't tie your pitch to one of them, you're dead.",
            "keyTakeaways": [
                "The 3 Universal B2B Buying Drivers: (1) Make Money (Increase Revenue Velocity), (2) Save Money/Time (Convert Drag into Net Liquidity), (3) Reduce Risk (Compliance, SLA failure, turnover).",
                "In B2B, you are never spending the buyer's personal grocery money—you are reallocating corporate capital that must yield a positive return.",
                "Price is never the real issue in B2B when ROI is mathematically undeniable."
            ],
            "content": """
                <div class="prose-section">
                    <h3>Welcome to B2B (Business-to-Business) Sales</h3>
                    <p>If you've never worked in B2B sales before, forget every sleazy stereotype you've seen in movies. B2B enterprise sales is not about fast-talking someone into buying a timeshare they can't afford. <strong>B2B sales is commercial problem-solving backed by math.</strong></p>
                    <p>Every business on earth—whether they sell staffing, legal services, HVAC commercial installs, or SaaS—wakes up every morning trying to solve a simple equation on their Profit & Loss (P&L) statement. Every single dollar spent in B2B must map to one of the <strong>Three Executive Levers</strong>:</p>

                    <div class="tier-grid-3">
                        <div class="tier-card">
                            <div class="tier-badge">LEVER 01 · TOP LINE</div>
                            <h4>Increase Revenue</h4>
                            <p class="tier-desc">Speed up lead response times from 4 hours to 30 seconds, automate outbound prospecting, increase rep selling time from 30% to 75%, and convert more pipeline via Conversion Web Experiences.</p>
                        </div>
                        <div class="tier-card tier-featured">
                            <div class="tier-badge">LEVER 02 · BOTTOM LINE</div>
                            <h4>Increase Net Liquidity</h4>
                            <p class="tier-desc">Reclaim 15+ hours/week of high-cost human labor per workflow, avoid hiring 3 additional admin headcount ($195K/yr saved), and eliminate overtime and manual error rework.</p>
                        </div>
                        <div class="tier-card">
                            <div class="tier-badge">LEVER 03 · PROTECTION</div>
                            <h4>Eliminate Existential Risk</h4>
                            <p class="tier-desc">Prevent key data from walking out the door when an employee quits, enforce SOC 2 / GDPR governance over AI usage, and stop SLA breaches that cause client churn.</p>
                        </div>
                    </div>

                    <p class="mt-4">Notice how MAB AI Strategies hits <strong>all three levers simultaneously</strong>. When you talk to a Sales VP, pull Lever 1. When you talk to a COO or CFO, pull Lever 2. When you talk to a CTO or General Counsel, pull Lever 3.</p>
                </div>
            """
        },
        {
            "id": "pb1-p7",
            "phase": "PHASE 1B · B2B SALES FUNDAMENTALS (PAGE 2 OF 4)",
            "title": "Consultative Diagnostic Selling vs. 'Pitch-Slapping'",
            "tagline": "Prescription before diagnosis is malpractice—in medicine and in enterprise sales.",
            "keyTakeaways": [
                "'Pitch-Slapping' is showing up to a call and vomiting features for 20 minutes without knowing what hurts.",
                "Diagnostic Selling means acting like an elite orthopedic surgeon: ask sharp questions, take the X-ray, point to the fracture, and let the patient beg for the surgery.",
                "People argue with your claims, but they never argue with their own conclusions."
            ],
            "content": """
                <div class="prose-section">
                    <h3>Imagine Walking Into a Doctor's Office...</h3>
                    <p>Imagine you walk into a surgeon's office. Before you even sit down or say what hurts, the doctor bursts through the door waving a scalpel and yells: <em>"Good news! We're having a 20% off special on triple-bypass heart surgery today! I went to Johns Hopkins, my scalpels are German steel, let's get you on the table!"</em></p>
                    <p>You would run out of the building thinking the guy is a lunatic—even if he actually <em>did</em> go to Johns Hopkins! Why? Because <strong>he prescribed surgery before diagnosing your condition</strong>.</p>
                    <p>Yet 90% of rookie salespeople do that exact thing every day. They get an executive on the phone and immediately start word-vomiting: <em>"We build LangGraph agents and RAG pipelines and we have Foundation and Accelerator tiers!"</em> Stop doing that shit.</p>

                    <div class="comparison-grid">
                        <div class="comp-card comp-bad">
                            <h4>❌ The Rookie "Feature Vomiter"</h4>
                            <p>• Talks 80% of the time, listens 20%.<br/>
                            • Tries to sound smart by using technical buzzwords.<br/>
                            • Quotes prices before knowing what the problem costs the client.<br/>
                            • Gets hit with: <em>"Sounds interesting, send me some info and we'll look at it next quarter."</em></p>
                        </div>
                        <div class="comp-card comp-good">
                            <h4>✅ The MAB AI Diagnostic Architect</h4>
                            <p>• Listens 80% of the time, speaks 20%.<br/>
                            • Asks surgical questions that expose how many hours and dollars the client is losing right now.<br/>
                            • Gets the prospect to admit out loud: <em>"Holy shit, this manual process is costing us $9,000 every month."</em><br/>
                            • Positions our architecture as the obvious mathematical cure.</p>
                        </div>
                    </div>
                </div>
            """
        },
        {
            "id": "pb1-p8",
            "phase": "PHASE 1B · B2B SALES FUNDAMENTALS (PAGE 3 OF 4)",
            "title": "The Mathematics of B2B ROI: Pricing the Cost of Inaction",
            "tagline": "When you prove a prospect is burning $12,000 a month standing still, a $4,000 investment isn't an expense—it's an $8,000 monthly raise.",
            "keyTakeaways": [
                "Formula: Annual Operational Bleed = (Hours Lost/Week × People Involved × Fully Burdened Hourly Rate × 52 Weeks) + Annual Error/Delay Opportunity Cost.",
                "Never use base hourly wage alone; executives pay ~1.3x in taxes, benefits, and overhead ('Fully Burdened Rate').",
                "Use the interactive Cost-of-Inaction Calculator below to practice running live math with prospects."
            ],
            "content": """
                <div class="prose-section">
                    <h3>How to Run Live Napkin Math That Makes CFOs Salivate</h3>
                    <p>Nothing commands respect in a B2B meeting faster than doing calm, conservative math with the prospect's own numbers. Even if you hated math in high school, you only need one simple formula for the rest of your career at MAB AI Strategies:</p>
                    <div class="motto-banner">
                        <div class="motto-eyebrow">THE COST OF INACTION FORMULA</div>
                        <div class="motto-text">Weekly Hours Lost × Team Members × Hourly Cost × 52 Weeks = Annual Liquidity Bleed</div>
                    </div>

                    <!-- INTERACTIVE ROI & COST OF INACTION CALCULATOR -->
                    <div class="infographic-box" id="roi-calculator-box">
                        <div class="infographic-header">
                            <div>
                                <span class="badge-emerald">INTERACTIVE SIMULATOR</span>
                                <h4>LIVE B2B COST-OF-INACTION & PAYBACK CALCULATOR</h4>
                            </div>
                            <span class="text-xs font-mono text-zinc-400">ADJUST SLIDERS TO SEE REAL-TIME DISCOVERY MATH</span>
                        </div>

                        <div class="calc-grid">
                            <div class="calc-inputs">
                                <div class="calc-row">
                                    <label>Employees Touching This Manual Process: <strong id="calc-emp-val">3</strong></label>
                                    <input type="range" min="1" max="25" value="3" id="calc-emp" oninput="updateROICalc()" />
                                </div>
                                <div class="calc-row">
                                    <label>Hours Wasted Per Employee / Week: <strong id="calc-hrs-val">12 hrs</strong></label>
                                    <input type="range" min="2" max="30" value="12" id="calc-hrs" oninput="updateROICalc()" />
                                </div>
                                <div class="calc-row">
                                    <label>Fully Burdened Hourly Cost ($/hr): <strong id="calc-rate-val">$55/hr</strong></label>
                                    <input type="range" min="25" max="150" step="5" value="55" id="calc-rate" oninput="updateROICalc()" />
                                </div>
                            </div>
                            <div class="calc-results">
                                <div class="calc-stat-row">
                                    <span>Total Hours Burned / Year:</span>
                                    <strong id="calc-out-hrs" class="text-white">1,872 hrs/yr</strong>
                                </div>
                                <div class="calc-stat-row">
                                    <span>Cost of Standing Still (Monthly Bleed):</span>
                                    <strong id="calc-out-mo" class="text-rose-400">$8,580 / month</strong>
                                </div>
                                <div class="calc-stat-row">
                                    <span>Annual Recoverable Liquidity (80% Automated):</span>
                                    <strong id="calc-out-yr" class="text-emerald-400">$82,368 / year</strong>
                                </div>
                                <div class="calc-pitch-script" id="calc-out-script">
                                    "So conservatively, leaving this process manual is costing you $8,580 every single month—over $102K a year in payroll drag alone, before we even count missed revenue."
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            """
        },
        {
            "id": "pb1-p9",
            "phase": "PHASE 1B · B2B SALES FUNDAMENTALS (PAGE 4 OF 4)",
            "title": "Navigating the B2B Buying Committee: Champions, Buyers & Blockers",
            "tagline": "In B2B, the person who loves your idea isn't always the person who signs the Docusign—and the person who never joins the call can kill your deal in the hallway.",
            "keyTakeaways": [
                "The 4 Key Roles in any B2B Deal: (1) The Champion, (2) The Economic Buyer, (3) The Technical/Security Gatekeeper, (4) The End-User.",
                "Never confuse an enthusiastic Manager (Influence, No Money) with an Economic Buyer (Can say YES when everyone else says no, and NO when everyone else says yes).",
                "Always ask early: 'Besides yourself, who else weighs in when you approve an operational architecture investment like this?'"
            ],
            "content": """
                <div class="prose-section">
                    <h3>Who Is Sitting Around the Virtual Table?</h3>
                    <p>When you sell a $150 pair of sneakers, the person trying on the shoes is the user, the evaluator, and the wallet. In B2B sales, those functions are split across multiple human beings with competing agendas:</p>

                    <div class="module-cards-grid">
                        <div class="spec-card">
                            <div class="spec-num">ROLE 01 · THE CHAMPION</div>
                            <h4>The Operational Pain-Bearer (Usually COO, VP Ops, Director of Staff, VP Sales)</h4>
                            <p>They feel the pain every day. Their team is working until 8 PM, and their KPIs are suffering. They want MAB AI to win because our automation makes them look like a genius and gives them their life back. <strong>Your job:</strong> Arm your Champion with hard ROI math so they can sell internally when you aren't in the room.</p>
                        </div>
                        <div class="spec-card">
                            <div class="spec-num">ROLE 02 · THE ECONOMIC BUYER</div>
                            <h4>The P&L Owner (CEO, Founder, Managing Partner, CFO)</h4>
                            <p>They control the budget and have final veto power. They don't care which Python library we use; they care about <strong>payback window, net liquidity, and strategic moat</strong>. <strong>Your job:</strong> Get the Economic Buyer on the Strategic Briefing or Architecture Readout call—never rely solely on a mid-level manager to pitch the CEO for you.</p>
                        </div>
                        <div class="spec-card">
                            <div class="spec-num">ROLE 03 · THE TECHNICAL GATEKEEPER</div>
                            <h4>The Guardian of the Stack (CTO, VP of IT, InfoSec Lead)</h4>
                            <p>They rarely have budget to buy, but they have the power to say <em>"No, this is a security risk."</em> They fear shadow AI, messy code, and extra maintenance work. <strong>Your job:</strong> Neutralize their fear early by emphasizing our SOC 2 / GDPR governance, human-in-the-loop audit logs, and zero-maintenance delivery.</p>
                        </div>
                        <div class="spec-card">
                            <div class="spec-num">ROLE 04 · THE SILENT BLOCKER</div>
                            <h4>The Status-Quo Defender (Insecure Middle Manager)</h4>
                            <p>Occasionally, a middle manager whose entire job is compiling manual Friday spreadsheets gets terrified that automation will expose how little strategic value they add. <strong>Your job:</strong> Frame our motto clearly—we automate the drudgery so human staff can be elevated into higher-leverage strategy and leadership.</p>
                        </div>
                    </div>
                </div>
            """
        },

        # =====================================================================
        # PHASE 1C: INTRODUCTION TO ICP AND DECISION MAKERS (3 PAGES)
        # =====================================================================
        {
            "id": "pb1-p10",
            "phase": "PHASE 1C · ICP & DECISION MAKERS (PAGE 1 OF 3)",
            "title": "Our Ideal Customer Profile (ICP) Blueprint",
            "tagline": "If you pitch a $50,000 architecture engine to a broke guy running a lemonade stand, you will starve. Hunt where the liquidity lives.",
            "keyTakeaways": [
                "Firmographic Sweet Spot: $5M–$150M annual revenue, 20–500 employees, U.S. / North America & English-speaking global operators.",
                "Technographic Sweet Spot: Already using modern cloud tools (Salesforce/HubSpot/Pipedrive, Slack/Teams, Google Workspace/M365, QuickBooks/NetSuite, Greenhouse/Bullhorn) with APIs we can wire together.",
                "Psychographic Sweet Spot: Growth-oriented leadership frustrated by operational bottlenecks or rising payroll costs."
            ],
            "content": """
                <div class="prose-section">
                    <h3>What Is an ICP (Ideal Customer Profile)?</h3>
                    <p>Your most precious asset as a Senior Account Executive isn't your laptop—it's the 40 to 50 hours of prime calling and selling windows you get each week. Spending those hours chasing companies that either <strong>don't have the problem</strong> or <strong>can't afford the solution</strong> is financial suicide.</p>
                    <p>Before you add a single company to your worklist in Playbook 2, run them through the <strong>MAB AI 4-Point ICP Filter</strong>:</p>

                    <div class="stat-grid-4">
                        <div class="stat-card">
                            <span class="stat-num">$5M–$150M</span>
                            <span class="stat-label">Annual Revenue Sweet Spot</span>
                        </div>
                        <div class="stat-card">
                            <span class="stat-num">20–500</span>
                            <span class="stat-label">Employee Headcount Range</span>
                        </div>
                        <div class="stat-card">
                            <span class="stat-num">3+ Tools</span>
                            <span class="stat-label">Disconnected Cloud Software Silos</span>
                        </div>
                        <div class="stat-card">
                            <span class="stat-num">&gt;$150K/yr</span>
                            <span class="stat-label">Estimated Admin / Ops Payroll Drag</span>
                        </div>
                    </div>

                    <h3>Why "3+ Disconnected Cloud Tools" Is the Ultimate Tell</h3>
                    <p>When a company uses HubSpot for sales, Bullhorn or Greenhouse for recruiting, Slack for internal comms, and QuickBooks or NetSuite for billing—guess who is connecting those four tools? <strong>Overpaid humans playing copy-paste monkey 15 hours a week.</strong> That gap between their tools is where MAB AI Strategies prints money.</p>
                </div>
            """
        },
        {
            "id": "pb1-p11",
            "phase": "PHASE 1C · ICP & DECISION MAKERS (PAGE 2 OF 3)",
            "title": "Inside the Minds of C-Suite Decision Makers (The Business Council Matrix)",
            "tagline": "Never pitch a CFO the way you pitch a VP of Sales. Speak the exact dialect of the executive sitting across from you.",
            "keyTakeaways": [
                "CEO / Founder: Speaks in Enterprise Valuation, Margin Expansion, Scaling Without Headcount Bloat, and Competitive Moat.",
                "COO / VP of Operations / Director of Staff: Speaks in Throughput, SLA Consistency, Bottleneck Elimination, and Reclaimed Hours.",
                "CFO (Marcus): Speaks in Payback Period (<90 days), Net Liquidity, OpEx Reduction, and Risk-Adjusted ROI.",
                "CRO / VP of Sales (Titan): Speaks in Speed-to-Lead, Pipeline Velocity, Rep Quota Attainment, and Zero CRM Admin.",
                "CTO / VP of Engineering (Cipher): Speaks in API Security, SOC 2 / GDPR Compliance, Vendor Neutrality, and Zero Tech Debt."
            ],
            "content": """
                <div class="prose-section">
                    <h3>Matching Your Pitch to the Executive's Scoreboard</h3>
                    <p>Remember <strong>The Business Council</strong> from Mark's Intelligence Library? Every executive wakes up staring at a different scoreboard. If you talk about "clean Python code" to a CFO, their eyes glaze over. If you talk about "EBITDA payback" to an IT Director, they tune out. Use this translation matrix on every call:</p>

                    <div class="table-wrapper">
                        <table class="playbook-table">
                            <thead>
                                <tr>
                                    <th>Title / Persona</th>
                                    <th>What Keeps Them Awake at 2 AM</th>
                                    <th>Words That Turn Them Off</th>
                                    <th class="highlight-col">Words That Make Them Lean In</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>CEO / Founder</strong></td>
                                    <td>Competitors moving faster; revenue stalling because ops can't scale without hiring 10 more people</td>
                                    <td>"Webhooks, JSON, prompts, zapier zaps"</td>
                                    <td class="highlight-col"><strong>"Scale output 10% YoY without adding payroll; build an autonomous moat before your competitors do."</strong></td>
                                </tr>
                                <tr>
                                    <td><strong>COO / Director of Staff</strong></td>
                                    <td>Balls dropping between departments; spending 15 hrs/wk babysitting repetitive handoffs</td>
                                    <td>"High-level futuristic AI theory"</td>
                                    <td class="highlight-col"><strong>"Reclaim 15+ hours a week per workflow with 24/7 failure-recovered execution wired into your stack."</strong></td>
                                </tr>
                                <tr>
                                    <td><strong>CFO (Marcus)</strong></td>
                                    <td>Wasting budget on shelfware; bloated SG&A payroll; unmeasured consulting bills</td>
                                    <td>"Cool shiny AI experiment"</td>
                                    <td class="highlight-col"><strong>"Price the cost of inaction down to the hour; $40K annual net liquidity per deployment; 90-day ROI guarantee."</strong></td>
                                </tr>
                                <tr>
                                    <td><strong>CRO / VP of Sales (Titan)</strong></td>
                                    <td>Reps spending 4 hours a day on admin instead of selling; leads waiting 6 hours for a call</td>
                                    <td>"More mandatory forms for reps"</td>
                                    <td class="highlight-col"><strong>"Instant speed-to-lead enrichment, automated CRM logging from Zoom, and 2x selling time per rep."</strong></td>
                                </tr>
                                <tr>
                                    <td><strong>CTO / VP IT (Cipher)</strong></td>
                                    <td>Employees pasting company data into public ChatGPT; brittle tools IT has to fix</td>
                                    <td>"No-code magic black box"</td>
                                    <td class="highlight-col"><strong>"SOC 2 / GDPR-aware governance, human-in-the-loop guardrails, vendor-neutral stack, full audit logs."</strong></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            """
        },
        {
            "id": "pb1-p12",
            "phase": "PHASE 1C · ICP & DECISION MAKERS (PAGE 3 OF 3)",
            "title": "The Anti-ICP: Who to Disqualify in Under 90 Seconds",
            "tagline": "Every hour you spend humoring a broke tire-kicker is an hour you stole from a $50,000 Accelerator client.",
            "keyTakeaways": [
                "Disqualify 'Wantrepreneurs' with pre-revenue ideas who want you to build their SaaS startup for equity.",
                "Disqualify companies with <5 employees and zero repeatable processes (there is no volume to automate).",
                "Disqualify prospects who refuse to share basic operational metrics or bring the Economic Buyer to the Architecture Readout."
            ],
            "content": """
                <div class="prose-section">
                    <h3>Protect Your Pipeline From Time Vampires</h3>
                    <p>When you are brand new to sales, getting <em>anyone</em> to talk to you on the phone feels exciting. You'll be tempted to spend three hours chatting with a guy who has a "billion-dollar AI app idea" and $400 in his checking account. <strong>Don't do it.</strong></p>
                    <p>At MAB AI Strategies, we disqualify ruthlessly when we see any of these 4 Red Flags:</p>
                    <ul>
                        <li>🚩 <strong>Red Flag 1: "Will you build my startup for a % of future profits?"</strong> No. We are an enterprise AI architecture consultancy, not a venture capital charity.</li>
                        <li>🚩 <strong>Red Flag 2: Zero Process Volume.</strong> If a task only happens twice a month and takes 10 minutes, automating it saves 4 hours a year. We look for high-frequency bottlenecks burning 10 to 100+ hours every single week.</li>
                        <li>🚩 <strong>Red Flag 3: Shopping for $8/hr Offshore Virtual Assistants.</strong> If their mindset is "find the cheapest warm body overseas," they won't value precision engineering.</li>
                        <li>🚩 <strong>Red Flag 4: Secretive / Combative on Discovery.</strong> If a prospect says, <em>"I won't tell you what tools we use or what our bottlenecks are, just send me a price list,"</em> politely end the call. Doctors don't write prescriptions for patients who refuse to take off their coat.</li>
                    </ul>
                </div>
            """
        },

        # =====================================================================
        # PHASE 1D: INTRODUCTION TO VERTICALS AND LOW-HANGING FRUIT (3 PAGES)
        # =====================================================================
        {
            "id": "pb1-p13",
            "phase": "PHASE 1D · VERTICALS & LOW-HANGING FRUIT (PAGE 1 OF 3)",
            "title": "Our Top 4 High-Yield Industry Verticals",
            "tagline": "Where paper, people, and repetitive coordination collide—that is where MAB AI Strategies prints ROI.",
            "keyTakeaways": [
                "Vertical 1: Staffing, Recruiting & Executive Search (Candidate vetting, outreach, onboarding — proven 15 hr/wk & $40K liquidity anchor).",
                "Vertical 2: B2B Professional Services, Legal, Accounting & Marketing Agencies (Client onboarding, document review, reporting, invoice chasing).",
                "Vertical 3: Logistics, Supply Chain, Commercial Construction & Field Services (Quote generation, vendor reconciliation, dispatch routing).",
                "Vertical 4: Financial Services, Insurance, Real Estate & Healthcare Admin (Intake triage, compliance auditing, policy/document extraction)."
            ],
            "content": """
                <div class="prose-section">
                    <h3>Where Should You Hunt First?</h3>
                    <p>While our architecture works across any B2B company with 20–500 employees, four specific verticals close fastest because they are drowning in high-volume administrative coordination:</p>

                    <div class="module-cards-grid">
                        <div class="spec-card">
                            <div class="spec-num">VERTICAL 01 · OUR SLAM DUNK</div>
                            <h4>Staffing, Recruiting & HR Firms</h4>
                            <p><strong>Why they bleed:</strong> Recruiters and Directors of Staff spend 60% of their week reading resumes, matching keywords, sending initial outreach, scheduling interviews, and chasing onboarding paperwork.</p>
                            <p class="mt-2 text-emerald-400"><strong>Your Anchor Proof:</strong> Our Director of Staff deployment reclaimed 15 hrs/wk and ~$40K annual net liquidity from one agent.</p>
                        </div>
                        <div class="spec-card">
                            <div class="spec-num">VERTICAL 02 · HIGH MARGIN, HIGH DRAG</div>
                            <h4>Professional Services (Legal, CPA, Agencies, Consultancies)</h4>
                            <p><strong>Why they bleed:</strong> Highly paid partners ($300–$600/hr billable value) and account managers waste hours provisioning new client workspaces, compiling monthly KPI reports, reviewing standard contracts, and chasing overdue invoices.</p>
                            <p class="mt-2 text-emerald-400"><strong>Your Anchor Proof:</strong> Onboarding Bot + Contract Sentinel + QBR Wizard + Invoice Chaser.</p>
                        </div>
                        <div class="spec-card">
                            <div class="spec-num">VERTICAL 03 · OPERATIONAL HEAVYWEIGHTS</div>
                            <h4>Logistics, Distribution & Commercial Field Ops</h4>
                            <p><strong>Why they bleed:</strong> Every shipment, RFP, or work order generates PDFs, emails, and ERP updates. Dispatchers and ops coordinators manually key data from emails into legacy ERPs all day.</p>
                            <p class="mt-2 text-emerald-400"><strong>Your Anchor Proof:</strong> Receipt/Document Scraper + Real-Time Data Synthesis + ERP Automation.</p>
                        </div>
                        <div class="spec-card">
                            <div class="spec-num">VERTICAL 04 · COMPLIANCE & INTAKE INTENSIVE</div>
                            <h4>Financial Advisory, Insurance, Real Estate & Healthcare Admin</h4>
                            <p><strong>Why they bleed:</strong> Massive client intake forms, document verification checklists, Tier-1 status inquiries, and strict compliance requirements (SOC 2 / HIPAA / GDPR governance).</p>
                            <p class="mt-2 text-emerald-400"><strong>Your Anchor Proof:</strong> Support Triage Agent + RAG over proprietary policy docs + Guardrailed Workflows.</p>
                        </div>
                    </div>
                </div>
            """
        },
        {
            "id": "pb1-p14",
            "phase": "PHASE 1D · VERTICALS & LOW-HANGING FRUIT (PAGE 2 OF 3)",
            "title": "How to Spot 'Low-Hanging Fruit' Triggers in 60 Seconds",
            "tagline": "Don't knock on random doors hoping someone is hungry. Look for the smoke pouring out of the kitchen window.",
            "keyTakeaways": [
                "Trigger #1: Active Job Postings for Admin/Ops Roles (Recruiting Coordinator, Sales Ops Analyst, Billing Specialist, Customer Support Rep).",
                "Trigger #2: New Executive Hire in the Last 90 Days (New COO, CFO, or VP of Sales has a 90-day mandate to improve efficiency).",
                "Trigger #3: M&A / Private Equity Acquisition or Rapid Headcount Growth (2+ legacy tech stacks colliding in chaos).",
                "Trigger #4: Public Tech Stack & Hiring Clues on LinkedIn."
            ],
            "content": """
                <div class="prose-section">
                    <h3>The #1 Low-Hanging Fruit Hack in B2B AI Sales: The Job-Board Arbitrage</h3>
                    <p>Want to know how to book 3x more meetings than an average rep? Go onto LinkedIn Jobs or Indeed and look at mid-market companies currently trying to hire a <strong>$55,000–$75,000 Operations Coordinator, Recruiting Coordinator, Sales Operations Admin, or Data Entry Specialist</strong>.</p>
                    <p>Why did that company post that job? <strong>Because they have a bottleneck that is currently overwhelming their team, AND they have already approved $60,000+ in budget to solve it!</strong></p>

                    <div class="founder-note">
                        <div class="founder-badge">THE JOB-POSTING ARBITRAGE HOOK</div>
                        <p>"Hey [Name] — saw you're hiring a Recruiting Coordinator right now to handle candidate screening, interview scheduling, and onboarding handoffs. Before you spend $65K+ in salary and 90 days ramping a new hire, we just deployed an autonomous agent for a Director of Staff that handles that exact workflow 24/7—reclaiming 15 hours a week and ~$40K in annual net liquidity. Worth a 15-minute look to see if you can automate 80% of that role before hiring?"</p>
                    </div>

                    <h3>3 More Buying Signals That Scream "Call Me Today"</h3>
                    <ol>
                        <li><strong>The "New Sheriff in Town" Signal (Exec Hired &lt;90 Days Ago):</strong> When a company hires a new COO, CFO, or VP of Sales, that executive was hired to fix something broken. They have zero emotional attachment to the old, messy way of doing things and want a fast win in their first 90 days.</li>
                        <li><strong>Post-Merger / PE Roll-Up Chaos:</strong> Private Equity-backed companies that just acquired two smaller competitors are living in absolute data hell—three different CRMs, three different invoicing processes, and angry boards demanding margin expansion.</li>
                        <li><strong>Rapid Headcount Surge Without Ops Growth:</strong> If a company grew Sales headcount by 30% on LinkedIn over the last 6 months, but their Operations team stayed flat, their back-office is guaranteed to be on fire.</li>
                    </ol>
                </div>
            """
        },
        {
            "id": "pb1-p15",
            "phase": "PHASE 1D · VERTICALS & LOW-HANGING FRUIT (PAGE 3 OF 3)",
            "title": "Interactive Vertical → Wedge Offer Mapper",
            "tagline": "Select any target vertical below to generate their bleeding pains, low-hanging fruit triggers, and our exact wedge pitch.",
            "keyTakeaways": [
                "Customize your terminology to the prospect's vertical (Staffing calls customers 'Clients & Candidates'; Legal calls them 'Matters & Retainers'; Logistics calls them 'Shippers & Carriers').",
                "Use the mapper below whenever you build a vertical-specific worklist."
            ],
            "content": """
                <div class="prose-section">
                    <div class="infographic-box" id="vertical-mapper-box">
                        <div class="infographic-header">
                            <div>
                                <span class="badge-electric">INTERACTIVE PLAYBOOK TOOL</span>
                                <h4>VERTICAL PAIN → LOW-HANGING FRUIT → WEDGE PRESCRIPTION</h4>
                            </div>
                            <span class="text-xs font-mono text-zinc-400">CLICK A VERTICAL TO LOAD BATTLE CARD</span>
                        </div>

                        <div class="scenario-btn-grid">
                            <button class="scen-btn active" onclick="selectVerticalCard(0)" id="vert-btn-0">1. Staffing & Recruiting</button>
                            <button class="scen-btn" onclick="selectVerticalCard(1)" id="vert-btn-1">2. Legal, CPA & B2B Agencies</button>
                            <button class="scen-btn" onclick="selectVerticalCard(2)" id="vert-btn-2">3. Logistics & Field Ops</button>
                            <button class="scen-btn" onclick="selectVerticalCard(3)" id="vert-btn-3">4. Wealth, Insurance & Healthcare Admin</button>
                        </div>

                        <div class="scen-output" id="vert-output">
                            <div class="scen-col">
                                <span class="scen-label">BLEEDING OPERATIONAL PAINS</span>
                                <h4 id="vert-pain-title" class="text-rose-400">Manual Resume Screening & Onboarding Lag</h4>
                                <p id="vert-pain-desc">Recruiters waste 15+ hrs/wk reading unqualified resumes in Bullhorn/Greenhouse, playing calendar tag, and manually chasing I-9s and onboarding packets.</p>
                            </div>
                            <div class="scen-col">
                                <span class="scen-label">LOW-HANGING TRIGGER TO SPOT</span>
                                <h4 id="vert-trig-title" class="text-gold">Hiring "Recruiting Coordinator" or "Talent Ops"</h4>
                                <p id="vert-trig-desc">Filter Apollo/LinkedIn for Staffing agencies (25–200 headcount) with open job reqs for Coordinators or Directors of Staff.</p>
                            </div>
                            <div class="scen-col">
                                <span class="scen-label">EXACT WEDGE & RETAINER PATH</span>
                                <h4 id="vert-wedge-title" class="text-emerald-400">Single Agent Build → Accelerator</h4>
                                <p id="vert-wedge-desc">Lead with our proven 15 hr/wk & $40K liquidity Director of Staff deployment (5–15 day build), then expand across outbound sourcing and CRM hygiene on Accelerator.</p>
                            </div>
                        </div>
                    </div>
                </div>
            """
        },

        # =====================================================================
        # PHASE 1E: INTRODUCTION TO PROSPECTING, OUTREACH AND SEQUENCING (2 PAGES)
        # =====================================================================
        {
            "id": "pb1-p16",
            "phase": "PHASE 1E · PROSPECTING & SEQUENCING (PAGE 1 OF 2)",
            "title": "The Multi-Channel Orchestration Engine: Why Single-Channel Reps Starve",
            "tagline": "Email alone gets buried. Cold calls alone have no visual proof. LinkedIn alone is too slow. Orchestrate all three and you become unavoidable.",
            "keyTakeaways": [
                "It takes an average of 6 to 9 high-value touches across multiple channels to book a C-Suite / VP meeting in modern B2B.",
                "A 'Sequence' is a structured, multi-day choreography of Email + Phone + LinkedIn touches designed to build familiarity and curiosity—never annoyance.",
                "Every touch must introduce a fresh angle (Trigger -> Case Study -> Cost of Inaction -> Breakup), never 'Just checking in on my last email.'"
            ],
            "content": """
                <div class="prose-section">
                    <h3>What Is Outbound Sequencing?</h3>
                    <p>When a green salesperson sends one cold email to a CEO, gets no reply in 24 hours, and says, <em>"Well, I guess they aren't interested,"</em> I want to throw my coffee mug through a wall. Busy executives get 150 emails a day. Missing your first email doesn't mean they hate you; it means they were in a board meeting when it landed.</p>
                    <p><strong>Sequencing</strong> is the systematic choreography of touches across <strong>Email, Phone, and LinkedIn</strong> over a 14-to-21-day window so that your name, MAB AI Strategies, and our <em>Chaos → Consistency → Currency</em> thesis register across multiple mediums.</p>

                    <div class="table-wrapper">
                        <table class="playbook-table">
                            <thead>
                                <tr>
                                    <th>Day</th>
                                    <th>Channel Combo</th>
                                    <th>Strategic Angle of the Touch</th>
                                    <th>Goal</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>Day 1</strong></td>
                                    <td>📧 Email #1 + 🔗 LinkedIn View/Connect</td>
                                    <td><strong>The Signal + Field Evidence Hook:</strong> Reference specific company trigger + Director of Staff 15 hr/wk ($40K) proof point.</td>
                                    <td>Spark immediate curiosity</td>
                                </tr>
                                <tr>
                                    <td><strong>Day 2</strong></td>
                                    <td>📞 Cold Call #1 (Morning Block)</td>
                                    <td><strong>The Direct Pattern Interrupt:</strong> Reference the note sent yesterday; ask one diagnostic question; pitch 30-min Strategic Briefing.</td>
                                    <td>Live conversation or crisp 20-sec voicemail</td>
                                </tr>
                                <tr>
                                    <td><strong>Day 4</strong></td>
                                    <td>📧 Email #2 (Reply in Thread)</td>
                                    <td><strong>The Cost-of-Inaction Math Angle:</strong> Share quick napkin math on what manual handoffs in their vertical cost per month.</td>
                                    <td>Appeal to analytical / CFO brain</td>
                                </tr>
                                <tr>
                                    <td><strong>Day 7</strong></td>
                                    <td>📞 Cold Call #2 + 💬 LinkedIn Voice/Note</td>
                                    <td><strong>The "Built, Not Bolted On" Architecture Angle:</strong> Contrast native stack integration vs. shelfware tools.</td>
                                    <td>Multi-channel familiarity</td>
                                </tr>
                                <tr>
                                    <td><strong>Day 10</strong></td>
                                    <td>📧 Email #3</td>
                                    <td><strong>The 30-Minute Roadmap Offer:</strong> Highlight that the Strategic Briefing leaves them with a free 3-workflow ROI roadmap either way.</td>
                                    <td>Eliminate perceived risk</td>
                                </tr>
                                <tr>
                                    <td><strong>Day 14</strong></td>
                                    <td>📞 Call #3 + 📧 Email #4 (Breakup)</td>
                                    <td><strong>The Polite Walk-Away ("Win Fast, Lose Fast"):</strong> "Assuming automating [X] isn't a Q3 priority—closing your file for now."</td>
                                    <td>Trigger loss aversion (often gets highest reply rate!)</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            """
        },
        {
            "id": "pb1-p17",
            "phase": "PHASE 1E · PROSPECTING & SEQUENCING (PAGE 2 OF 2)",
            "title": "Signal-Based Precision vs. 'Spray-and-Pray' AI Slop",
            "tagline": "Every lazy rep on earth is using ChatGPT to blast 5,000 generic emails that start with 'I hope this email finds you well.' Stand out by being surgical.",
            "keyTakeaways": [
                "Never use cliché AI filler ('I hope this email finds you thriving', 'In today's fast-paced digital landscape', 'Delve into revolutionary synergies').",
                "Keep cold emails under 90 words—readable on an iPhone screen without scrolling.",
                "Signal-based outreach converts at 8x–12x the rate of generic blasts while protecting our domain reputation."
            ],
            "content": """
                <div class="prose-section">
                    <h3>The Death of Generic Outbound</h3>
                    <p>Because we are an elite AI strategy firm, our outreach must look like it was written by a sharp human executive—<strong>never like a cheap spam bot</strong>. Look at the difference:</p>

                    <div class="comparison-grid">
                        <div class="comp-card comp-bad">
                            <h4>🤮 Generic "AI Slop" (Instant Spam Report)</h4>
                            <p><em>"Dear Sir/Madam, I hope this email finds you well in today's rapidly evolving business landscape! At MAB AI Strategies, we leverage cutting-edge revolutionary artificial intelligence synergies to delve into your digital transformation journey..."</em><br/><br/><strong>Verdict:</strong> Every executive deletes this within 0.4 seconds.</p>
                        </div>
                        <div class="comp-card comp-good">
                            <h4>⚡ MAB AI Signal-Based Precision (Books the Call)</h4>
                            <p><em>"Sarah — noticed Apex Staffing has 3 open reqs for Recruiting Coordinators alongside your Bullhorn rollout. Before adding $180K in manual admin payroll, we deployed an autonomous vetting & onboarding agent for a Director of Staff that reclaimed 15 hrs/wk (~$40K annual net liquidity). Open to a 30-min briefing where we map your top 3 ROI automations?"</em></p>
                        </div>
                    </div>
                </div>
            """
        },

        # =====================================================================
        # PHASE 1F: INTRODUCTION TO CRM — HOW TO USE AND WHY (2 PAGES)
        # =====================================================================
        {
            "id": "pb1-p18",
            "phase": "PHASE 1F · NEXUS CRM MASTERY (PAGE 1 OF 2)",
            "title": "Introduction to Nexus CRM: Why It Exists & How It Prints Money",
            "tagline": "Rule #1 of MAB AI Sales Operations: If it isn't in Nexus CRM, it didn't fucking happen.",
            "keyTakeaways": [
                "A CRM (Customer Relationship Management system) is not a 'big brother surveillance tool'—it is your external brain and commission vault.",
                "At MAB AI Strategies, we use Nexus CRM to track every Account, Contact, Signal, Activity, Discovery Pain Metric, Deal Stage, and Next Step.",
                "Why? Because human memory leaks 70% of details within 24 hours, and unlogged deals die in the cracks."
            ],
            "content": """
                <div class="prose-section">
                    <h3>What Is a CRM, and Why Do Rookies Fight It While Pros Worship It?</h3>
                    <p>If you are brand new to sales, CRM stands for <strong>Customer Relationship Management</strong>. At MAB AI Strategies, our central command center is <strong>Nexus CRM</strong>.</p>
                    <p>Amateur salespeople treat the CRM like homework they have to do on Friday afternoon so the boss doesn't yell at them. Top 1% Account Executives treat <strong>Nexus CRM</strong> like a cockpit instrument panel flying a fighter jet at night. Here is why:</p>
                    <ul>
                        <li><strong>You cannot juggle 80 active conversations in your head:</strong> In week one, you might remember that the COO at Acme Corp told you to call back after their board meeting on the 14th. By week six, when you have 120 prospects in flight, you will forget—and a competitor will take the deal.</li>
                        <li><strong>It powers our own internal AI automations:</strong> When you log clean data in Nexus CRM, our internal workflows (<em>Briefing Bot, Zoom Summary, Proposal Generator, Onboarding Bot</em>) automatically fire using that data. Garbage in = garbage out.</li>
                        <li><strong>It protects your territory and commissions:</strong> Ownership of an account or opportunity is determined strictly by active, documented touches and dated Next Steps in Nexus CRM.</li>
                    </ul>
                </div>
            """
        },
        {
            "id": "pb1-p19",
            "phase": "PHASE 1F · NEXUS CRM MASTERY (PAGE 2 OF 2)",
            "title": "The Architecture of Nexus CRM: Objects, Pipeline Stages & Non-Negotiable Rules",
            "tagline": "Learn the 4 core objects and the Iron Law of the Dated Next Step.",
            "keyTakeaways": [
                "The 4 Core Objects in Nexus CRM: (1) Account (the company), (2) Contact (the people), (3) Opportunity/Deal (the revenue engagement), (4) Activity/Task (calls, emails, meetings, next steps).",
                "The Iron Law of Nexus CRM: Zero active Opportunities may ever exist without a future-dated Next Step Task.",
                "Every Discovery call must log Quantified Pain (hrs/wk + $/yr), Tech Stack, Decision Makers, and Recommended Tier."
            ],
            "content": """
                <div class="prose-section">
                    <h3>The 4 Core Building Blocks Inside Nexus CRM</h3>
                    <div class="module-cards-grid">
                        <div class="spec-card">
                            <div class="spec-num">OBJECT 01 · ACCOUNT</div>
                            <h4>The Company Record</h4>
                            <p>Stores company-level intelligence: Domain, Vertical, Annual Revenue ($M), Employee Headcount, Current Tech Stack (CRM/ATS/ERP), and Buying Signals (e.g., open job postings).</p>
                        </div>
                        <div class="spec-card">
                            <div class="spec-num">OBJECT 02 · CONTACT</div>
                            <h4>The Human Decision Makers</h4>
                            <p>Linked to the Account. Stores Name, Title, Verified Email, Direct Mobile Phone, LinkedIn URL, and Persona Tag (<em>Economic Buyer, Champion, Technical Gatekeeper</em>).</p>
                        </div>
                        <div class="spec-card">
                            <div class="spec-num">OBJECT 03 · OPPORTUNITY (DEAL)</div>
                            <h4>The Revenue Container</h4>
                            <p>Created once a Strategic Briefing is booked. Tracks Deal Stage, Recommended Offer (e.g., <em>AI Readiness Audit, Accelerator Retainer</em>), Estimated Contract Value, Quantified Client Pain ($/yr), and Close Date.</p>
                        </div>
                        <div class="spec-card">
                            <div class="spec-num">OBJECT 04 · ACTIVITY & NEXT STEP</div>
                            <h4>The Pulse of the Deal</h4>
                            <p>Every call, email, Gemini Notebook link, and meeting summary—plus the mandatory <strong>Dated Next Step Task</strong> that drives the deal forward.</p>
                        </div>
                    </div>

                    <div class="callout-warning">
                        <strong>🔒 The Iron Law of Nexus CRM:</strong> Every single open Opportunity in your pipeline MUST have a concrete, future-dated <strong>Next Step Task</strong> attached to it at all times. If a deal does not have a scheduled next step on the calendar, it is not a real deal—it is a wish.
                    </div>
                </div>
            """
        },

        # =====================================================================
        # PHASE 1G: INTRODUCTION TO SALES PSYCHOLOGY AND STRATEGY (3 PAGES)
        # =====================================================================
        {
            "id": "pb1-p20",
            "phase": "PHASE 1G · SALES PSYCHOLOGY & STRATEGY (PAGE 1 OF 3)",
            "title": "Status, Frame Control & Killing 'Commission Breath'",
            "tagline": "Executives can smell a desperate salesperson through a fiber-optic cable from 2,000 miles away.",
            "keyTakeaways": [
                "'Commission Breath' is the needy, over-eager vocal tone and behavior of a rep who acts like the prospect is doing them a favor.",
                "Peer-to-Peer Diagnostic Frame: You are not a beggar asking for alms; you are an architectural specialist evaluating whether their business qualifies for one of our scarce deployment slots.",
                "High-status behaviors: Calm vocal pacing, comfortable silence, zero apologies for calling, and willingness to walk away if there is no fit."
            ],
            "content": """
                <div class="prose-section">
                    <h3>What Is "Commission Breath"—And How Do You Kill It?</h3>
                    <p>Have you ever walked onto a car lot and had a salesperson sprint toward you with wide, desperate eyes because they haven't sold a car all month and rent is due tomorrow? You immediately put your guard up, right? That stench of desperation is called <strong>Commission Breath</strong>.</p>
                    <p>In B2B executive sales, Commission Breath manifests as:</p>
                    <ul>
                        <li>Talking at 200 miles per hour in a high-pitched, overly bubbly voice.</li>
                        <li>Apologizing for existing: <em>"I'm so sorry to bother you, I know you're super busy..."</em></li>
                        <li>Agreeing with everything the prospect says like a bobblehead doll instead of challenging their assumptions.</li>
                        <li>Chasing prospects with <em>"Just checking in!!"</em> emails when they haven't earned the next step.</li>
                    </ul>

                    <h3>Adopting the "Scarce Architect" Frame</h3>
                    <p>Remember what <a href="https://mabaistrategies.com" target="_blank" class="text-electric underline">mabaistrategies.com</a> states on <em>The Convergence</em> section: <strong>"Slots are deliberately scarce."</strong> Because every client gets direct architectural access to Mark Bockrath rather than an offshore factory, we literally <em>cannot</em> take every company that wants to work with us.</p>
                    <p>When you internalize that truth, your entire posture changes. You are not calling to beg for their money; you are calling to <strong>see if their operational drag is big enough and their leadership is decisive enough to warrant one of our deployment slots</strong>.</p>
                </div>
            """
        },
        {
            "id": "pb1-p21",
            "phase": "PHASE 1G · SALES PSYCHOLOGY & STRATEGY (PAGE 2 OF 3)",
            "title": "Loss Aversion & The Psychology of the Status Quo",
            "tagline": "Your #1 competitor is not another AI agency. Your #1 competitor is 'Do Nothing.'",
            "keyTakeaways": [
                "Nobel laureate Daniel Kahneman proved that human beings experience the pain of a loss 2.5x more intensely than the pleasure of an equivalent gain.",
                "If a prospect thinks doing nothing is 'safe and free,' they will always delay. Your job is to prove that doing nothing is actively bleeding cash every single week.",
                "Contrast 'Future Gain' (weak) with 'Current Daily Bleed' (unstoppable)."
            ],
            "content": """
                <div class="prose-section">
                    <h3>Why "Do Nothing" Beats Weak Salespeople</h3>
                    <p>Most B2B deals don't lose to a competitor—they lose to <strong>inertia</strong> ("Let's revisit this in Q4"). Why? Because making a decision requires energy and carries career risk, whereas doing nothing feels "free."</p>
                    <p>To defeat inertia, you must use <strong>Loss Aversion</strong>—proving mathematically that standing still is the riskiest, most expensive decision on the board:</p>

                    <div class="comparison-grid">
                        <div class="comp-card comp-bad">
                            <h4>❌ Weak "Gain Frame" (Easy to Delay)</h4>
                            <p><em>"If you hire MAB AI Strategies, we could help your team save 15 hours a week and make an extra $40,000 next year!"</em><br/><br/><strong>Executive Brain:</strong> "Cool, that's a nice-to-have bonus. We can look at that in six months."</p>
                        </div>
                        <div class="comp-card comp-good">
                            <h4>✅ Surgical "Loss Aversion Frame" (Creates Urgency Now)</h4>
                            <p><em>"Right now, every week this workflow stays manual, your Director of Staff burns 15 hours and $770 in unrecovered payroll drag. Waiting until next quarter means setting $10,000 on fire over the next 90 days for zero return."</em><br/><br/><strong>Executive Brain:</strong> "Stop the bleeding now."</p>
                        </div>
                    </div>
                </div>
            """
        },
        {
            "id": "pb1-p22",
            "phase": "PHASE 1G · SALES PSYCHOLOGY & STRATEGY (PAGE 3 OF 3)",
            "title": "The 'Long-Term Greedy' Stoic Strategist",
            "tagline": "Detach from the outcome of any single call, obsess over the quality of your inputs, and play long-term greedy.",
            "keyTakeaways": [
                "In Mark's Field Note 'Fatherhood & Leadership', 'Long-Term Greedy' means never sacrificing long-term trust and compounding value for a cheap short-term trick.",
                "You cannot control whether a specific CEO had a fight with their spouse 5 minutes before you called. You CAN control 100% of your preparation, your dial volume, your tone, and your diagnostic precision.",
                "Complete the Playbook 1 Certification Exam below to unlock Playbook 2!"
            ],
            "content": """
                <div class="prose-section">
                    <h3>What "Long-Term Greedy" Means in Sales</h3>
                    <p>Amateur reps are <em>short-term greedy</em>: they exaggerate what a system can do just to get a quick signature, or they push a client into the wrong tier. Six weeks later, the client churns, demands a refund, and tells ten CEO friends to avoid them.</p>
                    <p>At MAB AI Strategies, we are <strong>Long-Term Greedy</strong>:</p>
                    <ul>
                        <li>If a prospect is only ready for a <strong>1–2 week AI Readiness Audit</strong> or a <strong>Single Workflow</strong>, we sell them that exact wedge, crush the delivery, prove the ROI in dollars and hours, and earn their <strong>Accelerator or Principal Retainer</strong> for years to come.</li>
                        <li>Even on our free 30-Minute Strategic Briefing, we give them a real, actionable ROI roadmap whether they hire us today or not—because when they realize how complex building it alone actually is two weeks later, they come straight back to the only architect who told them the truth.</li>
                    </ul>

                    <div class="exam-launch-cta">
                        <div>
                            <h4>Ready to Certify on Playbook 1?</h4>
                            <p>You've completed all 7 foundational phases (22 pages). Pass the 12-question Playbook 1 Certification Exam to unlock Playbook 2 and dispatch your results to Mark Bockrath.</p>
                        </div>
                        <button class="btn-primary-glow" onclick="launchModuleExam('pb1')">Launch Playbook 1 Certification Exam →</button>
                    </div>
                </div>
            """
        }
    ],
    "popQuizzes": [
        {
            "id": "pb1-pop1",
            "triggerAfterPage": 5,
            "title": "Pop Quiz: AI Industry & Market Fundamentals",
            "questions": [
                {
                    "q": "What is the difference between a deterministic workflow automation (Make/n8n) and an autonomous AI agent (LangGraph/CrewAI/AG2)?",
                    "options": [
                        "There is no difference; they are synonyms.",
                        "Deterministic workflows follow strict 'If This, Then That' rules across APIs, while autonomous AI agents perform multi-step reasoning, use tools dynamically, and apply judgment with human-in-the-loop guardrails.",
                        "Workflows only work on Mac, while agents only work on Windows.",
                        "Agents cannot connect to CRMs."
                    ],
                    "correct": 1,
                    "explanation": "Deterministic workflows execute fixed rule pipelines; autonomous agents perform multi-step reasoning and tool orchestration."
                },
                {
                    "q": "How do we prevent an LLM from 'hallucinating' (making up false company information) when answering questions about a client's internal policies or pricing?",
                    "options": [
                        "Tell the LLM nicely not to lie.",
                        "Engineer a RAG (Retrieval-Augmented Generation) pipeline backed by vector/SQL databases (Pinecone, Supabase, PostgreSQL) so the model retrieves verified company documents before responding.",
                        "Only use free public chatbots.",
                        "Disable the internet."
                    ],
                    "correct": 1,
                    "explanation": "RAG (Retrieval-Augmented Generation) grounds the model in the client's proprietary, verified data layer."
                }
            ]
        },
        {
            "id": "pb1-pop2",
            "triggerAfterPage": 12,
            "title": "Pop Quiz: B2B Economics, ICP & Decision Makers",
            "questions": [
                {
                    "q": "What are the Three Universal B2B Buying Levers that every corporate investment must map to?",
                    "options": [
                        "Entertainment, aesthetics, and popularity",
                        "Increase Revenue, Increase Net Liquidity (Save Time/Cost), and Eliminate Risk",
                        "Buying more office furniture, hiring more interns, and printing brochures",
                        "Getting more likes on Instagram"
                    ],
                    "correct": 1,
                    "explanation": "Every B2B purchase must drive Revenue, Net Liquidity (Cost/Time savings), or Risk Mitigation."
                },
                {
                    "q": "A prospect has 4 employees, $180K in total annual revenue, no CRM, and wants us to build a custom consumer mobile app in exchange for 10% equity. What is your move?",
                    "options": [
                        "Book a 2-hour call with Mark Bockrath immediately.",
                        "Politely disqualify in under 90 seconds—they fall completely outside our ICP ($5M–$150M B2B sweet spot, repeatable process volume, paid architecture).",
                        "Spend 3 weeks writing a custom proposal.",
                        "Offer them a Principal Retainer at a 95% discount."
                    ],
                    "correct": 1,
                    "explanation": "Protect your pipeline from non-ICP time vampires. We do not build pre-revenue ideas for equity."
                }
            ]
        },
        {
            "id": "pb1-pop3",
            "triggerAfterPage": 19,
            "title": "Pop Quiz: Verticals, Sequencing & Nexus CRM",
            "questions": [
                {
                    "q": "Why is a mid-market company with an active job posting for a 'Recruiting Coordinator' or 'Operations Specialist' considered prime low-hanging fruit?",
                    "options": [
                        "Because we want to apply for the job.",
                        "Because it proves they have an active operational bottleneck AND have already approved $55K–$75K+ in annual budget to solve it—which our autonomous agents can solve faster and cheaper.",
                        "Because HR people have nothing to do all day.",
                        "It isn't a good signal."
                    ],
                    "correct": 1,
                    "explanation": "Job-board arbitrage proves both an active pain bottleneck and pre-approved budget."
                },
                {
                    "q": "What is the 'Iron Law' of Opportunity management inside Nexus CRM?",
                    "options": [
                        "Only update Nexus CRM once a month.",
                        "Every open Opportunity must have a concrete, future-dated Next Step Task attached at all times—if it isn't in Nexus CRM, it didn't happen.",
                        "Never log discovery notes until after the contract is signed.",
                        "Delete deals if the prospect asks a hard question."
                    ],
                    "correct": 1,
                    "explanation": "Zero open Opportunities may exist without a future-dated Next Step Task in Nexus CRM."
                }
            ]
        }
    ],
    "finalExam": {
        "title": "Playbook 1 Certification Exam: Industry, B2B Sales, ICP, Verticals & Psychology",
        "passingScore": 80,
        "questions": [
            {
                "category": "Industry & Market",
                "q": "In Mark Bockrath's Field Note 'The Agentic Workforce', what fundamental shift defines the move from the SaaS era to the Agentic era?",
                "options": [
                    "Moving from 'Software-as-a-Service' (buying tools to help humans work faster) to 'Service-as-Software' (deploying autonomous agents and silicon employees to execute the work itself).",
                    "Moving back from cloud software to paper filing cabinets.",
                    "Replacing all databases with Microsoft Word.",
                    "Hiring more manual data-entry clerks."
                ],
                "correct": 0,
                "explanation": "We are moving from SaaS (tools for humans) to Service-as-Software (agents doing the work itself)."
            },
            {
                "category": "Industry & Market",
                "q": "A prospect says, 'Our internal IT guy is already looking into building AI for us.' What is the strongest diagnostic response?",
                "options": [
                    "Tell them their IT guy is incompetent.",
                    "Validate their IT lead as an asset, then explain that internal IT is already at 110% capacity managing infrastructure/tickets—partnering with MAB AI brings 250+ pre-built templates and deploys in weeks instead of 12–18 months.",
                    "Hang up immediately.",
                    "Offer to replace their IT department."
                ],
                "correct": 1,
                "explanation": "Never insult internal IT; position MAB AI as the force-multiplier that saves them 12–18 months of R&D."
            },
            {
                "category": "B2B Sales Economics",
                "q": "Using our Cost-of-Inaction formula, if 2 operations staff each waste 10 hours/week on manual data reconciliation at a $50/hr fully burdened rate, what is the annual payroll bleed alone (52 weeks)?",
                "options": [
                    "$5,200 / year",
                    "$52,000 / year (20 hrs/wk × $50/hr × 52 weeks)",
                    "$520,000 / year",
                    "$1,000 / year"
                ],
                "correct": 1,
                "explanation": "2 staff × 10 hrs/wk = 20 hrs/wk × $50/hr = $1,000/week × 52 weeks = $52,000/year in direct payroll drag."
            },
            {
                "category": "B2B Sales Economics",
                "q": "In a B2B buying committee, what distinguishes the 'Champion' from the 'Economic Buyer'?",
                "options": [
                    "They are always the exact same person.",
                    "The Champion feels the daily operational pain and advocates internally for your solution, while the Economic Buyer owns the P&L budget and holds final veto/approval authority.",
                    "The Champion is in Legal and the Economic Buyer is an intern.",
                    "The Economic Buyer never cares about ROI."
                ],
                "correct": 1,
                "explanation": "You arm your Champion with ROI math so you can align and close the Economic Buyer."
            },
            {
                "category": "ICP & Decision Makers",
                "q": "Which company profile best matches MAB AI Strategies' core Ideal Customer Profile (ICP)?",
                "options": [
                    "A solo college student with an app idea and $0 revenue.",
                    "A $28M/year staffing and recruiting firm with 85 employees using Bullhorn, HubSpot, Slack, and QuickBooks, currently hiring two Recruiting Coordinators.",
                    "A local corner bakery with 2 part-time cashiers.",
                    "A government agency with a 4-year RFP freeze."
                ],
                "correct": 1,
                "explanation": "Mid-market revenue ($5M–$150M), 20–500 headcount, multi-tool cloud stack, and active hiring/operational friction."
            },
            {
                "category": "ICP & Decision Makers",
                "q": "When speaking to a CFO ('Marcus' persona) vs. a CTO ('Cipher' persona), how should you tailor your primary value emphasis?",
                "options": [
                    "Use the exact same technical jargon for both.",
                    "For the CFO, emphasize hourly cost-of-inaction, net liquidity, and <90-day payback guarantee; for the CTO, emphasize SOC 2/GDPR governance, human-in-the-loop guardrails, vendor neutrality, and zero tech debt.",
                    "Pitch the CFO on Python syntax and the CTO on accounting rules.",
                    "Avoid speaking to either of them."
                ],
                "correct": 1,
                "explanation": "Match the executive's scoreboard: CFOs buy Risk-Adjusted Payback & Liquidity; CTOs buy Security, Governance & Architecture."
            },
            {
                "category": "Verticals & Low-Hanging Fruit",
                "q": "Which four industry verticals represent our highest-velocity low-hanging fruit?",
                "options": [
                    "Staffing/Recruiting, B2B Professional Services (Legal/CPA/Agencies), Logistics/Field Ops, and Financial/Insurance/Healthcare Admin",
                    "Public elementary schools, hobby farms, food trucks, and dog walkers",
                    "Video game graphics studios only",
                    "Cryptocurrency day traders only"
                ],
                "correct": 0,
                "explanation": "Those four B2B verticals have massive coordination volume, multi-system silos, and immediate ROI from our library."
            },
            {
                "category": "Prospecting & Sequencing",
                "q": "Why does MAB AI Strategies use a 14-day multi-channel sequence (Email + Phone + LinkedIn) rather than sending a single cold email?",
                "options": [
                    "Because we enjoy spamming people.",
                    "Because busy executives rarely respond to a single cold email; orchestrating value-driven touches across Email, Phone, and LinkedIn multiplies conversion rates by 6x–10x.",
                    "Because phones don't work anymore.",
                    "Because LinkedIn is the only channel allowed."
                ],
                "correct": 1,
                "explanation": "Multi-channel orchestration builds executive familiarity across asynchronous and live channels."
            },
            {
                "category": "Prospecting & Sequencing",
                "q": "Why is sending 'Just checking in / bumping this to the top of your inbox' banned at MAB AI Strategies?",
                "options": [
                    "It screams low-status 'commission breath' and adds zero diagnostic value to the executive.",
                    "It uses too many bytes.",
                    "Email servers block the word 'bump'.",
                    "It is too technical."
                ],
                "correct": 0,
                "explanation": "Every touch in a sequence must bring a fresh signal, case study, or cost-of-inaction insight—never needy begging."
            },
            {
                "category": "Nexus CRM Mastery",
                "q": "What are the 4 core objects inside Nexus CRM, and what must always be attached to an open Opportunity?",
                "options": [
                    "Account, Contact, Opportunity, and Activity/Task — and every open Opportunity must have a future-dated Next Step Task.",
                    "Spreadsheets, Sticky Notes, Bookmarks, and Folders.",
                    "Only Contact names with no company records.",
                    "Invoices only."
                ],
                "correct": 0,
                "explanation": "Accounts, Contacts, Opportunities, and Activities/Tasks—governed by the Iron Law of the Dated Next Step."
            },
            {
                "category": "Sales Psychology",
                "q": "How does Behavioral Economics' principle of 'Loss Aversion' change the way you frame a pitch?",
                "options": [
                    "Executives work ~2.5x harder to stop an active, quantified weekly financial bleed ('standing still costs you $2,100 every week') than to chase a vague hypothetical future gain.",
                    "You should threaten the prospect with lawsuits.",
                    "You should never mention money on a call.",
                    "Loss aversion means giving away free work."
                ],
                "correct": 0,
                "explanation": "Pricing the active weekly bleed makes 'Do Nothing' visibly painful and urgent."
            },
            {
                "category": "Sales Psychology",
                "q": "What does playing 'Long-Term Greedy' mean when prescribing a MAB AI solution?",
                "options": [
                    "Overcharging a small client for things they don't need.",
                    "Prescribing the exact right entry wedge (e.g., AI Readiness Audit or Single Agent) with total integrity, proving undeniable ROI, and compounding that relationship into a multi-year Accelerator or Principal Retainer.",
                    "Refusing to ever talk about retainers.",
                    "Hiding our pricing until after they sign."
                ],
                "correct": 1,
                "explanation": "Long-Term Greedy means optimizing for compounding client trust and multi-year LTV over short-sighted tricks."
            }
        ]
    }
}
