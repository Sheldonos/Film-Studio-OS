# Lifecycle Expansion Sources — v0.4.0

**Checked:** 2026-08-15  
**Purpose:** Record the external basis for Bob onboarding and department boundaries. Repository source and supplied production-role materials remain the primary implementation inputs; these sources constrain claims rather than granting authority.

| Source | Evidence used | Implementation consequence |
|---|---|---|
| [IBM Bob — Skills](https://bob.ibm.com/docs/ide/features/skills) | Project skills live under `.bob/skills/<skill>/SKILL.md`; descriptions drive activation; supporting files are available; the Skills Settings tab shows discovery; skills currently require Advanced mode. | `AGENTS.md` tells operators to select a skill-capable/Advanced mode, verify discovery, and keep skills project-local rather than “pip installing” them. |
| [IBM Bob — Modes](https://bob.ibm.com/docs/ide/features/modes) | Modes define task behavior/tool access; Plan, Agent and Ask have different intended scopes. | Setup distinguishes planning from implementation and retains least-privilege custom modes. |
| [IBM Bob demo repository](https://github.com/IBM/bob-demo) | IBM's examples emphasize choosing the appropriate mode, clear prompts, iteration and documentation. | Bootstrap and diagnostic are explicit, reviewable steps rather than hidden assumptions. |
| [ScreenSkills — Film and TV drama roles](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/) | Casting, locations, costume, hair/makeup, art, production, camera, sound and post are separate collaborative departments with distinct responsibilities. | New skills prepare department-specific artifacts and handoffs; one generic “film expert” is not treated as credible coverage. |

## Research limits

- Current local law, union/guild agreements, permits, festival/platform rules and vendor schemas must be verified at the time of a real decision.
- Role descriptions inform scope; they do not license Bob to practice law, approve safety, hire, negotiate, perform medical work or replace a department head.
- External pages can change. The package records the checked date and intentionally keeps operational authority in versioned project evidence and qualified humans.
