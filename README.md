# mackayi Marketplace - Skills & Plugins

Keith MacKay's Claude Code plugin marketplace. This repo hosts only the marketplace catalog (`.claude-plugin/marketplace.json`) — each listed plugin lives in its own repository and keeps its own version history, README, and release cadence.

## Installation

`/plugin marketplace add` and `/plugin install` are slash commands — run them inside an active Claude Code session, not in your shell.

```
/plugin marketplace add keithmackay/mackayi
/plugin install <plugin-name>@mackayi
```

If the install summary says `Run /reload-plugins to activate.`, run that command too.

For non-interactive installs, the marketplace must already be known — either added once via `/plugin marketplace add` in a prior session, or declared in `.claude/settings.json` under [`extraKnownMarketplaces`](https://code.claude.com/docs/en/settings#extraknownmarketplaces) — then install with the shell CLI:

```bash
claude plugin install <plugin-name>@mackayi --scope user
```

## Plugins and Skills

The mackayi marketplace includes a variety of plugins and skills, spanning the following categories:
- Project Lifecycle (tools to help create, release, and document skills/plugins/apps)
- Improve & Refine (tools to radically improve your projects and comms clarity)
- Product & Planning (product design and estimation skills)
- Knowledge and Docs 
Grouped by purpose below (a README-level convention only — `marketplace.json` itself has no category field, so this grouping isn't visible in the `/plugin` UI, just here). Version numbers reflect each repo's latest GitHub release and are kept in sync automatically by `/git-release`.

### Project Lifecycle

| Plugin                        | Version | Repo                                                                  |
| ----------------------------- | ------- | --------------------------------------------------------------------- |
| [`bootstrap`](#bootstrap)     | v1.1.0  | [keithmackay/bootstrap](https://github.com/keithmackay/bootstrap)     |
| [`port-skill`](#port-skill)   | v1.0.0  | [keithmackay/port-skill](https://github.com/keithmackay/port-skill)   |
| [`make-readme`](#make-readme) | v1.0.0  | [keithmackay/make-readme](https://github.com/keithmackay/make-readme) |
| [`git-release`](#git-release) | v1.0.1  | [keithmackay/git-release](https://github.com/keithmackay/git-release) |

### Improve & Refine

| Plugin                          | Version | Repo                                                                    |
| ------------------------------- | ------- | ----------------------------------------------------------------------- |
| [`improve-this`](#improve-this) | v1.0.0  | [keithmackay/improve-this](https://github.com/keithmackay/improve-this) |
| [`plsfix`](#plsfix)             | v1.0.0  | [keithmackay/plsfix](https://github.com/keithmackay/plsfix)             |

### Product & Planning

| Plugin                                                | Version | Repo                                                                  |
| ----------------------------------------------------- | ------- | --------------------------------------------------------------------- |
| [`marty-caganize`](#marty-caganize)                   | v1.0.0  | [keithmackay/marty-caganize](https://github.com/keithmackay/marty-caganize) |
| [`estimate-acem-cost`](#estimate-acem-cost)           | v1.0.0  | [keithmackay/estimate-acem-cost](https://github.com/keithmackay/estimate-acem-cost) |

### Knowledge & Docs

| Plugin                          | Version | Repo                                                                    |
| ------------------------------- | ------- | ----------------------------------------------------------------------- |
| [`wikify`](#wikify)             | v1.0.0  | [keithmackay/wikifyskill](https://github.com/keithmackay/wikifyskill)   |
| [`pseudocodify`](#pseudocodify) | v1.0.0  | [keithmackay/pseudocodify](https://github.com/keithmackay/pseudocodify) |
| [`obstagger`](#obstagger)       | v1.2.0  | [keithmackay/obstagger](https://github.com/keithmackay/obstagger)       |

### Monitoring & Optimization

| Plugin                          | Version | Repo                                                                    |
| ------------------------------- | ------- | ----------------------------------------------------------------------- |
| [`sessionstats`](#sessionstats) | v1.0.0  | [keithmackay/sessionstats](https://github.com/keithmackay/sessionstats) |
| [`tokentamer`](#tokentamer)     | v1.1.0  | [keithmackay/tokentamer](https://github.com/keithmackay/tokentamer)     |
| [`do-retro`](#do-retro)         | v1.1.0  | [keithmackay/do-retro](https://github.com/keithmackay/do-retro)         |

### Marketing

| Plugin                  | Version | Repo                                                            |
| ----------------------- | ------- | --------------------------------------------------------------- |
| [`url-eval`](#url-eval) | v1.0.0  | [keithmackay/url-eval](https://github.com/keithmackay/url-eval) |

### Utilities

| Plugin                        | Version | Repo                                                                  |
| ----------------------------- | ------- | --------------------------------------------------------------------- |
| [`voxtral-tts`](#voxtral-tts) | v1.0.0  | [keithmackay/voxtral-tts](https://github.com/keithmackay/voxtral-tts) |

## Plugin Details

### sessionstats

Auto-tracks Claude Code sessions: hooks fire on session start/end to record project name, timestamp, session ID, duration, and cost/token metrics parsed from the session transcript against a built-in pricing table. Data is stored per-project in `.sessionstats/session_stats.json` with a regenerated markdown view. Provides `/session_stats` (per-project summary) and `/sessionstats_report` (cross-project totals, filterable by tag), plus per-model breakdown, orphan/crash detection, tagging, and multi-user support. Runs automatically once installed — no manual invocation needed.

[Help](https://github.com/keithmackay/sessionstats/blob/main/help.md) · [Changelog](https://github.com/keithmackay/sessionstats/blob/main/CHANGELOG.md)

### port-skill

Ports a skill/plugin/slash command between four coding-agent platforms (Claude Code, Codex, Antigravity, Gemini CLI) via `/port-skill <path-to-skill-directory> [--dry-run]`. Detects the source platform, generates the required manifest/context files for each target platform, adapts the SKILL.md content, and documents platform-specific feature gaps in a `## Platform Limitations` section and compatibility matrix. Also rewrites the skill's README with per-platform install instructions and validates every generated file before finishing.

[Help](https://github.com/keithmackay/port-skill/blob/main/help.md) · [Changelog](https://github.com/keithmackay/port-skill/blob/main/CHANGELOG.md)

### improve-this

An evaluate-only review skill that inspects a project and reports potential improvements without ever modifying files. Infers the project type, proposes tailored evaluation categories (UI/UX, code efficiency, test coverage, security for code; clarity, completeness, redundancy, token efficiency for docs/skills), then produces a priority-ranked, categorized list of findings with Impact/Confidence ratings. Can optionally save the report and generate a phased implementation plan.

[Help](https://github.com/keithmackay/improve-this/blob/main/help.md) · [Changelog](https://github.com/keithmackay/improve-this/blob/main/CHANGELOG.md)

### url-eval

Scores candidate domain names/URLs across 8 weighted, research-backed dimensions (memorability, spelling reliability, pronunciation, brand fit, relevance, competitor overlap, TLD appropriateness, etc.) via `/url-eval`. Checks live availability via web search, generates and scores alternative name suggestions, and produces a structured report with top-3 recommendations and a full score table. An `--update` flag refreshes the baked-in scoring research via live web search.

[Help](https://github.com/keithmackay/url-eval/blob/main/help.md) · [Changelog](https://github.com/keithmackay/url-eval/blob/main/CHANGELOG.md)

### plsfix

Improves spec documents, prompts, requirements docs, or any instruction set by applying 12 writing principles (Structure, Content, Delivery) synthesized from major AI-lab prompt-engineering guidance. Reads the document, flags principle violations with location, rewrites it with minimal changes (marking assumed details with `[CONFIRM]` tags), and produces a change report mapping each edit to its rationale.

[Help](https://github.com/keithmackay/plsfix/blob/main/help.md) · [Changelog](https://github.com/keithmackay/plsfix/blob/main/CHANGELOG.md)

### estimate-acem-cost

*(experimental, ymmv)* Estimates what it would cost (time/dollars) for an AI coding agent to build an existing codebase, or forecasts token + human-review cost for a planned agentic project, using the ACEM model (`Total_Cost = C_LLM + C_HITL + C_Infra`). Inventories the codebase into artifact types, assigns token estimates, applies corrective multipliers, estimates human-in-the-loop review cost, and runs a bundled calculator script (optionally Monte Carlo) to produce a p10/p50/p90 cost range rather than a single point estimate.

[Help](https://github.com/keithmackay/estimate-acem-cost/blob/main/skill/estimate-acem-cost/help.md) · [Changelog](https://github.com/keithmackay/estimate-acem-cost/blob/main/CHANGELOG.md)

### wikify

Builds and maintains an LLM-compiled knowledge wiki following the "Karpathy pattern," where the LLM handles bookkeeping (page creation, cross-references, contradiction detection, confidence tracking) while the human curates source material in a `raw/` directory. Auto-detects context on invocation, routing to Init, Ingest, Query, Lint, or Learning Plan sub-workflows based on directory state. A bundled script can render the wiki into a website; also builds a knowledge graph.

[Help](https://github.com/keithmackay/wikifyskill/blob/main/src/skill/help.md) · [Changelog](https://github.com/keithmackay/wikifyskill/blob/main/CHANGELOG.md)

### make-readme

Generates or improves a project's `README.md` by analyzing the codebase (package manifests, directory structure, CI config, entry points) to auto-detect project type, language, and framework. In Create mode, builds a full README from a section template with conditional sections; in Improve mode, maps and scores existing sections (Strong/Adequate/Weak/Missing), presents a gap report, and enhances only what's needed. Also offers to generate companion files (CONTRIBUTING.md, LICENSE, CHANGELOG.md, SECURITY.md, issue/PR templates) — including, for a project that's itself a skill or plugin, a `--help`/`:help` mechanism backed by a `help.md` file.

[Help](https://github.com/keithmackay/make-readme/blob/main/skill/help.md) · [Changelog](https://github.com/keithmackay/make-readme/blob/main/CHANGELOG.md)

### marty-caganize

Applies Marty Cagan/SVPG product-management methodology (*INSPIRED*, *EMPOWERED*, *TRANSFORMED*) to product strategy, team structure, discovery, and roadmap work. Provides frameworks including empowered vs. feature teams, the PM/design/tech-lead product trio, vision/strategy/roadmap distinctions, the four discovery risks with opportunity solution trees, and outcome-based OKR writing. Used both diagnostically (classifying a described team/artifact and flagging anti-patterns) and generatively (drafting vision docs, OKRs, discovery plans), including staged/partial adoption guidance for constrained orgs.

[Help](https://github.com/keithmackay/marty-caganize/blob/main/help.md) · [Changelog](https://github.com/keithmackay/marty-caganize/blob/main/CHANGELOG.md)

### bootstrap

Starts a new software project from scratch: copies template files (including a seeded `CHANGELOG.md`), sets up `README.md`, initializes git, optionally creates a GitHub repo (public/private), then guides an idea-refinement design session and produces a full phased implementation plan written to `docs/plans/`. Safe to re-run on an already-bootstrapped project — detects existing setup and never overwrites or duplicates completed steps.

[Help](https://github.com/keithmackay/bootstrap/blob/main/help.md) · [Changelog](https://github.com/keithmackay/bootstrap/blob/main/CHANGELOG.md)

### git-release

Prepares a project for public release on GitHub: adds an MIT license, verifies `README.md`, `CHANGELOG.md`, and `.gitignore`, checks for a `--help`/`:help` mechanism if the project is itself a skill or plugin (adds a `--version`/`:version` command directly if missing, which reports the installed version plus a best-effort check for a newer GitHub release), creates a GitHub remote if one doesn't exist, applies branch protection requiring PRs, bumps the `version` field in every plugin manifest to match the release tag, finalizes `CHANGELOG.md` by mechanically renaming its `Unreleased` section to the new version and date (refusing to proceed silently — and asking for confirmation instead — if `Unreleased` is empty; never generating changelog prose itself), offers to sync the version into any local marketplace listing, and cuts a tagged GitHub release.

[Help](https://github.com/keithmackay/git-release/blob/main/help.md) · [Changelog](https://github.com/keithmackay/git-release/blob/main/CHANGELOG.md)

### pseudocodify

Wraps the [`pseudocodify`](https://github.com/keithmackay/pseudocodify) CLI to convert a codebase into human-readable, language-agnostic pseudocode. Analyzes the codebase in two phases — building a structured map, then generating per-file pseudocode using that map for cross-file coherence — in CLRS/Cormen, Structured English, or Pascal-like style, with incremental re-runs and a Recursive Language Model fallback for codebases exceeding context limits. Useful as a first step before porting logic to a new language, or for documenting unfamiliar code without reading every file.

[Help](https://github.com/keithmackay/pseudocodify/blob/main/skill/pseudocodify/help.md) · [Changelog](https://github.com/keithmackay/pseudocodify/blob/main/CHANGELOG.md)

### do-retro

Generates or updates a `docs/PROJECT_HISTORY.md` chronicling a project's development history: git commits, design decisions, and every user prompt pulled from Claude Code session transcripts, plus a retroactive-learning section of hindsight lessons. Supports flags to generate subsets into separate files (e.g. `--prompts`). Triggers on "build story," "document how this was built," "do a retro," or "do-retro."

[Help](https://github.com/keithmackay/do-retro/blob/main/help.md) · [Changelog](https://github.com/keithmackay/do-retro/blob/main/CHANGELOG.md)

### tokentamer

Audits a project's Claude Code session transcripts to find concrete, evidence-backed opportunities to have used fewer tokens: repeated/duplicated work, context pollution, unused MCP tools, poorly-disclosed skills, bloated prompts, verbose CLAUDE.md/memory files, wrong model choices, missed memory-save opportunities, and places a deterministic script would have beaten an LLM call. Every finding cites a session id, timestamp, and quote or tool-call sequence — a bundled script parses transcript JSONL directly rather than asking the model to eyeball raw logs. Analyzes transcript history, not the codebase itself.

[Help](https://github.com/keithmackay/tokentamer/blob/main/help.md) · [Changelog](https://github.com/keithmackay/tokentamer/blob/main/CHANGELOG.md)

### voxtral-tts

Converts text to speech using Mistral's Voxtral model ($0.016/1,000 chars, ~70ms latency) and delivers it as a voice note over Discord or Telegram, or hands back a local file path. Triggers on an explicit `--voice` flag or phrases like "read that to me." Supports 8 voices, `--strip-md` to clean agent output before speaking it, and `--truncate` for overly long input. Requires a `MISTRAL_API_KEY`.

[Help](https://github.com/keithmackay/voxtral-tts/blob/main/help.md) · [Changelog](https://github.com/keithmackay/voxtral-tts/blob/main/CHANGELOG.md)

### obstagger

Fills in YAML frontmatter (`context`, `type`, `subtype`, `subsubtype`, `tags`) on Obsidian notes — a single file or an entire folder tree recursively — guided by a living per-vault taxonomy schema file. Proposes and writes new taxonomy entries and tags to the schema automatically when content doesn't fit existing ones, and `--updatetags` can build a schema from scratch by analyzing a vault's existing notes. Never silently overwrites populated frontmatter fields unless `--yolo` is passed. Works with any vault, remembering the last one used as the default for next time.

[Help](https://github.com/keithmackay/obstagger/blob/main/skill/help.md) · [Changelog](https://github.com/keithmackay/obstagger/blob/main/CHANGELOG.md)

## Adding a plugin

Each entry in `.claude-plugin/marketplace.json`'s `plugins` array needs a `name` and a `source`. For a plugin in its own repo:

```json
{
  "name": "plugin-name",
  "source": { "source": "github", "repo": "keithmackay/plugin-repo" },
  "description": "..."
}
```

The referenced repo needs its own `.claude-plugin/plugin.json` at its root (or wherever its `source` points), following the [plugin manifest schema](https://code.claude.com/docs/en/plugins-reference#plugin-manifest-schema).

## License

[MIT](LICENSE) © Keith MacKay
