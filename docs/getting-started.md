# Getting Started with OpenClaw

This guide provides a summary of the official OpenClaw documentation to get you up and running quickly.

## Prerequisites

Before you begin, ensure you have:

- **Node.js**: Version 22 or higher
- **pnpm**: Recommended for building from source
- **Brave Search API Key**: Recommended for web search (configure with `openclaw configure --section web`)

For Windows users, **WSL2** (Windows Subsystem for Linux 2) with Ubuntu is strongly recommended.

## Installation

### Quick Install (Recommended)

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

### Alternative: npm/pnpm

```bash
npm install -g openclaw@latest
# or
pnpm add -g openclaw@latest
```

### Docker

```bash
docker pull openclaw/openclaw:latest
```

See the [Docker documentation](https://docs.openclaw.ai/install/docker) for full setup instructions.

## Onboarding Wizard

The easiest way to configure OpenClaw:

```bash
openclaw onboard --install-daemon
```

This wizard guides you through:

- Setting up the gateway (local or remote)
- Configuring authentication with your model provider (Anthropic, OpenAI, OpenRouter, etc.)
- Connecting to chat channels (WhatsApp, Telegram, Discord, etc.)
- Installing the background daemon

## Starting the Gateway

Check status:
```bash
openclaw gateway status
```

Manual foreground run:
```bash
openclaw gateway --port 18789 --verbose
```

## Verification

```bash
openclaw status
openclaw health
```

## Next Steps

- [Official Documentation](https://docs.openclaw.ai/start/getting-started)
- [Discord Community](https://discord.com/invite/clawd)
- [ClawHub Skills](https://clawhub.com/)
