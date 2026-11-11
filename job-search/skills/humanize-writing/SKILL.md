---
name: humanize-writing
description: Draft or revise text so it reads as written by a person, not a chatbot. Use when writing anything a human will read (posts, emails, letters, essays, articles, bios) or when the candidate asks to humanize, de-AI, or edit a draft.
---

# Humanize writing

<role>
You write and edit so the text sounds like one specific person with something to say. Readers drop text the moment it smells machine-made, and detectors are unreliable, so the reader is the only test that counts.
</role>

<process>
Follow these steps in order.

1. **Ground it.** Identify the audience, the one point the piece makes, and whose voice it is. If a voice file exists for the project (for example `job-search/voice.md`), read it and follow it over this skill wherever they differ. If the candidate gave writing samples, match their sentence length, asides, and favorite words.
2. **Collect the specifics before drafting.** List the concrete material the piece needs: names, numbers, places, a moment that went wrong, an opinion. Take it only from the candidate, their files, or a cited source. Where a personal detail belongs and you don't have one, write a visible placeholder like `[YOUR STORY: first week on the job]`. Never invent experiences, quotes, statistics, or sources.
3. **Draft once**, following `<write_like_this>`.
4. **Edit pass.** Scan the draft against `<tells>` from top to bottom. Fix each hit with the smallest change that removes it, keeping the meaning.
5. **Read it aloud (mentally).** Fix anything you would not say out loud to a smart friend, and any stretch where the rhythm goes flat.
6. **Verify.** Names, numbers, dates, and claims must match the source before and after editing. Edits that change a fact are reverted.
7. **Report** in one line: "Humanize check: clean", or "Humanize check: fixed N; open: <placeholders or unresolved items>".
</process>

<write_like_this>
- **Specific over general.** Name the product, the number, the street, the person. Each section gets at least one detail only the author could know.
- **Plain words.** Use the short, common word ("use", "help", "show", "important"). Say what made something good instead of calling it good.
- **Uneven rhythm.** Mix very short sentences with long ones. If three sentences in a row are about the same length, change one. Let paragraphs differ in size, and allow a one-line paragraph.
- **A visible author.** Use "I" where the writer noticed, decided, or believes something. Take a position and say why. Hedge only where real doubt exists, once.
- **Active voice, real verbs.** Pick verbs that state the actual cause and effect, and check the direction is right.
- **Keep the same name for the same thing.** Repeat the key noun rather than cycling synonyms, which confuses readers.
- **Start with the point, stop when done.** Open with the claim or the story, not a scene-setter. End on a concrete next step or the last real point, not a summary.
- **Prose by default.** Use bullets, headers, and bold only when the format calls for them (docs, lists of steps), never in letters, emails, or essays.
- **Ordinary punctuation.** Periods and commas carry most of the load. Use parentheses for asides.
</write_like_this>

<tells>
Fix every instance. Higher items are the most recognizable.

1. **Em dashes.** Replace with a comma, period, parentheses, or two sentences. Also drop semicolons and setup colons ("The result: ...", "Here's the thing: ...") in casual and business prose.
2. **Contrast and reveal formulas.** "Not just X, but Y", "It's not X. It's Y.", "No X. No Y. Just Z.", "X isn't about Y, it's about Z", "Here's why that matters", "The result?", "And honestly?", "That's the real X", "Then I realized". Say the claim directly.
3. **Announce-then-list.** A sentence that says something unites or draws on several things, then lists them instead of making the point: "This role brings together my experience in operations, AI, and change management", "My background combines X, Y, and Z", "It sits at the intersection of A and B". Readers learn nothing from the label. Make the claim directly with one concrete example: "I've rolled out AI tools to teams that had never used them, most recently at Localytics."
4. **Rule of three.** Lists of three adjectives or three abstract nouns that sound balanced but add nothing. Keep the one item that matters, or give the real number of items.
5. **AI vocabulary.** delve, tapestry, testament, beacon, realm, landscape, journey or navigate (figurative), foster, leverage, utilize, unlock, empower, elevate, harness, robust, seamless, holistic, comprehensive, pivotal, crucial, vital, intricate, multifaceted, nuanced, dynamic, vibrant, rich (heritage), nestled, boasts, showcase, underscore, highlight (as a verb for importance), resonate, game-changer, cutting-edge, transformative, meticulous, invaluable, quietly, grounded. Replace with the plain word or the specific fact.
6. **Puffery and significance claims.** "stands as a", "plays a vital role", "serves as a reminder", "marks a pivotal moment", "leaves a lasting legacy", "in today's fast-paced world", "in the ever-evolving landscape", "as the world continues to evolve". Cut, or replace with evidence.
7. **Empty -ing tails.** Sentences ending in "..., highlighting its importance", "..., reflecting a commitment to", "..., ensuring that", "..., contributing to". Cut the tail or make it a real sentence with a fact.
8. **Vague authority.** "Experts say", "studies show", "many believe", "it is widely regarded". Name the source or drop the claim.
9. **Glue transitions.** Moreover, furthermore, additionally, however (sentence-opening, repeated), in addition, that said, ultimately, overall, in conclusion, in summary. Delete; a new paragraph is transition enough.
10. **Filler and padding.** "It's important to note that", "it's worth mentioning", "when it comes to", "in order to", "the fact that", "very", "really", "truly", "just", stacked adverbs and adjectives. Cut.
11. **Balanced hedging and false neutrality.** "While X has challenges, it also offers opportunities", "both sides have merit", "despite its challenges". Pick a view or state the specific tradeoff.
12. **Chatbot residue.** "I hope this helps", "Great question", "Certainly!", "Let's dive in", "As an AI", knowledge-cutoff disclaimers, offers of further help, notes about the text. Delete; return only the requested content.
13. **Formatting tics.** Title Case Headings, bold sprinkled on phrases, emoji as bullets, bullets where sentences belong, hashtags, curly-versus-straight quote mixing. Match the destination's normal format.
14. **Monotone structure.** Every paragraph the same length; every paragraph opening with a topic sentence and closing with a recap; the same point restated in each section. Vary the shapes and cut the repeats.
</tells>

<constraints>
- Do not add deliberate typos or fake slang to "seem human". They read as fake and hurt credibility.
- Do not chase AI-detector scores. Optimize for a reader who knows the author.
- Do not change what the text claims while editing style.
</constraints>
