# Hardware for Running OpenClaw

OpenClaw can run on a variety of hardware, from powerful desktops to low-power single-board computers.

## Recommended Options

### Mac Mini

The Mac Mini is a popular choice due to:
- Compact size
- Powerful performance (especially M-series chips)
- Native macOS support for iMessage, Apple Notes, etc.
- Silent operation
- Low power consumption

**Recommended:** M2 or M4 Mac Mini with 16GB+ RAM

### Raspberry Pi

For always-on, low-power setups:
- **Raspberry Pi 5** - Recommended for best performance
- **Raspberry Pi 4** (4GB+) - Budget option
- Use 64-bit Raspberry Pi OS
- Consider USB SSD for better performance

See: [I use Clawdbot on a Raspberry Pi - Crazy Good!](https://www.youtube.com/watch?v=qePhufA1hSE)

### Linux Desktop/Server

Any x86_64 or ARM64 Linux machine works well:
- Ubuntu 22.04+ LTS recommended
- Debian 12+
- Arch Linux (for advanced users)

### Windows (via WSL2)

Windows users should use WSL2:
- Install WSL2 with Ubuntu
- Run OpenClaw inside WSL
- Full compatibility with Linux instructions

### Cloud VPS

For 24/7 operation without home hardware:
- Hetzner, DigitalOcean, Linode, Vultr
- Minimum specs: 2 vCPU, 4GB RAM, 20GB SSD
- See [Deployment Guide](../docs/deployment.md)

## Creative Setups from the Community

| Setup | Link | Description |
|-------|------|-------------|
| Mac inside a G4 iMac | [Tweet](https://x.com/josesaezmerino/status/201576952339949568) | Modern Mac in vintage case |
| Raspberry Pi + Cloudflare | Reddit | Secure remote access setup |

## Hardware Considerations

### Processing Power

- **API-only usage:** Minimal CPU needed (RPi works great)
- **Local models (Ollama):** Need powerful CPU/GPU
- **Heavy automation:** More CPU helps for parallel tasks

### Memory (RAM)

- **Minimum:** 2GB (API-only, light usage)
- **Recommended:** 4-8GB
- **Local models:** 16GB+ depending on model size

### Storage

- **Minimum:** 10GB
- **Recommended:** 50GB+ SSD
- **With local models:** 100GB+ depending on models

### Network

- Stable internet required for API calls and chat channels
- Consider ethernet over WiFi for reliability
- Static IP or dynamic DNS for remote access

### Always-On Operation

For 24/7 operation, consider:
- UPS for power protection
- Automatic restart on failure
- Monitoring and alerting
- Regular backups

## Power Consumption

| Hardware | Typical Power |
|----------|---------------|
| Raspberry Pi 4/5 | 3-6W |
| Mac Mini (M-series) | 5-20W |
| Intel NUC | 10-40W |
| Cloud VPS | N/A (hosted) |

---

*Last updated: 2026-02-01*
