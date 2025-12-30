#!/usr/bin/env python3
"""
Config-Fu Master: Because your config files should work, not make you cry.
Turns cryptic YAML/JSON/TOML errors into human-ish language.
"""

import sys
import json
import yaml
import tomllib
from pathlib import Path

def diagnose_yaml(filepath):
    """YAML: Where indentation is a religion and commas are heresy."""
    try:
        with open(filepath, 'r') as f:
            yaml.safe_load(f)
        return "YAML looks fine! (Probably. No promises.)"
    except yaml.YAMLError as e:
        return f"YAML says: {str(e)[:100]}... (Hint: Check your spaces, you heathen)"

def diagnose_json(filepath):
    """JSON: The format where missing commas cause existential crises."""
    try:
        with open(filepath, 'r') as f:
            json.load(f)
        return "JSON is valid! (The commas are all present and accounted for)"
    except json.JSONDecodeError as e:
        return f"JSON error at line {e.lineno}: {e.msg} (Probably a comma drama)"

def diagnose_toml(filepath):
    """TOML: Because we needed another way to configure things."""
    try:
        with open(filepath, 'rb') as f:
            tomllib.load(f)
        return "TOML parses! (This is surprisingly rare)"
    except tomllib.TOMLDecodeError as e:
        return f"TOML decode error: {str(e)[:100]}... (Tables, arrays, who knows?)"

def main():
    """Main function: Less talk, more config-fu."""
    if len(sys.argv) != 2:
        print("Usage: python config_fu_master.py <config_file>")
        print("Example: python config_fu_master.py config.yaml")
        sys.exit(1)
    
    filepath = Path(sys.argv[1])
    if not filepath.exists():
        print(f"File not found: {filepath} (Maybe it's hiding?)")
        sys.exit(1)
    
    suffix = filepath.suffix.lower()
    
    print(f"\n🔍 Examining: {filepath}")
    print("-" * 40)
    
    if suffix in ['.yaml', '.yml']:
        print(diagnose_yaml(filepath))
    elif suffix == '.json':
        print(diagnose_json(filepath))
    elif suffix == '.toml':
        print(diagnose_toml(filepath))
    else:
        print(f"Unsupported format: {suffix} (I only speak YAML, JSON, and TOML)")
    
    print("-" * 40)
    print("Config-Fu complete. You're welcome.")

if __name__ == "__main__":
    main()