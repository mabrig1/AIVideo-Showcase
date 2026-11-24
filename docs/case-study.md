# Engineering case study: AIVideo

## Problem
AI filmmaking requires consistent scene planning, duration management, media generation, cost control and review.

## Design approach
Separate the storyboard from rendering and treat provider output as unverified until a playable artifact is available. Require explicit authorization before chargeable work and preserve a clear record of unknown provider balances.

## Portfolio evidence
The independent sample in this repository validates scene durations and produces a timeline. It does not call an AI provider or generate video. The related product is https://aivideo.mabrigkorie.org; live generation capabilities, availability and benchmarks are not independently established by this showcase.

## Interview discussion
Asynchronous job design, media metadata, failure recovery, provider abstraction, spending safeguards and testable state transitions.
