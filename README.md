# mackayi

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

## Plugins

Grouped by purpose below (a README-level convention only — `marketplace.json` itself has no category field, so this grouping isn't visible in the `/plugin` UI, just here). Version numbers reflect each repo's latest GitHub release and are kept in sync automatically by `/git-release`.

### Project Lifecycle

| Plugin | Version | Repo |
|--------|---------|------|
| [`bootstrap`](#bootstrap) | v1.1.0 | [keithmackay/bootstrap](https://github.com/keithmackay/bootstrap) |
| [`git-release`](#git-release) | v1.0.1 | [keithmackay/git-release](https://github.com/keithmackay/git-release) |
| [`make-readme`](#make-readme) | v1.0.0 | [keithmackay/make-readme](https://github.com/keithmackay/make-readme) |
| [`do-retro`](#do-retro) | v1.1.0 | [keithmackay/do-retro](https://github.com/keithmackay/do-retro) |
| [`port-skill`](#port-skill) | v1.0.0 | [keithmackay/port-skill](https://github.com/keithmackay/port-skill) |

### Quality & Review

| Plugin | Version | Repo |
|--------|---------|------|
| [`improve-this`](#improve-this) | v1.0.0 | [keithmackay/improve-this](https://github.com/keithmackay/improve-this) |
| [`plsfix`](#plsfix) | v1.0.0 | [keithmackay/plsfix](https://github.com/keithmackay/plsfix) |

### Product & Planning

| Plugin | Version | Repo |
|--------|---------|------|
| [`product-discovery-cagan`](#product-discovery-cagan) | v1.0.0 | [keithmackay/cagan-skill](https://github.com/keithmackay/cagan-skill) |
| [`acem-cost-estimation`](#acem-cost-estimation) | v1.0.0 | [keithmackay/estimator](https://github.com/keithmackay/estimator) |

### Knowledge & Docs

| Plugin | Version | Repo |
|--------|---------|------|
| [`wikify`](#wikify) | v1.0.0 | [keithmackay/wikifyskill](https://github.com/keithmackay/wikifyskill) |
| [`pseudocodify`](#pseudocodify) | v1.0.0 | [keithmackay/pseudocodify](https://github.com/keithmackay/pseudocodify) |

### Monitoring & Optimization

| Plugin | Version | Repo |
|--------|---------|------|
| [`sessionstats`](#sessionstats) | v1.0.0 | [keithmackay/sessionstats](https://github.com/keithmackay/sessionstats) |
| [`tokentamer`](#tokentamer) | v1.1.0 | [keithmackay/tokentamer](https://github.com/keithmackay/tokentamer) |

### Utilities

| Plugin | Version | Repo |
|--------|---------|------|
| [`url-eval`](#url-eval) | v1.0.0 | [keithmackay/url-eval](https://github.com/keithmackay/url-eval) |
| [`voxtral-tts`](#voxtral-tts) | v1.0.0 | [keithmackay/voxtral-tts](https://github.com/keithmackay/voxtral-tts) |

## Plugin Details

### sessionstats

Auto-tracks Claude Code sessions: hooks fire on session start/end to record project name, timestamp, session ID, duration, and cost/token metrics parsed from the session transcript against a built-in pricing table. Data is stored per-project in `.sessionstats/session_stats.json` with a regenerated markdown view. Provides `/session_stats` (per-project summary) and `/sessionstats_report` (cross-project totals, filterable by tag), plus per-model breakdown, orphan/crash detection, tagging, and multi-user support. Runs automatically once installed — no manual invocation needed.

### port-skill

Ports a skill/plugin/slash command between four coding-agent platforms (Claude Code, Codex, Antigravity, Gemini CLI) via `/port-skill <path-to-skill-directory> [--dry-run]`. Detects the source platform, generates the required manifest/context files for each target platform, adapts the SKILL.md content, and documents platform-specific feature gaps in a `## Platform Limitations` section and compatibility matrix. Also rewrites the skill's README with per-platform install instructions and validates every generated file before finishing.

### improve-this

An evaluate-only review skill that inspects a project and reports potential improvements without ever modifying files. Infers the project type, proposes tailored evaluation categories (UI/UX, code efficiency, test coverage, security for code; clarity, completeness, redundancy, token efficiency for docs/skills), then produces a priority-ranked, categorized list of findings with Impact/Confidence ratings. Can optionally save the report and generate a phased implementation plan.

### url-eval

Scores candidate domain names/URLs across 8 weighted, research-backed dimensions (memorability, spelling reliability, pronunciation, brand fit, relevance, competitor overlap, TLD appropriateness, etc.) via `/url-eval`. Checks live availability via web search, generates and scores alternative name suggestions, and produces a structured report with top-3 recommendations and a full score table. An `--update` flag refreshes the baked-in scoring research via live web search.

### plsfix

Improves spec documents, prompts, requirements docs, or any instruction set by applying 12 writing principles (Structure, Content, Delivery) synthesized from major AI-lab prompt-engineering guidance. Reads the document, flags principle violations with location, rewrites it with minimal changes (marking assumed details with `[CONFIRM]` tags), and produces a change report mapping each edit to its rationale.

### acem-cost-estimation

*(experimental, ymmv)* Estimates what it would cost (time/dollars) for an AI coding agent to build an existing codebase, or forecasts token + human-review cost for a planned agentic project, using the ACEM model (`Total_Cost = C_LLM + C_HITL + C_Infra`). Inventories the codebase into artifact types, assigns token estimates, applies corrective multipliers, estimates human-in-the-loop review cost, and runs a bundled calculator script (optionally Monte Carlo) to produce a p10/p50/p90 cost range rather than a single point estimate.

### wikify

Builds and maintains an LLM-compiled knowledge wiki following the "Karpathy pattern," where the LLM handles bookkeeping (page creation, cross-references, contradiction detection, confidence tracking) while the human curates source material in a `raw/` directory. Auto-detects context on invocation, routing to Init, Ingest, Query, Lint, or Learning Plan sub-workflows based on directory state. A bundled script can render the wiki into a website; also builds a knowledge graph.

### make-readme

Generates or improves a project's `README.md` by analyzing the codebase (package manifests, directory structure, CI config, entry points) to auto-detect project type, language, and framework. In Create mode, builds a full README from a section template with conditional sections; in Improve mode, maps and scores existing sections (Strong/Adequate/Weak/Missing), presents a gap report, and enhances only what's needed. Also offers to generate companion files (CONTRIBUTING.md, LICENSE, CHANGELOG.md, SECURITY.md, issue/PR templates) — including, for a project that's itself a skill or plugin, a `--help`/`:help` mechanism backed by a `help.md` file.

### product-discovery-cagan

Applies Marty Cagan/SVPG product-management methodology (*INSPIRED*, *EMPOWERED*, *TRANSFORMED*) to product strategy, team structure, discovery, and roadmap work. Provides frameworks including empowered vs. feature teams, the PM/design/tech-lead product trio, vision/strategy/roadmap distinctions, the four discovery risks with opportunity solution trees, and outcome-based OKR writing. Used both diagnostically (classifying a described team/artifact and flagging anti-patterns) and generatively (drafting vision docs, OKRs, discovery plans), including staged/partial adoption guidance for constrained orgs.

### bootstrap

Starts a new software project from scratch: copies template files (including a seeded `CHANGELOG.md`), sets up `README.md`, initializes git, optionally creates a GitHub repo (public/private), then guides an idea-refinement design session and produces a full phased implementation plan written to `docs/plans/`. Safe to re-run on an already-bootstrapped project — detects existing setup and never overwrites or duplicates completed steps.

### git-release

Prepares a project for public release on GitHub: adds an MIT license, verifies `README.md`, `CHANGELOG.md`, and `.gitignore`, checks for a `--help`/`:help` mechanism if the project is itself a skill or plugin, creates a GitHub remote if one doesn't exist, applies branch protection requiring PRs, bumps the `version` field in every plugin manifest to match the release tag, finalizes `CHANGELOG.md` by mechanically renaming its `Unreleased` section to the new version and date (never generating changelog prose itself), and cuts a tagged GitHub release.

### pseudocodify

Wraps the [`pseudocodify`](https://github.com/keithmackay/pseudocodify) CLI to convert a codebase into human-readable, language-agnostic pseudocode. Analyzes the codebase in two phases — building a structured map, then generating per-file pseudocode using that map for cross-file coherence — in CLRS/Cormen, Structured English, or Pascal-like style, with incremental re-runs and a Recursive Language Model fallback for codebases exceeding context limits. Useful as a first step before porting logic to a new language, or for documenting unfamiliar code without reading every file.

### do-retro

Generates or updates a `docs/PROJECT_HISTORY.md` chronicling a project's development history: git commits, design decisions, and every user prompt pulled from Claude Code session transcripts, plus a retroactive-learning section of hindsight lessons. Supports flags to generate subsets into separate files (e.g. `--prompts`). Triggers on "build story," "document how this was built," "do a retro," or "do-retro."

### tokentamer

Audits a project's Claude Code session transcripts to find concrete, evidence-backed opportunities to have used fewer tokens: repeated/duplicated work, context pollution, unused MCP tools, poorly-disclosed skills, bloated prompts, verbose CLAUDE.md/memory files, wrong model choices, missed memory-save opportunities, and places a deterministic script would have beaten an LLM call. Every finding cites a session id, timestamp, and quote or tool-call sequence — a bundled script parses transcript JSONL directly rather than asking the model to eyeball raw logs. Analyzes transcript history, not the codebase itself.

### voxtral-tts

Converts text to speech using Mistral's Voxtral model ($0.016/1,000 chars, ~70ms latency) and delivers it as a voice note over Discord or Telegram, or hands back a local file path. Triggers on an explicit `--voice` flag or phrases like "read that to me." Supports 8 voices, `--strip-md` to clean agent output before speaking it, and `--truncate` for overly long input. Requires a `MISTRAL_API_KEY`.

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
