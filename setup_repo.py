#!/usr/bin/env python3
"""
Repository Setup Script
Helps initialize the GitHub repository with proper URLs and settings
"""

import os
import re
import json

def update_file_urls(file_path, username, repo_name):
    """Update placeholder URLs in a file"""
    if not os.path.exists(file_path):
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace placeholder URLs
    content = content.replace('YOUR_USERNAME', username)
    content = content.replace('YOUR_REPO', repo_name)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated URLs in {file_path}")

def main():
    """Main setup function"""
    print("Pi-hole Ad Blocking List Converter - Repository Setup")
    print("=" * 60)
    
    # Get user input
    username = input("Enter your GitHub username: ").strip()
    repo_name = input("Enter your repository name: ").strip()
    
    if not username or not repo_name:
        print("Error: Username and repository name are required")
        return
    
    print(f"\nSetting up repository: {username}/{repo_name}")
    
    # Files to update
    files_to_update = [
        'README.md',
        '.github/workflows/update-lists.yml',
        'convert_lists.py'
    ]
    
    # Update files
    for file_path in files_to_update:
        update_file_urls(file_path, username, repo_name)
    
    # Update config.json with proper URLs
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        
        # Update the settings if needed
        config['settings']['repository_url'] = f"https://github.com/{username}/{repo_name}"
        
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=2)
        
        print("Updated config.json with repository URL")
    except Exception as e:
        print(f"Warning: Could not update config.json: {e}")
    
    print("\n" + "=" * 60)
    print("Setup Complete!")
    print("\nNext steps:")
    print("1. Initialize git repository:")
    print("   git init")
    print("   git add .")
    print("   git commit -m 'Initial commit'")
    print("\n2. Create GitHub repository and push:")
    print(f"   git remote add origin https://github.com/{username}/{repo_name}.git")
    print("   git branch -M main")
    print("   git push -u origin main")
    print("\n3. Enable GitHub Actions in repository settings")
    print("\n4. Test the automation by running:")
    print("   python convert_lists.py")
    print("\n5. Your Pi-hole list will be available at:")
    print(f"   https://raw.githubusercontent.com/{username}/{repo_name}/main/pihole_list.txt")

if __name__ == "__main__":
    main()
