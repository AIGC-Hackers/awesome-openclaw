# Deployment Options for OpenClaw

OpenClaw can be deployed in multiple ways depending on your needs, from a local Raspberry Pi to cloud VPS providers.

## Self-Hosted Options

### Local Machine (macOS/Linux)

The simplest approach - run OpenClaw directly on your computer:

```bash
openclaw onboard --install-daemon
openclaw gateway start
```

### Docker

For containerized deployments:

```bash
# Using the setup script
curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw/main/docker-setup.sh | bash

# Or manually
docker run -d --name openclaw \
  -v ~/.openclaw:/root/.openclaw \
  -p 18789:18789 \
  openclaw/openclaw:latest
```

### Raspberry Pi

OpenClaw runs well on Raspberry Pi 4/5 for always-on, low-power setups:

- Use 64-bit Raspberry Pi OS
- Minimum 4GB RAM recommended
- Consider SSD for better performance

## Cloud VPS Providers

### One-Click Deploy

| Provider | Link |
|----------|------|
| DigitalOcean | [Tutorial](https://www.digitalocean.com/community/tutorials/how-to-run-openclaw) |
| Vultr | [Docs](https://docs.vultr.com/how-to-deploy-openclaw-autonomous-ai-agent-platform) |
| Hostinger | [Tutorial](https://www.hostinger.com/tutorials/how-to-set-up-openclaw) |
| Alibaba Cloud | [Blog](https://www.alibabacloud.com/blog/openclaw-launches-on-alibaba-cloud-simple-application-server_602845) |

### DIY Cloud Setup

Popular VPS providers for running OpenClaw:

- **Hetzner** - Great value, European servers
- **DigitalOcean** - Easy setup, good documentation
- **Linode** - Reliable, competitive pricing
- **AWS/GCP/Azure** - Enterprise options

Recommended specs:
- 2+ vCPUs
- 4GB+ RAM
- 20GB+ SSD
- Ubuntu 22.04 LTS

### Cloudflare Workers

For edge deployment: [MoltWorker](https://github.com/cloudflare/moltworker)

## Advanced Deployment

### Pulumi + Tailscale

Infrastructure-as-code deployment with private networking:
[Tutorial](https://www.pulumi.com/blog/deploy-openclaw-aws-hetzner/)

### Security Considerations

- Use HTTPS/TLS for gateway endpoints
- Configure firewall rules
- Set up authentication tokens
- Consider running in isolated containers
- Regular backups of `~/.openclaw/`

## Resources

- [Docker Setup Docs](https://docs.openclaw.ai/install/docker)
- [Docker Setup Script](https://github.com/openclaw/openclaw/blob/main/docker-setup.sh)
- [Security Best Practices](https://www.reddit.com/r/LocalLLM/comments/1qri661/whats_the_most_securesafest_way_to_run_openclaw/)
