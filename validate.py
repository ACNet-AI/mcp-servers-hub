#!/usr/bin/env python3
"""
Local validation script for MCP Servers Registry
Script for local validation of registry data integrity
"""

import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("❌ Missing jsonschema dependency")
    print("   Run: pip install jsonschema")
    sys.exit(1)


def validate_registry() -> bool:
    """Validate registry data"""
    print("🔍 Validating MCP Servers Registry...")

    # Check file existence
    registry_file = Path("registry.json")
    schema_file = Path("registry-schema.json")

    if not registry_file.exists():
        print("❌ registry.json not found")
        return False

    if not schema_file.exists():
        print("❌ registry-schema.json not found")
        return False

    # Load files
    try:
        with open(registry_file, encoding="utf-8") as f:
            registry = json.load(f)
        print("✅ registry.json loaded successfully")
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in registry.json: {e}")
        return False
    except Exception as e:
        print(f"❌ Error reading registry.json: {e}")
        return False

    try:
        with open(schema_file, encoding="utf-8") as f:
            schema = json.load(f)
        print("✅ registry-schema.json loaded successfully")
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in registry-schema.json: {e}")
        return False
    except Exception as e:
        print(f"❌ Error reading registry-schema.json: {e}")
        return False

    # Schema validation
    try:
        jsonschema.validate(registry, schema)
        print("✅ Schema validation passed")
    except jsonschema.ValidationError as e:
        print(f"❌ Schema validation failed: {e.message}")
        if e.path:
            print(f"   Path: {' -> '.join(str(p) for p in e.path)}")
        return False
    except Exception as e:
        print(f"❌ Schema validation error: {e}")
        return False

    # Basic data validation
    projects = registry.get("projects", [])
    print(f"📊 Found {len(projects)} projects")

    # Check for duplicates
    names = [p["name"] for p in projects]
    repos = [p["repository"] for p in projects]

    if len(names) != len(set(names)):
        duplicates = [name for name in set(names) if names.count(name) > 1]
        print(f"❌ Duplicate project names found: {duplicates}")
        return False

    if len(repos) != len(set(repos)):
        duplicates = [repo for repo in set(repos) if repos.count(repo) > 1]
        print(f"❌ Duplicate repository URLs found: {duplicates}")
        return False

    print("✅ No duplicates found")

    # Project details
    for project in projects:
        name = project["name"]
        print(f"  📦 {name} by {project['author']}")
        print(f"     🏷️  {', '.join(project['tags'])}")
        print(f"     📝 {project['description']}")

    print("\n🎉 Registry validation completed successfully!")
    print(f"   Projects: {len(projects)}")
    print(f"   Authors: {len({p['author'] for p in projects})}")
    print(f"   Languages: {len({p['language'] for p in projects})}")

    return True


if __name__ == "__main__":
    success = validate_registry()
    sys.exit(0 if success else 1)
