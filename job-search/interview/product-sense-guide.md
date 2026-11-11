# Product sense interview guide

<purpose>
How to pass a product sense round (also called product design or product case). Built on 2026-10-24 from articles the candidate pasted: Ben Erez in Lenny's Newsletter (the main source), Rohan Katyal, igotanoffer's Meta guide with ex-Meta coaches, Adam Li, Jens-Fabian Goetzmann, Aakash Gupta, ProdPad, PMMockr, Prepfully, and a Hacker News thread. Use it to prep for any product sense round. Section 10 is the rubric for product sense mocks.
</purpose>

## 1. What the round is

- One open prompt, about 45 minutes, roughly 35 for the case after intros and your questions [Erez]. You lead. The interviewer mostly listens, nudges, and often answers your questions with "that's up to you."
- It compresses discovery into one sitting: why the product matters, who it's for, what hurts them, and what to build first. Meta calls this the "Understand, Identify" part of "Understand, Identify, Execute" [igotanoffer]. Building and shipping are tested in the execution round, not here [Prepfully].
- The rubric is about the same at every level [Erez, Akila at igotanoffer]. Level is mostly set by the behavioral round. What changes with seniority is where you spend time: junior candidates rush to clever solutions, experienced ones spend it on segments and pain points [Akila]. At director level and above (Meta L7+), interviewers also look for "10x" thinking, a bigger bet than an incremental feature [igotanoffer, Nancy Chu].
- The interviewer is usually a busy PM filling a scorecard. Your job is to hand them clear, easy-to-find signals [Erez].

### The five dimensions you're scored on [Erez]
You need at least a passing score on every one. A great solution can't make up for weak segmentation.

| Dimension | What they want to see |
|---|---|
| Clear communication | Assumptions, a stated plan, signposts, check-ins |
| Product motivation | Why the product exists, for users and for the company, ending in a mission |
| Segmentation | Ecosystem players, three distinct segments, one picked with a reason, a persona |
| Problem identification | A journey, three real problems (not needs), one picked by frequency and severity |
| Solution development | Three different solutions, one picked by impact and effort, a v1, risks |

Meta scores each criterion as Below Expectations, Meets, Strong, or Exceptional, and the interviewer adds a summary such as "soft no" or "strong yes" [igotanoffer].

### When "product sense" isn't a case (learned 2026-10-26)
At startups, an exec round billed as product sense can be product judgment instead: "a time you got the customer wrong", an ops blind spot, and "walk me through something you built with your own hands". For any exec round labeled product sense, also prep a customer-misread story and a 90-second hands-on AI build told as decisions (what you chose not to build, what the AI got wrong).

## 2. Prompt types

| Type | Example | Notes |
|---|---|---|
| Design (0 to 1) | "Design a product for gardening at Meta." "Build a podcast product for Netflix." "Design a product to help users find a doctor on Facebook." | The most common case format at Meta |
| Improve | "How would you improve Facebook Groups?" "Improve LinkedIn messaging." | Same framework, start from the existing product |
| Favorite product | "Tell me about a product you love and how you'd improve it." | The single most asked prompt [Gunaca]. Have two ready |
| Strategy | "Should Meta enter dating?" "Facebook Events is struggling, turn it around." | Same flow, lighter on users, heavier on market and company advantage |
| AI product sense | "Define success for Meta AI chat." "AI meeting notes cut Zoom attendance. What do you do?" | At Meta this is now a separate round, sometimes with live vibe coding [igotanoffer] |
| Growth, pricing, metrics | "Improve retention for X." "Price this new product." | Overlap with the analytical round [Gupta] |

Some interviewers skip the case and run it from your own apps: "List apps you use, I'll pick one" [Goetzmann]. Some ask "What's your favorite product?" as casual chat and turn it into a case [Gupta]. Treat both as the same exam.

## 3. The game plan and time budget (35 minutes)

| Step | Minutes | Output |
|---|---|---|
| 0. Pause, assumptions, plan | 3–5 | 2–4 assumptions, the plan, "does this sound good?" |
| 1. Product motivation | 3–5 | What it is, why it matters, company fit, mission |
| 2. Segmentation | 8–10 | Ecosystem, pick one player, 3 segments, pick one, persona |
| 3. Problems | 8–10 | Journey, 3 problems, pick one by frequency × severity |
| 4. Solutions | 8–10 | 3 different solutions, pick one by impact × effort, v1, risks |
| 5. Metrics and wrap | 2–3 | Success metric, counter-metric, validation step, one-line summary |

Before each step, take 30 seconds to 2 minutes of silent thinking, then present, then check in [Erez]. Take about 20 seconds right after the prompt [Katyal]. Ask for the time: "Mind if I take a minute to organize my thoughts?"

### Step 0. Assumptions and plan

Restate the prompt in one sentence [Adam Li]. Then make 2–4 assumptions that narrow the scope without picking the answer [Erez]:
- **Role and context:** "I'm the PM for a new zero-to-one product at Netflix."
- **Geography:** "US first, built so it can go global."
- **Platform or constraint:** "Inside Meta's apps rather than standalone, for distribution."
- **Scope:** "Home gardening, not commercial."

Other useful levers: company stage, timeline, team size, hardware or software, for-profit or social good [Adam Li, Medium "Define the basics"].

State, don't interrogate. The sources split here. Katyal and the HN commenter want clarifying questions, Prepfully says don't start with vague questions or ask permission. The way through both is to state the assumption and invite a correction: "I'll assume X. Stop me if you had something else in mind." Ask a real question only when the answer changes the whole case (for example "improve engagement on Maps" could mean businesses or drivers [Katyal]).

Then the plan, nearly word for word [Erez]:
> "Before I dive in, here's my plan. I'll start with what the product is and why it matters. Then I'll look at the audience and pick a segment. Then I'll find that segment's key problems and pick one. Then I'll brainstorm solutions and pick one, and if we have time, sketch a v1 and how we'd measure it. Does that sound good?"

#### Examples
**Good 1 (Netflix podcasts):** "So you'd like a podcast product for Netflix. I'll assume I'm the PM for a new zero-to-one product, US first, built inside the Netflix app so we start with existing subscribers, and audio rather than video podcasts since most listening is audio-only. Stop me if you had something else in mind. Here's my plan: why this matters for Netflix, who it's for, their biggest problem, then solutions and a v1. Sound good?"
*Why it works:* four assumptions that bound the case without choosing the answer, each with a reason, and a plan the interviewer can track.

**Good 2 (Meta gardening):** "Let me take a minute to organize my thoughts. ... Okay. I'm a PM at Meta building something new for gardening. I'll focus on personal and home gardening, not commercial farms, and I'll build within Facebook, Instagram, and WhatsApp for distribution. US first. One question that changes the case: is there a business goal you'd like me to favor, or is that up to me? ... Up to me, great. I'll optimize for people getting value first and come back to monetization at the end."
*Why it works:* asks for thinking time, asks only the one question that matters, and handles "up to you" by making a call.

**Bad 1:** "Okay, podcasts on Netflix. So I think the first thing is a podcast tab, and then maybe recommendations based on what you watched, and we could add video clips..."
*Why it fails:* no assumptions, no plan, straight into features. The interviewer can't tell where this is going or score any dimension yet.

**Bad 2:** "Before I start, a few questions. What's the budget? How big is the team? What's the timeline? Which platforms? Which countries? Should I focus on listeners or creators? What would you like me to cover first?"
*Why it fails:* an interrogation that hands the work back to the interviewer. The last two questions read as no ownership. State assumptions instead and ask at most one question.

### Step 1. Product motivation

Three parts [Erez]:
1. **What it is and the human need behind it.** Not "helps users share photos" but "lets people stay close to family through pictures when they're apart."
2. **Why this company, why now.** Mission fit, the company's unfair advantages (users, graph, content, data, brand), competitors, and a trend that makes it timely [Adam Li]. Include substitutes and non-consumption, not only obvious rivals [Goetzmann].
3. **A mission statement** that guides every later choice. Specific enough to rule things out, broad enough to leave room. Example: "Help people connect and grow through gardening, in their communities and their gardens."

Define the goal as a user outcome, not a metric. "Help people get around," not "increase route searches" [Katyal]. Optionally name the business objective you'll favor (growth, engagement, monetization) and why [Adam Li, Medium].

Pitfalls: listing features instead of purpose, a vague mission ("help users be more productive"), a direction that ignores the company's strengths [Erez].

#### Examples
**Good 1 (Netflix podcasts):** "Netflix wants to entertain the world, and people already spend hours a day listening while they commute, work out, or cook, moments when they can't watch a screen. Spotify and Apple lead podcasts, but discovery there is weak and most shows don't make money. Netflix brings a recommendation engine, stories people already love, and a paid subscription. The mission I'll use: help people stay with the stories they love when they can't watch."
*Why it works:* human need (listening when you can't watch), company advantage, competitors with their weakness, and a mission that will rule things in and out later.

**Good 2 (Meta gardening):** "Gardening is food, beauty, and calm for a lot of people, and it surged during the pandemic. The knowledge is scattered across YouTube, nursery staff, and Reddit, and most of it isn't local to your climate or your balcony. Meta's mission is to bring people closer together, and it already has local groups and a social graph. The real competitor is often your neighbor who's good with plants. Mission: help people learn to grow things from people near them."
*Why it works:* names a substitute (the neighbor), ties to Meta's real asset, and the mission points toward a community-shaped solution.

**Bad 1:** "Podcasts are a big market, worth billions of dollars and growing. Netflix should get into it to increase engagement and watch time. My goal is to increase daily active users."
*Why it fails:* market size instead of a human need, and a metric posing as a goal. Nothing here guides the later choices.

**Bad 2:** "Gardening is a hobby a lot of people like. Meta could build an app with plant identification, a watering reminder, a marketplace, and a forum. The mission is to help people garden better."
*Why it fails:* a feature list instead of purpose, and a mission too vague to rule anything out.

### Step 2. Segmentation

1. **Ecosystem players.** Demand side, supply side, third parties, regulators [Adam Li]. Netflix podcasts: listeners, creators, advertisers, internal teams, competing platforms. Pick one player with a one-line reason, then check in: "I'd like to focus on listeners because they're the demand side. Does that make sense before I segment them?" [Erez]
2. **Three segments** within that player, based on motivation and behavior, not age or income [Erez, idoh on HN: "never segment on age, that's boring"]. Start from why people use the product, then use levers like frequency, context, expertise, constraints (time, money, space), and goals. Gardening: food growers, decorators, wellness gardeners, social gardeners.
3. **Mutual exclusivity test.** Could one person sit in two segments at once? If yes, redraw them [Erez].
4. **Pick one** with a consistent lens. Erez uses reach × how underserved (force Low or High, no middle). Adam Li adds strategy fit and company strength. Say the lens out loud before you score [Katyal].
5. **Persona.** One person with a name, context, and constraint. "Casey, 29, marketing job, city apartment with a small balcony, excited but doesn't know where to start." Think of someone you know [Adam Li].

The ex-Meta view: "If user segmentation is strong, it sets the rest of the interview up for a win" [Akila]. Prepfully adds that the interviewer cares less that the segment is perfect and more that you can defend it.

#### Examples
**Good 1 (Netflix podcasts):** "The ecosystem has listeners, podcast creators, advertisers, Netflix's own content teams, and rival platforms. I'll focus on listeners, since without demand nothing else matters. Does that work? ... Within listeners, three segments by why they listen: story-followers who want more of a show they loved, learners who finish a documentary and want to go deeper, and background listeners who want company while they do chores. A learner and a background listener want opposite things, so they don't overlap. On reach and how underserved they are, learners are high on both, since nobody links a documentary to deeper audio today. Persona: Alex, 34, watches a science documentary most weekends and then spends an hour on Wikipedia, and listens to podcasts on a 40-minute commute."
*Why it works:* ecosystem first with a check-in, segments built on motivation, an exclusivity check, a stated lens, and a persona with real behavior.

**Good 2 (Meta gardening):** "I'll focus on home gardeners. Three segments: food growers who want a harvest, decorators who want their space to look good, and first-timers who've never kept a plant alive. They differ in goal and skill, not age. First-timers are high reach and highly underserved, since every guide assumes some basics, and Meta can reach them where they already are. Persona: Casey, 29, marketing job, apartment with a small north-facing balcony, bought two plants that died and is close to giving up."
*Why it works:* each segment needs a different product, and the persona's constraint (north-facing, two dead plants) will drive the problems.

**Bad 1:** "My target users are millennials, Gen Z, and older adults. I'll pick millennials because they use Netflix the most."
*Why it fails:* demographic segments say nothing about needs, and there's no ecosystem view. This is the most common segmentation failure in the sources.

**Bad 2:** "Segments: beginner gardeners, people who grow vegetables, urban gardeners, and people who use Instagram. I'll go with urban gardeners."
*Why it fails:* the segments overlap (one person can be all four), there's no reason for the choice, and no persona.

### Step 3. Problems

1. **A journey specific to the persona,** a day in their life, not a generic before/during/after [Erez]. Gardening: inspiration, research, planning, buying, setup, care, troubleshooting, harvest.
2. **Three problems,** spread across the journey. Write them as obstacles, not wishes:
   - Need: "I want flowers in my apartment."
   - Problem: "I can't tell which flowers will survive my apartment's low light, so I keep buying plants that die." [Erez]
   - Not a solution in disguise: "users need a better recommendation algorithm" is a solution. "Users can't find content that fits them" is the problem [Erez].
3. **Pick one** by frequency × severity [Erez]. Other lenses: how poor current alternatives are, urgency, company fit [Adam Li]. Use the same lens style as segmentation [Katyal].
4. **Tie it to the mission.** "This matters most because if Casey picks the wrong plant, she quits before she starts, and our mission is about people growing."

Do a 15-second recap before this step and before solutions: what we decided, what's next, any concerns? [Adam Li]

#### Examples
**Good 1 (Netflix podcasts):** "Quick recap: we're serving learners like Alex. Here's Alex's journey: finishes a documentary, looks for more, judges whether a show is worth the time, listens on the commute, and tries to remember or share what they learned. Three problems. First, after the credits, Alex can't find audio that goes deeper on the same topic, so the curiosity fades by Monday. Second, they can't tell whether a podcast will repeat what they just watched. Third, they forget most of it within a week. On frequency and severity, the first is highest: it happens after every documentary, and losing that moment is the whole opportunity. It fits our mission of staying with the story when you can't watch."
*Why it works:* a journey specific to Alex, problems written as obstacles with a consequence, a stated lens, and a tie to the mission.

**Good 2 (Meta gardening):** "Casey's day: she sees a friend's balcony on Instagram, searches what might grow on hers, buys plants, sets them up, waters, notices yellow leaves, and wonders what she did wrong. Problems: she can't tell which plants will survive her light and space, she can't diagnose a sick plant before it dies, and she has nobody nearby to ask. The first one is the worst. It happens at the very start, and two dead plants are why she's about to quit."
*Why it works:* each problem sits at a different journey step, and the pick is defended with severity tied to the persona.

**Bad 1:** "Pain points: users want better recommendations, users want an easy interface, and users want more content. I'll pick better recommendations."
*Why it fails:* these are wishes and disguised solutions, not obstacles, and they'd fit any product. No journey, no lens.

**Bad 2:** "The biggest problem is that there's no AI plant assistant in Instagram, so I'll solve that."
*Why it fails:* the problem is the absence of a solution. The interviewer hears that you started from the answer and worked backward.

### Step 4. Solutions

1. **Brainstorm three that differ in mechanism,** not three versions of one idea. One practical, one ambitious, one moonshot [Adam Li, Prepfully]. Sources of ideas: the company's assets, an analogy from another industry, a new technology used for a reason, another business model (marketplace, network, matching, subscription) [Erez, Adam Li].
2. **Pick one** by impact × effort, with reasons tied to the problem and the company's strengths [Erez]. Goetzmann's best answers tie the choice to strategy and admit the ideas are uncertain and need validation.
3. **v1.** Concrete enough to picture: who sees it, where, what they do, what they get. "A short questionnaire in Instagram about light, space, and time. AI suggests 3–5 plants with care steps. Start with the 50 most common houseplants." [Erez] Say where the "aha" moment is [Prepfully].
4. **Go to market.** How users find it, inside existing surfaces where possible [Erez].
5. **Risks and mitigations,** two of them. "Wrong recommendations kill plants and trust. Partner with experts and let users report results." [Erez]

At Director level, add a short "where this goes" line: what v3 looks like if v1 works, and why competitors would struggle to copy it [Erez on defensibility, Prepfully on vision].

#### Examples
**Good 1 (Netflix podcasts):** "Three ideas. Practical: a short audio companion series for top documentaries, with the director and experts going deeper. Ambitious: an AI-generated audio briefing, personalized to what you watched, with sources linked. Moonshot: a live audio room after a big documentary drops, with the experts taking questions. On impact and effort, I'd pick the companion series. It solves the after-credits moment directly, uses relationships Netflix already has, and Spotify can't copy it because it doesn't own the documentaries. v1: 5 documentaries, 3 episodes each, surfaced on the end-credits screen and in a Listen row. The aha moment is tapping 'keep going' as the credits roll. Risks: lower quality than the film, so the original teams produce it. And listening may cannibalize watching, so we track total time with Netflix, not just audio."
*Why it works:* three different mechanisms, a choice tied to the problem and a moat, a concrete v1 with an entry point, and two real risks.

**Good 2 (Meta gardening):** "Options: an AI plant matcher that asks about your light and space, a local mentor match with experienced gardeners nearby through Groups, and a camera that diagnoses a sick plant. I'd start with the matcher, high impact and moderate effort, using Meta's AI. Then I'd add the mentor match in v2, since that's where Meta's graph makes it hard to copy and it fits the connection mission. v1: a five-question flow in Instagram, 3–5 plant picks with care steps, the 50 most common balcony plants. Risk: bad picks kill plants and trust, so we start narrow, check picks with experts, and let users report results."
*Why it works:* picks the fast win, then shows where it goes and why it's defensible. That's the senior-level "where this goes" signal.

**Bad 1:** "I'd build a podcast tab with recommendations, playlists, offline downloads, a sleep timer, speed controls, and social sharing."
*Why it fails:* one solution dressed as a feature list. No alternatives, no prioritization, and nothing tied to Alex's problem.

**Bad 2:** "Three ideas: plant recommendations by AI, plant recommendations by quiz, and plant recommendations by experts. I'll do all three in phase one."
*Why it fails:* three versions of one idea, then a refusal to choose. Avoiding a pick is a weak response in every source.

### Step 5. Metrics, validation, wrap

- **One success metric** that shows the user problem got solved, plus a counter-metric to watch [Prepfully, Goetzmann].
- **Validate cheaply first.** User research, prototype tests, and existing data come before an A/B test [Goetzmann]. A small two-week test in a subset is a good final step [PMMockr]. State what result would prove you wrong.
- Know the A/B trap: you can't A/B test feature adoption, since control adoption is always zero [Goetzmann]. Test behavior change.
- **Summary in one sentence** [Adam Li]: "We designed [solution] for [segment] to solve [problem], so that [user outcome and business outcome]." A short tagline makes it memorable [Prepfully].

#### Examples
**Good 1 (Netflix podcasts):** "Success is the share of documentary completers who start a companion episode within 48 hours, and how many come back for a second episode. Counter-metric: total Netflix time per member, so audio adds to watching instead of replacing it. Before building, I'd interview ten documentary fans and test a mock end-credits prompt. Then a pilot on two titles. If fewer than [X]% start an episode, the problem isn't as strong as I thought. Summary: companion audio for documentary learners so the story keeps going after the credits, which deepens the reason to keep a Netflix subscription."
*Why it works:* a metric that shows the problem got solved, a counter-metric, cheap validation before a test, a result that would prove it wrong, and a one-line summary.

**Good 2 (Meta gardening):** "I'd measure whether matched plants are still alive at 30 days, from a quick check-in, and whether people come back to ask the next question. I'd watch that we don't flood feeds with plant content people didn't ask for. I'd validate with a prototype and 20 first-time gardeners before an A/B test, and when we do test, I'd measure plant survival and return visits, since adoption can't be compared against a control."
*Why it works:* measures a change in behavior and avoids the adoption trap Goetzmann describes.

**Bad 1:** "I'd look at daily active users, engagement, and revenue."
*Why it fails:* generic metrics that would fit any product and say nothing about whether Alex's problem got solved. No counter-metric.

**Bad 2:** "We'd launch it and A/B test adoption of the plant matcher to see if people like it."
*Why it fails:* jumps to the most expensive test, and adoption in the control group is zero by definition, so the test proves nothing.

## 4. Running the room

- **Signpost every transition.** "Now that we have a segment, I'll map Casey's journey." [Erez]
- **Lead, then check in.** Check-ins are "does this make sense?" after a decision, never "what would you like me to do next?" or "should I do X or Y?" That reads as no ownership [Erez, Prepfully]. Don't ask the interviewer to brainstorm for you [Medium].
- **Treat hints as instructions.** "Any other problems you'd consider?" means they want more breadth. A question about why you picked something means explain your lens [Erez]. A probe means they're scoring you seriously.
- **Hold or adapt under pushback.** If you can defend a choice, defend it calmly. If they push a different direction, take it without backtracking on everything [Prepfully, PMMockr].
- **Use the same prioritization logic all the way.** A segment picked for reach, a problem picked for severity, and a solution picked for ease can end up solving nothing you claimed mattered [Katyal].
- **Don't sound scripted.** Frameworks are a guide. Reading one out like a checklist is a top complaint from interviewers [ProdPad, Medium author who failed Google this way]. Adapt the steps to the prompt.
- **Write things down.** Prompt, assumptions, mission, chosen segment and problem. You'll refer back to them [Medium].
- **Separate yourself from the user.** You're one user, maybe an unusual one [Goetzmann].

#### Examples
**Good 1 (signposting and a check-in):** "We've picked first-time gardeners. Before I map Casey's journey, does that segment make sense to you?" ... Interviewer: "Why not food growers?" ... "Food growers are a bigger group, but they're well served by seed catalogs and forums. First-timers are where people quit, so the gap is bigger. If you'd rather I go with food growers, I can switch."
*Why it works:* signposts, checks in after a decision, defends the lens calmly, and stays open.

**Good 2 (taking a hint):** Interviewer: "Any other problems you'd consider?" ... "Yes, let me go wider. Beyond choosing plants, there's getting supplies to an apartment without a car, and the social side, since no one around her gardens. I'd still pick plant choice, because it decides whether she starts at all."
*Why it works:* reads the hint as a request for breadth, adds real options, and keeps the decision with its reason.

**Bad 1:** "Okay, I've listed segments. What would you like me to do next? Should I pick one, or do you want me to do pain points for all of them?"
*Why it fails:* hands the structure back to the interviewer, the exact ownership failure Erez and Prepfully warn about.

**Bad 2:** Interviewer: "Why learners over story-followers?" ... "Oh, good point. Let's switch to story-followers. Actually, maybe background listeners. I'm not sure, either could work."
*Why it fails:* folds on the first probe and abandons the lens. A probe is a request for reasoning, not a sign you were wrong.

## 5. The AI product sense round (Meta and others)

Candidates get a case and use AI tools to explore or prototype it. Prompt quality isn't the grade. Judgment is [Audrey at igotanoffer]:
- **The human delta:** spot generic, wrong, or misaligned AI output and say why and how to fix it.
- **Strategic leverage:** let the AI draft the commodity parts (baseline segments, feature lists, metric outlines) and spend your time on the hard trade-offs.
- **Product direction:** turn a vague goal into clear instructions with constraints, and iterate when output lacks depth.
- **Audit and redirect:** catch feasibility, privacy, policy, and cross-team problems the AI misses.

#### Examples
**Good 1 (the human delta):** "The AI gave me five segments. Three are age groups, so I'll rewrite them by motivation. It also suggested a feature that scans users' photos to find gardeners. That's a privacy problem at Meta's scale, so I'm cutting it and asking for options that rely on what people choose to share."
*Why it works:* spots generic output and a policy risk, says why, and redirects the AI.

**Good 2 (leverage):** "I'll have the AI draft a baseline list of user journeys and metrics so we can spend our time on the trade-off that matters: whether a plant matcher or a mentor match better fits the mission. I'll prompt it with the persona and the constraint that v1 ships in one quarter inside Instagram."
*Why it works:* uses AI for commodity thinking and gives it clear constraints, keeping the judgment for themselves.

**Bad 1:** "Here's what the AI came up with," then reading out its list of features without changing anything.
*Why it fails:* no human delta. The interviewer learns nothing about your judgment.

**Bad 2:** Spending ten minutes perfecting a long, clever prompt and never questioning the output.
*Why it fails:* the grade is judgment, not prompt quality [Audrey]. A beautiful prompt with unchecked output scores low.

## 6. Why experienced PMs fail this round

A senior PM on Hacker News with 5 years at a Big Tech company and 0-to-1 launches kept failing product sense despite strong real experience. The replies, plus the guides, point to the same causes:
- Answering from "how we did it at my company" instead of playing the case's game. The round grades the visible structure, not the experience behind it.
- Unclear user and problem. Most failures trace back to loose segments, weak scoping, or a solution that doesn't connect to the chosen segment's chosen pain [Akila].
- Jumping to features. One Medium interviewer calls this "a 100% no hire" [Medium].
- Not projecting confidence, so good answers sound like guesses [altdataseller on HN].

For the candidate specifically: the round is the same at Head of Product level, so the basics still decide it. Use real experience as evidence inside a step ("in my experience, novice users quit at setup, so I'd weight that problem higher"), not as a replacement for the step. Spend the saved time on segments and problems, and close with the bigger "where this goes" bet.

## 7. Pitfalls checklist

- [ ] Brainstorming before any structure
- [ ] No assumptions, or assumptions that pre-pick the answer
- [ ] Asking the interviewer what to do next
- [ ] Mission that is vague or just a metric
- [ ] Skipping the ecosystem and going straight to end users
- [ ] Segments by age or income, or segments that overlap
- [ ] Problems written as needs or as solutions
- [ ] Generic journey that fits any product
- [ ] One solution only, or three variations of one idea
- [ ] Feature lists instead of how it solves the problem
- [ ] Solution that ignores the company's strengths
- [ ] Changing prioritization logic between steps
- [ ] No metric, no counter-metric, or jumping straight to A/B tests
- [ ] Sounding rehearsed
- [ ] Running out of time before solutions (watch the clock at minute 15 and minute 25)

## 8. One-page template

```
PROMPT (restated):
ASSUMPTIONS: role/company · geography · platform · scope
PLAN: motivation → segments → problems → solutions → v1 + metrics  ("sound good?")

MOTIVATION: what it is / human need / why this company + now / competitors + substitutes
MISSION: "To help ___ ___ so that ___."

ECOSYSTEM: demand · supply · third parties · regulators   → pick ___ because ___ (check in)
SEGMENTS (by motivation/behavior):  A ___  B ___  C ___     (mutually exclusive?)
  reach H/L · underserved H/L          → pick ___ because ___
PERSONA: name, age, context, constraint

JOURNEY: step → step → step → step → step
PROBLEMS (obstacles, not wishes): 1 ___ 2 ___ 3 ___
  frequency H/L · severity H/L         → pick ___, ties to mission because ___ (recap)

SOLUTIONS (different mechanisms): practical ___ ambitious ___ moonshot ___
  impact H/L · effort H/L              → pick ___ because ___
V1: who / where / what they do / what they get / aha moment / how they find it
RISKS: 1 ___ → mitigation   2 ___ → mitigation
METRICS: success ___  counter ___  validate first by ___
VISION: if v1 works, v3 is ___ (why hard to copy)
SUMMARY: We built ___ for ___ to solve ___ so that ___.
```

## 9. Practice plan

- **Openings:** rehearse assumptions and the plan for 20–30 prompts until they're automatic [Erez].
- **One full case a day,** 30–45 minutes, then review against the checklist [PMMockr].
- **Drills** [Erez]: map 5+ ecosystem players for 5–10 products you use; rewrite 5 needs as problems; generate 3 different solutions in 5 minutes; place every option on a forced High/Low 2x2 and say it aloud.
- **Favorite products:** have two ready, each with a why, a segment, a problem, and an improvement. Know a few new apps you've tried and what you admire or dislike in each [Goetzmann].
- **Record yourself** on a call and watch it back [Medium].
- **Company prep:** for each loop, know the mission, main products, users, and competitors, and expect a prompt about their own product [ProdPad].

### Question bank
- Design a social travel product for Facebook. Design a travel product for Instagram.
- Design a jobs product for Facebook.
- Design a product to help users find a doctor on Facebook.
- Design a product for gardening at Meta. Build a podcast product for Netflix.
- Design a product for people to plan group activities.
- Design an app for neighbors to connect in their local community.
- Design a 10x better airplane boarding experience.
- Design a map-based product for SFMOMA.
- Design the ideal kitchen for a retirement community.
- What would you build to differentiate Reels from TikTok?
- How would you improve Facebook Groups? Facebook birthdays? LinkedIn messaging? Google Calendar? ChatGPT?
- Facebook Events is struggling. How would you turn it around?
- Should Meta enter dating? Come up with a new market Google could enter.
- How would you monetize Facebook Marketplace or Messenger?
- You're the PM for Meta AI chat. How would you define success?
- AI meeting notes went to all Zoom invitees and attendance dropped. What do you do?
- You're the PM for Spotify Podcasts. What goals and success metrics would you set?

## 10. Scoring rubric for product sense mocks

Score each dimension Below, Meets, Strong, or Exceptional, quote the moment that earned it, and give one rewritten line for anything below Strong.

| Dimension | Meets | Strong / Exceptional |
|---|---|---|
| Communication | Plan stated, sections clear | Owns the structure, signposts every turn, check-ins only after decisions, adapts to hints |
| Motivation | Says what it does and fits the company | Human need, company advantage, substitutes, a mission that later decisions visibly use |
| Segmentation | Three segments, one picked | Ecosystem first, motivation-based and exclusive segments, stated lens, vivid persona |
| Problems | Three problems, one picked | Specific journey, obstacles with context and emotion, root cause, tied to mission |
| Solutions | Several ideas, one picked, a v1 | Different mechanisms, company strengths, concrete v1 and aha, risks, defensible vision |
| Metrics and validation | A success metric | Metric tied to the problem, counter-metric, cheap validation before A/B |
| Time | Reached solutions | Reached v1, metrics, and summary inside 35 minutes |

Verdict per `mock-interview`: Strong hire, Hire, Lean no, or No hire, defaulting to Lean no unless the answer clearly earns more. Any dimension below Meets is a no.
