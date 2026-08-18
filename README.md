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

| Plugin | Repo | Description |
|--------|------|-------------|
| `sessionstats` | [keithmackay/sessionstats](https://github.com/keithmackay/sessionstats) | Auto stats tracker plugin (total aggregated time/cost/tokens per Claude Code project) |

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

MIT
