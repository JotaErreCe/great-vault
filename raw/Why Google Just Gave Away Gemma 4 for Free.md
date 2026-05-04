---
title: "Why Google Just Gave Away Gemma 4 for Free"
source: "https://www.youtube.com/watch?v=sXgZhGzqPmU"
author:
  - "[[Ali H. Salem]]"
published: 2026-05-03
created: 2026-05-04
description: "Why did Google give away Gemma 4 for free? Because the AI market just split in two, and Google is the only company built to win in both halves at once.What you will learn:- Decode the open weight t"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=sXgZhGzqPmU)

Why did Google give away Gemma 4 for free? Because the AI market just split in two, and Google is the only company built to win in both halves at once.  
  
What you will learn:  
\- Decode the open weight tier that is quietly reshaping how enterprises actually deploy AI  
\- Map Google's three stacked plays behind the Gemma 4 release: cloud capture, blocking China, and locking in the next generation of developers  
\- Understand why OpenAI's gpt-oss release was inevitable, and why Anthropic is moving in the opposite direction with Project Glasswing and Claude Mythos  
\- See the Stanford data showing how the gap between closed and open frontier models has opened, closed, and opened again  
\- Learn the right question to ask about your own AI stack, and which workflows belong on which tier  
  
Why this matters:  
The AI market has structurally split into a closed tier and an open tier, and the companies that recognize the split first will have meaningfully better unit economics than the ones still treating AI as a single market. This shift is going to shape procurement decisions, vendor strategy, and competitive positioning across every industry over the next five years.  
  
Become my friend:  
LinkedIn: https://www.linkedin.com/in/ali-h-salem-b500b4116/  
  
About me:  
I am Ali Salem, and I currently work as a director in a tech company. On this channel, I help you turn tech and finance into your personal advantage by breaking down the shifts that actually matter.  
  
#Gemma4 #OpenSourceAI #GoogleAI #AIstrategy #DeepSeek

## Transcript

**0:00** · Google just gave away a model that cost them hundreds of millions of dollars to build. No subscription, no API fee, no revenue share. You can download it, run it on your own hardware, and build a business on top of it without paying Google a single scent. That is not normal corporate behavior. Companies do not hand out their most expensive assets for free. So, either Google has lost its mind or something is happening in the AI market most people have not fully noticed yet. Here's what's actually going on. Google is not running one strategy with this move.

**0:32** · They're running three stacked on top of each other. Each one worth billions. Each one aimed at a different competitor. And one of them is specifically designated to stop China from capturing a piece of the AI market that Western companies have barely started paying attention to.

**0:48** · And in this episode, I'm going to walk you through exactly what those three moves are, why OpenAI and Anthropic are moving in two completely different directions, and why this whole thing points to a split in the AI market that is going to shape how you and I use this technology for the coming years. If we haven't met before, I'm Ali Salam and I currently work as a director in the tech company. And on this channel, I'll help you turn tech and finance into your personal advantage.

**1:15** · Now, let me show you what's actually happening in the AI market because once you see it, Google's move will stop looking strange and start looking like one of the most calculated plays we've seen in the industry. For the first 2 years after Chat GBT launched, there was essentially one way you could use AI in your company. You called an API, you paid per token, your data went to OpenAI, Anthropic or Google, and came back with an answer.

**1:43** · Then you got a bill at the end of the month. That was the model. Simple, right? But as companies have actually started using AI at scale, a second model has emerged alongside of it. And it works completely differently. You download a model, you run it on your own hardware or on cloud infrastructure that you rent directly. You never call an API. You control the entire stack. This is the open weight tier and it's growing really fast.

**2:11** · Now, before I go any further, I want to address something head-on because if you know a little bit about the space, you might be thinking, "Hold on, companies are already running closed models securely. Open AI just signed a Pentagon deal. XAI signed one, too. Large banks are deploying GPT through Azure. So, what's actually different here? Yes, you can run a closed model securely. You can route your data through private cloud configuration where it never gets sent to the provider servers for training.

**2:42** · That is real and it works for a large number of enterprise use cases, but it does not change the fundamental economics. You're still paying per token. You're still dependent on the cloud provider's pricing. You're still operating on the infrastructure the provider controls. You're basically renting access. You're not owning the model. Open weights are different. You physically have the model file. You load it onto your own GPUs.

**3:07** · The marginal cost per token collapses to the cost of electricity and hardware, which at scale can be 10 or 100 times cheaper than API pricing. You fine-tune it however you want. You control when you want to upgrade. You control what it will and will not do. And if the company that released it disappears tomorrow, your deployment would still be running. So the decision is not really about security. It's about economics and control. And here's the key insight.

**3:32** · For any company that uses AI at serious volume, the math eventually tips towards open weights. A startup spending $2,000 a month on API calls will stay on closed models because convenience matters more than cost. But a company spending $2 million a month will start asking whether they should be running their own. And that customer is not rare. In a few years, that customer will be completely normal. Airbnb already did this.

**4:02** · They moved significant AI workloads off OpenAI onto Quen because at their volume it was dramatically cheaper. They're not a bank. They're not a defense contractor. They're just a company that ran the numbers. And more companies are going to run those same numbers over the next 2 three years. So the AI market is splitting into two.

**4:21** · A closed tier where you pay premium prices for the best possible model and you accept the trade-off of renting and an open tier where you take on the complexity of running your own infrastructure in exchange for lower cost more control independence of any single provider different customers different economics and ultimately it's different business models which brings us to the strategic question of all the major AI labs who is competing in both tiers at the same time open AI is almost entirely in the closed tier.

**4:53** · Anthropic the same story. Meta is almost entirely in the open tier. Deepseek, same story.

**5:01** · Each of them is picking a lane. And Google is the only company seriously playing in both lanes. Gemini is for the customer who wants the best models and are willing to pay for API access.

**5:12** · Whereas Gemma is built for the customer who would otherwise go to Llama, Quen or DeepSeek because they need something they can run themselves. So ultimately Google is not cannibalizing Gemini by releasing Gemma. Google is capturing a segment that Gemini could never reach.

**5:28** · That is what makes Google's position in this market unique. Now once you understand the two-tier setup, the real question becomes what exactly is Google getting out of the openweight tier because they're not charging for Gemma directly. So where's the payoff? And in reality there are three of them. Each one answers a different strategic question. How do we make money out of this? How do we stop our competitors from winning? And how do we make our other products stronger because of this?

**5:57** · The first payoff is about how Google actually makes money from Gemma because the model itself is free. So where does the revenue come from? And the answer is cloud. Gemma is free to download. But the moment you want to do something serious with it, like fine-tune it on your own data, serve it to thousands of users, or build an agent on top of it, you need infrastructure.

**6:20** · And Google has positioned Gemma 4 directly inside Google's cloud stack, serving on Google's own TPU chips, deployment on Cloudr Run, integration with agent development kits, sovereign cloud options for regulated industry. The model is free, but the rails it runs on are not. Last quarter, Google Cloud did 17.7 billion in revenue, growing 48% year-over-year with a backlog of $240 billion in committed contracts. That backlog is the business.

**6:53** · Gemma is the funnel. Now, there's a second piece to the commercial story, which is on device. The smallest Gemma 4 models, E2B and E4B, are built to run directly on phones, laptops, and even inside browsers. Now, think about it. Google owns Android. They own Pixel. They own Chrome. And now they have a capable model that runs natively on Google hardware. And Google's software strengthens all of those three platforms against Apple intelligence and Samsung's AI stack.

**7:25** · And that protects multi-billion dollar device ecosystems and the advertising revenue that flows through them. So that is payoff number one, commercial capture. Give the model away for free. capture the value in the cloud and on device. The second payoff is about blocking the competition. And this is where Gemma 4 has a genuine sense of urgency right now. The biggest competitive threat to Google in the openweight tier is not Meta, it's China.

**7:55** · Over the past year, China labs like Alibaba, Deepseek, Moonshot, and Z.AI have released openweight models that in some cases rival GPT5 and Claude. And for any western enterprise that decides to run AI on their own infrastructure, the best option was starting to look like a Chinese one. Now, think about what that actually means.

**8:15** · A major European bank fine-tuning their AI assistant on Quen or a US healthcare company running medical workflows on DeepSync or a government agency building their internal tools on a Chinese model.

**8:33** · That is a geopolitical problem, a commercial problem and a national security problem for Google all at once.

**8:39** · If Chinese openweight models becomes the default for western enterprise deployments, Google loses so much more than developer attention, Google loses the cloud revenue attached to every one of those enterprises because those workloads risk running on infrastructure that is not Google's. And Gemma 4 is like Google planting a flag. It's Google saying you do no longer need to go to a Chinese model to get open weights.

**9:04** · Here's a western alternative built by a US company with enterprise asurances that does not hoover over your corporate data to train future models. And it runs on infrastructure you already know. And that is not an abstract competitive concern. This is Google deliberately shutting a door on Chinese competitors before it opened. And here's the second part of the competitive story. It is the pressure Gemma puts on closed competitors. OpenAI and Anthropic charge premium prices for their frontier APIs.

**9:35** · That pricing only holds up as long as there's no free alternative close enough in quality. When Google releases an openweight model that runs near Frontier, it puts pressure on those premium prices and Google can absorb that hit because Google does not make the majority of its money from API tokens. However, OpenAI and Enthropic do. So, every time Gemma gets better, the pricing round underneath the closed API business gets a little bit softer.

**10:05** · So, that is payoff number two. It's competitive denial. Block China from capturing Western openweight segments and squeeze the margins of closed competitors at the same time. The third payoff is what most people completely miss. It's about how Gemma makes Google's other AI products stronger by simply existing. Start with Gemini.

**10:27** · Gemini is Google's flagship close model, the only one they actually charge for.

**10:32** · And Gemma 4 is built on the same underlying research, the same underlying technology as Gemini 3. Every benchmark that Gemma wins, every positive developer review, every time someone says that Gemma is impressive, it reinforces the perception that the underlying technology under Gemini is worldclass. Gemma is in effect a credibility engine for Gemini. The free model does not just attract developers, it sells the paid one.

**10:59** · And then there is the whole developer ecosystem effect which is the slowest burning but possibly the most valuable one. Gemma 4 is released under Apache 2.0, one of the most permissive licenses in the software industry. It removes the legal friction that was holding back enterprises on earlier versions. And every time a developer builds a fine-tune, publishes a tutorial, integrates Gemma into a tool or ships a product on top of it, something very important is happening.

**11:30** · That is the same developer that is becoming fluent in Google's AI stack.

**11:35** · Not Metas, not Alibabas, not OpenAIs.

**11:39** · And here's why that matters. That same engineer who learned Gemma today is going to be the same engineer who 3 to 5 years from now is going to be sitting in a meeting deciding which cloud provider their company's going to use. They are the same engineer that's going to write the technical recommendation for the next $5 million procurement decision.

**11:58** · Developer fluency today converts into procurement decisions tomorrow. That is how you win a decadel long platform war.

**12:07** · You get the next generation engineers to think in your stack. So that is payoff number three, portfolio reinforcement.

**12:15** · Every Gemma release makes Gemini look stronger. Every developer who builds on Gemma becomes an advocate for Google inside their company. The free model is a credibility engine and a talent pipeline at the same time. Now put those three payoffs together and the picture becomes clear. commercial capture, competitive denial, and portfolio reinforcement, all feeding back into the same underlying business. That is why Google is spending this much money on a model that they're giving away for free.

**12:43** · It is not the generosity or charity.

**12:45** · It's a company that has looked at the AI market, saw it splitting in two, and decided to compete in both halves.

**12:52** · Charge where you can charge, give away where giving away wins you the segment, and make sure that wherever the market is going, Google is going to be there.

**13:01** · Now, here's what should be bothering you by now. If Google is doing such a smart strategy, why is no one else doing it?

**13:10** · OpenAI, Anthropic, some of the most well-funded and most talented companies in the world, and they are only playing in one tier. Why? The obvious answer is that they do not have what Google has.

**13:24** · No cloud, no TPUs, no Android. The model is the business. give it away and there's nothing left to sell. But the interesting signal is not there. It is in what Open AI and Entropic are doing at the edges of the open tier because although it looks like they're both locked out of the frontier, they are making two completely different decisions on how to engage with the openweight world. And those choices might tell you where this whole market is going.

**13:51** · Start with OpenAI because they actually did step into the open tier in August 2025. They released something called GPTO OSS. It was two openweight models, free to download, Apache 2.0 license. And if you've been paying attention, you might have expected that.

**14:11** · What is more interesting is why they did it. Because it was not for one reason.

**14:16** · It was four, all hitting at the same time. The first was Deepseek. In January 2025, a Chinese lab released R1, an openweight reasoning model roughly as capable as OpenAI's 01 at the time, reportedly trained for under $6 million.

**14:34** · That release wiped about $600 billion off of Nvidia's market value in a single day, the biggest one-day loss for any company in US stock market history. Sam Alman went on Reddit within weeks and wrote, "I personally think we have been on the wrong side of history here and need to figure out a different open-source strategy." That is the language of a CEO reacting to a market he did not control. So that is reason number one. The other three landed quietly behind it.

**15:04** · The second was enterprise customers leaving to Llama and Chinese models because OpenAI didn't have any product for self-hosted workloads. Third was that the research community was drifting towards open models because it's difficult to meaningfully study a closed model. And fourth was political. The Trump administration's AI action plan back in July 2025 endorsed openweight models as geostrategically valuable.

**15:31** · Altman called GPTO OSS an open AI stack created in the United States based on democratic values. almost identical language to the administration. But here's the critical detail. GPTO OSS was positioned at 04 mini level, a tier below OpenAI's best at the time. And 2 days after releasing it, they released GPT5 fully closed. The actual frontier stays locked.

**15:59** · And when they followed up two months later with GPT OSS safeguard, that was not a general purpose model at all. It was a narrow safety classifier, basically a compliance tool. So the pattern is consistent. Open AAI will release openweight models when it serves a strategic purpose, but those releases are always subfrontier, narrowly specified, or both. That is the shape of their open tier strategy.

**16:25** · Now, Anthropic is a completely different story entirely. And this is one of the most interesting parts because they're not just holding the closed line for business reasons. They're holding it for philosophical ones. Now whether it is genuine conviction or a strategic posture, I'll leave it up to you to decide. Personally, I think it's both.

**16:51** · Anthropic has never released an openweight model. Not a single one. And the recent behavior shows that they are even further in the other direction.

**17:00** · Just a few weeks ago in April 2026, Anthropic announced a model called Claude Mythos and their own description of what this model can do is striking.

**17:10** · They said it has identified thousands of security vulnerabilities, including some in every major operating system and web browser. Some of those vulnerabilities had been undiscovered for decades.

**17:24** · Anthropic judged the model too dangerous for public release. But here's where that part matters for understanding their strategy. They did not just keep Mythos internal. They launched a program called Project Glasswing which gives Mythos access to a carefully vetted set of around 50 organizations. Microsoft, Google, Apple, Amazon, Nvidia, JP Morgan. Now why those companies?

**17:46** · Because those are the organizations whose systems the rest of the internet depends on. operating systems, cloud infrastructure, financial network, chipmakers. If Mythos can find vulnerabilities and every major operating system, Anthropic wants those vulnerabilities patched by the companies running the infrastructure before an adversary can find them first.

**18:09** · Now, some of you might be thinking, hold on, you said one of the reasons why OpenAI released GPTO OSS was because they were losing the research community. And wouldn't that same pressure apply to Atropic? And it would except that the research community is actually split in two and only one of them was actually ever available to anthropic. The first is the capability research community.

**18:34** · The people who try to make the models more powerful. They need open weights to do their work. That is the community that OpenAI was losing and the one that Anthropic was never going to win because Anthropic does not release openweight models and never has. Whereas the second community is the safety and alignment community, the people that are trying to make the model safer and most of their work happens through API access, red team agreements and published research.

**19:02** · That is the community that Anthropic has been building for years through their fellowship program, their interpretability research and their published constitution. So this is not Anthropic ignoring the research pressure. It's Anthropic playing in the only research community their business model lets them play in. Now whether that is the right play in the long run, only time will tell. So the real picture looks like this. Google competes in both tiers because its business lets it.

**19:30** · Open AAI stays closed with occasionally carefully scoped open releases when external pressure makes it useful.

**19:39** · Anthropic stays closed on principle and goes one step further with restricted modes like Mythos where they control who gets access. And on the other side, Meta open sources aggressively because its money comes from advertising. And the Chinese labs use openweight models to break into the global market. And this split is not temporary. It's structural.

**20:03** · locked in by how each of these company makes money and by the philosophies that they've built their brands around.

**20:09** · Stanford have been tracking it. The capability gap between the best closed and the best open models narrowed dramatically throughout 2024 and 2025.

**20:20** · It then briefly hit par and as of March this year, it has widened back to roughly three points as the closed labs pull ahead again. The lead has changed hands multiple times. That is what a competitive two-tier market actually looks like. Which actually means that you don't really need to pick a winner between these two tiers. Both are going to exist. Both are going to keep getting better. And now, of course, there are many other players. I have not mapped out here. Microsoft, Amazon, Perplexity, XAI, each one is making its own bets.

**20:56** · And walking through them all would require an episode of its own. But what you should walk away with is an understanding of how the AI market has quietly split in two. Why Google is uniquely positioned to compete in both halves while open AAI and Anthropic take very different paths and why this split will shape how you and your company use AI for the coming years.

**21:16** · And once you see that split clearly, the right question stops being which AI is best and starts being which tier your workflow belongs in before you even start assessing the available options.

**21:31** · And I know this video was very different from what I normally release. So let me know if you want me to make more of these because this channel is for you.

**21:40** · So I promise I will listen. In fact, this whole video exists because you asked me to do it in the comments of the Gemma 4 video. And speaking of which, if you want to learn how to actually use Gemma 4, I will point you to this video over here, which will take you through how to set it up and use it for free on your computer and phone. And as always, thank you for trusting me with your time. And until next time, take care.