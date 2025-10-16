#!/usr/bin/env python3
"""
Pi-hole Ad Blocking List Converter
Automatically converts various ad-blocking lists to Pi-hole format
"""

import requests
import re
import os
import json
import hashlib
from datetime import datetime, timezone
from urllib.parse import urlparse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PiHoleListConverter:
    def __init__(self, config_file='config.json'):
        """Initialize the converter with configuration"""
        self.config = self.load_config(config_file)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Pi-hole List Converter/1.0'
        })
        
    def load_config(self, config_file):
        """Load configuration from JSON file"""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Configuration file {config_file} not found")
            return {}
    
    def fetch_list(self, url, list_name):
        """Fetch a list from URL with error handling"""
        try:
            logger.info(f"Fetching {list_name} from {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.error(f"Failed to fetch {list_name} from {url}: {e}")
            return None
    
    def parse_hosts_format(self, content, list_name):
        """Parse hosts file format (127.0.0.1 domain)"""
        domains = set()
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue
            
            # Parse hosts format: IP domain
            parts = line.split()
            if len(parts) >= 2:
                domain = parts[1]
                # Clean domain (remove comments)
                domain = domain.split('#')[0].strip()
                if self.is_valid_domain(domain):
                    domains.add(domain)
        
        logger.info(f"Parsed {len(domains)} domains from {list_name}")
        return domains
    
    def parse_adblock_format(self, content, list_name):
        """Parse AdBlock Plus format"""
        domains = set()
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            # Skip comments and empty lines
            if not line or line.startswith('!'):
                continue
            
            # Parse AdBlock format
            if line.startswith('||') and line.endswith('^'):
                # Domain rule: ||example.com^
                domain = line[2:-1]
                if self.is_valid_domain(domain):
                    domains.add(domain)
            elif line.startswith('||') and '^' in line:
                # Domain with path: ||example.com^$domain=example.com
                domain = line[2:].split('^')[0]
                if self.is_valid_domain(domain):
                    domains.add(domain)
            elif not line.startswith('||') and not line.startswith('|') and not line.startswith('@@'):
                # Simple domain rule
                if self.is_valid_domain(line):
                    domains.add(line)
        
        logger.info(f"Parsed {len(domains)} domains from {list_name}")
        return domains
    
    def parse_plain_domains(self, content, list_name):
        """Parse plain domain list (one domain per line)"""
        domains = set()
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue
            
            # Clean domain (remove comments)
            domain = line.split('#')[0].strip()
            if self.is_valid_domain(domain):
                domains.add(domain)
        
        logger.info(f"Parsed {len(domains)} domains from {list_name}")
        return domains
    
    def is_valid_domain(self, domain):
        """Check if domain is valid for blocking"""
        if not domain:
            return False
        
        # Remove wildcards and other AdBlock syntax
        domain = domain.replace('*', '').replace('^', '').replace('|', '')
        
        # Skip invalid patterns
        if any(skip in domain.lower() for skip in ['localhost', '127.0.0.1', '0.0.0.0', '::1']):
            return False
        
        # Basic domain validation
        if '.' not in domain or len(domain) < 3:
            return False
        
        # Skip IP addresses
        if re.match(r'^\d+\.\d+\.\d+\.\d+$', domain):
            return False
        
        return True
    
    def convert_to_pihole_format(self, all_domains, output_file='pihole_list.txt'):
        """Convert domains to Pi-hole format"""
        timestamp = datetime.now(timezone.utc).strftime('%d %B %Y %H:%M:%S (UTC)')
        total_domains = len(all_domains)
        
        # Create Pi-hole formatted content
        content = f"""# Title: Auto-Generated Pi-hole Blocklist
#
# This hosts file is a merged collection of hosts from reputable sources,
# automatically converted and updated via GitHub Actions
#
# Date: {timestamp}
# Number of unique domains: {total_domains:,}
#
# Fetch the latest version of this file: https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/master/pihole_list.txt
# Project home page: https://github.com/YOUR_USERNAME/YOUR_REPO
# Project releases: https://github.com/YOUR_USERNAME/YOUR_REPO/releases
#
# ===============================================================

127.0.0.1 localhost
127.0.0.1 localhost.localdomain
127.0.0.1 local
255.255.255.255 broadcasthost
::1 localhost
::1 ip6-localhost
::1 ip6-loopback
fe80::1%lo0 localhost
ff00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
ff02::2 ip6-allhosts
0.0.0.0 0.0.0.0

# Custom host records are listed here.

# End of custom host records.
# Start Auto-Generated Blocklist

#=====================================
# Title: Auto-Generated Pi-hole Blocklist
# Generated from multiple reputable sources

"""
        
        # Add domains in sorted order
        for domain in sorted(all_domains):
            content += f"0.0.0.0 {domain}\n"
        
        content += "\n# End of auto-generated blocklist.\n"
        
        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"Generated Pi-hole list with {total_domains} domains in {output_file}")
        return total_domains
    
    def process_all_lists(self):
        """Process all configured lists and generate combined Pi-hole list"""
        all_domains = set()
        processed_lists = []
        
        for list_config in self.config.get('lists', []):
            name = list_config['name']
            url = list_config['url']
            format_type = list_config.get('format', 'auto')
            
            logger.info(f"Processing {name}...")
            content = self.fetch_list(url, name)
            
            if content is None:
                continue
            
            # Determine format and parse
            if format_type == 'hosts' or (format_type == 'auto' and '127.0.0.1' in content):
                domains = self.parse_hosts_format(content, name)
            elif format_type == 'adblock' or (format_type == 'auto' and '||' in content):
                domains = self.parse_adblock_format(content, name)
            else:
                domains = self.parse_plain_domains(content, name)
            
            all_domains.update(domains)
            processed_lists.append({
                'name': name,
                'url': url,
                'domains': len(domains),
                'status': 'success'
            })
        
        # Generate combined Pi-hole list
        total_domains = self.convert_to_pihole_format(all_domains)
        
        # Generate summary
        summary = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'total_domains': total_domains,
            'processed_lists': processed_lists,
            'output_file': 'pihole_list.txt'
        }
        
        with open('summary.json', 'w') as f:
            json.dump(summary, f, indent=2)
        
        logger.info(f"Processing complete. Generated list with {total_domains} unique domains.")
        return summary

def main():
    """Main function"""
    converter = PiHoleListConverter()
    summary = converter.process_all_lists()
    
    print(f"\n[SUCCESS] Successfully generated Pi-hole list!")
    print(f"[STATS] Total domains: {summary['total_domains']:,}")
    print(f"[FILE] Output file: {summary['output_file']}")
    print(f"[INFO] Processed {len(summary['processed_lists'])} lists")

if __name__ == "__main__":
    main()
