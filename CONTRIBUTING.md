# Contributing Guide

Thank you for your interest in contributing to the Pi-hole Ad Blocking List Converter! This guide will help you get started with contributing to the project.

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- Git
- GitHub account
- Basic understanding of ad-blocking lists

### Fork and Clone

1. Fork this repository on GitHub
2. Clone your fork locally:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

3. Add the upstream repository:
```bash
git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPO.git
```

## 🔧 Development Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Test the Converter

```bash
python convert_lists.py
```

This should generate `pihole_list.txt` and `summary.json`.

### 3. Verify Output

Check that the generated files are valid:
- `pihole_list.txt` should contain domains in Pi-hole format
- `summary.json` should contain processing statistics

## 📝 Types of Contributions

### 🆕 Adding New Sources

To add a new ad-blocking source:

1. **Research the Source**
   - Ensure it's from a reputable maintainer
   - Check that it's actively maintained
   - Verify the format and content

2. **Test the Source**
   ```bash
   # Create a test config
   cp config.json test_config.json
   # Edit test_config.json to include only your new source
   python convert_lists.py
   ```

3. **Add to Configuration**
   Edit `config.json`:
   ```json
   {
     "name": "Your Source Name",
     "url": "https://example.com/your-list.txt",
     "format": "adblock"  // or "hosts" or "auto"
   }
   ```

4. **Submit Pull Request**
   - Include source information
   - Explain why it's valuable
   - Provide test results

### 🐛 Bug Fixes

When fixing bugs:

1. **Identify the Issue**
   - Check GitHub Actions logs
   - Test locally with problematic sources
   - Document the problem

2. **Fix the Code**
   - Update parsing logic if needed
   - Improve error handling
   - Add validation

3. **Test Thoroughly**
   ```bash
   python convert_lists.py
   # Check for errors and warnings
   ```

### 🔧 Improvements

Common improvement areas:

- **Parsing Logic**: Better format detection
- **Error Handling**: More robust error recovery
- **Performance**: Faster processing
- **Documentation**: Clearer instructions

## 🧪 Testing

### Local Testing

1. **Test with All Sources**
   ```bash
   python convert_lists.py
   ```

2. **Test with Specific Sources**
   Create a minimal `config.json`:
   ```json
   {
     "lists": [
       {
         "name": "Test Source",
         "url": "https://example.com/test.txt",
         "format": "auto"
       }
     ]
   }
   ```

3. **Test Error Handling**
   - Use invalid URLs
   - Test with malformed content
   - Check timeout scenarios

### GitHub Actions Testing

1. **Push to Feature Branch**
   ```bash
   git checkout -b feature/your-feature
   git add .
   git commit -m "Add your feature"
   git push origin feature/your-feature
   ```

2. **Check Actions Tab**
   - Verify the workflow runs
   - Check for errors
   - Review generated output

## 📋 Pull Request Process

### Before Submitting

1. **Test Your Changes**
   ```bash
   python convert_lists.py
   # Verify output is correct
   ```

2. **Update Documentation**
   - Update README.md if needed
   - Add usage examples
   - Update configuration docs

3. **Check Code Quality**
   - Follow Python style guidelines
   - Add comments for complex logic
   - Ensure error handling is robust

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Configuration change

## Testing
- [ ] Tested locally
- [ ] GitHub Actions pass
- [ ] No breaking changes

## Additional Notes
Any additional information or context
```

### Review Process

1. **Automated Checks**
   - GitHub Actions must pass
   - No syntax errors
   - Valid configuration

2. **Manual Review**
   - Code quality
   - Documentation completeness
   - Impact on existing functionality

3. **Testing**
   - Reviewer will test changes
   - Verify output format
   - Check for regressions

## 📚 Code Style Guidelines

### Python Code

```python
# Use descriptive variable names
domain_count = len(domains)

# Add docstrings for functions
def parse_hosts_format(self, content, list_name):
    """Parse hosts file format (127.0.0.1 domain)"""
    # Implementation here

# Use type hints when helpful
def is_valid_domain(self, domain: str) -> bool:
    """Check if domain is valid for blocking"""
    # Implementation here
```

### Configuration Files

```json
{
  "lists": [
    {
      "name": "Descriptive Name",
      "url": "https://example.com/list.txt",
      "format": "auto"
    }
  ]
}
```

### Documentation

- Use clear, concise language
- Include examples where helpful
- Update all relevant files
- Check for typos and grammar

## 🐛 Reporting Issues

### Before Reporting

1. **Check Existing Issues**
   - Search for similar problems
   - Check if it's already reported

2. **Gather Information**
   - GitHub Actions logs
   - Configuration file (remove sensitive info)
   - Error messages
   - Steps to reproduce

### Issue Template

```markdown
## Description
Clear description of the problem

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. See error

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- Python version
- Operating system
- Repository version

## Additional Context
Any other relevant information
```

## 💡 Feature Requests

### Before Requesting

1. **Check Existing Features**
   - Review current functionality
   - Check if it's already possible

2. **Consider Implementation**
   - How complex would it be?
   - Does it fit the project goals?
   - Are there alternatives?

### Feature Request Template

```markdown
## Feature Description
Clear description of the requested feature

## Use Case
Why is this feature needed?

## Proposed Solution
How should it work?

## Alternatives Considered
What other options were considered?

## Additional Context
Any other relevant information
```

## 🏆 Recognition

Contributors will be recognized in:

- **README.md**: Listed in acknowledgments
- **GitHub Contributors**: Automatic recognition
- **Release Notes**: Mentioned in relevant releases

### Types of Contributions

- **Code**: Bug fixes, new features, improvements
- **Documentation**: README updates, usage guides
- **Sources**: New ad-blocking lists
- **Testing**: Bug reports, testing improvements
- **Community**: Helping other users

## 📞 Getting Help

### Resources

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and ideas
- **Documentation**: README.md and USAGE.md
- **Wiki**: Detailed guides and tutorials

### Community Guidelines

- Be respectful and constructive
- Help others when possible
- Follow the code of conduct
- Report inappropriate behavior

## 🔄 Release Process

### Automatic Releases

- Triggered by GitHub Actions
- Created when lists are updated
- Include changelog and statistics

### Manual Releases

- For major changes
- Include detailed release notes
- Tag with semantic versioning

---

Thank you for contributing to the Pi-hole Ad Blocking List Converter! Your contributions help make ad-blocking more effective for everyone.
