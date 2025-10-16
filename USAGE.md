# Usage Guide

This guide explains how to use the Pi-hole Ad Blocking List Converter for different scenarios.

## 🚀 Quick Setup

### 1. Fork and Clone

1. Fork this repository to your GitHub account
2. Clone your fork:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2. Update Repository URLs

Replace `YOUR_USERNAME` and `YOUR_REPO` in these files:
- `README.md`
- `.github/workflows/update-lists.yml`
- `convert_lists.py` (in the header comments)

### 3. Enable GitHub Actions

1. Go to your repository's **Settings**
2. Navigate to **Actions** → **General**
3. Ensure "Allow all actions and reusable workflows" is selected
4. Save the settings

## 🔧 Configuration

### Adding Custom Sources

Edit `config.json` to add your own ad-blocking sources:

```json
{
  "lists": [
    {
      "name": "My Custom List",
      "url": "https://example.com/my-list.txt",
      "format": "adblock"
    }
  ]
}
```

### Supported Formats

- **`hosts`**: Standard hosts file format
  ```
  127.0.0.1 example.com
  0.0.0.0 ads.example.com
  ```

- **`adblock`**: AdBlock Plus format
  ```
  ||example.com^
  ||ads.example.com^$domain=example.com
  ```

- **`auto`**: Auto-detect format (recommended)

### Modifying Update Schedule

Edit `.github/workflows/update-lists.yml`:

```yaml
on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM UTC
    # - cron: '0 */6 * * *'  # Every 6 hours
    # - cron: '0 0 * * 0'    # Weekly on Sunday
```

## 📱 Using with Pi-hole

### Method 1: Direct URL (Recommended)

1. Open your Pi-hole Admin Panel
2. Go to **Settings** → **Blocklists**
3. Add this URL:
   ```
   https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/pihole_list.txt
   ```
4. Click **Save and Update**

### Method 2: Local File

1. Download the latest `pihole_list.txt`
2. Upload it to your Pi-hole server
3. Add the local path to your blocklists

### Method 3: SSH/Command Line

```bash
# Add to Pi-hole blocklists
echo "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/pihole_list.txt" | sudo tee -a /etc/pihole/adlists.list

# Update gravity
sudo pihole -g
```

## 🛡️ Using with AdGuard Home

### Web Interface

1. Open AdGuard Home Admin Panel
2. Go to **Filters** → **DNS blocklists**
3. Add this URL:
   ```
   https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/pihole_list.txt
   ```
4. Click **Save**

### Configuration File

Add to your `AdGuardHome.yaml`:

```yaml
filters:
  - enabled: true
    url: https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/pihole_list.txt
    name: "Auto-Generated Pi-hole List"
```

## 🔄 Automation

### Manual Trigger

1. Go to your repository's **Actions** tab
2. Select **Update Pi-hole Blocklist**
3. Click **Run workflow**
4. Choose the branch and click **Run workflow**

### Webhook Integration

Set up webhooks to trigger updates when source lists change:

1. Go to repository **Settings** → **Webhooks**
2. Add webhook URL: `https://api.github.com/repos/YOUR_USERNAME/YOUR_REPO/dispatches`
3. Select **Repository dispatch** events

### Monitoring

Check the automation status:

- **Actions Tab**: View workflow runs and logs
- **Releases**: See when lists were last updated
- **Commits**: Track changes to the generated list

## 🧪 Testing

### Local Testing

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the converter:
```bash
python convert_lists.py
```

3. Check the output:
```bash
ls -la pihole_list.txt summary.json
```

### Testing Specific Sources

Create a test configuration:

```json
{
  "lists": [
    {
      "name": "Test List",
      "url": "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
      "format": "hosts"
    }
  ]
}
```

## 📊 Monitoring and Analytics

### GitHub Actions Logs

- View detailed logs in the **Actions** tab
- Check for failed list fetches
- Monitor processing times

### Summary File

The `summary.json` file contains:
- Total domain count
- Processing timestamp
- Status of each source list
- Error information

### Release Notes

Each release includes:
- Domain count changes
- New sources added
- Processing timestamp
- Usage instructions

## 🛠️ Troubleshooting

### Common Issues

#### 1. Lists Not Updating

**Problem**: GitHub Actions not running
**Solution**: 
- Check repository settings
- Ensure Actions are enabled
- Verify workflow file syntax

#### 2. Source List Failures

**Problem**: Some sources fail to fetch
**Solution**:
- Check source URLs in `config.json`
- Verify network connectivity
- Review GitHub Actions logs

#### 3. Format Detection Issues

**Problem**: Wrong format detected
**Solution**:
- Specify format explicitly in `config.json`
- Check source list content
- Test with `format: "auto"`

### Debug Mode

Enable detailed logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Manual Override

If automation fails:

1. Run locally: `python convert_lists.py`
2. Commit changes: `git add . && git commit -m "Manual update"`
3. Push: `git push origin main`

## 🔒 Security Considerations

### Source Verification

- All sources are from reputable maintainers
- Lists are fetched over HTTPS
- No executable code is downloaded

### Content Validation

- Domains are validated before inclusion
- Malicious patterns are filtered out
- Standard Pi-hole format is maintained

### Access Control

- Repository can be private for sensitive use
- GitHub Actions use read-only permissions
- No external API keys required

## 📈 Performance

### Optimization Tips

1. **Reduce Sources**: Remove unnecessary lists from `config.json`
2. **Update Frequency**: Adjust cron schedule based on needs
3. **Caching**: GitHub Actions cache dependencies automatically

### Resource Usage

- **Runtime**: ~2-5 minutes per update
- **Storage**: ~2-5 MB per generated list
- **Bandwidth**: ~10-50 MB per update cycle

## 🤝 Contributing

### Adding New Sources

1. Research the source for reliability
2. Test the format detection
3. Add to `config.json`
4. Submit a pull request

### Improving Parsing

1. Identify parsing issues in logs
2. Update parsing methods in `convert_lists.py`
3. Test with various formats
4. Submit improvements

### Documentation

1. Update README.md for new features
2. Add usage examples
3. Improve troubleshooting guides

## 📞 Support

### Getting Help

- **Issues**: Create GitHub issues for bugs
- **Discussions**: Use GitHub Discussions for questions
- **Wiki**: Check the repository wiki for detailed guides

### Reporting Problems

When reporting issues, include:
- GitHub Actions logs
- Configuration file (remove sensitive info)
- Expected vs actual behavior
- Steps to reproduce

---

For more information, see the main [README.md](README.md) file.
