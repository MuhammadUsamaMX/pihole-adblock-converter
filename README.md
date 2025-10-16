# Pi-hole Ad Blocking List Converter

[![GitHub Actions](https://github.com/MuhammadUsamaMX/pihole-adblock-converter/workflows/Update%20Pi-hole%20Blocklist/badge.svg)](https://github.com/MuhammadUsamaMX/pihole-adblock-converter/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An automated system that converts various ad-blocking lists into a unified Pi-hole format and keeps them updated via GitHub Actions.

## 🚀 Features

- **Automated Updates**: Runs daily via GitHub Actions to fetch the latest lists
- **Multiple Format Support**: Converts AdBlock Plus, hosts files, and plain domain lists
- **22+ Reputable Sources**: Aggregates from trusted ad-blocking communities
- **Pi-hole Compatible**: Outputs in standard Pi-hole hosts format
- **Deduplication**: Removes duplicate domains across all sources
- **Auto-releases**: Creates GitHub releases when lists are updated

## 📊 Current Stats

- **Total Domains**: ~80,000+ unique domains
- **Sources**: 22+ reputable ad-blocking lists
- **Update Frequency**: Daily at 2 AM UTC
- **Last Updated**: [Auto-updated via GitHub Actions]

## 🎯 Quick Start

### For Pi-hole Users

Add this URL to your Pi-hole configuration:

```
https://raw.githubusercontent.com/MuhammadUsamaMX/pihole-adblock-converter/main/pihole_list.txt
```

1. Go to your Pi-hole Admin Panel
2. Navigate to **Settings** → **Blocklists**
3. Add the URL above
4. Click **Save and Update**

### For AdGuard Users

The generated list is also compatible with AdGuard Home:

```
https://raw.githubusercontent.com/MuhammadUsamaMX/pihole-adblock-converter/main/pihole_list.txt
```

## 📋 Included Sources

This repository automatically aggregates from the following reputable sources:

| Source | Type | Description |
|--------|------|-------------|
| AdGuard DNS filter | AdBlock | AdGuard's comprehensive DNS filter |
| AdAway Default | Hosts | Popular Android ad-blocker list |
| Dan Pollock's List | Hosts | Well-known hosts file |
| OISD Blocklist | AdBlock | The "OISD" (OISD.nl) blocklist |
| Peter Lowe's List | AdBlock | Peter Lowe's ad server list |
| NoCoin Filter | Hosts/AdBlock | Cryptocurrency mining blocker |
| WindowsSpyBlocker | Hosts | Windows telemetry blocking |
| Smart-TV Blocklist | AdBlock | Smart TV ad blocking |
| Game Console List | AdBlock | Gaming console ad blocking |
| Anti-Malware Lists | AdBlock | Malware and phishing protection |
| And 12+ more... | Various | Additional specialized lists |

## 🔧 Local Development

### Prerequisites

- Python 3.9+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/MuhammadUsamaMX/pihole-adblock-converter.git
cd pihole-adblock-converter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the converter:
```bash
python convert_lists.py
```

### Configuration

Edit `config.json` to add or modify source lists:

```json
{
  "lists": [
    {
      "name": "Your Custom List",
      "url": "https://example.com/your-list.txt",
      "format": "adblock"
    }
  ]
}
```

**Supported formats:**
- `hosts`: Standard hosts file format (127.0.0.1 domain)
- `adblock`: AdBlock Plus format
- `auto`: Auto-detect format

## 🤖 Automation

### GitHub Actions

The repository uses GitHub Actions for automated updates:

- **Schedule**: Daily at 2 AM UTC
- **Manual Trigger**: Available via GitHub Actions tab
- **Auto-commit**: Changes are automatically committed
- **Auto-release**: Creates releases when lists are updated

### Workflow Features

- ✅ Fetches latest lists from all sources
- ✅ Converts to Pi-hole format
- ✅ Deduplicates domains
- ✅ Commits changes automatically
- ✅ Creates GitHub releases
- ✅ Updates documentation

## 📁 Repository Structure

```
├── .github/
│   └── workflows/
│       └── update-lists.yml    # GitHub Actions workflow
├── convert_lists.py            # Main conversion script
├── config.json                 # Source list configuration
├── requirements.txt            # Python dependencies
├── pihole_list.txt            # Generated Pi-hole list (auto-generated)
├── summary.json               # Processing summary (auto-generated)
└── README.md                  # This file
```

## 🔍 Output Format

The generated `pihole_list.txt` follows the standard Pi-hole hosts format:

```
# Title: Auto-Generated Pi-hole Blocklist
# Date: 13 October 2025 12:52:53 (UTC)
# Number of unique domains: 79,414
#
# ===============================================================

127.0.0.1 localhost
127.0.0.1 localhost.localdomain
# ... standard localhost entries ...

# Start Auto-Generated Blocklist
0.0.0.0 ad.example.com
0.0.0.0 tracking.example.com
# ... blocked domains ...
```

## 🛠️ Customization

### Adding New Sources

1. Edit `config.json`
2. Add your source with proper format specification
3. The system will automatically include it in the next update

### Modifying Update Schedule

Edit `.github/workflows/update-lists.yml`:

```yaml
schedule:
  - cron: '0 2 * * *'  # Change this cron expression
```

### Custom Output Format

Modify the `convert_to_pihole_format()` method in `convert_lists.py` to customize the output format.

## 📈 Monitoring

### GitHub Actions

Monitor the automation status:
- Go to the **Actions** tab in your repository
- Check the **Update Pi-hole Blocklist** workflow
- View logs for any issues

### Release History

All updates are tracked via GitHub releases:
- Automatic releases when lists change
- Version tags with timestamps
- Detailed changelogs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally with `python convert_lists.py`
5. Submit a pull request

### Adding New Sources

To add a new ad-blocking source:

1. Add it to `config.json`
2. Test the format detection
3. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Thanks to all the maintainers of the source lists:

- [AdGuard](https://adguard.com/) - AdGuard DNS filter
- [AdAway](https://adaway.org/) - AdAway hosts file
- [Dan Pollock](https://someonewhocares.org/) - Dan's hosts file
- [OISD](https://oisd.nl/) - OISD blocklist
- [Peter Lowe](https://pgl.yoyo.org/) - Peter Lowe's list
- [Dandelion Sprout](https://github.com/DandelionSprout) - Various specialized lists
- And many more contributors to the ad-blocking community!

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/MuhammadUsamaMX/pihole-adblock-converter/issues)
- **Discussions**: [GitHub Discussions](https://github.com/MuhammadUsamaMX/pihole-adblock-converter/discussions)
- **Releases**: [GitHub Releases](https://github.com/MuhammadUsamaMX/pihole-adblock-converter/releases)

---

**Note**: This repository is configured for Muhammad Usama (MuhammadUsamaMX) with automated Pi-hole ad-blocking list generation.
