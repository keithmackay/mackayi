#!/usr/bin/env python3
"""
Interactively review Keith's authored Claude Code skills/plugins across ~/Projects
and manage inclusion in the mackayi marketplace.

For each item:
  - Prints name, public/private repo status, and description.
  - If public and not already in the marketplace: asks whether to add it.
  - If already in the marketplace: says so, and asks whether to keep it
    (yes = do nothing, no = remove it).

Edits ~/Projects/mackayi/.claude-plugin/marketplace.json in place.
"""

import json
import subprocess
from pathlib import Path

MARKETPLACE_PATH = Path.home() / "Projects" / "mackayi" / ".claude-plugin" / "marketplace.json"

# Inventory of Keith's own authored skills/plugins, gathered from a survey of ~/Projects.
# (Excludes vendored/installed skills from other authors, and the mackayi marketplace repo itself.)
ITEMS = [
    {
        "name": "sessionstats",
        "repo": "keithmackay/sessionstats",
        "public": False,
        "description": "Auto stats tracker plugin (total aggregated time/cost/tokens per Claude Code project)",
    },
    {
        "name": "skillporter",
        "repo": "keithmackay/skillporter",
        "public": True,
        "description": "Ports a skill/plugin/slash command between Claude Code, Codex, Antigravity, Gemini CLI",
    },
    {
        "name": "improve-this",
        "repo": "keithmackay/improve-this",
        "public": False,
        "description": "Evaluate a project for potential improvements. Strictly evaluate-and-report — never modifies files",
    },
    {
        "name": "obstagger",
        "repo": "keithmackay/obstagger",
        "public": False,
        "description": "Fills in YAML frontmatter tags for Obsidian notes per the KeithVault taxonomy",
    },
    {
        "name": "urleval",
        "repo": "keithmackay/urleval",
        "public": False,
        "description": "Scores candidate domain names/URLs across 8 dimensions, checks availability, produces a report",
    },
    {
        "name": "plsfix",
        "repo": "keithmackay/plsfix",
        "public": True,
        "description": "Rewrites vague specs/prompts/instructions into clear, actionable ones",
    },
    {
        "name": "acem-cost-estimation",
        "repo": "keithmackay/estimator",
        "public": True,
        "description": "ACEM methodology to estimate AI-agent build cost (time/$) for an existing or planned codebase",
    },
    {
        "name": "wikify",
        "repo": "keithmackay/wikifyskill",
        "public": True,
        "description": "Builds/maintains an LLM-compiled knowledge wiki (Karpathy pattern)",
    },
    {
        "name": "readme",
        "repo": "keithmackay/ReadMeSkill",
        "public": False,
        "description": "Generates or improves a project's README.md",
    },
    {
        "name": "product-discovery-cagan",
        "repo": "keithmackay/cagan-skill",
        "public": True,
        "description": "Applies Marty Cagan/SVPG product methodology (INSPIRED/EMPOWERED/TRANSFORMED)",
    },
    {
        "name": "deckreview",
        "repo": "keithmackay/deckreview",
        "public": False,
        "description": "Reviews PPTX investment decks for PE investors / IC clarity",
    },
    {
        "name": "publish-pipeline",
        "repo": "keithmackay/publishall",
        "public": False,
        "description": "Orchestrates publishing Obsidian markdown to LinkedIn, Bluesky, X, Substack",
    },
    {
        "name": "voxtral-tts",
        "repo": "keithmackay/mistralskill",
        "public": False,
        "description": "Text-to-speech via Mistral Voxtral, for voice-note responses",
    },
    {
        "name": "writeli",
        "repo": "keithmackay/llm-toolkit",
        "public": False,
        "description": "Generates LinkedIn articles for C-suite/business audiences",
    },
    {
        "name": "keithvault",
        "repo": "keithmackay/llm-toolkit",
        "public": False,
        "description": "Generates KeithVault Obsidian notes (person/company/meeting/idea) from templates",
    },
]


def load_marketplace():
    data = json.loads(MARKETPLACE_PATH.read_text())
    data.setdefault("plugins", [])
    return data


def save_marketplace(data):
    MARKETPLACE_PATH.write_text(json.dumps(data, indent=2) + "\n")


def find_entry(data, repo):
    for entry in data["plugins"]:
        source = entry.get("source")
        if isinstance(source, dict) and source.get("repo") == repo:
            return entry
    return None


def make_repo_public(repo):
    """Flip a GitHub repo's visibility to public via gh CLI. Returns True on success."""
    result = subprocess.run(
        ["gh", "repo", "edit", repo, "--visibility", "public", "--accept-visibility-change-consequences"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"  Failed to make {repo} public: {result.stderr.strip()}")
        return False
    print(f"  {repo} is now public.")
    return True


def ask_yes_no(prompt):
    while True:
        answer = input(f"{prompt} [y/n]: ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer y or n.")


def process_item(item):
    data = load_marketplace()

    visibility = "public" if item["public"] else "private"
    print("\n" + "-" * 60)
    print(f"Skill: {item['name']}  [{visibility}]  ({item['repo']})")
    print(f"  {item['description']}")

    existing = find_entry(data, item["repo"])

    if existing:
        print(f"  -> Already included in the mackayi marketplace as '{existing['name']}'.")
        keep = ask_yes_no("  Keep it in the marketplace?")
        if keep:
            print("  Keeping as-is.")
        else:
            data["plugins"].remove(existing)
            save_marketplace(data)
            print(f"  Removed '{existing['name']}' from the marketplace.")
        return

    if not item["public"]:
        make_public = ask_yes_no("  -> Private repo, not eligible for the public marketplace. Make it public?")
        if make_public:
            if make_repo_public(item["repo"]):
                item["public"] = True
                process_item(item)  # restart the decision loop for this item
            return
        print("  Skipped.")
        return

    add = ask_yes_no("  Not in the marketplace yet. Add it?")
    if add:
        data["plugins"].append(
            {
                "name": item["name"],
                "source": {"source": "github", "repo": item["repo"]},
                "description": item["description"],
            }
        )
        save_marketplace(data)
        print(f"  Added '{item['name']}' to the marketplace.")
    else:
        print("  Skipped.")


def main():
    for item in ITEMS:
        process_item(item)

    print("\n" + "-" * 60)
    print("Done. Current marketplace.json:")
    print(json.dumps(load_marketplace(), indent=2))


if __name__ == "__main__":
    main()
