/* NeuroSpect v2 — NeuroFusion (SIHRE) Deep Dive Page */

/* ═══ REASONING SCENARIOS DATA ═══ */
var REASONING_SCENARIOS = [
  { id: 'bias', title: 'Pre-Market Bias', icon: '\u{1F9ED}',
    desc: 'It\'s 8:45 AM ET. NQ futures are 40 points above yesterday\'s close. Asian session swept a key low overnight.',
    question: 'What\'s your directional bias for the NY AM session?',
    options: ['Bullish — price is above previous close', 'Bearish — liquidity sweep suggests reversal', 'Neutral — wait for London close confirmation', 'Bullish but cautious — need FVG confirmation'],
    sihre_answer: 2,
    reasoning: [
      { type: 'Statistical', color: '#3b82f6', says: 'Leans bullish. 67% of sessions with 40+ point overnight gaps continue in direction for the first 30 minutes.' },
      { type: 'Structural', color: '#8b5cf6', says: 'Flags caution. The Asia sweep of a key low is a classic reversal setup. Historical reversal rate after this pattern: 58%.' },
      { type: 'Regime-Aware', color: '#10b981', says: 'Detects current regime is "expansion after consolidation" — a regime where overnight gaps are unreliable directional signals.' },
      { type: 'Uncertainty', color: '#f59e0b', says: 'Confidence interval is wide. Two signals disagree. Recommends waiting for London close to narrow the distribution before committing bias.' },
      { type: 'Orchestrator', color: '#fbbf24', says: 'Synthesis: Neutral. Statistical lean is bullish, but structural pattern contradicts, and regime context weakens the gap signal. Wait for confirming price action. No edge in premature commitment.' },
    ]},
  { id: 'entry', title: 'Entry or Pass?', icon: '\u{1F3AF}',
    desc: 'A fair value gap forms on the 15-minute chart after a displacement candle. Price is retracing into it. Your checklist says "go."',
    question: 'Do you take this entry?',
    options: ['Yes — setup is textbook, enter now', 'Yes — but reduce size due to session timing', 'No — wait for a lower timeframe confirmation', 'No — something feels off, pass entirely'],
    sihre_answer: 2,
    reasoning: [
      { type: 'Pattern Match', color: '#3b82f6', says: 'Setup matches historical criteria. Win rate for this pattern in this session: 54%. Marginal but positive.' },
      { type: 'Contextual', color: '#8b5cf6', says: 'Flags that the displacement candle occurred during low-volume transition (11:30 AM). Similar setups during lunch hours have 38% win rate — below baseline.' },
      { type: 'Adversarial', color: '#ef4444', says: 'Challenges the entry. Finds 3 counter-arguments: liquidity above is thin, no higher-timeframe alignment, and today\'s session profile doesn\'t match A+ setup criteria.' },
      { type: 'Uncertainty', color: '#f59e0b', says: 'Conviction score: 0.41 (below 0.55 threshold). If entering, recommends 40% of standard position size.' },
      { type: 'Orchestrator', color: '#fbbf24', says: 'Synthesis: Wait for LTF confirmation. The setup is structurally valid but context degrades it. If a 1-minute or 5-minute bullish reaction appears at the FVG, re-evaluate with tighter stop.' },
    ]},
  { id: 'sizing', title: 'Position Sizing', icon: '\u{1F4CA}',
    desc: 'You have an A+ setup: HTF bias aligned, LTF entry confirmed, FVG respected. But you\'re already down 1.2% on the day from two earlier losses.',
    question: 'How do you size this trade?',
    options: ['Full size — the setup quality demands it', 'Reduced (50%) — account for daily loss', 'Increased — make back losses with this A+ setup', 'Standard size — prior losses are irrelevant to this trade'],
    sihre_answer: 1,
    reasoning: [
      { type: 'Setup Quality', color: '#3b82f6', says: 'Confirms A+ classification. Historical expectancy for this setup at this conviction level: +2.4R.' },
      { type: 'Risk Governor', color: '#ef4444', says: 'Daily drawdown is 1.2%. Risk budget remaining: 0.8% before daily limit. Full-size trade risks hitting limit on any adverse move.' },
      { type: 'Behavioral', color: '#8b5cf6', says: 'Detects "recovery bias" pattern. After 2+ losses, traders historically over-size by 30% and widen stops. Flags increased psychological risk.' },
      { type: 'Uncertainty', color: '#f59e0b', says: 'Setup conviction is high (0.78) but risk-adjusted sizing must account for remaining daily budget. Optimal: 55% of standard size.' },
      { type: 'Orchestrator', color: '#fbbf24', says: 'Synthesis: Reduce to ~50%. The setup is genuinely strong, but risk governance takes priority. Preserving remaining daily budget means you can still trade the PM session if another setup appears. A great setup at reduced size still has positive expectancy.' },
    ]},
  { id: 'news', title: 'News Event Response', icon: '\u{1F4F0}',
    desc: 'You\'re in a long position, up 1.5R. CPI data drops in 3 minutes. Consensus expects 3.2%, whisper number is 3.4%.',
    question: 'What do you do with your open position?',
    options: ['Hold — the trend is your friend', 'Close entirely — never hold through news', 'Partial close (50%) and trail the rest', 'Move stop to breakeven and hold'],
    sihre_answer: 2,
    reasoning: [
      { type: 'Statistical', color: '#3b82f6', says: 'CPI releases cause average 45-point NQ moves. Current profit (1.5R) could be fully erased in the initial spike. Historical win rate holding longs through above-consensus CPI: 31%.' },
      { type: 'Scenario Generator', color: '#10b981', says: 'Simulates 3 scenarios: consensus (3.2%) = mild continuation, hot (3.4%) = sharp selloff erasing position, cool (3.0%) = rally adds 2R. Weighted expected value of holding: -0.3R.' },
      { type: 'Risk Governor', color: '#ef4444', says: 'Open exposure through a binary event violates risk framework. The stop-loss may not execute at the intended price due to gap risk.' },
      { type: 'Memory', color: '#8b5cf6', says: 'Recalls 14 prior CPI events in similar conditions. Partial close + trail preserved 68% of profits on average vs. 41% for full hold.' },
      { type: 'Orchestrator', color: '#fbbf24', says: 'Synthesis: Partial close 50%, trail the remainder with a breakeven stop. Locks in 0.75R guaranteed profit while maintaining upside exposure if the print is favorable. Risk-adjusted optimal path given gap risk.' },
    ]},
  { id: 'streak', title: 'Loss Streak Management', icon: '\u{1F6E1}️',
    desc: 'You\'ve had 4 consecutive losses over 2 days. Each followed your plan. Total drawdown: 3.2%. A valid setup appears on your screen right now.',
    question: 'What\'s your next move?',
    options: ['Take the trade — plan is working, variance happens', 'Skip today entirely — reset mentally', 'Take it at 25% size to stay engaged', 'Review the 4 losses first before deciding'],
    sihre_answer: 3,
    reasoning: [
      { type: 'Statistical', color: '#3b82f6', says: '4 consecutive losses is within normal variance for a 55% win rate system (occurs ~4% of the time). The strategy hasn\'t broken — this is expected.' },
      { type: 'Behavioral', color: '#8b5cf6', says: 'After 4+ losses, traders in this profile show 2.3x higher rates of plan deviation on the 5th trade. Emotional decision-making risk is elevated regardless of intellectual understanding.' },
      { type: 'Forensic', color: '#10b981', says: 'Analyzes the 4 losses for hidden pattern. Finds: 3 of 4 occurred during the same session (NY AM) on the same instrument. This may not be variance — it could be a regime-specific degradation worth investigating.' },
      { type: 'Uncertainty', color: '#f59e0b', says: 'Current system confidence has decayed from 0.72 to 0.54 due to recent results. Below the standard execution threshold but above the full-stop threshold.' },
      { type: 'Orchestrator', color: '#fbbf24', says: 'Synthesis: Review the 4 losses first. The forensic layer surfaced a potential pattern (3/4 in same session + instrument) that could indicate regime-specific failure, not pure variance. If the pattern is confirmed, adjust the routing. If it\'s noise, resume with standard sizing tomorrow.' },
    ]},
  { id: 'regime_shift', title: 'Regime Transition', icon: '\u{1F30A}',
    desc: 'Your trend-following setups have been printing money for 3 weeks. This week, two setups that "should have worked" both stopped out at breakeven.',
    question: 'How do you interpret this?',
    options: ['Noise — keep trading the trend system', 'Market is ranging — switch to mean reversion', 'Reduce size until clarity returns', 'Stop trading and wait for a clear signal'],
    sihre_answer: 2,
    reasoning: [
      { type: 'Regime Detection', color: '#3b82f6', says: 'Volatility compression detected. Average true range has declined 34% over the past 5 sessions. Trend-continuation setups have a 29% lower win rate in this volatility regime.' },
      { type: 'Structural', color: '#8b5cf6', says: 'Price is coiling between two key levels with decreasing range. Classic transition from expansion to consolidation. Duration of similar consolidations historically: 3-8 sessions.' },
      { type: 'Memory', color: '#10b981', says: 'Last 6 similar transitions in this instrument showed: trend strategies degraded for an average of 5.2 sessions before either resuming or reversing.' },
      { type: 'Adaptive', color: '#f59e0b', says: 'Recommends reducing exposure while the regime is ambiguous. The transition is real but the destination is unknown — could resume trending or enter prolonged range.' },
      { type: 'Orchestrator', color: '#fbbf24', says: 'Synthesis: Reduce size. The regime transition is confirmed by multiple signals, but the destination regime is uncertain. Cutting size preserves capital during the ambiguous period while maintaining market exposure for when clarity emerges. Do NOT switch to mean reversion prematurely — wait for the range to establish boundaries first.' },
    ]},
  { id: 'fvg_quality', title: 'FVG Quality Assessment', icon: '\u{1F50E}',
    desc: 'Two fair value gaps formed today. FVG-A is on the 1-hour chart in a trending market. FVG-B is on the 5-minute chart after a news spike.',
    question: 'Which FVG do you prioritize?',
    options: ['FVG-A — higher timeframe is always better', 'FVG-B — it\'s fresher and closer to current price', 'Both equally valid — trade whichever fills first', 'Neither — need more context before choosing'],
    sihre_answer: 0,
    reasoning: [
      { type: 'Structural', color: '#3b82f6', says: 'FVG-A: formed during organic price delivery in a trending session. Historical fill rate: 72%, continuation after fill: 64%. FVG-B: formed during news volatility, a mechanically different event. Fill rate: 81% but continuation: 39%.' },
      { type: 'Contextual', color: '#8b5cf6', says: 'News-spike FVGs are "displacement artifacts" — they look like valid imbalances but are caused by liquidity vacuums, not institutional order flow. Different cause, different reliability.' },
      { type: 'Causal', color: '#10b981', says: 'Proposes that FVG-A has a causal mechanism (institutional accumulation in trend) while FVG-B\'s mechanism (news liquidity vacuum) is transient. Causal stability score: A=0.71, B=0.28.' },
      { type: 'Uncertainty', color: '#f59e0b', says: 'Conviction on FVG-A: 0.67 (tradeable). Conviction on FVG-B: 0.34 (below threshold). The difference is not subjective — it\'s quantifiable.' },
      { type: 'Orchestrator', color: '#fbbf24', says: 'Synthesis: Prioritize FVG-A. Higher timeframe + organic formation + trending regime + causal stability all converge. FVG-B is a trap for traders who don\'t distinguish between structural and artifactual imbalances.' },
    ]},
  { id: 'multi_tf', title: 'Timeframe Conflict', icon: '\u{23F1}️',
    desc: 'Daily chart is bearish (lower highs). 4-hour is neutral (range-bound). 15-minute just printed a bullish market structure shift.',
    question: 'How do you resolve this conflict?',
    options: ['Follow the daily — higher timeframe wins', 'Trade the 15-min MSS — momentum is shifting', 'Wait for 4-hour to confirm either direction', 'Short — use the 15-min bounce as entry for the daily bear trend'],
    sihre_answer: 3,
    reasoning: [
      { type: 'Multi-Scale', color: '#3b82f6', says: 'Quantifies the conflict: Daily bearish conviction 0.72, 4H neutral 0.50, 15M bullish 0.61. Weighted by timeframe reliability, net directional score: -0.38 (bearish lean).' },
      { type: 'Structural', color: '#8b5cf6', says: 'Recognizes the pattern: bearish daily + bullish 15M = classic "return to FVG" before continuation. The 15M bullish shift is likely the retracement INTO the bearish daily structure, not a reversal of it.' },
      { type: 'Historical', color: '#10b981', says: 'In this specific conflict pattern (bearish D1 + bullish 15M MSS), the D1 direction continued 71% of the time. The 15M MSS served as the entry trigger FOR the higher timeframe direction.' },
      { type: 'Uncertainty', color: '#f59e0b', says: 'Short entry conviction: 0.64 (above threshold). Key risk: the 4H range could provide support. Recommends tight stop above the 15M MSS high.' },
      { type: 'Orchestrator', color: '#fbbf24', says: 'Synthesis: Use the 15M bullish move as a short entry. The lower timeframe "bullish" shift is actually providing a premium entry into the higher timeframe bearish structure. This is how multi-timeframe alignment works — the LTF isn\'t contradicting the HTF, it\'s giving you a better entry for it.' },
    ]},
  { id: 'correlation', title: 'Cross-Market Signal', icon: '\u{1F310}',
    desc: 'ES and NQ have been moving in lockstep all week. Today, ES breaks a key high while NQ fails to make a new high at the same time.',
    question: 'What does this divergence mean?',
    options: ['Bullish — ES is leading, NQ will follow', 'Bearish — NQ weakness signals a reversal for both', 'Meaningless — minor timing difference', 'Need more data — watch for 30 more minutes'],
    sihre_answer: 1,
    reasoning: [
      { type: 'Correlation', color: '#3b82f6', says: 'ES/NQ correlation has been 0.94 this week. Today\'s divergence at a key level is a 2-sigma event. Historical outcome when this divergence occurs at highs: reversal 68% of the time within 2 hours.' },
      { type: 'Structural', color: '#8b5cf6', says: 'This is a classic SMT (Smart Money Technique) divergence. ES making a high while NQ fails suggests the move is retail-driven, not institutional. Institutional flow would move both indices.' },
      { type: 'Causal', color: '#10b981', says: 'Proposes mechanism: one index sweeping liquidity while the other fails = engineered stop hunt. The "real" move is the failure, not the breakout. Causal confidence: 0.62.' },
      { type: 'Memory', color: '#f59e0b', says: 'Recalls 23 similar ES/NQ divergences at key levels in the past 6 months. 16 resulted in reversal (70%), average reversal move: 35 NQ points within 90 minutes.' },
      { type: 'Orchestrator', color: '#fbbf24', says: 'Synthesis: Bearish signal. Multiple independent reasoning paths converge: statistical correlation break, structural SMT pattern, causal mechanism, and historical precedent all point to reversal. This is a high-conviction signal — the kind that emerges when heterogeneous signals agree.' },
    ]},
  { id: 'exit', title: 'Optimal Exit Timing', icon: '\u{1F3C1}',
    desc: 'You\'re in a short trade, currently at +2.8R. Price is approaching a key support level 15 points below. Your original target was +3R.',
    question: 'Do you hold for the full target?',
    options: ['Hold — target is only 15 points away', 'Close now — 2.8R is excellent, don\'t give it back', 'Trail stop tightly and let it play out', 'Close 75% and let 25% run for the target'],
    sihre_answer: 3,
    reasoning: [
      { type: 'Statistical', color: '#3b82f6', says: 'Trades that reach 2.8R achieve 3.0R only 52% of the time in this instrument. Expected value of holding for 0.2R more: +0.04R (marginal). Risk of support bounce taking it back to 2.0R: 23%.' },
      { type: 'Structural', color: '#8b5cf6', says: 'The support level ahead is a daily level with historical respect. Price often reacts violently at these levels. The last 15 points may be the hardest.' },
      { type: 'Behavioral', color: '#10b981', says: 'Detects "anchoring bias" — fixation on the 3R target is a cognitive trap. The market doesn\'t know your target. Optimal exit is probabilistic, not target-based.' },
      { type: 'Risk-Adjusted', color: '#f59e0b', says: 'Partial close maximizes risk-adjusted return. Close 75% to lock in 2.1R guaranteed. Trail 25% with a stop at 2.0R. Worst case: 2.6R total. Best case: 2.85R total. Both outcomes are excellent.' },
      { type: 'Orchestrator', color: '#fbbf24', says: 'Synthesis: Close 75%, trail 25%. The math favors partial exit. Holding everything for 0.2R more has negative expected value when accounting for the support level reaction risk. Partial close converts a good trade into a guaranteed great trade while preserving upside optionality.' },
    ]},
];

/* ═══ SIMULATOR SCENARIOS ═══ */
var SIM_STEPS = [
  { title: 'Pre-Market Analysis',
    situation: 'ES futures gapped up 20 points overnight. Asia session was bullish. European session is currently pulling back into yesterday\'s value area.',
    question: 'What\'s your pre-market bias?',
    options: [
      { label: 'Strong bullish', score: 2 },
      { label: 'Cautious bullish', score: 4 },
      { label: 'Neutral — wait and see', score: 3 },
      { label: 'Bearish — fade the gap', score: 1 },
    ],
    sihre_choice: 1,
    sihre_reasoning: 'Multiple signals converge on cautious bullish: gap + Asia momentum support direction, but European pullback + key level proximity warrant reduced conviction until NY open price action confirms.',
  },
  { title: 'Setup Identification',
    situation: 'At 9:45 AM, a bullish FVG forms on the 5-minute chart after a sweep of the overnight low. The displacement is 12 points. Volume is above average.',
    question: 'How do you classify this setup?',
    options: [
      { label: 'A+ setup — take full size', score: 3 },
      { label: 'B+ setup — take 70% size', score: 4 },
      { label: 'C setup — too early to tell', score: 2 },
      { label: 'Skip — don\'t trust early session', score: 1 },
    ],
    sihre_choice: 1,
    sihre_reasoning: 'Setup quality is high (sweep + displacement + FVG + volume confluence), but it\'s only 15 minutes into the session. Historical data shows the first 20 minutes have 18% more false signals. B+ classification with 70% sizing optimizes the risk-reward while respecting the session timing context.',
  },
  { title: 'Risk Management',
    situation: 'You enter the trade. Stop is below the swept low (8 points risk). Price moves in your favor by 6 points, then stalls for 4 minutes at a minor resistance level.',
    question: 'How do you manage the position?',
    options: [
      { label: 'Move stop to breakeven', score: 2 },
      { label: 'Keep original stop, trust the setup', score: 3 },
      { label: 'Partial close 30%, trail the rest', score: 4 },
      { label: 'Close everything — stall means reversal', score: 1 },
    ],
    sihre_choice: 2,
    sihre_reasoning: 'Minor resistance stalls are normal price delivery. Moving to breakeven prematurely would result in a stop-out 41% of the time in this pattern. The original thesis (sweep + FVG + displacement) hasn\'t been invalidated. Partial close is suboptimal this early — the full move hasn\'t developed. Hold with original stop.',
  },
  { title: 'Mid-Trade Decision',
    situation: 'Price breaks through the minor resistance and reaches +12 points (+1.5R). A bearish engulfing candle prints on the 5-minute chart. Higher timeframe trend is still bullish.',
    question: 'React to the bearish candle?',
    options: [
      { label: 'Close immediately — bearish signal', score: 1 },
      { label: 'Move stop to +0.8R, hold for target', score: 3 },
      { label: 'Close 50%, trail rest at +0.8R', score: 4 },
      { label: 'Ignore it — higher TF is bullish', score: 2 },
    ],
    sihre_choice: 2,
    sihre_reasoning: 'A single bearish engulfing on the LTF against a bullish HTF is noise 62% of the time. However, at +1.5R, risk management becomes asymmetric: protecting the open profit is now more valuable than marginal upside. Partial close + trail balances both considerations optimally.',
  },
  { title: 'Final Outcome',
    situation: 'After your management decision, price consolidates for 8 minutes then runs another 10 points. The daily target zone (your original TP) is hit at +2.8R.',
    question: 'Post-trade: what\'s your biggest takeaway?',
    options: [
      { label: 'I should have held full size the whole time', score: 2 },
      { label: 'My process was correct regardless of outcome', score: 4 },
      { label: 'I need to trust bearish signals more', score: 1 },
      { label: 'The partial close was right — even if I left money', score: 3 },
    ],
    sihre_choice: 1,
    sihre_reasoning: 'Outcome bias is the most dangerous trap in trading. This trade worked — but that doesn\'t validate "hold everything." Across 1,000 similar situations, partial close + trail produces higher risk-adjusted returns than full hold, even though full hold occasionally captures more. Process over outcome. Always.',
  },
];

/* ═══ NEUROFUSION PAGE ═══ */
function NeuroFusionPage() {
  var scenarioState = React.useState(null);
  var openScenario = scenarioState[0], setOpenScenario = scenarioState[1];
  var answersState = React.useState({});
  var answers = answersState[0], setAnswers = answersState[1];
  var revealedState = React.useState({});
  var revealed = revealedState[0], setRevealed = revealedState[1];

  var simState = React.useState(0);
  var simStep = simState[0], setSimStep = simState[1];
  var simAnswersState = React.useState([]);
  var simAnswers = simAnswersState[0], setSimAnswers = simAnswersState[1];
  var simDoneState = React.useState(false);
  var simDone = simDoneState[0], setSimDone = simDoneState[1];
  var simRevealState = React.useState(false);
  var simReveal = simRevealState[0], setSimReveal = simRevealState[1];

  function selectAnswer(scenarioId, optionIdx) {
    var next = Object.assign({}, answers);
    next[scenarioId] = optionIdx;
    setAnswers(next);
  }
  function revealReasoning(scenarioId) {
    var next = Object.assign({}, revealed);
    next[scenarioId] = true;
    setRevealed(next);
  }
  function selectSimAnswer(optionIdx) {
    var next = simAnswers.concat([optionIdx]);
    setSimAnswers(next);
    if (next.length >= SIM_STEPS.length) {
      setSimDone(true);
    } else {
      setSimStep(simStep + 1);
    }
  }
  function resetSim() {
    setSimStep(0);
    setSimAnswers([]);
    setSimDone(false);
    setSimReveal(false);
  }

  var simScore = 0;
  var simSihreScore = 0;
  simAnswers.forEach(function(a, i) {
    simScore += SIM_STEPS[i].options[a].score;
    simSihreScore += SIM_STEPS[i].options[SIM_STEPS[i].sihre_choice].score;
  });

  return (
    <div className="page">
      {/* Hero */}
      <Rv>
        <div className="hero-grad" style={{ padding: 'clamp(2rem,4vw,3rem)', marginBottom: '1.5rem', borderImage: 'linear-gradient(135deg, rgba(251,191,36,0.3), rgba(251,191,36,0.05)) 1', borderImageSlice: 1 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 16 }}>
            <span className="badge badge-gold"><span className="badge-dot"></span>Patent Pending</span>
            <span className="badge badge-gold" style={{ background: 'rgba(251,191,36,0.15)' }}>v0.1</span>
          </div>
          <h1 style={{ marginBottom: 12 }}>
            <span className="grad-text-gold">NeuroFusion</span>
          </h1>
          <p style={{ fontFamily: "'Orbitron',sans-serif", fontWeight: 500, fontSize: '0.85rem', color: 'var(--gold-400)', letterSpacing: '0.06em', marginBottom: 8 }}>
            SELF-IMPROVING HETEROGENEOUS REASONING ENSEMBLE (SIHRE)
          </p>
          <p style={{ fontSize: '0.92rem', color: 'var(--text-b)', maxWidth: 560, lineHeight: 1.7, marginBottom: 24 }}>
            A proprietary AI architecture that fuses fundamentally different types of intelligence into a unified reasoning system. Not a bigger model — a new kind of model.
          </p>
          <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap' }}>
            <a href="https://sihre.ai" target="_blank" rel="noopener" className="btn btn-gold btn-sm">Learn more at sihre.ai</a>
            <button className="btn btn-ghost btn-sm" onClick={function() { document.getElementById('sihre-whitepaper').scrollIntoView({ behavior: 'smooth' }); }}>Download Whitepaper</button>
          </div>
        </div>
      </Rv>

      {/* Whitepaper download */}
      <Rv delay={60}>
        <div id="sihre-whitepaper" className="card card-sihre" style={{ marginBottom: '1.5rem', padding: '1.5rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: 16 }}>
            <div style={{ flex: 1, minWidth: 240 }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 8 }}>
                <span style={{ fontSize: '1.5rem' }}>&#128220;</span>
                <h3 style={{ fontSize: '1rem', color: 'var(--gold-300)' }}>SIHRE Whitepaper</h3>
              </div>
              <p style={{ fontSize: '0.85rem', color: 'var(--text-b)', lineHeight: 1.6, marginBottom: 6 }}>
                <em>Meta-Orchestrated Heterogeneous Reasoning for Adaptive Intelligence Under Non-Stationarity</em>
              </p>
              <p style={{ fontSize: '0.78rem', color: 'var(--text-m)', lineHeight: 1.5, marginBottom: 12 }}>
                By Paul Russell (chartShooter) &middot; v0.1 &middot; May 2026
              </p>
              <a href="#pricing" className="btn btn-gold btn-sm">
                &#128196; Request Whitepaper (PDF)
              </a>
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
              {['Architecture overview', 'Signal fusion design', 'Governance framework', 'Domain applications', 'Competitive analysis'].map(function(item) {
                return <div key={item} style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: '0.72rem' }}>
                  <span style={{ color: 'var(--gold-400)', fontSize: '0.5rem' }}>{'●'}</span>
                  <span style={{ color: 'var(--text-m)' }}>{item}</span>
                </div>;
              })}
            </div>
          </div>
        </div>
      </Rv>

      {/* Disclaimer */}
      <Rv delay={80}>
        <div className="card" style={{ marginBottom: '1.5rem', borderColor: 'rgba(251,191,36,0.15)', padding: '1rem 1.25rem' }}>
          <div style={{ display: 'flex', alignItems: 'flex-start', gap: 10 }}>
            <span style={{ fontSize: '0.9rem', marginTop: 1 }}>&#9888;&#65039;</span>
            <div>
              <strong style={{ fontSize: '0.82rem', color: 'var(--text-h)', display: 'block', marginBottom: 4 }}>Proprietary Technology</strong>
              <p style={{ fontSize: '0.78rem', color: 'var(--text-m)', lineHeight: 1.6 }}>
                NeuroFusion and the SIHRE architecture are proprietary technologies with a patent pending. The examples on this page illustrate <em>how the system reasons</em> at a conceptual level — they do not reveal the underlying signal architecture, model weights, or orchestration algorithms. For detailed technical information, visit <a href="https://sihre.ai" target="_blank" rel="noopener" style={{ color: 'var(--gold-400)' }}>sihre.ai</a> or request the whitepaper above.
              </p>
            </div>
          </div>
        </div>
      </Rv>

      {/* Interactive reasoning examples */}
      <Rv delay={100}>
        <div style={{ marginBottom: '1.5rem' }}>
          <h2 style={{ fontSize: '1.2rem', marginBottom: 6 }}>How Does SIHRE Reason?</h2>
          <p style={{ fontSize: '0.82rem', color: 'var(--text-m)', marginBottom: 16, maxWidth: 560, lineHeight: 1.6 }}>
            Choose your answer for each scenario, then reveal how heterogeneous reasoning approaches the same problem. See where your intuition aligns — and where it diverges.
          </p>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
            {REASONING_SCENARIOS.map(function(s, idx) {
              var isOpen = openScenario === s.id;
              var userAnswer = answers[s.id];
              var isRevealed = revealed[s.id];
              var isCorrect = userAnswer === s.sihre_answer;

              return (
                <Rv key={s.id} delay={idx * 30}>
                  <div className={'card ' + (isOpen ? 'card-active' : '')}
                    style={{ cursor: 'pointer', borderLeftWidth: 3, borderLeftColor: isOpen ? 'var(--gold-400)' : 'rgba(251,191,36,0.1)' }}
                    onClick={function() { if (!isOpen) setOpenScenario(s.id); }}>
                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}
                      onClick={function(e) { if (isOpen) { e.stopPropagation(); setOpenScenario(null); } }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                        <span style={{ fontSize: '1rem' }}>{s.icon}</span>
                        <div>
                          <strong style={{ fontSize: '0.85rem', color: isOpen ? 'var(--gold-300)' : 'var(--text-h)' }}>{s.title}</strong>
                          {isRevealed != null && userAnswer != null && (
                            <span className={'badge ' + (isCorrect ? 'badge-green' : 'badge-blue')} style={{ marginLeft: 8, fontSize: '0.5rem', padding: '1px 6px' }}>
                              {isCorrect ? 'Aligned' : 'Diverged'}
                            </span>
                          )}
                        </div>
                      </div>
                      <span style={{ fontSize: '0.7rem', color: 'var(--text-d)', transition: 'transform 0.3s', transform: isOpen ? 'rotate(180deg)' : 'rotate(0)', fontFamily: 'var(--font-m)', cursor: 'pointer' }}>{'▼'}</span>
                    </div>

                    <div style={{ maxHeight: isOpen ? 3000 : 0, overflow: 'hidden', transition: 'max-height 0.6s cubic-bezier(0.16,1,0.3,1)' }}>
                      <div style={{ paddingTop: 16 }} onClick={function(e) { e.stopPropagation(); }}>
                        <p style={{ fontSize: '0.82rem', color: 'var(--text-b)', lineHeight: 1.6, marginBottom: 14, padding: '10px 14px', borderRadius: 8, background: 'rgba(59,130,246,0.04)', borderLeft: '2px solid rgba(59,130,246,0.2)' }}>
                          {s.desc}
                        </p>
                        <p style={{ fontSize: '0.85rem', color: 'var(--text-h)', marginBottom: 10, fontWeight: 600 }}>{s.question}</p>

                        <div style={{ display: 'flex', flexDirection: 'column', gap: 6, marginBottom: 14 }}>
                          {s.options.map(function(opt, oi) {
                            var isSelected = userAnswer === oi;
                            var isSihre = isRevealed && oi === s.sihre_answer;
                            var borderCol = isSihre ? 'rgba(251,191,36,0.5)' : isSelected ? 'var(--border-hover)' : 'var(--border)';
                            var bgCol = isSihre ? 'rgba(251,191,36,0.06)' : isSelected ? 'rgba(59,130,246,0.08)' : 'transparent';
                            return (
                              <div key={oi}
                                onClick={function() { if (!isRevealed) selectAnswer(s.id, oi); }}
                                style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '10px 14px', borderRadius: 10, border: '1px solid ' + borderCol, background: bgCol, cursor: isRevealed ? 'default' : 'pointer', transition: 'all 0.2s' }}>
                                <div style={{ width: 20, height: 20, borderRadius: '50%', border: '2px solid ' + (isSelected ? 'var(--blue-400)' : isSihre ? 'var(--gold-400)' : 'var(--border)'), display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0, transition: 'all 0.2s' }}>
                                  {isSelected && <div style={{ width: 10, height: 10, borderRadius: '50%', background: 'var(--blue-400)' }}></div>}
                                  {isSihre && !isSelected && <div style={{ width: 10, height: 10, borderRadius: '50%', background: 'var(--gold-400)' }}></div>}
                                </div>
                                <span style={{ fontSize: '0.82rem', color: isSihre ? 'var(--gold-300)' : isSelected ? 'var(--text-h)' : 'var(--text-b)' }}>{opt}</span>
                                {isSihre && <span className="badge badge-gold" style={{ fontSize: '0.5rem', padding: '1px 5px', marginLeft: 'auto' }}>SIHRE</span>}
                              </div>
                            );
                          })}
                        </div>

                        {userAnswer != null && !isRevealed && (
                          <button className="btn btn-gold btn-sm" onClick={function() { revealReasoning(s.id); }}>
                            Reveal SIHRE's Reasoning
                          </button>
                        )}

                        {isRevealed && (
                          <div style={{ marginTop: 4 }}>
                            <span className="label" style={{ color: 'var(--gold-400)', marginBottom: 10, display: 'block' }}>How heterogeneous reasoning approaches this</span>
                            <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                              {s.reasoning.map(function(r, ri) {
                                var isOrch = r.type === 'Orchestrator';
                                return (
                                  <div key={ri} style={{ padding: '10px 14px', borderRadius: 10, background: isOrch ? 'rgba(251,191,36,0.06)' : 'rgba(59,130,246,0.03)', borderLeft: '3px solid ' + r.color }}>
                                    <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 4 }}>
                                      <span style={{ width: 8, height: 8, borderRadius: '50%', background: r.color, boxShadow: '0 0 6px ' + r.color + '50' }}></span>
                                      <strong style={{ fontSize: '0.72rem', color: r.color, fontFamily: 'var(--font-m)', letterSpacing: '0.04em', textTransform: 'uppercase' }}>{r.type}</strong>
                                    </div>
                                    <p style={{ fontSize: '0.78rem', color: isOrch ? 'var(--gold-300)' : 'var(--text-b)', lineHeight: 1.55, fontWeight: isOrch ? 500 : 400 }}>{r.says}</p>
                                  </div>
                                );
                              })}
                            </div>
                          </div>
                        )}
                      </div>
                    </div>
                  </div>
                </Rv>
              );
            })}
          </div>
        </div>
      </Rv>

      {/* Simulator */}
      <Rv delay={120}>
        <div style={{ marginBottom: '1.5rem' }}>
          <h2 style={{ fontSize: '1.2rem', marginBottom: 6 }}>Trade Reasoning Simulator</h2>
          <p style={{ fontSize: '0.82rem', color: 'var(--text-m)', marginBottom: 16, maxWidth: 560, lineHeight: 1.6 }}>
            Walk through a complete trade from pre-market to post-trade review. Make your decisions at each stage, then compare your reasoning process against SIHRE's approach.
          </p>

          {!simDone ? (
            <div className="card card-sihre" style={{ padding: '1.5rem' }}>
              {/* Progress bar */}
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 16 }}>
                {SIM_STEPS.map(function(_, i) {
                  var done = i < simStep;
                  var active = i === simStep;
                  return (
                    <div key={i} style={{ flex: 1, height: 4, borderRadius: 2, background: done ? 'var(--gold-400)' : active ? 'rgba(251,191,36,0.3)' : 'rgba(251,191,36,0.08)', transition: 'background 0.3s' }}></div>
                  );
                })}
                <span style={{ fontSize: '0.65rem', color: 'var(--text-d)', fontFamily: 'var(--font-m)', flexShrink: 0 }}>{simStep + 1}/{SIM_STEPS.length}</span>
              </div>

              <div style={{ marginBottom: 6 }}>
                <span className="label" style={{ color: 'var(--gold-400)' }}>{'Stage ' + (simStep + 1)}</span>
              </div>
              <h3 style={{ fontSize: '1rem', marginBottom: 10, color: 'var(--gold-300)' }}>{SIM_STEPS[simStep].title}</h3>
              <p style={{ fontSize: '0.85rem', color: 'var(--text-b)', lineHeight: 1.65, marginBottom: 16, padding: '10px 14px', borderRadius: 8, background: 'rgba(59,130,246,0.04)', borderLeft: '2px solid rgba(59,130,246,0.2)' }}>
                {SIM_STEPS[simStep].situation}
              </p>
              <p style={{ fontSize: '0.88rem', color: 'var(--text-h)', marginBottom: 12, fontWeight: 600 }}>{SIM_STEPS[simStep].question}</p>

              <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                {SIM_STEPS[simStep].options.map(function(opt, oi) {
                  return (
                    <button key={oi}
                      onClick={function() { selectSimAnswer(oi); }}
                      style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '12px 16px', borderRadius: 10, border: '1px solid var(--border)', background: 'var(--surface)', cursor: 'pointer', textAlign: 'left', transition: 'all 0.2s', color: 'var(--text-b)', fontSize: '0.85rem' }}
                      onMouseOver={function(e) { e.currentTarget.style.borderColor = 'rgba(251,191,36,0.3)'; e.currentTarget.style.background = 'rgba(251,191,36,0.04)'; }}
                      onMouseOut={function(e) { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.background = 'var(--surface)'; }}>
                      <span style={{ width: 24, height: 24, borderRadius: 6, display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'rgba(251,191,36,0.08)', border: '1px solid rgba(251,191,36,0.15)', fontFamily: 'var(--font-m)', fontSize: '0.65rem', color: 'var(--gold-400)', flexShrink: 0 }}>{String.fromCharCode(65 + oi)}</span>
                      {opt.label}
                    </button>
                  );
                })}
              </div>
            </div>
          ) : (
            <div className="card card-sihre" style={{ padding: '1.5rem' }}>
              <h3 style={{ fontSize: '1rem', marginBottom: 16, color: 'var(--gold-300)' }}>Simulation Complete</h3>

              {/* Score comparison */}
              <div className="bento bento-2" style={{ marginBottom: 20 }}>
                <div className="card" style={{ textAlign: 'center', borderColor: 'var(--border-hover)' }}>
                  <span className="label" style={{ marginBottom: 6, display: 'block' }}>Your Score</span>
                  <div className="mono" style={{ fontSize: '2rem', fontWeight: 700, color: 'var(--blue-400)' }}>{simScore}</div>
                  <span style={{ fontSize: '0.7rem', color: 'var(--text-d)' }}>out of {SIM_STEPS.length * 4}</span>
                </div>
                <div className="card" style={{ textAlign: 'center', borderColor: 'var(--border-gold)' }}>
                  <span className="label" style={{ color: 'var(--gold-400)', marginBottom: 6, display: 'block' }}>SIHRE Score</span>
                  <div className="mono" style={{ fontSize: '2rem', fontWeight: 700, color: 'var(--gold-400)' }}>{simSihreScore}</div>
                  <span style={{ fontSize: '0.7rem', color: 'var(--text-d)' }}>out of {SIM_STEPS.length * 4}</span>
                </div>
              </div>

              <div style={{ marginBottom: 16, padding: '12px 16px', borderRadius: 10, background: 'rgba(251,191,36,0.04)', borderLeft: '3px solid var(--gold-400)' }}>
                <p style={{ fontSize: '0.82rem', color: 'var(--text-b)', lineHeight: 1.6 }}>
                  {simScore >= simSihreScore
                    ? 'Impressive — your reasoning aligned with or exceeded SIHRE\'s approach. You\'re already thinking in multi-signal terms. Imagine that consistency across every trade, every session, every market condition.'
                    : simScore >= simSihreScore - 3
                    ? 'Close match. Your intuition is strong, but SIHRE found edge in the nuances — the places where context, uncertainty quantification, and cross-signal validation change the optimal decision.'
                    : 'This is exactly why heterogeneous reasoning exists. Individual traders rely on 1-2 reasoning modes. SIHRE fuses many different types of intelligence simultaneously — each catching what the others miss.'}
                </p>
              </div>

              {!simReveal ? (
                <div style={{ display: 'flex', gap: 10 }}>
                  <button className="btn btn-gold btn-sm" onClick={function() { setSimReveal(true); }}>Show Step-by-Step Comparison</button>
                  <button className="btn btn-ghost btn-sm" onClick={resetSim}>Try Again</button>
                </div>
              ) : (
                <div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: 10, marginBottom: 16 }}>
                    {SIM_STEPS.map(function(step, i) {
                      var userOpt = step.options[simAnswers[i]];
                      var sihreOpt = step.options[step.sihre_choice];
                      var match = simAnswers[i] === step.sihre_choice;
                      return (
                        <div key={i} className="card" style={{ borderLeftWidth: 3, borderLeftColor: match ? '#10b981' : 'var(--gold-400)' }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 8 }}>
                            <span className="label" style={{ color: match ? '#10b981' : 'var(--gold-400)' }}>{'Stage ' + (i + 1) + ': ' + step.title}</span>
                            <span className={'badge ' + (match ? 'badge-green' : 'badge-gold')} style={{ fontSize: '0.5rem', padding: '1px 5px' }}>{match ? 'Match' : 'Diverged'}</span>
                          </div>
                          <div className="bento bento-2" style={{ gap: 8, marginBottom: 8 }}>
                            <div style={{ padding: '8px 10px', borderRadius: 8, background: 'rgba(59,130,246,0.04)', border: '1px solid rgba(59,130,246,0.1)' }}>
                              <span style={{ fontSize: '0.62rem', color: 'var(--blue-400)', fontFamily: 'var(--font-m)', letterSpacing: '0.04em', textTransform: 'uppercase' }}>You chose</span>
                              <p style={{ fontSize: '0.78rem', color: 'var(--text-b)', marginTop: 2 }}>{userOpt.label}</p>
                            </div>
                            <div style={{ padding: '8px 10px', borderRadius: 8, background: 'rgba(251,191,36,0.04)', border: '1px solid rgba(251,191,36,0.1)' }}>
                              <span style={{ fontSize: '0.62rem', color: 'var(--gold-400)', fontFamily: 'var(--font-m)', letterSpacing: '0.04em', textTransform: 'uppercase' }}>SIHRE chose</span>
                              <p style={{ fontSize: '0.78rem', color: 'var(--gold-300)', marginTop: 2 }}>{sihreOpt.label}</p>
                            </div>
                          </div>
                          <p style={{ fontSize: '0.75rem', color: 'var(--text-m)', lineHeight: 1.55, fontStyle: 'italic' }}>{step.sihre_reasoning}</p>
                        </div>
                      );
                    })}
                  </div>
                  <button className="btn btn-ghost btn-sm" onClick={resetSim}>Run Simulation Again</button>
                </div>
              )}
            </div>
          )}
        </div>
      </Rv>

      {/* CTA */}
      <Rv delay={140}>
        <div className="card card-gold" style={{ textAlign: 'center', padding: '2rem' }}>
          <h2 style={{ fontSize: '1.1rem', marginBottom: 8 }}>Experience NeuroFusion</h2>
          <p style={{ color: 'var(--text-m)', marginBottom: 16, fontSize: '0.88rem' }}>
            Join the waitlist for early access to heterogeneous reasoning.
          </p>
          <div style={{ display: 'flex', gap: 10, justifyContent: 'center', flexWrap: 'wrap' }}>
            <a href="#pricing" className="btn btn-gold">Join Waitlist</a>
            <a href="https://sihre.ai" target="_blank" rel="noopener" className="btn btn-ghost">Visit sihre.ai</a>
          </div>
        </div>
      </Rv>
    </div>
  );
}

window.NeuroFusionPage = NeuroFusionPage;
